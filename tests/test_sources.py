from datetime import datetime

import pytest

from energyprices.slots import UTC
from energyprices.sources import ecb, eds, entsoe


def test_eds_parses_all_areas_at_15_minutes(fixture_bytes):
    got = eds.parse(fixture_bytes("eds_dayahead_2026-10-04.json"))
    assert sorted(got) == ["DE", "DK1", "DK2", "NO2", "SE3", "SE4"]
    for p in got.values():
        assert p.step == 15 and len(p.prices) == 192
    assert got["SE4"].prices[datetime(2026, 10, 3, 22, tzinfo=UTC)] == pytest.approx(113.349998)


def test_ecb_parses_rates(fixture_bytes):
    day, rates = ecb.parse(fixture_bytes("ecb_eurofxref_2026-10-02.xml"))
    assert day == "2026-10-02" and rates["DKK"] == pytest.approx(7.4736) and "EUR" not in rates


DOC = """<?xml version="1.0" encoding="UTF-8"?>
<Publication_MarketDocument xmlns="urn:iec62325.351:tc57wg16:451-3:publicationdocument:7:3">
  <TimeSeries>
    <currency_Unit.name>EUR</currency_Unit.name>
    <price_Measure_Unit.name>MWH</price_Measure_Unit.name>
    <curveType>A03</curveType>
    <Period>
      <timeInterval><start>2026-10-03T22:00Z</start><end>2026-10-03T23:00Z</end></timeInterval>
      <resolution>PT15M</resolution>
      <Point><position>1</position><price.amount>10</price.amount></Point>
      <Point><position>3</position><price.amount>-5.5</price.amount></Point>
    </Period>
  </TimeSeries>
  <TimeSeries>
    <currency_Unit.name>EUR</currency_Unit.name>
    <price_Measure_Unit.name>MWH</price_Measure_Unit.name>
    <curveType>A01</curveType>
    <Period>
      <timeInterval><start>2026-10-03T22:00Z</start><end>2026-10-04T00:00Z</end></timeInterval>
      <resolution>PT60M</resolution>
      <Point><position>1</position><price.amount>99</price.amount></Point>
      <Point><position>2</position><price.amount>20</price.amount></Point>
    </Period>
  </TimeSeries>
</Publication_MarketDocument>"""


def test_entsoe_expands_a03_and_fills_coarser_hours_into_finer_slots():
    p = entsoe.parse(DOC.encode())
    t = lambda h, m: datetime(2026, 10, 3, h, m, tzinfo=UTC)
    assert p.step == 15
    # A03: position 2 repeats position 1, position 4 repeats position 3.
    assert [p.prices[t(22, m)] for m in (0, 15, 30, 45)] == [10, 10, -5.5, -5.5]
    # The second hour exists only hourly, so it is split into quarters.
    assert [p.prices[t(23, m)] for m in (0, 15, 30, 45)] == [20] * 4


def test_entsoe_acknowledgement_is_no_data():
    ack = b"""<Acknowledgement_MarketDocument xmlns="urn:iec62325.351:tc57wg16:451-1:acknowledgementdocument:7:0">
      <Reason><code>999</code><text>No matching data found</text></Reason></Acknowledgement_MarketDocument>"""
    with pytest.raises(entsoe.NoData, match="No matching data"):
        entsoe.parse(ack)


def _day(name, d):
    from energyprices.slots import day_values
    from pathlib import Path
    p = entsoe.parse((Path(__file__).parent / "fixtures" / name).read_bytes())
    return p, day_values(p, d)


def test_entsoe_real_15_minute_document_fills_a03_repeats():
    from datetime import date
    # 91 points for 96 quarters: A03 omits a point that repeats the one before.
    p, values = _day("entsoe_se3_2026-10-05.xml", date(2026, 10, 5))
    assert p.step == 15 and len(values) == 96 and values[:3] == [5.01, 4.95, 3.0]
    assert min(values) == -5.05  # negative prices pass through


def test_entsoe_real_hourly_document():
    from datetime import date
    p, values = _day("entsoe_ch_2026-10-05.xml", date(2026, 10, 5))
    assert p.step == 60 and len(values) == 24 and values[:3] == [192.11, 180.0, 175.1]


def test_entsoe_two_auctions_keeps_sequence_1():
    from datetime import date
    # DE-LU: sequence 2 (EXAA) comes first in the document and starts at 200;
    # sequence 1 (SDAC) starts at 161.27.
    _p, values = _day("entsoe_de-lu_2026-10-05.xml", date(2026, 10, 5))
    assert values[0] == 161.27 and len(values) == 96


def test_entsoe_duplicate_unsequenced_series():
    from datetime import date
    # NO3 (and PL) send the same curve twice, mRID 1 and 2, with no sequence.
    p, values = _day("entsoe_no3_2026-10-05.xml", date(2026, 10, 5))
    assert p.step == 15 and len(values) == 96 and values[0] == 19.68


def test_entsoe_matches_energi_data_service(fixture_bytes):
    # Both publish the same SDAC result; recorded within a minute of each other.
    e = eds.parse(fixture_bytes("eds_dayahead_2026-10-05.json"))
    for area, name in [("SE3", "entsoe_se3_2026-10-05.xml"), ("DE", "entsoe_de-lu_2026-10-05.xml")]:
        p = entsoe.parse(fixture_bytes(name))
        assert p.prices.keys() == e[area].prices.keys()
        assert all(abs(p.prices[t] - e[area].prices[t]) < 0.001 for t in p.prices)


def test_entsoe_real_acknowledgement(fixture_bytes):
    # Sent with HTTP 200 when an area has nothing for the interval.
    with pytest.raises(entsoe.NoData, match="No matching data found"):
        entsoe.parse(fixture_bytes("entsoe_ack_ie-sem_2026-10-05.xml"))


def test_eia_latest_complete_month_states_and_us(fixture_bytes):
    from energyprices.sources import eia
    period, prices, sales = eia.parse(fixture_bytes("eia_retail_sales_res_2026-07.json"))
    assert sales["CA"] > sales["VT"] > 0
    assert period == "2026-07" and len(prices) == 52  # 50 states, DC and the US
    assert prices["US"] == pytest.approx(0.1831) and prices["CA"] == pytest.approx(0.3361)
    assert not any(len(k) != 2 for k in prices)  # census divisions dropped
