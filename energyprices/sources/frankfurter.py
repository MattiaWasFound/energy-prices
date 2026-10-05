"""Frankfurter v2: a blend of ~100 central banks' reference rates, every billing currency.

Used for the currencies the ECB does not quote. Each quote carries its own date;
the caller drops stale ones. Code MIT; each rate falls under its central bank's
terms, so README.md credits the source (https://frankfurter.dev/license/).
"""

import json
from datetime import date

from .. import http

URL = "https://api.frankfurter.dev/v2/rates"


def fetch() -> bytes:
    return http.get(URL, {"base": "EUR"})


def parse(body: bytes) -> dict[str, tuple[date, float]]:
    """currency -> (quote date, units per EUR)."""
    out = {}
    for q in json.loads(body):
        assert q["base"] == "EUR", q
        if q["rate"] and q["rate"] > 0:
            out[q["quote"]] = (date.fromisoformat(q["date"]), float(q["rate"]))
    assert out, "empty Frankfurter response"
    return out
