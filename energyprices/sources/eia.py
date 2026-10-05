"""US EIA: average residential electricity price by state, monthly (API v2, needs a free key).

`electricity/retail-sales`, sector RES: revenue / sales in cents per kWh, for
the 50 states, DC, the census divisions and the US as a whole. State figures
lag about two months. US government work, public domain.

Revenue includes taxes the utility pays (gross receipts, franchise) but most
likely not taxes levied on the household (sales tax, utility users' taxes);
config/household_taxes.csv adds those.
"""

import json

from .. import http

URL = "https://api.eia.gov/v2/electricity/retail-sales/data/"


def fetch(key: str) -> bytes:
    # The key rides in the query string (EIA v2 has no header form); http.get
    # keeps URLs out of its error messages.
    return http.get(URL, {
        "api_key": key,
        "frequency": "monthly",
        "data[0]": "price",
        "data[1]": "sales",
        "facets[sectorid][]": "RES",
        "sort[0][column]": "period",
        "sort[0][direction]": "desc",
        "length": "200",
    })


def parse(body: bytes) -> tuple[str, dict[str, float], dict[str, float]]:
    """(latest month every state has, state or "US" -> USD per kWh,
    state -> residential sales in MWh that month). Census divisions dropped."""
    rows = [r for r in json.loads(body)["response"]["data"]
            if len(r["stateid"]) == 2 and r.get("price") not in (None, "")]
    prices: dict[str, dict[str, float]] = {}
    sales: dict[str, dict[str, float]] = {}
    for r in rows:
        prices.setdefault(r["period"], {})[r["stateid"]] = round(float(r["price"]) / 100, 6)
        if r.get("sales") not in (None, ""):
            sales.setdefault(r["period"], {})[r["stateid"]] = float(r["sales"])
    # The newest month is sometimes published for only some states first.
    complete = [p for p, states in prices.items() if len(states) >= 52]
    assert complete, "no month with every state in the EIA response"
    period = max(complete)
    return period, prices[period], sales.get(period, {})
