import dataclasses
import json
from datetime import datetime

import pytest

from energyprices import validate
from energyprices.build import build
from energyprices.slots import UTC
from energyprices.sources import eds

FX = {"EUR": 1.0, "DKK": 7.47, "SEK": 11.0, "NOK": 11.7, "USD": 1.12}
# 14:00 CEST on 4 October: today's and tomorrow's prices are both published.
AFTERNOON = datetime(2026, 10, 4, 12, 0, tzinfo=UTC)
MORNING = datetime(2026, 10, 4, 8, 0, tzinfo=UTC)


@pytest.fixture
def spot(fixture_bytes):
    return eds.parse(fixture_bytes("eds_dayahead_2026-10-04.json"))


def _build(cfg, spot, now=AFTERNOON, fx=FX, previous=None):
    doc, notes = build(now, cfg, spot, fx, previous)
    assert validate.check(doc, cfg, now) == [], notes
    return doc, notes


def test_live_entry_covers_today_and_tomorrow_with_addon_and_vat(cfg, spot):
    doc, _ = _build(cfg, spot)
    dk = doc["countries"]["DK"]["average"]
    assert dk["precision"] == "live" and dk["basis"] == "day-ahead"
    s = dk["series"]
    assert s["start"] == "2026-10-03T22:00:00Z" and s["step_minutes"] == 15 and len(s["values"]) == 192
    first = datetime(2026, 10, 3, 22, tzinfo=UTC)
    expected = sum(w * (spot[a].prices[first] / 1000 * 7.47 + 1.0) * 1.25 for a, w in (("DK1", .45), ("DK2", .55)))
    assert s["values"][0] == pytest.approx(expected, abs=1e-4)
    # flat is the mean of the most recent complete day (tomorrow).
    assert dk["flat"] == pytest.approx(sum(s["values"][96:]) / 96, abs=1e-3)


def test_series_ends_after_today_when_tomorrow_is_not_published(cfg, spot):
    cut = datetime(2026, 10, 4, 22, tzinfo=UTC)
    today_only = {a: dataclasses.replace(p, prices={t: v for t, v in p.prices.items() if t < cut})
                  for a, p in spot.items()}
    doc, _ = _build(cfg, today_only, now=MORNING)
    assert len(doc["countries"]["DK"]["average"]["series"]["values"]) == 96


def test_zone_override_and_population_weighting(cfg, spot):
    se = _build(cfg, spot)[0]["countries"]["SE"]
    assert se["zone_label"] == "Elområde" and [z["id"] for z in se["zones"]] == ["SE3", "SE4"]
    se3, se4 = (z["series"]["values"][0] for z in se["zones"])
    assert se["average"]["series"]["values"][0] == pytest.approx(0.7 * se3 + 0.3 * se4, abs=2e-4)
    first = datetime(2026, 10, 3, 22, tzinfo=UTC)
    assert se4 == pytest.approx((spot["SE4"].prices[first] / 1000 * 11 + 0.9) * 1.25, abs=1e-4)


def test_support_scheme_pays_share_above_threshold(cfg, spot):
    no = _build(cfg, spot)[0]["countries"]["NO"]["average"]
    first = datetime(2026, 10, 3, 22, tzinfo=UTC)
    raw = spot["NO2"].prices[first] / 1000 * 11.7
    paid = raw - max(0, raw - 0.9625) * 0.9
    assert no["series"]["values"][0] == pytest.approx((paid + 0.6) * 1.25, abs=1e-4)


def test_norgespris_is_an_option_beside_spot(cfg, spot):
    no = _build(cfg, spot)[0]["countries"]["NO"]
    assert no["average"]["basis"] == "day-ahead"
    (opt,) = no["options"]
    assert opt["id"] == "norgespris" and opt["name"] == "Norgespris"
    assert opt["average"] == {"precision": "estimated", "basis": "country-table", "as_of": "2026-01",
                              "flat": pytest.approx((0.4 + 0.6) * 1.25)}
    assert opt["zones"] == []  # tests/config has no Norwegian zones
    assert "options" not in _build(cfg, spot)[0]["countries"]["DK"]


def test_fallback_chain_static_zones_regional_global(cfg, spot):
    c = _build(cfg, spot)[0]["countries"]
    assert c["FI"]["average"] == {"precision": "estimated", "basis": "country-table", "as_of": "2025-12", "flat": 0.2}
    assert c["US"]["average"]["flat"] == pytest.approx(0.4 * 0.33 + 0.6 * 0.15)
    assert c["US"]["average"]["as_of"] == "2026-07"
    assert c["AQ"]["average"]["basis"] == "global-average"
    assert c["AQ"]["zone_label"] is None and c["AQ"]["zones"] == []


def test_failed_source_carries_previous_entries_forward(cfg, spot):
    yesterday, _ = _build(cfg, spot)
    # The next day, every live source fails.
    next_day = datetime(2026, 10, 5, 12, 0, tzinfo=UTC)
    doc, notes = _build(cfg, {a: None for a in spot}, now=next_day, previous=yesterday)
    dk_before, dk = yesterday["countries"]["DK"]["average"], doc["countries"]["DK"]["average"]
    assert dk["basis"] == "day-ahead" and dk["flat"] == dk_before["flat"]
    assert dk["series"]["start"] == "2026-10-04T22:00:00Z"
    assert dk["series"]["values"] == dk_before["series"]["values"][96:]
    assert any("DK: no fresh day-ahead prices, carried forward" in n for n in notes)
    # A day later still, the carried series no longer reaches today and is dropped.
    later = datetime(2026, 10, 6, 12, 0, tzinfo=UTC)
    doc2, _ = _build(cfg, {a: None for a in spot}, now=later, previous=doc)
    assert "series" not in doc2["countries"]["DK"]["average"]
    assert doc2["countries"]["DK"]["average"]["flat"] == dk_before["flat"]
    assert set(doc2["countries"]) == set(cfg.countries)


def test_failed_fx_carries_previous_rates(cfg, spot):
    first, _ = _build(cfg, spot)
    doc, notes = _build(cfg, spot, fx={"EUR": 1.0, "DKK": 7.5}, previous=first)
    assert doc["fx"] == {**first["fx"], "DKK": 7.5}
    assert "fx: carried forward from the previous file: NOK, SEK, USD" in notes


def test_no_data_and_no_previous_falls_back_without_dropping_a_country(cfg):
    doc, _ = _build(cfg, {})
    assert doc["countries"]["DK"]["average"]["basis"] == "regional-average"
    assert doc["countries"]["SE"]["zones"][0]["basis"] == "regional-average"


def test_idempotent_apart_from_generated_at(cfg, spot):
    a, _ = build(AFTERNOON, cfg, spot, FX, None)
    b, _ = build(AFTERNOON.replace(minute=30), cfg, spot, FX, a)
    a.pop("generated_at"), b.pop("generated_at")
    assert json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)


def test_validation_rejects_bad_documents(cfg, spot):
    doc, _ = _build(cfg, spot)
    bad = json.loads(json.dumps(doc))
    bad["countries"]["DK"]["average"]["series"]["start"] = "2026-10-02T22:00:00Z"
    bad["countries"]["FI"]["average"]["flat"] = 40.0
    del bad["countries"]["AQ"]
    problems = validate.check(bad, cfg, AFTERNOON)
    assert any("DK: series starts" in p for p in problems)
    assert any("FI:" in p and "outside" in p for p in problems)
    assert any("countries missing: ['AQ']" in p for p in problems)
    schema_bad = json.loads(json.dumps(doc))
    schema_bad["countries"]["FI"]["average"]["precision"] = "live"
    assert validate.check(schema_bad, cfg, AFTERNOON)[0].startswith("schema:")


def test_table_instead_of_live_uses_the_static_row(cfg, spot):
    cfg = dataclasses.replace(cfg, settings={**cfg.settings, "table_instead_of_live": ["DK"]},
                              static={**cfg.static, ("DK", None): dataclasses.replace(cfg.static[("FI", None)], country="DK", price=2.5, currency="DKK")})
    doc, notes = _build(cfg, spot)
    assert doc["countries"]["DK"]["average"] == {"precision": "estimated", "basis": "country-table", "as_of": "2025-12", "flat": 2.5}
    assert not any(n.startswith("DK:") for n in notes)


def test_no_published_price_has_a_reason_and_no_price(cfg, spot):
    cfg = dataclasses.replace(cfg, settings={**cfg.settings, "no_published_price": {"AQ": "No permanent residents."}})
    doc, notes = _build(cfg, spot)
    aq = doc["countries"]["AQ"]
    assert aq["average"] == {"precision": "none", "basis": "no-published-price", "reason": "No permanent residents."}
    assert aq["zones"] == [] and aq["zone_label"] is None
    assert not any(n.startswith("AQ:") for n in notes)
    bad = json.loads(json.dumps(doc))
    bad["countries"]["AQ"]["average"]["flat"] = 0.2
    assert validate.check(bad, cfg, AFTERNOON)[0].startswith("schema:")
    bad = json.loads(json.dumps(doc))
    del bad["countries"]["FI"]["average"]["flat"]
    assert validate.check(bad, cfg, AFTERNOON)[0].startswith("schema:")


def test_educated_guess_is_converted_labelled_and_kept_out_of_the_means(cfg, spot):
    plain = _build(cfg, spot)[0]["countries"]
    cfg = dataclasses.replace(cfg, settings={**cfg.settings, "educated_guess": {
        "FI": {"price": 0.5, "currency": "EUR", "reason": "A guess."}}},
        static={k: v for k, v in cfg.static.items() if k != ("FI", None)})
    c = _build(cfg, spot)[0]["countries"]
    assert c["FI"]["average"] == {"precision": "estimated", "basis": "educated-guess", "reason": "A guess.", "flat": 0.5}
    # AQ's global average is computed without the guess: FI was in it before, so it moves.
    assert c["AQ"]["average"]["flat"] != plain["AQ"]["average"]["flat"]
    assert c["AQ"]["average"]["basis"] == "global-average"


def _eia_rows(cfg, us=0.18, ca=0.40, tx=0.14):
    from energyprices.config import StaticPrice
    return {"US": {None: StaticPrice("US", None, us, "USD", "2026-07"),
                   "US-CA": StaticPrice("US", "US-CA", ca, "USD", "2026-07"),
                   "US-TX": StaticPrice("US", "US-TX", tx, "USD", "2026-07")}}


def test_fetched_table_replaces_config_rows_and_uses_the_national_figure(cfg, spot):
    doc, _ = build(AFTERNOON, cfg, spot, FX, None, _eia_rows(cfg))
    us = doc["countries"]["US"]
    assert us["average"] == {"precision": "estimated", "basis": "country-table", "as_of": "2026-07", "flat": 0.18}
    assert [(z["id"], z["flat"]) for z in us["zones"]] == [("US-CA", 0.4), ("US-TX", 0.14)]


def test_failed_table_source_carries_the_previous_entries(cfg, spot):
    first, _ = build(AFTERNOON, cfg, spot, FX, None, _eia_rows(cfg))
    doc, notes = _build_fetched(cfg, spot, first, {"US": None})
    assert doc["countries"]["US"] == first["countries"]["US"]
    assert "US: table source failed, carried forward" in notes


def test_failed_table_source_without_previous_falls_back_to_config_rows(cfg, spot):
    doc, notes = _build_fetched(cfg, spot, None, {"US": None})
    assert doc["countries"]["US"]["zones"][0]["flat"] == 0.33  # tests/config/static_prices.csv
    assert "US/US-CA: table source failed, nothing to carry" in notes


def _build_fetched(cfg, spot, previous, fetched):
    doc, notes = build(AFTERNOON, cfg, spot, FX, previous, fetched)
    assert validate.check(doc, cfg, AFTERNOON) == [], notes
    return doc, notes
