"""The publish gate: the schema, then the rules a schema can't express.

Returns a list of problems; an empty list means the document may be published.
"""

import json
import math
from datetime import datetime, timedelta
from pathlib import Path

import jsonschema

from .config import Config
from .slots import day_start, delivery_day

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schema" / "prices.schema.json"
MAX_BYTES = 500_000


def schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text())


def serialize(doc: dict) -> bytes:
    return (json.dumps(doc, ensure_ascii=False, separators=(",", ":"), allow_nan=False) + "\n").encode()


def _parse_utc(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def check(doc: dict, cfg: Config, now: datetime) -> list[str]:
    validator = jsonschema.Draft202012Validator(schema())
    problems = [f"schema: /{'/'.join(map(str, e.absolute_path))}: {e.message}"
                for e in sorted(validator.iter_errors(doc), key=lambda e: list(e.absolute_path))]
    if problems:
        return problems

    size = len(serialize(doc))
    if size > MAX_BYTES:
        problems.append(f"size: {size} bytes is over {MAX_BYTES}")

    missing = sorted(set(cfg.countries) - set(doc["countries"]))
    if missing:
        problems.append(f"countries missing: {missing}")

    fx = doc["fx"]
    if fx["EUR"] != 1:
        problems.append("fx: EUR must be 1")
    bounds = cfg.settings["bounds"]
    today_start = day_start(delivery_day(now))
    for code, c in doc["countries"].items():
        if c["currency"] not in fx:
            problems.append(f"{code}: no fx rate for {c['currency']}")
            continue
        rate = fx[c["currency"]]
        entries = [(f"{code}", c["average"])] + [(f"{code}/{z['id']}", z) for z in c["zones"]]
        for o in c.get("options", []):
            if [z["id"] for z in o["zones"]] != [z["id"] for z in c["zones"]]:
                problems.append(f"{code}: option {o['id']} zones differ from the country's")
            entries += [(f"{code}:{o['id']}", o["average"])] + [(f"{code}:{o['id']}/{z['id']}", z) for z in o["zones"]]
        for label, e in entries:
            lo, hi = (bounds["live_min"], bounds["live_max"]) if e["precision"] == "live" else \
                     (bounds["static_min"], bounds["static_max"])
            values = ([e["flat"]] if "flat" in e else []) + e.get("series", {}).get("values", [])
            for v in values:
                if not math.isfinite(v) or not lo <= v / rate <= hi:
                    problems.append(f"{label}: {v} {c['currency']} is outside {lo}..{hi} EUR/kWh")
                    break
            s = e.get("series")
            if s:
                start = _parse_utc(s["start"])
                end = start + timedelta(minutes=s["step_minutes"] * len(s["values"]))
                if start != today_start:
                    problems.append(f"{label}: series starts {s['start']}, not at today's delivery day start")
                if day_start(delivery_day(end - timedelta(minutes=1)) + timedelta(days=1)) != end:
                    problems.append(f"{label}: series does not end at a delivery day boundary")
    return problems
