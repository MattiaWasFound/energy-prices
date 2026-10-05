"""`python -m energyprices generate`: fetch, build, validate, write prices.json.

Exit status 0 means a valid file was written (possibly with entries carried
forward, listed on stderr). Exit status 1 means validation failed and nothing
was written. Tokens come from the environment and never reach a log line.
"""

import argparse
import json
import os
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from pathlib import Path

from . import config, validate
from .build import area_days, build
from .http import FetchError
from .slots import UTC, Points, day_start, delivery_day
from .config import StaticPrice
from .sources import ecb, eds, eia, entsoe, frankfurter

# A Frankfurter quote older than this is ignored (some central banks stop publishing).
FX_MAX_AGE_DAYS = 7


def fetch_spot(cfg: config.Config, now: datetime, token: str | None, failing: set[str],
               log) -> dict[str, Points | None]:
    """Each live area from ENTSO-E, with Energi Data Service as the backup where
    it carries the area. Whichever gives more complete delivery days wins."""
    today = delivery_day(now)
    days = [today, today + timedelta(days=1)]
    start, end = day_start(days[0]), day_start(days[-1] + timedelta(days=1))
    areas = {a.area: a for a in cfg.areas}  # one fetch per area, even when it spans countries

    primary: dict[str, Points | None] = {}
    for area, a in areas.items():
        primary[area] = None
        if not a.entsoe_eic:
            continue
        if not token or "entsoe" in failing:
            continue
        try:
            primary[area] = entsoe.parse(entsoe.fetch(token, a.entsoe_eic, start, end))
        except (FetchError, entsoe.NoData, ET.ParseError) as e:
            log(f"entsoe {area}: {e}")
    if not token:
        log("entsoe: ENTSOE_TOKEN is not set, skipping")

    want_backup = [a.eds_area for area, a in areas.items()
                   if a.eds_area and len(area_days(primary[area], days)) < len(days)]
    backup: dict[str, Points] = {}
    if want_backup:
        try:
            if "eds" in failing:
                raise FetchError("simulated failure")
            backup = eds.parse(eds.fetch(sorted(set(want_backup)), start, end))
        except (FetchError, json.JSONDecodeError, KeyError) as e:
            log(f"eds: {e}")
    spot = {}
    for area, a in areas.items():
        candidates = [primary[area], backup.get(a.eds_area) if a.eds_area else None]
        spot[area] = max(candidates, key=lambda p: len(area_days(p, days)))
        if not area_days(spot[area], days):
            spot[area] = None
    return spot


def fetch_fx(now: datetime, failing: set[str], log) -> dict[str, float]:
    """Units per EUR: the ECB's reference rates where it quotes the currency,
    Frankfurter for the rest. A currency neither has (or a stale quote) is left
    out; build() carries it from the previous file."""
    rates: dict[str, float] = {"EUR": 1.0}
    try:
        if "fx" in failing:
            raise FetchError("simulated failure")
        oldest = delivery_day(now) - timedelta(days=FX_MAX_AGE_DAYS)
        for cur, (day, rate) in frankfurter.parse(frankfurter.fetch()).items():
            if day >= oldest:
                rates[cur] = rate
    except (FetchError, json.JSONDecodeError, KeyError, AssertionError) as e:
        log(f"fx frankfurter: {e}")
    try:
        if "fx" in failing:
            raise FetchError("simulated failure")
        _day, ecb_rates = ecb.parse(ecb.fetch())
        rates.update(ecb_rates)
    except (FetchError, ET.ParseError, AssertionError) as e:
        log(f"fx ecb: {e}")
    return rates


def fetch_tables(cfg: config.Config, failing: set[str], log) -> dict[str, dict | None]:
    """Country-table rows that come from a source at run time (settings.toml
    `fetched_static`). None for a country whose source failed."""
    out: dict[str, dict | None] = {}
    for country, source in cfg.settings.get("fetched_static", {}).items():
        assert source == "eia", f"unknown fetched_static source {source}"
        key = os.environ.get("EIA_API_KEY")
        try:
            if not key:
                raise FetchError("EIA_API_KEY is not set")
            if "eia" in failing:
                raise FetchError("simulated failure")
            period, prices, sales = eia.parse(eia.fetch(key))
        except (FetchError, json.JSONDecodeError, KeyError, AssertionError) as e:
            log(f"eia: {e}")
            out[country] = None
            continue
        rows = {}
        for state, price in prices.items():
            zone = f"{country}-{state}"
            t = cfg.taxes.get(zone)
            if t:
                rows[zone] = StaticPrice(country, zone, price * (1 + t["rate"] + t["local_rate"]) + t["per_kwh"], "USD", period)
        # EIA's national figure gets the states' taxes weighted by residential kWh sold.
        weighted = [(sales[z[-2:]], cfg.taxes[z]) for z in rows if sales.get(z[-2:])]
        total = sum(w for w, _ in weighted)
        if not total:
            log("eia: no residential sales to weight the national taxes")
            out[country] = None
            continue
        pct = sum(w * (t["rate"] + t["local_rate"]) for w, t in weighted) / total
        per_kwh = sum(w * t["per_kwh"] for w, t in weighted) / total
        rows[None] = StaticPrice(country, None, prices["US"] * (1 + pct) + per_kwh, "USD", period)
        zone_ids = {z.id for z in cfg.zones_of(country)}
        missing = zone_ids - set(rows)
        if missing:
            log(f"eia: no price for {sorted(missing)}")
            out[country] = None
            continue
        out[country] = rows
    return out


def generate(out_dir: Path, now: datetime, failing: set[str]) -> int:
    def log(msg: str) -> None:
        print(msg, file=sys.stderr)

    cfg = config.load()
    target = out_dir / "prices.json"
    previous = json.loads(target.read_text()) if target.exists() else None
    spot = fetch_spot(cfg, now, os.environ.get("ENTSOE_TOKEN") or None, failing, log)
    fx = fetch_fx(now, failing, log)
    fetched = fetch_tables(cfg, failing, log)
    doc, notes = build(now, cfg, spot, fx, previous, fetched)
    for n in notes:
        log(n)
    problems = validate.check(doc, cfg, now)
    if problems:
        log(f"VALIDATION FAILED, nothing written ({len(problems)} problems):")
        for p in problems[:50]:
            log(f"  {p}")
        return 1
    out_dir.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(".tmp")
    tmp.write_bytes(validate.serialize(doc))
    tmp.replace(target)
    live = sum(1 for c in doc["countries"].values() if c["average"]["basis"] == "day-ahead")
    log(f"wrote {target} ({target.stat().st_size} bytes, {len(doc['countries'])} countries, {live} live)")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="energyprices")
    sub = p.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("generate", help="build and validate prices.json")
    g.add_argument("--out", type=Path, default=Path("out"), help="folder for prices.json (default: out)")
    g.add_argument("--now", help="pretend the time is this ISO timestamp (UTC if no offset)")
    g.add_argument("--fail", default="", help="simulate failing sources: comma list of entsoe, eds, eia, fx")
    args = p.parse_args(argv)
    now = datetime.now(UTC).replace(microsecond=0)
    if args.now:
        now = datetime.fromisoformat(args.now)
        now = now if now.tzinfo else now.replace(tzinfo=UTC)
    return generate(args.out, now, {s for s in args.fail.split(",") if s})


if __name__ == "__main__":
    sys.exit(main())
