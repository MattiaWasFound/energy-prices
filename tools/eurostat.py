"""Refresh the European static prices and print the add-on baseline for live countries.

    uv run python tools/eurostat.py [--period 2025-S2]

Reads Eurostat nrg_pc_204 (household electricity, band DC 2 500-4 999 kWh/year,
all taxes / excluding VAT, national currency) and Ember's monthly wholesale
prices. Prints two CSV blocks for a human to paste into config/:

1. static_prices.csv rows for every country Eurostat covers, from the
   all-taxes price. Live countries need one too: it is their fallback when
   there is no fresh day-ahead data and nothing to carry forward.
2. The add-on baseline for every live country: the price excluding VAT minus the
   period's mean wholesale price, in national currency per kWh. tariffs.csv
   starts from this and adds the tax changes since the period (see the row's note).

It writes nothing itself: the tables are hand-maintained, and a semester's
refresh is a reviewed diff. Licences: Eurostat, reuse with the source
acknowledged; Ember, CC BY 4.0.
"""

import argparse
import csv
import io
import json
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from energyprices import config, http  # noqa: E402

EUROSTAT = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nrg_pc_204"
EMBER = "https://files.ember-energy.org/public-downloads/price/outputs/european_wholesale_electricity_price_data_monthly.csv"
# Eurostat's own geo codes where they differ from ISO 3166-1.
GEO_TO_ISO = {"EL": "GR", "UK": "GB"}
# Eurostat still reports 2025 in BGN; Bulgaria bills in EUR since 2026-01-01 at the fixed rate.
FIXED_CONVERSION = {"BGN": ("EUR", 1.95583)}
SEMESTER_MONTHS = {"S1": ["01", "02", "03", "04", "05", "06"], "S2": ["07", "08", "09", "10", "11", "12"]}


def _get(url: str, params: list[tuple[str, str]] | None = None) -> bytes:
    return http.get(url + ("?" + urllib.parse.urlencode(params) if params else ""))


def eurostat(period: str) -> dict[tuple[str, str, str], float]:
    """(iso country, tax, currency) -> price per kWh."""
    params = [("format", "JSON"), ("nrg_cons", "KWH2500-4999"), ("unit", "KWH"), ("time", period),
              ("tax", "I_TAX"), ("tax", "X_VAT"), ("currency", "NAC"), ("currency", "EUR")]
    d = json.loads(_get(EUROSTAT, params))
    dims = d["id"]
    sizes = d["size"]
    index = {dim: {pos: code for code, pos in d["dimension"][dim]["category"]["index"].items()} for dim in dims}
    out = {}
    for flat, value in d["value"].items():
        flat, coords = int(flat), {}
        for dim, size in reversed(list(zip(dims, sizes))):
            coords[dim] = index[dim][flat % size]
            flat //= size
        geo = GEO_TO_ISO.get(coords["geo"], coords["geo"])
        if len(geo) == 2:
            out[(geo, coords["tax"], coords["currency"])] = float(value)
    return out


def ember(period: str) -> dict[str, float]:
    """ISO3 -> mean wholesale EUR/MWh over the semester's months."""
    year, sem = period.split("-")
    months = {f"{year}-{m}-01" for m in SEMESTER_MONTHS[sem]}
    sums: dict[str, list[float]] = {}
    for r in csv.DictReader(io.StringIO(_get(EMBER).decode())):
        if r["Date"] in months and r["Price (EUR/MWhe)"]:
            sums.setdefault(r["ISO3 Code"], []).append(float(r["Price (EUR/MWhe)"]))
    return {k: sum(v) / len(v) for k, v in sums.items() if len(v) == len(months)}


ISO3 = {"AL": "ALB", "AT": "AUT", "BE": "BEL", "BG": "BGR", "CH": "CHE", "CZ": "CZE", "DE": "DEU", "DK": "DNK",
        "EE": "EST", "ES": "ESP", "FI": "FIN", "FR": "FRA", "GB": "GBR", "GR": "GRC", "HR": "HRV", "HU": "HUN",
        "IE": "IRL", "IT": "ITA", "LT": "LTU", "LU": "LUX", "LV": "LVA", "ME": "MNE", "MK": "MKD", "NL": "NLD",
        "NO": "NOR", "PL": "POL", "PT": "PRT", "RO": "ROU", "RS": "SRB", "SE": "SWE", "SI": "SVN", "SK": "SVK"}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--period", default="2025-S2")
    args = p.parse_args()
    cfg = config.load(check=False)  # the tool exists to fill the tables the check needs
    year, sem = args.period.split("-")
    as_of = f"{year}-{SEMESTER_MONTHS[sem][-1]}"
    es = eurostat(args.period)
    live = {a.country for a in cfg.areas}
    def nac(geo: str, tax: str) -> tuple[float, str] | None:
        """The price in the currency the country bills in today."""
        v = es.get((geo, tax, "NAC"))
        if v is None or geo not in cfg.countries:
            return None
        if geo == "BG":
            cur, rate = FIXED_CONVERSION["BGN"]
            return v / rate, cur
        return v, cfg.countries[geo].currency

    w = csv.writer(sys.stdout, lineterminator="\n")
    print(f"# static_prices.csv rows (Eurostat nrg_pc_204 {args.period}, band DC, all taxes)")
    for geo in sorted(cfg.countries):
        got = nac(geo, "I_TAX")
        if got:
            w.writerow([geo, "", round(got[0], 4), got[1], as_of,
                        f"Eurostat nrg_pc_204 {args.period} band DC all taxes",
                        "Eurostat: reuse authorised, source acknowledged", ""])
    print(f"\n# add-on baseline (Eurostat excl. VAT minus Ember mean wholesale, {args.period})")
    w.writerow(["country", "currency", "price_excl_vat", "wholesale_per_kwh", "addon_baseline", "effective_vat"])
    wholesale = ember(args.period)
    for geo in sorted(live):
        x_vat, i_tax = nac(geo, "X_VAT"), nac(geo, "I_TAX")
        eur_x = es.get((geo, "X_VAT", "EUR"))
        if not x_vat or geo not in ISO3 or ISO3[geo] not in wholesale or not eur_x:
            w.writerow([geo, "", "", "", "missing", ""])
            continue
        rate = x_vat[0] / eur_x
        ws = wholesale[ISO3[geo]] / 1000 * rate
        w.writerow([geo, x_vat[1], round(x_vat[0], 4), round(ws, 4), round(x_vat[0] - ws, 4),
                    round(i_tax[0] / x_vat[0] - 1, 4)])


if __name__ == "__main__":
    main()
