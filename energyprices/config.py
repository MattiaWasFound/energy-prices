"""The hand-maintained tables in config/, loaded and cross-checked.

Every table is a CSV so it diffs cleanly and opens in a spreadsheet. The column
meanings are documented in README.md ("Config tables"); this module asserts the
rules that tie the tables together, so a bad edit fails before any fetch.
"""

import csv
import tomllib
from dataclasses import dataclass
from pathlib import Path

CONFIG_DIR = Path(__file__).resolve().parent.parent / "config"

TARIFF_NUMBERS = ("addon", "vat", "support_threshold", "support_share", "fixed_energy")


@dataclass(frozen=True)
class Country:
    code: str
    name: str
    currency: str
    region: str
    zone_label: str | None


@dataclass(frozen=True)
class Area:
    """A day-ahead bidding area's share of one country's population."""

    area: str
    country: str
    weight: float
    entsoe_eic: str | None
    eds_area: str | None


@dataclass(frozen=True)
class Zone:
    country: str
    id: str
    name: str
    area: str | None  # live zones name their bidding area; static zones leave it empty
    weight: float | None  # static zones only; live zones take theirs from areas.csv


@dataclass(frozen=True)
class StaticPrice:
    country: str
    zone: str | None
    price: float
    currency: str
    as_of: str | None


@dataclass(frozen=True)
class Config:
    countries: dict[str, Country]
    areas: list[Area]
    zones: list[Zone]
    tariffs: dict[str, dict]  # scope (country code or area id) -> row, numbers parsed
    static: dict[tuple[str, str | None], StaticPrice]
    settings: dict
    taxes: dict[str, dict]  # zone -> household taxes added to a fetched table price

    def areas_of(self, country: str) -> list[Area]:
        return [a for a in self.areas if a.country == country]

    def zones_of(self, country: str) -> list[Zone]:
        return [z for z in self.zones if z.country == country]

    def tariff(self, country: str, area: str) -> dict:
        """The country's tariff row, with any non-empty field of the area's row on top."""
        row = dict(self.tariffs[country])
        for k, v in self.tariffs.get(area, {}).items():
            if v is not None and k != "scope":
                row[k] = v
        return row


def _rows(name: str, config_dir: Path) -> list[dict]:
    with open(config_dir / name, newline="", encoding="utf-8") as f:
        rows = [{k: (v.strip() or None) for k, v in r.items()} for r in csv.DictReader(f)]
    return [r for r in rows if not (r[next(iter(r))] or "").startswith("#")]


def _num(v: str | None) -> float | None:
    return None if v is None else float(v)


def load(config_dir: Path = CONFIG_DIR, check: bool = True) -> Config:
    countries = {
        r["code"]: Country(r["code"], r["name"], r["currency"], r["region"], r["zone_label"])
        for r in _rows("countries.csv", config_dir)
    }
    areas = [
        Area(r["area"], r["country"], float(r["weight"]), r["entsoe_eic"], r["eds_area"])
        for r in _rows("areas.csv", config_dir)
    ]
    zones = [
        Zone(r["country"], r["id"], r["name"], r["area"], _num(r["weight"]))
        for r in _rows("zones.csv", config_dir)
    ]
    tariffs = {}
    for r in _rows("tariffs.csv", config_dir):
        assert r["scope"] not in tariffs, f"tariffs.csv: duplicate scope {r['scope']}"
        tariffs[r["scope"]] = {k: (_num(v) if k in TARIFF_NUMBERS else v) for k, v in r.items()}
    static = {}
    for r in _rows("static_prices.csv", config_dir):
        key = (r["country"], r["zone"])
        assert key not in static, f"static_prices.csv: duplicate {key}"
        assert r["source"] and r["licence"], f"static_prices.csv: {key} needs source and licence"
        static[key] = StaticPrice(r["country"], r["zone"], float(r["price"]), r["currency"], r["as_of"])
    with open(config_dir / "settings.toml", "rb") as f:
        settings = tomllib.load(f)
    taxes = {r["zone"]: {"rate": float(r["rate"]), "local_rate": float(r["local_rate"]),
                         "per_kwh": float(r["per_kwh"])} for r in _rows("household_taxes.csv", config_dir)}
    cfg = Config(countries, areas, zones, tariffs, static, settings, taxes)
    if check:
        _check(cfg)
    return cfg


def _check(cfg: Config) -> None:
    area_ids = {a.area for a in cfg.areas}
    for a in cfg.areas:
        assert a.country in cfg.countries, f"areas.csv: unknown country {a.country}"
        assert a.entsoe_eic or a.eds_area, f"areas.csv: {a.area} has no source"
        assert a.country in cfg.tariffs, f"tariffs.csv: live country {a.country} has no row"
    for a in cfg.areas:
        for b in cfg.areas:
            if a.area == b.area:
                assert (a.entsoe_eic, a.eds_area) == (b.entsoe_eic, b.eds_area), f"areas.csv: {a.area} sources differ by row"
    for code in {a.country for a in cfg.areas}:
        total = sum(a.weight for a in cfg.areas_of(code))
        assert abs(total - 1) < 1e-6, f"areas.csv: weights for {code} sum to {total}"
    for scope, t in cfg.tariffs.items():
        if scope in cfg.countries:
            for k in ("addon", "vat", "currency", "source", "as_of"):
                assert t[k] is not None, f"tariffs.csv: {scope} needs {k}"
            assert t["currency"] == cfg.countries[scope].currency, f"tariffs.csv: {scope} currency"
        else:
            assert scope in area_ids, f"tariffs.csv: scope {scope} is neither a country nor an area"
    for o in cfg.settings.get("options", []):
        code = o["country"]
        assert o["kind"] == "fixed_energy", f"settings.toml: unknown option kind {o['kind']}"
        assert cfg.areas_of(code), f"settings.toml: option {o['id']} needs a live country"
        assert all(cfg.tariff(code, a.area)["fixed_energy"] is not None for a in cfg.areas_of(code)), (
            f"settings.toml: option {o['id']} but a {code} tariff row has no fixed_energy"
        )
        assert all(z.area for z in cfg.zones_of(code)), f"settings.toml: option {o['id']} needs live zones only"
    guesses = cfg.settings.get("educated_guess", {})
    for code, g in guesses.items():
        assert code in cfg.countries, f"settings.toml: educated_guess {code} is not a country"
        assert set(g) == {"price", "currency", "reason"}, f"settings.toml: educated_guess {code} needs price, currency, reason"
        assert code not in cfg.settings.get("no_published_price", {}), f"settings.toml: {code} is both a guess and no price"
        assert not cfg.areas_of(code) and not cfg.zones_of(code), f"settings.toml: {code} is a guess but has areas or zones"
        assert (code, None) not in cfg.static, f"settings.toml: {code} is a guess but has a static row"
    for code in cfg.settings.get("no_published_price", {}):
        assert code in cfg.countries, f"settings.toml: no_published_price {code} is not a country"
        assert not cfg.areas_of(code) and not cfg.zones_of(code), f"settings.toml: {code} has no published price but has areas or zones"
        assert (code, None) not in cfg.static, f"settings.toml: {code} has no published price but has a static row"
    for code in cfg.settings.get("table_instead_of_live", []):
        assert (code, None) in cfg.static, f"settings.toml: {code} is table_instead_of_live but has no static row"
        assert not any(z.area for z in cfg.zones_of(code)), f"settings.toml: {code} has live zones"
    for c in cfg.countries.values():
        zones = cfg.zones_of(c.code)
        assert bool(zones) == bool(c.zone_label), f"countries.csv: {c.code} zone_label must match zones"
        static_zones = [z for z in zones if z.area is None]
        if c.code in cfg.settings.get("fetched_static", {}):
            continue  # its rows come from a source at run time
        if static_zones and (c.code, None) not in cfg.static:
            total = sum(z.weight or 0 for z in static_zones)
            assert abs(total - 1) < 1e-3, f"zones.csv: {c.code} has no national row and weights sum to {total}"
    for z in cfg.zones:
        if z.area:
            assert any(a.area == z.area and a.country == z.country for a in cfg.areas), f"zones.csv: {z.id} area"
            assert z.weight is None, f"zones.csv: {z.id} is live; its weight belongs in areas.csv"
        elif z.country not in cfg.settings.get("fetched_static", {}):
            assert (z.country, z.id) in cfg.static, f"static_prices.csv: no row for zone {z.id}"
    for country in cfg.settings.get("fetched_static", {}):
        missing = [z.id for z in cfg.zones_of(country) if z.id not in cfg.taxes]
        assert not missing, f"household_taxes.csv: no row for {missing}"
    for (country, _zone), s in cfg.static.items():
        assert country in cfg.countries, f"static_prices.csv: unknown country {country}"
