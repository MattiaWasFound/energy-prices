"""The job's IO edge: sources turned into build inputs, with the network stubbed."""

import pytest

from energyprices import __main__ as job
from energyprices import config
from energyprices.sources import eia


def test_eia_rows_add_household_taxes(monkeypatch, fixture_bytes):
    monkeypatch.setenv("EIA_API_KEY", "test")
    monkeypatch.setattr(eia, "fetch", lambda key: fixture_bytes("eia_retail_sales_res_2026-07.json"))
    cfg = config.load()
    rows = job.fetch_tables(cfg, set(), lambda msg: None)["US"]
    assert len(rows) == 52
    _period, prices, _sales = eia.parse(fixture_bytes("eia_retail_sales_res_2026-07.json"))
    assert rows["US-CT"].price == pytest.approx(prices["CT"])  # residential exempt
    assert rows["US-IN"].price == pytest.approx(prices["IN"] * 1.07)  # 7% sales tax
    assert rows["US-DC"].price == pytest.approx(prices["DC"] + 0.007)  # per-kWh delivery tax
    assert prices["US"] < rows[None].price < prices["US"] * 1.06  # sales-weighted national uplift


def test_eia_failure_is_none_not_an_exception(monkeypatch):
    monkeypatch.delenv("EIA_API_KEY", raising=False)
    logged = []
    assert job.fetch_tables(config.load(), set(), logged.append) == {"US": None}
    assert logged == ["eia: EIA_API_KEY is not set"]
