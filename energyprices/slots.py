"""Delivery days and price slots.

European day-ahead markets trade one delivery day at a time, and that day runs
00:00-24:00 Central European time for every coupled zone, including the ones in
other time zones. A day therefore has 92, 96 or 100 quarter-hours.
"""

from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

CET = ZoneInfo("Europe/Brussels")
UTC = timezone.utc

# A gap of up to this many minutes inside a day is filled by carrying the
# previous slot forward. A longer one makes the day incomplete.
MAX_GAP_MINUTES = 120


@dataclass(frozen=True)
class Points:
    """One bidding area's spot prices in EUR/MWh, keyed by slot start (UTC)."""

    step: int
    prices: dict[datetime, float]


def delivery_day(now: datetime) -> date:
    return now.astimezone(CET).date()


def day_start(d: date) -> datetime:
    return datetime(d.year, d.month, d.day, tzinfo=CET).astimezone(UTC)


def slots_in_day(d: date, step: int) -> int:
    minutes = (day_start(d + timedelta(days=1)) - day_start(d)) // timedelta(minutes=1)
    assert minutes % step == 0, (d, step)
    return minutes // step


def day_values(points: Points, d: date) -> list[float] | None:
    """The day's prices at the points' own step, short gaps carried forward.
    None when the day is missing or has a gap longer than MAX_GAP_MINUTES."""
    start, n, step = day_start(d), slots_in_day(d, points.step), points.step
    raw = [points.prices.get(start + timedelta(minutes=i * step)) for i in range(n)]
    if raw[0] is None:
        # A missing first slot has nothing to carry forward from.
        return None
    out, gap = [], 0
    for v in raw:
        gap = gap + 1 if v is None else 0
        if gap * step > MAX_GAP_MINUTES:
            return None
        out.append(out[-1] if v is None else v)
    return out


def expand(values: list[float], step: int, to_step: int) -> list[float]:
    assert step % to_step == 0, (step, to_step)
    k = step // to_step
    return [v for v in values for _ in range(k)]
