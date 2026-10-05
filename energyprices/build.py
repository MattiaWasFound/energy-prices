"""Turns fetched spot prices, exchange rates and the config tables into prices.json.

`build` is the one function that decides which basis each entry gets. It does no
IO: the caller hands it what the sources returned (None for a source that
failed) and the previously published document, so every decision, carry-forward
included, is testable from fixtures.

A country may also carry `options` (settings.toml `[[options]]`): alternative
prices the user can pick, each with its own average and zones. Norgespris is
one: the tariff's fixed energy price in place of spot, labelled country-table.

Every country resolves through the same chain, and the step used is the entry's
`basis`:

1. day-ahead       spot + add-on, times VAT, where config/areas.csv lists a live area
                   (a failed fetch carries the entry forward from the previous file)
2. country-table   config/static_prices.csv (also for a live country listed in
                   settings.toml `table_instead_of_live`)
3. regional-average  mean of the countries in the same region that resolved at 1 or 2
4. global-average    mean of every country that resolved at 1 or 2
"""

from datetime import date, datetime, timedelta

from .config import Config
from .slots import UTC, Points, day_start, day_values, delivery_day, expand

SCHEMA_VERSION = 1


def _r(v: float) -> float:
    # Adding 0.0 turns a rounded -0.0 into 0.0, so the output is stable.
    return round(v, 4) + 0.0


def area_days(points: Points | None, days: list[date]) -> list[list[float]]:
    """The leading run of complete delivery days, in EUR/MWh at the points' step."""
    out = []
    for d in days:
        values = day_values(points, d) if points else None
        if values is None:
            break
        out.append(values)
    return out


def _household(spot_eur_mwh: float, rate: float, t: dict) -> float:
    """One slot's all-in household price per kWh in the country's currency."""
    spot = spot_eur_mwh / 1000 * rate
    if t["support_threshold"] is not None:
        # A state support scheme pays this share of the spot price above the threshold.
        spot -= max(0.0, spot - t["support_threshold"]) * t["support_share"]
    return (spot + t["addon"]) * (1 + t["vat"])


def live_entry(cfg: Config, country: str, weighted: list[tuple[str, float]],
               spot_days: dict[str, list[list[float]]], steps: dict[str, int],
               fx: dict, start: datetime) -> dict | None:
    """A day-ahead entry for the population-weighted mix of `weighted` areas, or
    None when any of them lacks today's prices."""
    n_days = min(len(spot_days.get(a, [])) for a, _ in weighted)
    if n_days == 0:
        return None
    rate = fx[cfg.countries[country].currency]
    step = min(steps[a] for a, _ in weighted)
    days: list[list[float]] = []
    for i in range(n_days):
        mixed = None
        for area, w in weighted:
            t = cfg.tariff(country, area)
            values = expand([_household(v, rate, t) for v in spot_days[area][i]], steps[area], step)
            mixed = [w * v for v in values] if mixed is None else [m + w * v for m, v in zip(mixed, values)]
        days.append(mixed)
    last = days[-1]
    return {
        "precision": "live",
        "basis": "day-ahead",
        "flat": _r(sum(last) / len(last)),
        "series": {
            "start": start.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "step_minutes": step,
            "values": [_r(v) for d in days for v in d],
        },
    }


def carried(prev: dict | None, start: datetime) -> dict | None:
    """A day-ahead entry from the previous file, its series trimmed to start
    today (or dropped when it no longer reaches today). Only the client's flat
    fallback is left then, which is what an out-of-date live entry should show."""
    if not prev or prev.get("basis") != "day-ahead":
        return None
    out = {k: v for k, v in prev.items() if k != "series"}
    s = prev.get("series")
    if s:
        s_start = datetime.fromisoformat(s["start"].replace("Z", "+00:00"))
        skip = (start - s_start) // timedelta(minutes=s["step_minutes"])
        if 0 <= skip < len(s["values"]):
            out["series"] = {
                "start": start.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "step_minutes": s["step_minutes"],
                "values": s["values"][skip:],
            }
    return out


def _prev_entry(previous: dict | None, country: str, zone: str | None) -> dict | None:
    c = (previous or {}).get("countries", {}).get(country)
    if not c:
        return None
    if zone is None:
        return c.get("average")
    return next((z for z in c.get("zones", []) if z["id"] == zone), None)


def _static(static: dict, cfg: Config, country: str, zone: str | None, fx: dict) -> dict | None:
    s = static.get((country, zone))
    if s is None:
        return None
    price = s.price / fx[s.currency] * fx[cfg.countries[country].currency]
    entry = {"precision": "estimated", "basis": "country-table"}
    if s.as_of:
        entry["as_of"] = s.as_of
    entry["flat"] = _r(price)
    return entry


def _fixed(cfg: Config, country: str, areas: list[tuple[str, float]]) -> dict:
    """The tariff's fixed energy price in place of spot (an option, e.g. Norgespris)."""
    price, as_of = 0.0, None
    for area, w in areas:
        t = cfg.tariff(country, area)
        price += w * (t["fixed_energy"] + t["addon"]) * (1 + t["vat"])
        as_of = t["as_of"]
    return {"precision": "estimated", "basis": "country-table", "as_of": as_of[:7], "flat": _r(price)}


def build(now: datetime, cfg: Config, spot: dict[str, Points | None], fx: dict[str, float],
          previous: dict | None, fetched: dict[str, dict | None] | None = None) -> tuple[dict, list[str]]:
    """Returns the document and a list of notes on what was carried forward or fell back.

    `fetched` holds country-table rows a source supplied this run (the US from
    EIA): country -> {zone or None: StaticPrice}, replacing that country's
    config rows, or None when the source failed, which carries the country's
    table entries forward from the previous file."""
    assert now.tzinfo is not None, "now must be timezone-aware"
    notes: list[str] = []
    guesses = cfg.settings.get("educated_guess", {})
    needed = ({c.currency for c in cfg.countries.values()} | {s.currency for s in cfg.static.values()}
              | {g["currency"] for g in guesses.values()} | {"EUR"})
    fx = dict(fx or {})
    carried_fx = sorted(c for c in needed - set(fx) if c in (previous or {}).get("fx", {}))
    for c in carried_fx:
        fx[c] = previous["fx"][c]
    if carried_fx:
        notes.append(f"fx: carried forward from the previous file: {', '.join(carried_fx)}")
    missing = sorted(needed - set(fx))
    assert not missing, f"no exchange rate for {missing}, fresh or carried"
    today = delivery_day(now)
    start = day_start(today)
    days = [today, today + timedelta(days=1)]
    spot_days = {a: area_days(p, days) for a, p in spot.items()}
    steps = {a: p.step for a, p in spot.items() if p}
    static = dict(cfg.static)
    stale: set[str] = set()
    for country, rows in (fetched or {}).items():
        if rows is None:
            stale.add(country)
            continue
        static = {k: v for k, v in static.items() if k[0] != country}
        static.update({(country, zone): row for zone, row in rows.items()})

    def table(country: str, zone: str | None) -> dict | None:
        if country in stale:
            prev = _prev_entry(previous, country, zone)
            label = f"{country}/{zone}" if zone else country
            if prev and prev.get("basis") == "country-table":
                notes.append(f"{label}: table source failed, carried forward")
                return {k: v for k, v in prev.items() if k not in ("id", "name")}
            notes.append(f"{label}: table source failed, nothing to carry")
        return _static(static, cfg, country, zone, fx)

    table_only = set(cfg.settings.get("table_instead_of_live", []))

    def resolve_live(country: str, weighted: list[tuple[str, float]], zone: str | None) -> dict | None:
        if country in table_only:
            return None  # the caller falls through to the static table
        e = live_entry(cfg, country, weighted, spot_days, steps, fx, start)
        if e is None:
            e = carried(_prev_entry(previous, country, zone), start)
            label = f"{country}/{zone}" if zone else country
            notes.append(f"{label}: no fresh day-ahead prices, " + ("carried forward" if e else "falling back"))
        return e

    # Pass 1: everything that resolves from live data or the country table.
    resolved: dict[str, dict] = {}
    no_price = cfg.settings.get("no_published_price", {})
    for code in sorted(cfg.countries):
        c = cfg.countries[code]
        if code in no_price:
            resolved[code] = {"name": c.name, "currency": c.currency, "zone_label": None, "zones": [],
                              "average": {"precision": "none", "basis": "no-published-price", "reason": no_price[code]}}
            continue
        if code in guesses:
            g = guesses[code]
            resolved[code] = {"name": c.name, "currency": c.currency, "zone_label": None, "zones": [],
                              "average": {"precision": "estimated", "basis": "educated-guess", "reason": g["reason"],
                                          "flat": _r(g["price"] / fx[g["currency"]] * fx[c.currency])}}
            continue
        areas = [(a.area, a.weight) for a in cfg.areas_of(code)]
        average = resolve_live(code, areas, None) if areas else None
        zones = []
        for z in cfg.zones_of(code):
            e = resolve_live(code, [(z.area, 1.0)], z.id) if z.area else table(code, z.id)
            zones.append({"id": z.id, "name": z.name, **(e or {})})
        if average is None:
            average = table(code, None)
        if average is None and zones and not areas and all("flat" in z for z in zones):
            # No national row in the table: the population-weighted mean of the zones.
            rows = cfg.zones_of(code)
            flat = sum(z.weight * e["flat"] for z, e in zip(rows, zones)) / sum(z.weight for z in rows)
            as_of = min((e["as_of"] for e in zones if "as_of" in e), default=None)
            average = {"precision": "estimated", "basis": "country-table",
                       **({"as_of": as_of} if as_of else {}), "flat": _r(flat)}
        resolved[code] = {"name": c.name, "currency": c.currency,
                          "zone_label": c.zone_label if zones else None,
                          "average": average, "zones": zones}
        options = [o for o in cfg.settings.get("options", []) if o["country"] == code]
        if options:
            resolved[code]["options"] = [{
                "id": o["id"], "name": o["name"],
                "average": _fixed(cfg, code, areas),
                "zones": [{"id": z.id, "name": z.name, **_fixed(cfg, code, [(z.area, 1.0)])} for z in cfg.zones_of(code)],
            } for o in options]

    # Pass 2: regional and global averages, in EUR, from the countries that resolved.
    def eur(code: str) -> float:
        return resolved[code]["average"]["flat"] / fx[cfg.countries[code].currency]

    known = [code for code, r in resolved.items() if r["average"] and r["average"]["basis"] in ("day-ahead", "country-table")]
    global_eur = sum(eur(c) for c in known) / len(known) if known else None
    for code, r in resolved.items():
        cur = cfg.countries[code].currency
        if r["average"] is None:
            peers = [c for c in known if cfg.countries[c].region == cfg.countries[code].region]
            if peers:
                r["average"] = {"precision": "estimated", "basis": "regional-average",
                                "flat": _r(sum(eur(c) for c in peers) / len(peers) * fx[cur])}
            else:
                assert global_eur is not None, "no country resolved at all"
                r["average"] = {"precision": "estimated", "basis": "global-average",
                                "flat": _r(global_eur * fx[cur])}
            notes.append(f"{code}: {r['average']['basis']}")
        for z in r["zones"]:
            if "flat" not in z:
                # A live zone with no data and nothing to carry: show the country's figure.
                z.update({k: v for k, v in r["average"].items() if k != "series"})
                notes.append(f"{code}/{z['id']}: took the country average")

    currencies = sorted({cfg.countries[c].currency for c in resolved} | {"EUR"})
    doc = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": now.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "unit": "kWh",
        "fx_base": "EUR",
        "fx": {c: fx[c] for c in currencies},
        "countries": resolved,
    }
    return doc, notes
