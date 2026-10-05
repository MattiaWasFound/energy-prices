"""Import researched country prices into config/static_prices.csv.

    uv run python tools/import_prices.py research.csv [more.csv ...] [--skip CF,HT] [--dry-run]

Input columns:
    country,price,currency,as_of,consumption_kwh_month,includes,source_url,licence,confidence,note

A row replaces the existing country-level row for that country (zone rows are
untouched); rows with an empty price are reported and skipped. Every imported
row keeps its source, licence and confidence, and the note records what the
figure includes and at what consumption.
"""

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TABLE = ROOT / "config" / "static_prices.csv"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("files", nargs="+", type=Path)
    p.add_argument("--skip", default="", help="comma list of country codes to leave out")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    skip = {c for c in args.skip.split(",") if c}

    rows = list(csv.DictReader(open(TABLE, encoding="utf-8")))
    fields = list(rows[0])
    by_key = {(r["country"], r["zone"]): r for r in rows}
    imported, empty = [], []
    for f in args.files:
        for r in csv.DictReader(open(f, encoding="utf-8")):
            code = r["country"].strip()
            if code in skip:
                continue
            if not (r.get("price") or "").strip():
                empty.append(code)
                continue
            as_of = (r.get("as_of") or "").strip()
            as_of = as_of if re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])", as_of) else ""
            kwh = (r.get("consumption_kwh_month") or "").strip()
            note = "; ".join(x for x in [
                f"{r['confidence'].strip()} confidence" if r.get("confidence") else "",
                f"at {kwh} kWh/month" if kwh else "",
                (r.get("note") or "").strip(),
            ] if x)
            by_key[(code, "")] = {
                "country": code, "zone": "", "price": str(float(r["price"])), "currency": r["currency"].strip(),
                "as_of": as_of, "source": f"{(r.get('includes') or '').strip()} | {r['source_url'].strip()}",
                "licence": r["licence"].strip(), "note": note,
            }
            imported.append(code)
    out = sorted(by_key.values(), key=lambda r: (r["country"], r["zone"]))
    print(f"imported {len(imported)}: {' '.join(sorted(imported))}", file=sys.stderr)
    if empty:
        print(f"no price (left to the fallback chain): {' '.join(sorted(empty))}", file=sys.stderr)
    if args.dry_run:
        return
    with open(TABLE, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(out)


if __name__ == "__main__":
    main()
