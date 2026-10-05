"""Record fresh source responses into tests/fixtures/ for a given delivery day.

    ENTSOE_TOKEN=… uv run python tools/record_fixtures.py [--day 2026-10-04] [--areas SE3,DE-LU,NO3,CH,IE-SEM,PL]

Writes entsoe_<area>_<day>.xml for each area (needs ENTSOE_TOKEN in the
environment), eds_dayahead_<day>.json, ecb_eurofxref_<day>.xml and
frankfurter_v2_rates_eur_<day>.json. Tests reference fixtures by name, so a
re-recording that should replace a borrowed file is a rename in the test too.
"""

import argparse
import os
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from energyprices import config  # noqa: E402
from energyprices.slots import day_start  # noqa: E402
from energyprices.sources import ecb, eds, entsoe, frankfurter  # noqa: E402

FIXTURES = Path(__file__).resolve().parent.parent / "tests" / "fixtures"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--day", default=date.today().isoformat())
    p.add_argument("--areas", default="SE3,DE-LU,NO3,CH,IE-SEM,PL")
    args = p.parse_args()
    day = date.fromisoformat(args.day)
    start, end = day_start(day), day_start(day + timedelta(days=1))
    eics = {a.area: a.entsoe_eic for a in config.load(check=False).areas}

    def save(name: str, body: bytes) -> None:
        (FIXTURES / name).write_bytes(body)
        print(f"wrote {name} ({len(body)} bytes)")

    token = os.environ.get("ENTSOE_TOKEN")
    if token:
        for area in args.areas.split(","):
            save(f"entsoe_{area.lower()}_{day}.xml", entsoe.fetch(token, eics[area], start, end))
    else:
        print("ENTSOE_TOKEN not set: skipping ENTSO-E")
    save(f"eds_dayahead_{day}.json", eds.fetch(["DK1", "DK2", "DE", "NO2", "SE3", "SE4"], start, end))
    save(f"ecb_eurofxref_{day}.xml", ecb.fetch())
    save(f"frankfurter_v2_rates_eur_{day}.json", frankfurter.fetch())


if __name__ == "__main__":
    main()
