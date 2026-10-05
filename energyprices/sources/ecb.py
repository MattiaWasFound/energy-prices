"""European Central Bank euro foreign exchange reference rates (daily, ~30 currencies).

Published around 16:00 CET on TARGET working days; free reuse with the source
named (https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/).
"""

import xml.etree.ElementTree as ET

from .. import http

URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"


def fetch() -> bytes:
    return http.get(URL)


def parse(body: bytes) -> tuple[str, dict[str, float]]:
    """(reference date, currency -> units per EUR)."""
    root = ET.fromstring(body)
    day = root.find(".//{*}Cube[@time]")
    assert day is not None, "no dated Cube in ECB reference rates"
    rates = {c.get("currency"): float(c.get("rate")) for c in day}
    assert rates, "empty ECB reference rates"
    return day.get("time"), rates
