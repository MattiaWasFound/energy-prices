from datetime import date, datetime, timedelta

from energyprices.slots import UTC, Points, day_start, day_values, delivery_day, expand, slots_in_day


def test_delivery_day_is_central_european():
    assert delivery_day(datetime(2026, 10, 4, 22, 30, tzinfo=UTC)) == date(2026, 10, 5)
    assert delivery_day(datetime(2026, 10, 4, 21, 59, tzinfo=UTC)) == date(2026, 10, 4)


def test_daylight_saving_days_have_100_and_92_quarters():
    assert slots_in_day(date(2026, 10, 25), 15) == 100
    assert slots_in_day(date(2026, 3, 29), 15) == 92
    assert slots_in_day(date(2026, 10, 4), 60) == 24


def _points(d, step, skip=()):
    start = day_start(d)
    n = slots_in_day(d, step)
    return Points(step, {start + timedelta(minutes=i * step): float(i) for i in range(n) if i not in skip})


def test_short_gap_carries_previous_value_forward():
    d = date(2026, 10, 4)
    values = day_values(_points(d, 15, skip={10, 11}), d)
    assert values[10] == values[11] == 9.0 and values[12] == 12.0


def test_long_gap_or_missing_first_slot_makes_the_day_incomplete():
    d = date(2026, 10, 4)
    assert day_values(_points(d, 15, skip=set(range(10, 19))), d) is None
    assert day_values(_points(d, 15, skip={0}), d) is None
    assert day_values(_points(d, 15), d + timedelta(days=1)) is None


def test_expand_repeats_coarse_slots():
    assert expand([1.0, 2.0], 60, 15) == [1.0] * 4 + [2.0] * 4
