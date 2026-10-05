"""The shipped config/ tables and schema, as the job will read them."""

import jsonschema

from energyprices import config, validate


def test_schema_is_a_valid_2020_12_schema():
    jsonschema.Draft202012Validator.check_schema(validate.schema())


def test_shipped_config_loads_and_cross_checks():
    cfg = config.load()
    assert cfg.countries


def test_every_iso_country_plus_kosovo_is_configured():
    import csv
    from pathlib import Path
    iso = {r["alpha2"] for r in csv.DictReader(open(Path(__file__).parent.parent / "browse" / "iso-numeric.csv"))}
    assert len(iso) == 249
    assert set(config.load().countries) == iso | {"XK"}
