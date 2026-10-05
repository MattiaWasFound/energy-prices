"""Mexico zone prices: a 2026 calendar year of CFE domestic bills per tariff zone.

Rates: SHCP Oficio 349-B-1-070 monthly tables for 2026 as reproduced by
appcfecontigo.com.mx/cfe-tarifas and cross-checked against
airegulasolutions.com/cfe/tarifas. MXN/kWh before IVA.
Run: python3 calc.py
"""
MONTHS = range(1, 13)
# Tarifa 1 and every tariff's fuera-de-verano rates (same three numbers), Jan..Dec 2026
T1 = {
    "bas": [1.110, 1.113, 1.116, 1.119, 1.122, 1.125, 1.128, 1.132, 1.136, 1.140, 1.144, 1.148],
    "int": [1.349, 1.353, 1.357, 1.361, 1.365, 1.369, 1.373, 1.377, 1.381, 1.385, 1.389, 1.393],
    "exc": [3.944, 3.956, 3.968, 3.980, 3.992, 4.004, 4.016, 4.028, 4.041, 4.054, 4.067, 4.080],
}
# Summer rates by month (Apr..Oct). 1A-1D share one set, 1E and 1F share básico / int. bajo.
SUM_1A_1D = {"bas": {5: 1.004, 6: 1.007, 7: 1.010, 8: 1.013, 9: 1.016, 10: 1.019},
             "ib":  {5: 1.163, 6: 1.167, 7: 1.171, 8: 1.175, 9: 1.179, 10: 1.183},
             "ia":  {5: 1.495, 6: 1.500, 7: 1.505, 8: 1.510, 9: 1.515, 10: 1.520}}
SUM_1E_1F = {"bas": {4: 0.836, 5: 0.839, 6: 0.842, 7: 0.845, 8: 0.848, 9: 0.851, 10: 0.854},
             "ib":  {4: 1.036, 5: 1.039, 6: 1.042, 7: 1.045, 8: 1.048, 9: 1.051, 10: 1.054},
             "ia_1E": {4: 1.344, 5: 1.348, 6: 1.352, 7: 1.356, 8: 1.360, 9: 1.364, 10: 1.368},
             "ia_1F": {4: 2.518, 5: 2.526, 6: 2.534, 7: 2.542, 8: 2.550, 9: 2.558, 10: 2.566}}
# Rates for months outside the published summer tables (Nov) are needed only if a summer runs into
# November; none does in this model.

def blocks_bill(kwh, blocks):
    """blocks: list of (size_kwh or None, rate)."""
    bill, left = 0.0, kwh
    for size, rate in blocks:
        q = left if size is None else min(left, size)
        bill += q * rate
        left -= q
        if left <= 0:
            break
    return bill

# Winter (fuera de verano) intermedio block size per tariff: básico 75, then this many kWh.
WINTER_INT = {"1": 65, "1A": 75, "1B": 100, "1C": 100, "1D": 125, "1E": 125, "1F": 125}

def month_bill(tariff, m, kwh, summer, sonora=False):
    i = m - 1
    if not summer:
        return blocks_bill(max(kwh, 25), [(75, T1["bas"][i]), (WINTER_INT[tariff], T1["int"][i]), (None, T1["exc"][i])])
    exc = T1["exc"][i]
    if tariff in ("1A", "1B", "1C", "1D"):
        s = SUM_1A_1D
        b, ib, ia = s["bas"][m], s["ib"][m], s["ia"][m]
        blocks = {"1A": [(100, b), (50, ib), (None, exc)],
                  "1B": [(125, b), (100, ib), (None, exc)],
                  "1C": [(150, b), (150, ib), (150, ia), (None, exc)],
                  "1D": [(175, b), (225, ib), (200, ia), (None, exc)]}[tariff]
    else:
        s = SUM_1E_1F
        b, ib = s["bas"][m], s["ib"][m]
        if tariff == "1E":
            blocks = [(300, b), (450, ib), (150, s["ia_1E"][m]), (None, exc)]
        elif sonora:  # Sonora 2025-26: 1-1,200 kWh at básico, 1,201-2,500 at intermedio-bajo rate
            blocks = [(1200, b), (1300, ib), (None, exc)]
        else:
            blocks = [(300, b), (900, ib), (1300, s["ia_1F"][m]), (None, exc)]
    return blocks_bill(max(kwh, 25), blocks)

def year(tariff, mean_kwh, ratio, summer_months, iva, sonora=False):
    """mean_kwh: annual mean per month; ratio: summer-month use / winter-month use."""
    ns = len(summer_months)
    if tariff == "1":
        w = s = mean_kwh
    else:
        w = 12 * mean_kwh / (ns * ratio + (12 - ns))
        s = ratio * w
    tot_bill = tot_kwh = sb = wb = 0.0
    for m in MONTHS:
        summer = m in summer_months
        kwh = s if summer else w
        bill = month_bill(tariff, m, kwh, summer, sonora) * (1 + iva)
        tot_bill += bill; tot_kwh += kwh
        if summer: sb += bill
        else: wb += bill
    nw = 12 - ns
    return {"price": tot_bill / tot_kwh, "summer_kwh": s, "winter_kwh": w,
            "summer_price": sb / (s * ns) if ns else None, "winter_price": wb / (w * nw),
            "annual_kwh": tot_kwh}

MAY_OCT = set(range(5, 11)); APR_OCT = set(range(4, 11))
# Sub-groups: (zone, label, users_weight_within_zone, tariff, mean kWh/month, summer/winter ratio, summer months, border share at 8% IVA, sonora)
GROUPS = [
    ("1",  "Tarifa 1 (temperate)",          1.0, "1",  90,  1.0, set(),  0.03, False),
    ("1A", "1A",                            1.0, "1A", 130, 1.3, MAY_OCT, 0.0, False),
    ("1B", "1B",                            1.0, "1B", 155, 1.5, MAY_OCT, 0.0, False),
    ("1C", "1C",                            1.0, "1C", 220, 2.0, MAY_OCT, 0.10, False),
    ("1D", "1D",                            1.0, "1D", 255, 1.8, MAY_OCT, 0.28, False),
    ("1E", "1E",                            1.0, "1E", 300, 2.2, MAY_OCT, 0.0, False),
    ("1F", "Sonora (all 72 municipalities)", 1.105, "1F", 381, 2.8, APR_OCT, 0.24, True),
    ("1F", "Sinaloa (all municipalities)",  0.821, "1F", 365, 2.8, MAY_OCT, 0.0, False),
    ("1F", "Mexicali + San Felipe (BC)",    0.42, "1F", 563, 3.0, MAY_OCT, 1.0, False),
]

def run():
    zones = {}
    for z, label, wt, tar, mean, ratio, sm, border, son in GROUPS:
        r16 = year(tar, mean, ratio, sm, 0.16, son)
        r8 = year(tar, mean, ratio, sm, 0.08, son)
        mix = {k: (r16[k] * (1 - border) + r8[k] * border) if isinstance(r16[k], float) else r16[k] for k in r16}
        print(f"{z:3s} {label:34s} mean {mean:4d} summer {r16['summer_kwh']:6.0f} winter {r16['winter_kwh']:5.0f} "
              f"| 16%: year {r16['price']:.3f} summer {r16['summer_price'] or 0:.3f} winter {r16['winter_price']:.3f} "
              f"| 8%: year {r8['price']:.3f} | border {border:.2f} -> {mix['price']:.3f}")
        zones.setdefault(z, []).append((wt * r16["annual_kwh"], wt, mix))
    print()
    out = {}
    for z, parts in zones.items():
        # Zone price = total bills / total kWh across sub-groups (kWh-weighted), summer/winter user-weighted
        W = sum(p[1] for p in parts)
        bills = sum(p[1] * p[2]["price"] * p[2]["annual_kwh"] for p in parts)
        kwh = sum(p[1] * p[2]["annual_kwh"] for p in parts)
        sp = sum(p[1] * (p[2]["summer_price"] or 0) for p in parts) / W
        wp = sum(p[1] * p[2]["winter_price"] for p in parts) / W
        out[z] = (bills / kwh, kwh / W / 12, sp, wp)
        print(f"zone {z:3s} price {bills/kwh:.3f} MXN/kWh at {kwh/W/12:.0f} kWh/month mean; summer {sp:.3f} winter {wp:.3f}")
    return out

if __name__ == "__main__":
    run()

# Weights: share of subsidised domestic users (base 49.5 M = 20.8 M summer-tariff users / 0.42).
WEIGHTS = {"1": 28.70, "1A": 5.025, "1B": 5.025, "1C": 5.81, "1D": 2.19, "1E": 0.40, "1F": 2.346}

def equal_use_table():
    print("\nJuly 2026 bill at equal consumption, IVA 16%, MXN/kWh:")
    for kwh in (150, 300, 600):
        row = []
        for tar, son in (("1", False), ("1A", False), ("1B", False), ("1C", False), ("1D", False), ("1E", False), ("1F", False), ("1F", True)):
            row.append(f"{tar}{'son' if son else ''} {month_bill(tar, 7, kwh, tar != '1', son) * 1.16 / kwh:.2f}")
        print(f"  {kwh:4d} kWh: " + "  ".join(row))

if __name__ == "__main__":
    out = run()
    equal_use_table()
    tot = sum(WEIGHTS.values())
    print("\nweights:", {z: round(w / tot, 4) for z, w in WEIGHTS.items()}, "sum", round(sum(round(w / tot, 4) for w in WEIGHTS.values()), 4))
    um = sum(WEIGHTS[z] * out[z][0] for z in out) / tot
    km = sum(WEIGHTS[z] * out[z][1] for z in out) / tot
    kw = sum(WEIGHTS[z] * out[z][0] * out[z][1] for z in out) / sum(WEIGHTS[z] * out[z][1] for z in out)
    print(f"national: user-weighted mean of zone prices {um:.3f}; kWh-weighted {kw:.3f}; mean use {km:.0f} kWh/month")
