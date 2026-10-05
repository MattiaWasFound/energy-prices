"""Build out/browse.html: one self-contained page to browse a prices.json.

    uv run python tools/browse.py [--prices out/prices.json] [--out out/browse.html]

The page (browse/index.html) gets everything inlined: the prices, the config
tables that explain them (sources, add-ons, weights), the research findings
(docs/findings.md) and a world map (world-atlas 50m, Natural Earth,
ISC licence, ids rewritten to ISO alpha-2). No network at view time.
"""

import argparse
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from energyprices import config  # noqa: E402

BROWSE = ROOT / "browse"
# Natural Earth features without an ISO numeric code, coloured as the code they belong to.
BY_NAME = {"Kosovo": "XK", "N. Cyprus": "CY", "Somaliland": "SO"}


def topology() -> dict:
    numeric = {r["numeric"]: r["alpha2"] for r in csv.DictReader(open(BROWSE / "iso-numeric.csv"))}
    topo = json.loads((BROWSE / "countries-50m.json").read_text())
    geoms = []
    for g in topo["objects"]["countries"]["geometries"]:
        code = numeric.get(g.get("id") or "") or BY_NAME.get(g["properties"]["name"])
        if code and g.get("arcs"):
            geoms.append({"type": g["type"], "arcs": g["arcs"], "id": code})
    return {"transform": topo["transform"], "arcs": topo["arcs"], "geometries": geoms}


def findings() -> list[dict]:
    """docs/findings.md: each `## title` with a `<!-- finding: k=v; ... -->` marker
    and the paragraph after it. The page lays them out; nothing renders markdown."""
    out, cur = [], None
    for line in (ROOT / "docs" / "findings.md").read_text().splitlines():
        if line.startswith("## "):
            cur = {"title": line[3:].strip(), "text": []}
        elif line.startswith("<!-- finding:") and cur is not None:
            meta = dict(kv.strip().split("=", 1) for kv in line[len("<!-- finding:"):-len("-->")].split(";") if "=" in kv)
            cur.update(figure=meta.get("figure", ""), countries=[c for c in meta.get("countries", "").split(",") if c])
            out.append(cur)
        elif cur is not None and cur in out and line.strip():
            cur["text"].append(line.strip())
    for f in out:
        f["text"] = " ".join(f["text"])
        assert f["text"], f"findings.md: '{f['title']}' needs a paragraph"
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--prices", type=Path, default=ROOT / "out" / "prices.json")
    p.add_argument("--out", type=Path, default=ROOT / "out" / "browse.html")
    args = p.parse_args()
    cfg = config.load()
    rows = lambda name: list(csv.DictReader(open(ROOT / "config" / name, encoding="utf-8")))
    data = {
        "prices": json.loads(args.prices.read_text()),
        "regions": {c.code: c.region for c in cfg.countries.values()},
        "tariffs": {r["scope"]: r for r in rows("tariffs.csv")},
        "static": {(r["country"] + ("/" + r["zone"] if r["zone"] else "")): r for r in rows("static_prices.csv")},
        "areas": rows("areas.csv"),
        "taxes": {r["zone"]: r for r in rows("household_taxes.csv")},
        "settings": cfg.settings,
        "findings": findings(),
        "geo": topology(),
    }
    mapped = {g["id"] for g in data["geo"]["geometries"]}
    unmapped = sorted(set(data["prices"]["countries"]) - mapped)
    if unmapped:
        print(f"no map shape (listed below the map): {', '.join(unmapped)}", file=sys.stderr)
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = (BROWSE / "index.html").read_text().replace("/*DATA*/null", blob)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(html)
    print(f"wrote {args.out} ({args.out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
