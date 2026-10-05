# Mexico (MX): CFE tariff zones, researched 2026-10-05

Files here: `zones.csv`, `static_prices.csv` (one row per zone), `mexico-national.csv`
(the same result as a single country row in the `rest-of-world/` format, for use without
zones), `calc.py` (the model; `python3 calc.py` reprints `results.txt`), all in
`rows/mexico/`. The fetched pages are not kept here.

## Recommendation in one paragraph

If Mexico gets zones, they should be the **tariff letters** (Tarifa 1, 1A to 1F), not
states. But the zone rule does not hold at typical use, so **my recommendation is no
zones**. Replace the national row (2.88 MXN/kWh) with **1.327 MXN/kWh at 140 kWh/month**
(`mexico-national.csv`).

The roughly 3x gap that the rest-of-world research found is real only at *equal* consumption. CFE sizes
each tariff's subsidised summer blocks to the heat, so each zone's typical household pays
about the same per kWh over a year: **1.17 to 1.35 MXN/kWh, about 1.15x**. The 2.88 row
priced a Tarifa 1 household at 250 kWh/month, nearly three times typical use and at the DAC
limit. The zone files are complete in case zones are wanted anyway, for example because
the client compares equal consumption.

## The price per zone

| Zone | Price MXN/kWh, year | Annual mean use, kWh/month | Summer / winter use | Summer / winter price | Weight | Confidence |
|---|---|---|---|---|---|---|
| Tarifa 1 | **1.352** | 90 | (no season) | 1.352 | 0.580 | medium |
| Tarifa 1A | **1.305** | 130 | 147 / 113 | 1.233 / 1.399 | 0.102 | low |
| Tarifa 1B | **1.307** | 155 | 186 / 124 | 1.235 / 1.416 | 0.102 | low |
| Tarifa 1C | **1.315** | 220 | 293 / 147 | 1.256 / 1.432 | 0.117 | low |
| Tarifa 1D | **1.310** | 255 | 328 / 182 | 1.236 / 1.442 | 0.044 | low |
| Tarifa 1E | **1.179** | 300 | 412 / 187 | 1.045 / 1.473 | 0.008 | low |
| Tarifa 1F | **1.172** | 408 | ~520-840 / ~190-280 | 1.022 / 1.598 | 0.047 | low |
| National (weighted) | **1.327** | 140 | | | | low |

At equal consumption the gap does appear: a July 2026 bill per kWh, IVA 16%.

| kWh/month | 1 | 1A | 1B | 1C | 1D | 1E | 1F |
|---|---|---|---|---|---|---|---|
| 150 | 1.65 | 1.23 | 1.20 | 1.17 | 1.17 | 0.98 | 0.98 |
| 300 | 3.16 | 2.95 | 2.11 | 1.26 | 1.25 | 0.98 | 0.98 |
| 600 | 3.91 | 3.80 | 3.38 | 2.23 | 1.43 | 1.10 | 1.10 (Sonora 0.98) |

So the answer depends on what the client's price is for. The method defines it as what a
typical household pays per kWh, and on that definition Mexico does not need zones. The
marginal kWh at typical use is also close across zones: 1.37 to 1.61 in 1 to 1D, 1.14 to
1.22 in 1E and 1F. It jumps to 4.7 MXN only once a household passes its tariff's
intermediate blocks.

## Rates (2026)

Domestic tariffs 1 to 1F are set by SHCP. The 2026 schedule is in Oficio 349-B-1-070
(DAC: 349-B-1-069), which is deliberately not published in the DOF. CFE's own tariff pages
return an Imperva 403 to automated clients, as in the rest-of-world research. The monthly
tables were read from two independent reproductions:

- appcfecontigo.com.mx/cfe-tarifas, the full 15-table layout with block limits.
- airegulasolutions.com/cfe/tarifas, a month-by-month data table, which lists rates but not
  block limits.

The two agree to ±0.001 on every block checked (May 2026: 1C 1.004/1.163/1.495; 1E
0.839/1.039/1.348; 1F 0.839/1.039/2.526; excedente 3.992). Rates rise 0.311% a month
(factor 1.00311), which also matches the Sep→Oct check in the rest-of-world research.

MXN/kWh before IVA, October 2026 (summer rates for 1A–1F; outside summer every tariff uses the Tarifa 1 rates):

| | Tarifa 1 (all year) / every tariff out of summer | 1A–1D summer | 1E summer | 1F summer |
|---|---|---|---|---|
| Básico | 1.140 | 1.019 | 0.854 | 0.854 |
| Intermedio (bajo) | 1.385 | 1.183 | 1.054 | 1.054 |
| Intermedio alto | – | 1.520 (1C, 1D) | 1.368 | 2.566 |
| Excedente | 4.054 | 4.054 | 4.054 | 4.054 |

Blocks, kWh/month:

| Tariff | Summer blocks | Out-of-summer blocks | DAC limit (12-month mean) |
|---|---|---|---|
| 1 | 75 / 65 / rest (all year) | | 250 |
| 1A | 100 / 50 / rest | 75 / 75 / rest | 300 |
| 1B | 125 / 100 / rest | 75 / 100 / rest | 400 |
| 1C | 150 / 150 / 150 / rest | 75 / 100 / rest | 850 |
| 1D | 175 / 225 / 200 / rest | 75 / 125 / rest | 1,000 |
| 1E | 300 / 450 / 150 / rest | 75 / 125 / rest | 2,000 |
| 1F | 300 / 900 / 1,300 / rest | 75 / 125 / rest | 2,500 |
| 1F Sonora scheme | 1,200 at básico / 1,300 at int.-bajo rate / rest | 75 / 125 / rest | 2,500 |

There is no fixed charge. Since 2026 a minimum of 25 kWh is billed. Most households are
billed every two months, so the blocks double per bill, but the per-month price is
unchanged.

## How each price is built (`calc.py`)

For each zone the model sums 12 monthly bills for the 2026 calendar year, each at that
month's published rates, adds IVA, and divides by the year's kWh. Summer months use the
summer table and the rest use the out-of-summer table.

- **Summer months.** The rule is six consecutive warm months, set by locality. The model
  uses May to October, the most common window. Sonora runs April to October (seven months)
  under its 2025–26 scheme (Dossier Político, 2026-03-20; Infoson, 2025-04-01). Sinaloa
  was granted one more month in September 2026 that the model does not include; it would
  lower 1F slightly. Some Gulf and central localities start in June. Rates move only 0.3%
  a month, so the exact window changes prices by under 1%.
- **Consumption.** CFE's 2017 residential sales by municipality (MWh, CFE open data
  cleaned on Zenodo record 4909262), divided by inhabited dwellings in the INEGI 2020
  census (ITER), for representative municipalities of each tariff. This gives the annual
  mean kWh per household per month.
  - Tarifa 1: CFE's own figure is 85 kWh/month (CFE SSB, Apr 2020, via Expansión
    2025-10-30). The data gives CDMX 98, Edomex 76 and Puebla 90. The model uses 90.
  - Cross-check: the users-weighted mean of the seven zones is 140 kWh/month. Total 2017
    residential sales divided by 2020 households is also 140 kWh/month (59,141 GWh / 35.2 M
    households / 12).
  - The means include the few DAC households, so they are slightly high for subsidised
    households.
- **Seasonal split** (assumption, no source found). The ratio of summer-month to
  winter-month use: 1A 1.3, 1B 1.5, 1C 2.0, 1D 1.8, 1E 2.2, 1F 2.8, Mexicali 3.0. Winter
  use is `12·mean / (n_summer·ratio + n_winter)`. Press reports of Hermosillo bills going
  from 800 MXN in winter to 4,500 MXN in July suggest 1F may swing more than 2.8. The
  yearly price barely moves with the ratio: what the summer blocks give, the winter
  excedente takes back.
- **Tarifa 1F zone.** The price is total bills over total kWh across three billing groups,
  weighted by users:
  - Sonora: all 72 municipalities, 1.105 M users, its own blocks. 1.063 MXN/kWh.
  - Sinaloa: all municipalities on the standard 1F blocks since 2024, 821,400 users
    (Noroeste, "Garantizan tarifa 1F a todo Sinaloa"). 1.188 MXN/kWh.
  - Mexicali and San Felipe: 8% IVA. 1.348 MXN/kWh, because their winter use crosses the
    200 kWh excedente line.

  The arithmetic for each zone is in its `source` column.

## Zones: tariff letter vs state

**Tariff letter, if zones are used.**

- **The letter is the price.** Every subsidised domestic household's tariff is one of the
  seven letters, and the letter is printed on the bill ("TARIFA 1C"). Residents know it,
  because the summer subsidy and DAC risk are in the news every spring.
- **States mix tariffs.** Veracruz, Jalisco, Chihuahua (Juárez is 1C), Coahuila,
  Tamaulipas, Guerrero and Oaxaca all span several letters, so a state zone would have no
  single price. 32 states would also be a long list.
- **Sonora and Sinaloa are no longer an argument for states.** Both have been 1F statewide
  in summer since 2024/2025, so they now sit inside the 1F zone.
- **Merging is possible.** If seven is too many, 1A+1B (1.305/1.307) and 1C+1D
  (1.315/1.310) could merge with no loss, giving four zones: 1, 1A–1B, 1C–1D, 1E–1F. That
  still does not meet the 2x rule.

`zone_label`: **"Tarifa"**, the bill's own word. Zone ids follow `MX-<SHORT>` (MX-T1,
MX-T1A … MX-T1F), because tariffs are not ISO subdivisions. Names are "Tarifa 1" … "Tarifa
1F".

**National row.** If zones are adopted, drop the existing national row so the average
becomes the weighted zone mean (1.327). The current row is a single Tarifa 1 household at
250 kWh, not a national average. If zones are not adopted, replace it with
`mexico-national.csv` (1.327 at 140 kWh, the same number).

## Weights (low confidence)

CFE's users-by-tariff open data (datos.cfe.gob.mx, "Usuarios y consumo de electricidad
por municipio") is offline and not in the Wayback Machine. The SENER SIE tables return 404.
The weights are built from partial CFE counts quoted in the press:

- The base is 20.8 M summer-tariff users, which CFE says is 42% of low-consumption
  (subsidised) domestic users, so 49.5 M in total. Tarifa 1 takes the residual,
  **28.7 M = 0.580**. This fits the 54.8% of domestic clients CFE reported on Tarifa 1 in
  April 2020.
- **1C: 5.81 M** (CFE, March 2025, via El Financiero 2025-06-04). **1D: 2.19 M** (the same
  article: Nuevo León's 83,077 1D users are 3.8% of the national total).
- **1F: 2.35 M.** Sonora 1.105 M plus Sinaloa 0.821 M plus Mexicali/San Felipe 0.42 M.
  Mexicali is estimated as 330k households × 1.26, Sonora's ratio of users to households.
- **1E: 0.40 M**, a guess. Since Sonora and Sinaloa moved to 1F, it is unclear which
  localities remain on 1E; Baja California Sur is likely.
- **1A and 1B** split the remaining 10.05 M **evenly**, an assumption.
- There is an overlap risk: the March 1C/1D counts may include Sinaloa and Sonora users
  whose base letter shows outside summer. Because 1A to 1D all price within 1.305–1.315,
  the national mean barely moves under any plausible reweighting (±0.01).

## IVA, DAC and DAP

- **IVA** is 16%. Northern border municipalities pay 8% under the border tax-incentive
  decree; the southern border region has the same incentive. The model applies 8% to an
  estimated share of each zone's users:
  - Tarifa 1: 3% (Tijuana, Tecate, Ensenada, Rosarito).
  - 1C: 10% (Ciudad Juárez).
  - 1D: 28% (Reynosa, Matamoros, Nuevo Laredo, Río Bravo).
  - 1F: Mexicali/San Felipe 100%, and 24% of Sonora (San Luis Río Colorado, Nogales, Agua
    Prieta, Puerto Peñasco, Caborca and others).

  These shares are from 2020 census households and are approximate. The 8% treatment of
  CFE bills was not checked on a bill. If 8% did not apply to electricity, prices would
  rise by at most 7% in those groups.
- **DAC** is left out of every zone. It is a penalty class for households whose 12-month
  mean exceeds the tariff's limit, not a region. October 2026, Central region: 145.79
  MXN/month fixed + 6.730 MXN/kWh, about 8.5 MXN/kWh all-in at 250 kWh (the rest-of-world research,
  `gapfill-world-gaps.md`). A typical household is far below every limit: 90 vs 250
  kWh/month on Tarifa 1, 408 vs 2,500 on 1F. If the client ever offers user-pickable
  options (like Norgespris), DAC is the obvious Mexican one.
- **DAP** (Derecho de Alumbrado Público) is excluded, as in the rest-of-world research. It is a municipal
  street-lighting levy collected on the CFE bill, set by each municipality (often a
  percentage of the energy amount, sometimes a fixed fee). Its inclusion would raise every
  zone by roughly the same few percent and does not affect the zone decision.

## Not settled

1. **CFE's own tables.** cfe.mx is geo-blocked, so the rates rest on two reproductions of
   the SHCP oficio. They agree with each other and with press figures (Sonora 2025: 0.803
   / 0.996 / 3.833).
2. **Users per tariff.** There is no CFE or SENER table. 1A/1B/1E are residual or guessed,
   and the 1C/1D March counts may overlap Sinaloa and Sonora.
3. **Locality-to-tariff mapping.** Secondary lists conflict. For example, appcfecontigo
   puts Hermosillo on 1D and La Paz on 1F, Culiacán is listed variously as 1C, 1E or 1F,
   and one source puts Guadalajara on 1B. The representative municipalities behind each
   zone's consumption are therefore partly unverified.
4. **Seasonal ratios** are assumed. Monthly sales by tariff would settle them; the
   per-month CFE file is gone.
5. **Sonora's 2026 scheme.** "1 to 2,400 kWh" per bimonthly bill at básico is read as
   1,200 per month. Dossier Político also mentions 195,000 more Sonora users being added
   in April, so Sonora may have 1.3 M users rather than 1.105 M.
6. **Average vs marginal price.** If the estimator costs *added* consumption (an air
   conditioner, an EV), Mexico's marginal block price matters. It can be 3x the average
   (Tarifa 1 above 140 kWh: 4.70 MXN all-in). That is a question about the client's price
   definition, not about zones.

## Sources

- Rates: https://appcfecontigo.com.mx/cfe-tarifas/ ; https://airegulasolutions.com/cfe/tarifas?year=2026&month=5&segment=DOMESTIC (and `month=1..10`)
- SHCP authorisation (2026 domestic tariffs): https://dof.gob.mx/nota_detalle.php?codigo=5777718&fecha=31/12/2025
- Summer-tariff users 20.8 M / 42%: https://expansion.mx/empresas/2026/03/30/cfe-tarifas-verano-2026-20-millones-consumidores-domesticos
- Tarifa 1 share and mean use (CFE SSB, Apr 2020): https://expansion.mx/finanzas-personales/2025/10/30/como-saber-tarifa-domestica-cfe-como-afecta-tu-recibo-de-luz
- 1C and 1D users (CFE, Mar 2025): https://www.elfinanciero.com.mx/monterrey/2025/06/04/lidera-nl-en-el-pais-usuarios-de-tarifa-1c/
- Sonora 1F, all municipalities, blocks, 1.105 M users: https://infoson.com.mx/2025/04/01/arranca-subsidio-electrico-en-sonora-tarifa-1f-se-aplica-en-todos-los-municipios-y-durara-siete-meses/ ; https://dossierpolitico.com/2026/03/20/cfe-sonora-tendra-subsidio-de-verano-primero-que-sinaloa-cuando-inicia/
- Sinaloa 1F, all municipalities, 821,400 users: https://www.noroeste.com.mx/buen-vivir/garantizan-tarifa-1f-a-todo-sinaloa-KANO235179 ; extension: https://lineadirectaportal.com/sinaloa/claudia-sheinbaum-anuncia-ampliacion-de-un-mes-al-subsidio-de-la-tarifa-de-verano-1f-en-sinaloa-2026-09-20__1705382
- Summer windows by region: https://www.noticiasgobierno.com/subsidio-cfe-verano-2026-estados-meses-tarifa/
- Residential sales by municipality 2017 (CFE): https://zenodo.org/records/4909262
- Households, census 2020 (INEGI ITER): https://www.inegi.org.mx/contenidos/programas/ccpv/2020/datosabiertos/iter/iter_00_cpv2020_csv.zip
- Notes this builds on: `rest-of-world/americas-central-mexico.md`, `gapfill-world-gaps.md`
