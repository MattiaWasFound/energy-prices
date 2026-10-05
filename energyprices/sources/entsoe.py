"""ENTSO-E Transparency Platform: day-ahead prices (document type A44).

Prices come in EUR/MWh. A response holds several TimeSeries for one area: one
per day, one per auction (DE-LU, AT), sometimes one per resolution or currency.
The parser keeps auction sequence 1 at the finest resolution present.
curveType A03 (the API default) omits a point whose price equals the previous
one, so a missing position repeats its predecessor up to the end of the period.
"No matching data" arrives as HTTP 200 with an Acknowledgement document.
Limits: 400 requests/minute per token; one fetch per area per run is far below.
"""

import re
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

from .. import http
from ..slots import UTC, Points

URL = "https://web-api.tp.entsoe.eu/api"


class NoData(Exception):
    """ENTSO-E answered with an acknowledgement instead of prices."""


def fetch(token: str, eic: str, start: datetime, end: datetime) -> bytes:
    fmt = "%Y%m%d%H%M"
    return http.get(URL, {
        "securityToken": token,
        "documentType": "A44",
        "in_Domain": eic,
        "out_Domain": eic,
        "contract_MarketAgreement.type": "A01",  # day-ahead only, no intraday auctions
        "periodStart": start.astimezone(UTC).strftime(fmt),
        "periodEnd": end.astimezone(UTC).strftime(fmt),
    })


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _child(el, name):
    for c in el:
        if _local(c.tag) == name:
            return c
    return None


def _children(el, name):
    return [c for c in el if _local(c.tag) == name]


def _minutes(resolution: str) -> int:
    m = re.fullmatch(r"PT(\d+)M|PT(\d+)H", resolution)
    assert m, f"unknown resolution {resolution}"
    return int(m.group(1)) if m.group(1) else int(m.group(2)) * 60


def _time(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(UTC)


def parse(body: bytes) -> Points:
    root = ET.fromstring(body)
    if _local(root.tag) == "Acknowledgement_MarketDocument":
        reason = root.findtext(".//{*}Reason/{*}text") or "no reason given"
        raise NoData(reason)
    assert _local(root.tag) == "Publication_MarketDocument", root.tag

    # (auction sequence, step) -> prices. DE-LU and AT publish two auctions:
    # sequence 1 is the coupled SDAC auction, 2 is EXAA; both are 15-minute now.
    by_seq: dict[int, dict[int, dict[datetime, float]]] = {}
    for ts in _children(root, "TimeSeries"):
        unit = ts.findtext("{*}price_Measure_Unit.name") or "MWH"
        if (ts.findtext("{*}currency_Unit.name") or "EUR") != "EUR":
            continue  # Poland also publishes a PLN copy of its series
        assert unit == "MWH", unit
        seq = int(ts.findtext("{*}classificationSequence_AttributeInstanceComponent.position") or 1)
        a03 = (ts.findtext("{*}curveType") or "A01") == "A03"
        for period in _children(ts, "Period"):
            interval = _child(period, "timeInterval")
            start = _time(interval.findtext("{*}start"))
            end = _time(interval.findtext("{*}end"))
            step = _minutes(period.findtext("{*}resolution"))
            n = (end - start) // timedelta(minutes=step)
            given = {}
            for p in _children(period, "Point"):
                amount = p.findtext("{*}price.amount")
                # A point without an amount has no value; it is not zero.
                given[int(p.findtext("{*}position"))] = float(amount) if amount else None
            prices = by_seq.setdefault(seq, {}).setdefault(step, {})
            last = None
            for pos in range(1, n + 1):
                v = given[pos] if pos in given else (last if a03 else None)
                if v is not None:
                    prices.setdefault(start + timedelta(minutes=(pos - 1) * step), v)
                last = v
    by_step = by_seq[min(by_seq)] if by_seq else {}
    if not by_step:
        raise NoData("document has no TimeSeries")
    # Keep the finest resolution; a slot only published coarser (one day still
    # hourly) is split into the finer slots it spans.
    step = min(by_step)
    prices = dict(by_step[step])
    for coarse, coarse_prices in by_step.items():
        for t, v in coarse_prices.items():
            for k in range(coarse // step):
                prices.setdefault(t + timedelta(minutes=k * step), v)
    return Points(step=step, prices=prices)
