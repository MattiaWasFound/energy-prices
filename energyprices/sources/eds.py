"""Energi Data Service (Energinet): day-ahead prices, no key.

Dataset `DayAheadPrices` replaced `Elspotprices` when the market moved to
15-minute slots (2025-10-01). It carries DK1, DK2 and the neighbouring areas
DE, NO2, SE3 and SE4. The job uses it as the backup for whichever of those
areas have an `eds_area` in config/areas.csv.
"""

import json
from datetime import datetime, timedelta

from .. import http
from ..slots import UTC, Points

URL = "https://api.energidataservice.dk/dataset/DayAheadPrices"


def fetch(areas: list[str], start: datetime, end: datetime) -> bytes:
    fmt = "%Y-%m-%dT%H:%M"
    return http.get(URL, {
        "start": start.astimezone(UTC).strftime(fmt),
        "end": end.astimezone(UTC).strftime(fmt),
        "timezone": "UTC",
        "filter": json.dumps({"PriceArea": areas}, separators=(",", ":")),
        "columns": "TimeUTC,PriceArea,DayAheadPriceEUR",
        "sort": "TimeUTC asc",
        "limit": "0",
    })


def parse(body: bytes) -> dict[str, Points]:
    """EDS area code -> Points. The step is read from the data, so a return
    to hourly publication would be picked up without a code change."""
    by_area: dict[str, dict[datetime, float]] = {}
    for r in json.loads(body)["records"]:
        if r["DayAheadPriceEUR"] is None:
            continue
        t = datetime.fromisoformat(r["TimeUTC"]).replace(tzinfo=UTC)
        by_area.setdefault(r["PriceArea"], {})[t] = float(r["DayAheadPriceEUR"])
    out = {}
    for area, prices in by_area.items():
        times = sorted(prices)
        steps = {(b - a) // timedelta(minutes=1) for a, b in zip(times, times[1:])}
        out[area] = Points(step=min(steps) if steps else 60, prices=prices)
    return out
