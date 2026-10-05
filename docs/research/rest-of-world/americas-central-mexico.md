# Americas North, group A: MX GT BZ SV HN NI CR PA

Researched 2026-10-04. All figures are local currency per kWh, all-in at the stated monthly consumption,
with on-bill subsidies applied where a household at that consumption gets them.

## MX: Mexico, 1.671 MXN/kWh (Tarifa 1, 150 kWh/month, Oct 2026), low confidence

The source is CFE's domestic tariff page (app.cfe.mx ... /Tarifa1.aspx). It returned an Imperva HTTP 403
to automated clients, so the block rates could not be read first-hand. The Wayback
snapshots only hold the form, not the values. Rates were taken from a reproduction of CFE's table
(airegulasolutions.com/cfe/tarifas). They are consistent with the published mechanism: the
SHCP agreement (DOF, sidof 5547404) applies a monthly adjustment factor from INPC, and Sep to Oct moved
about 0.3% on every block (Sep 1.136/1.381/4.041 to Oct 1.140/1.385/4.054). recibo-de-luz.com.mx
independently gives the same Sep values. Prices are pre-IVA.

Tarifa 1, Oct 2026, 150 kWh (assumed typical for a Tarifa-1 household; national average residential
use is lower, roughly 110-150 kWh):
- basico 75 kWh x 1.140 = 85.50
- intermedio 65 kWh x 1.385 = 90.03
- excedente 10 kWh x 4.054 = 40.54
- subtotal 216.06; IVA 16% gives 250.63 MXN; divided by 150 = **1.671 MXN/kWh**. There is no fixed charge;
  the minimum is 25 kWh.
- Sensitivity: 200 kWh = 2.43, 250 kWh = 2.88. Above a 250 kWh 12-month average the household moves
  to DAC, about 8 MXN/kWh.
- DAP (Derecho de Alumbrado Publico) is a municipal levy collected on the CFE bill, typically a few
  percent to about 10% of the energy amount. Its rate varies by municipality and is excluded here.
- IVA is 16%, or 8% in the northern and southern border regions (estimulo fiscal).

## GT: Guatemala, 1.590 GTQ/kWh (EEGSA tarifa social, Aug-Oct 2026), medium confidence

From the CNEE communique of 31 Jul 2026, tarifa social, Q/kWh: EEGSA 1.42, DEOCSA 2.03, DEORSA 1.98. Tarifa
no social (over 300 kWh/month): EEGSA 1.51, DEOCSA 2.12, DEORSA 2.06. 93% of users are on the tarifa social.
- 1.42 x 1.12 (IVA 12%) = **1.590 GTQ/kWh**. The price is flat per kWh, so at 200 kWh the bill is about Q318
  before municipal tax.
- Excluded: the municipal tasa de alumbrado publico, which each municipality sets. Users at or below
  100 kWh/month also get an INDE aporte (subsidy) that is not applied here.
- Caveat: CNEE calls this "the price of each kWh". It does not say whether the small cargo fijo is folded
  in, and the detailed pliego resolutions on cnee.gob.gt are scanned images.
- DEOCSA/DEORSA (west/east, rural) cost about 40% more than EEGSA: 2.03 x 1.12 = 2.27.

## BZ: Belize, 0.488 BZD/kWh (BEL residential, 300 kWh/month, Oct 2026), medium confidence

From the PUC Final Decision for ARP 2026/2027, Schedule 6A (Jan 2026 to Jun 2027, OCR of a scanned PDF).
Residential blocks: 0-50 kWh 0.34; 51-200 0.42; over 200 0.46; minimum charge 10.00. Social rate 0.22 for 0-60 kWh.
Plus the COPA (cost-of-power adjustment) for Oct 2026 of 0.0151/kWh, from the PUC decision of Sep 2026. The
government has exempted COPA from GST.
- 50 x 0.34 = 17.00; 150 x 0.42 = 63.00; 100 x 0.46 = 46.00, for a base of 126.00
- GST 12.5% on the base is 15.75; COPA 300 x 0.0151 = 4.53
- total 146.28 / 300 = **0.488 BZD/kWh**. Without GST it is 0.435.
- Caveat: the GST treatment of residential electricity is not verified. bel.com.bz returns 403. The decision
  implies electricity is otherwise GST-liable, but a residential threshold or exemption may exist.
- 300 kWh is the method's default; no Belize figure for typical use was sourced.

## SV: El Salvador, 0.225 USD/kWh (CAESS, 200 kWh/month), medium confidence

From the SIGET pliego of 1 May to 31 Jul 2026, the latest one posted. The government announces each quarter
that tariffs stay unchanged. Under the DGEHM agreements (Ac. 20/2024/DE and others), residential users who
averaged 300 kWh or less in Jan-Mar 2024 keep the Energy Charge of the 15 Jan to 14 Apr 2024 pliego.
Distribution and commercialisation charges are the 2026 values.
- CAESS, block 3 (200 kWh or more, applied to the whole consumption):
  - energy (frozen 2024 level) 0.146487
  - distribution 0.048346
  - fixed 0.871126 per month
- 200 x 0.194833 = 38.967, plus fixed 0.871, gives 39.838
- IVA 13% brings it to 45.017 USD; divided by 200 = **0.225 USD/kWh**
- 200 kWh is the method's low-income default. The residential subsidy for users under 105 kWh/month does not apply.
- Excluded: municipal fees billed with electricity, which vary.
- Users above 300 kWh pay the 2026 energy charge (0.190757), about 20% more per kWh.

## HN: Honduras, 6.432 HNL/kWh (ENEE, 200 kWh/month, Oct 2026), medium confidence

From the CREE structure for ENEE billing from Oct 2026, for residential consumption over 50 kWh:
- fixed 59.74
- first 50 kWh x 5.0031 = 250.16
- next 150 kWh x 6.5102 = 976.53
- total 1,286.43 HNL / 200 = **6.432 HNL/kWh**

Caveats:
- No ISV is applied. My understanding is that residential electricity is ISV-exempt below a high
  consumption threshold, but this is unverified.
- The state subsidy for low-consumption households (150 kWh/month or less) does not apply at 200 kWh, and
  the programme's current terms are unverified.
- CREE notes a 21% cost increase this quarter that ENEE deferred, so a jump is likely in 2027.

## NI: Nicaragua, 7.767 NIO/kWh (Disnorte-Dissur T-0, Managua, 200 kWh/month, Sep 2026), medium confidence

From the INE pliegos valid from 1 Sep 2026. T-0 energy blocks:
- 25 x 2.4807 = 62.02
- 25 x 5.9337 = 148.34
- 50 x 6.2212 = 311.06
- 50 x 8.2693 = 413.47
- 50 x 8.3895 = 419.48
- energy subtotal 1,354.36

Then add:
- commercialisation fixed charge, 151-500 kWh bracket: 105.03
- Managua alumbrado publico, residential 151-500 bracket: 93.93
- total 1,553.32 / 200 = **7.767 NIO/kWh**. Without AP it is 7.30.

Caveats:
- IVA is not applied. My understanding is that residential use of 300 kWh or less is exempt; unverified.
- The tarifa social (cargo social subsidiado) only covers 150 kWh or less. At 150 kWh the subsidised energy
  charges are roughly half.

## CR: Costa Rica, 82.04 CRC/kWh (CNFL T-RE, 300 kWh/month), medium confidence

From the CNFL tarifas vigentes: ARESEP tariffs from 1 Jan 2026, published in La Gaceta Alcance 161 of
16 Dec 2025. The page was updated 9 Sep 2026 and the tariffs are unchanged.
T-RE blocks:
- 0-30 kWh fixed 1,744.80
- 31-200 kWh x 58.16 = 9,887.20
- 201-300 kWh x 89.24 = 8,924.00
- energy subtotal 20,556.00

Then add:
- alumbrado publico 300 x 3.02 = 906.00
- Bomberos 1.75% of energy = 359.73
- IVA 13% on energy and AP = 2,790.06. IVA applies because consumption is over 280 kWh (Ley 9635; threshold
  not fetched, and the IVA base is assumed).
- total 24,611.79 / 300 = **82.04 CRC/kWh**

Sensitivity: at 200 kWh there is no IVA, giving 12,439.56 / 200 = 62.20 CRC/kWh. The 280 kWh IVA cliff makes
300 kWh unrepresentative of the median household. ICE serves the rest of the country and was not priced.
There is no on-bill residential subsidy.

## PA: Panama, 0.1145 PAB/kWh (EDEMET BTS, 300 kWh/month, Sep-Dec 2026), medium confidence

From the ASEP tariffs valid 1 Sep to 31 Dec 2026. BTS (tarifa simple) for EDEMET: fixed 3.17 covers the
first 10 kWh, then escalon 1 (11-300 kWh) at 0.17624.
- 3.17 + 290 x 0.17624 = 54.28
- FET (Fondo de Estabilizacion Tarifaria, state subsidy) for the 251-300 kWh bracket: -31.21%, giving 37.34
- Sep 2026 fuel variation (CVC, no FET applied) 300 x -0.00993 = -2.98
- total 34.36 / 300 = **0.1145 PAB/kWh**

Other cases:
- ENSA: 2.76 + 290 x 0.17737 = 54.20, x (1 - 0.2661) = 39.78, + 0.03 gives 0.1327
- EDECHI (Chiriqui) has a FET of -53.5%.
- The FET subsidy stops above 300 kWh: at 350 kWh EDEMET is about 0.178 PAB/kWh unsubsidised.

Caveats:
- ITBMS is assumed not to apply to residential electricity. Municipal fees (aseo) billed with electricity
  are excluded. Both are unverified.

## Currency

- **PA**: tariffs are set and billed in balboas (PAB, "B/."), pegged 1:1 to the US dollar. Payment is in US
  dollar notes, since Panama issues only balboa coins. Households are billed in PAB, which equals USD; the
  ASEP pliegos are denominated "B/.". PAB is used in the CSV.
- **SV**: USD, legal tender since 2001 (Ley de Integracion Monetaria). The SIGET pliego is denominated in US$.
  Bitcoin was removed as mandatory tender in 2025, and bills are in USD.
- **BZ**: BZD, pegged 2:1 to USD. PUC tariffs are in BZD.
- The rest are their national currencies: MXN, GTQ, HNL, NIO (cordoba), CRC (colon).

## Zone candidates

**Mexico: strong candidate.** Domestic tariffs are assigned by locality according to the minimum average
summer temperature. The subsidised summer blocks grow with heat, and the DAC trigger (a 12-month average
above which subsidy is lost) grows too.

| Tariff | Min. summer temp | Typical places | Summer subsidised blocks (kWh/month) | DAC trigger |
|---|---|---|---|---|
| 1 | below 25 C | CDMX, Edo. Mexico, Puebla, Toluca, Queretaro, Guadalajara | 75 basic + 65 intermedio, all year | 250 |
| 1A | 25 C | | 100 + 50 | 300 |
| 1B | 28 C | | 125 + 100 | 400 |
| 1C | 30 C | Monterrey area, Cancun | 150 + 150 + 150 | 850 |
| 1D | 31 C | Merida | 175 + 225 + 200 | 1,000 |
| 1E | 32 C | Hermosillo/Sonora coast, Culiacan | 300 + 450 + 150 | 2,000 |
| 1F | 33 C | Mexicali, Hermosillo | 300 basic + 900 intermedio bajo + 1,300 intermedio alto | 2,500 |

The summer block sizes are the CFE structure as I know it. They could not be re-read on cfe.mx (geo-blocked),
so they are low confidence. The DAC triggers match two secondary sources.

**DAC** (Aug 2026, secondary source traccionmedia.com; the arithmetic in its worked example checks out):

| | Value |
|---|---|
| Fixed charge | 145.04 MXN/month |
| Central | 6.630 MXN/kWh |
| Noroeste | 6.211 |
| Norte/Noreste | 6.051 |
| Sur/Peninsular | 6.148 |
| Baja California | 6.447 |
| Baja California Sur | 7.025 |

**Effective prices, Oct 2026.** I could not obtain the 1C-1F summer block prices. The 1F figures below
price its subsidised blocks at the Tarifa 1 basico/intermedio rates, which is an upper bound (historically
the summer rates are equal or lower).

| Case | Tax | MXN/kWh |
|---|---|---|
| CDMX, Tarifa 1, 150 kWh | IVA 16% | 1.67 |
| CDMX, Tarifa 1, 300 kWh (if not yet DAC) | IVA 16% | 3.19 |
| CDMX, DAC Central, 300 kWh | IVA 16% | (300 x 6.630 + 145.04) x 1.16 / 300 = 8.25 |
| Mexicali, 1F summer, 300 kWh (all basico) | IVA 8% | at most 1.23 |
| Mexicali, 1F summer, 600 kWh | IVA 8% | at most 1.36 |
| CDMX, DAC, 600 kWh | IVA 16% | 7.97 |

So at equal consumption the differences are:
- 300 kWh: 1F about 1.2 vs Tarifa 1 about 3.2, roughly 2.6x.
- 300 kWh against DAC: about 6.7x.
- 600 kWh: about 5.8x.

At each zone's own typical consumption the gap is smaller, about 1.2-1.4x, because hot-zone households use
far more kWh. Recognisable regions would be the states, grouped as:
- central/temperate (Tarifa 1/1A)
- Gulf/Yucatan (1C/1D)
- northwest desert (1E/1F: Sonora, Baja California, Sinaloa)
- the northern border region, which also gets the 8% IVA rate

**Guatemala: borderline, under 2x.** EEGSA (Guatemala, Escuintla, Sacatepequez departments) charges Q1.42.
DEOCSA (western departments) charges Q2.03, 1.43x higher. DEORSA (eastern departments) charges Q1.98.

**Panama: under 2x by tariff.** EDECHI (Chiriqui/Bocas) has a deeper FET subsidy, so subsidised residential
prices there are lower than in EDEMET or ENSA areas. Not a 2x gap.

**SV, HN, NI, CR, BZ:** no 2x regional differences. These have national or near-uniform tariffs. CR's
ICE/CNFL/cooperative tariffs differ by about 10-30%, and NI's isolated systems (ENATREL Caribbean coast,
Corn Island) are higher but small in population.

## Gaps

- **MX**: CFE's tariff site (app.cfe.mx) is geo-blocked (Imperva 403). The Tarifa 1 block rates come from a
  reproduction of CFE's table (airegulasolutions.com) and are cross-checked against the DOF monthly-factor
  mechanism and a second reproduction. The 1A-1F summer block prices could not be verified at all: the
  reproduction site shows Tarifa 1 values copied into every tariff, which is unusable. A re-fetch from a
  Mexican network, or from the DOF "Acervo historico" CFE PDFs, would raise confidence.
- **GT**: the detailed EEGSA pliego (cargo fijo vs energy split) is only in scanned resolutions; the CNEE
  headline Q/kWh was used.
- **SV**: the Aug-Oct 2026 pliego is not yet posted. The figure uses the May-Jul 2026 pliego plus the
  frozen 2024 energy charge, which the government says still applies.
- **BZ**: GST treatment is unverified (bel.com.bz returns 403).
- **Tax exemptions not fetched**: HN (ISV), NI (IVA at 300 kWh or less), CR (IVA at 280 kWh or less),
  PA (ITBMS).
- Municipal public-lighting fees are excluded in MX (DAP), GT, SV and HN.
