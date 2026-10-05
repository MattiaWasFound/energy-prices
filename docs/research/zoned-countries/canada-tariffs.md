# Canada: eight provinces rebuilt from utility tariffs (rates in force October 2026), researched 2026-10-04

Why this file exists: eight Canadian rows (AB, BC, MB, NL, ON, PE, QC, SK) depended on the CER market snapshot
(non-commercial terms) or Hydro-Québec's price comparison (all rights reserved). This file rebuilds each one from the
dominant utility's own published tariff, plus the tax and on-bill rebate rules. Rates are facts taken from public
regulatory documents. No CER or Hydro-Québec comparison figure is used. The rows are in
`config/static_prices.csv`. The bill calculations are below; the calculation script and the
downloaded tariffs are not kept here.

Convention: 1,000 kWh in a month of 365/12 = 30.42 days (this matters only for per-day charges). Taxes and on-bill
rebates are included. Every rate quoted is the one in force in October 2026.

## Result and comparison with the old rows

| Zone | Old row | Tariff rebuild | Change | Basis |
|---|---:|---:|---:|---|
| CA-AB | 24.48 | **23.66** | −3.3% | RoLR, Calgary/Edmonton |
| CA-BC | 14.36 | **13.76** | −4.2% | BC Hydro RS1101 tiered |
| CA-MB | 12.56 | **12.56** | 0.0% | Manitoba Hydro, Winnipeg, no electric heat |
| CA-NL | 19.94 | **19.92** | −0.1% | Newfoundland Power #1.1 |
| CA-ON | 19.25 | **18.90** | −1.8% | RPP TOU + Toronto Hydro + OER |
| CA-PE | 22.78 | **23.47** | +3.0% | Maritime Electric + Fiona adjustment |
| CA-QC | 9.82 | **9.74** | −0.8% | Hydro-Québec Rate D |
| CA-SK | 20.53 | **20.64** | +0.5% | SaskPower, 6% blended surcharge |

All figures are ¢/kWh including tax. **No row moves by more than 10%**, so the old rows were sound in level. The small
differences come from these sources:

- **AB −3.3%.** The old row was Hydro-Québec's April 2025 Calgary/Edmonton bills scaled by CPI. CPI also picks up
  customers on competitive contracts, whose energy prices fell in 2026 to about 8 ¢ against RoLR's 12 ¢. The actual
  2026 tariff is slightly lower.
- **BC −4.2%.** The old row compounded CER's 2025 figure by +3.75%. The real 1 Apr 2026 tariff paired a 0.59% base
  increase with a −1.5% deferral rider, and the tiered step-1 block is 675 kWh/month.
- **ON −1.8%.** CER averaged three distributors (Hydro One's rural rates are higher) and chose the lowest-cost plan.
  This rebuild uses Toronto Hydro and TOU.
- **PE +3.0%.** The old row left out the Fiona adjustment of 1 Aug 2026. It is now included.

---

## Bill calculations

### CA-QC — Hydro-Québec Rate D, effective 2026-04-01

Source: *2026 Electricity Rates*, Rate D, art. 2.5
([PDF](https://www.hydroquebec.com/data/documents-donnees/pdf/electricity-rates.pdf)). Block 1 covers
40 kWh × days = 1,217 kWh in an average month, so all 1,000 kWh fall in block 1.

| Item | CAD |
|---|---:|
| System access 46.154 ¢/day × 30.42 | 14.04 |
| Energy 1,000 kWh @ 7.065 ¢ | 70.65 |
| Subtotal | 84.69 |
| GST 5% | 4.23 |
| QST 9.975% | 8.45 |
| **Total** | **97.37 → 9.74 ¢/kWh** |

### CA-BC — BC Hydro Rate Schedule 1101 (tiered, the default), effective 2026-04-01

Source: BC Hydro Electric Tariff, RS 1101 rev. 13, RS 1901 and RS 1904, accepted 16 Mar 2026 (BCUC G-76-25 and
G-57-26) ([PDF](https://www.bchydro.com/content/dam/BCHydro/customer-portal/documents/corporate/tariff-filings/electric-tariff/bchydro-electric-tariff.pdf)).
The riders apply "to all charges … before taxes and levies".

| Item | CAD |
|---|---:|
| Basic charge 23.44 ¢/day × 30.42 | 7.13 |
| Step 1: 675 kWh @ 11.87 ¢ | 80.12 |
| Step 2: 325 kWh @ 14.08 ¢ | 45.76 |
| Deferral Account Rate Rider −1.5% | −2.00 |
| Trade Income Rate Rider 0% | 0.00 |
| Subtotal | 131.02 |
| GST 5% (residential electricity is PST-exempt) | 6.55 |
| **Total** | **137.57 → 13.76 ¢/kWh** |

The flat-rate option (RS 1151: 25.00 ¢/day + 12.70 ¢/kWh) works out to about 13.9 ¢. The $1.90/month Metro
Vancouver transit levy is excluded.

### CA-MB — Manitoba Hydro residential, effective 2026-01-01 (+4.0% interim, PUB)

Source: [Manitoba Hydro residential rates](https://www.hydro.mb.ca/accounts_and_services/rates/residential_rates/)
(≤200 A: $9.84/month + 9.970 ¢/kWh). The tax rates for a Winnipeg home without electric heat come from the
[City of Winnipeg gas and electricity tax page](https://assessment.winnipeg.ca/AsmtTax/English/Other_Taxes/GasElect.stm)
(2.5% on domestic non-heating use) and Manitoba Hydro's bill information (GST 5%, PST 7%, City tax 2.5%).

| Item | CAD |
|---|---:|
| Basic monthly charge | 9.84 |
| Energy 1,000 kWh @ 9.970 ¢ | 99.70 |
| Subtotal | 109.54 |
| PST 7% | 7.67 |
| City of Winnipeg tax 2.5% | 2.74 |
| GST 5% on charges + city tax | 5.61 |
| **Total** | **125.56 → 12.56 ¢/kWh** |

The GST basis is an assumption: I took GST to include the city tax. Leaving it out would change the result by
0.01 ¢. Homes with electric heat pay reduced PST and city tax, about 11.7 ¢ all-in.

### CA-NL — Newfoundland Power Rate #1.1 Domestic, effective 2026-07-01

Source: PUB Order [P.U. 16(2026)](http://www.pub.nf.ca/PU/orders/2026/P.U.%2016(2026).PDF), Schedule A. The order
approves a Rate Stabilization Adjustment of 2.283 ¢/kWh and an MTA factor of 1.02365, and the rates include both.
The province's $45M credit from the RRA account cut the increase from about 7% to 2.25%.

| Item | CAD |
|---|---:|
| Basic customer charge (≤200 A) | 17.36 |
| Energy 1,000 kWh @ 15.587 ¢ | 155.87 |
| Subtotal | 173.23 |
| HST 15% | 25.98 |
| **Total** | **199.21 → 19.92 ¢/kWh** |

The 1.5% prompt-payment discount is ignored. The same arithmetic on the 1 Jul 2025 schedule ($17.38 + 15.213 ¢) gives
169.51, which exactly matches CER's figure. That confirms the method.

### CA-ON — OEB Regulated Price Plan (TOU) + Toronto Hydro + Ontario Electricity Rebate

**Plan choice.** I used Time-of-Use. It is the default RPP plan: customers stay on it unless they opt into Tiered or
ULO. The prices run 1 Nov 2025 to 31 Oct 2026: off-peak 9.8 ¢, mid-peak 15.7 ¢, on-peak 20.3 ¢. I weighted them with
the OEB's own TOU consumption split of 64/18/18 (RPP Price Report, 17 Oct 2025, Table ES-2,
[PDF](https://www.oeb.ca/sites/default/files/rpp-price-report-20251017.pdf)), which gives 12.752 ¢. The OER has been
23.5% since 1 Nov 2025 (OEB RPP backgrounder of 17 Oct 2025).

**Distributor.** Toronto Hydro, using the tariff effective 1 Jan 2026 from OEB Decision and Rate Order EB-2025-0006
([PDF](https://www.rds.oeb.ca/CMWebDrawer/Record/925317/File/document)) and the
[Toronto Hydro rates page](https://www.torontohydro.com/for-home/rates). The total loss factor is 1.0295.

| Item | CAD |
|---|---:|
| Electricity: 1,000 kWh × 12.752 ¢ (TOU 64/18/18) | 127.52 |
| Delivery: service charge 51.18 + SME 0.41 + pole riders +0.01 + useful-life riders −2.74 = 48.86 per 30 days, × 30.42/30 | 49.54 |
| Delivery: DVA rider 0.112 ¢ + CBR rider 0.048 ¢ × 1,000 kWh | 1.60 |
| Delivery: transmission (network 1.346 + connection 0.895 = 2.241 ¢) × 1,029.5 kWh | 23.07 |
| Delivery: line losses, 29.5 kWh × 12.752 ¢ | 3.76 |
| Regulatory: WMS 0.41 + CBR 0.06 + RRRP 0.06 = 0.53 ¢ × 1,029.5 kWh, + SSS $0.25 per 30 days | 5.71 |
| Subtotal before HST and OER | 211.20 |
| HST 13% on the subtotal | 27.46 |
| Ontario Electricity Rebate, −23.5% of the subtotal (a pre-tax credit; HST is charged on the amount before the rebate) | −49.63 |
| **Total** | **189.03 → 18.90 ¢/kWh** |

The Tiered plan (summer threshold 600 kWh, which applies in October: 600 × 12.0 + 400 × 14.2) costs $128.80 on the
electricity line, against $127.52 for TOU, which is +0.08 ¢ all-in. Hydro One rural customers pay noticeably more
for delivery, so a province-wide customer-weighted figure would come out higher. RPP prices reset on 1 Nov 2026,
so this row needs updating then.

### CA-PE — Maritime Electric residential + Fiona adjustment from 2026-08-01

Sources:

- Maritime Electric *Schedule of "Adjusted Rates"*, still at the 1 Mar 2025 rates when captured on 4 Mar 2026
  ([PDF](https://www.maritimeelectric.com/media/qiolj0g5/schedule-of-adjusted-rates.pdf)). Urban rate 110 is
  $24.57/month and rural rate 130 is $26.92/month. Both charge 17.23 ¢ for the first 2,000 kWh, which includes ECAM
  0.475 ¢ and EE&C 0.121 ¢.
- Maritime Electric's
  [Fiona rate adjustment notice](https://www.maritimeelectric.com/about-us/messages-for-our-customers/hurricane-fiona-restoration-rate-adjustment-notice/)
  under IRAC Order UE26-07 (29 Jul 2026). It gives the benchmark rural bill at 1,000 kWh as $199.22 on 31 Jul 2026
  and $205.28 from 1 Aug 2026 (+3.1%). $199.22 is exactly $26.92 + 1,000 × 17.23 ¢, so the March 2025 rates were
  still in force on 31 Jul 2026.
- The 10% PEI Government Energy Rebate
  [ended 30 Jun 2026](https://www.maritimeelectric.com/about-us/messages-for-our-customers/elimination-of-the-pei-government-energy-rebate/).

| Item | CAD |
|---|---:|
| Service charge, average of urban 24.57 and rural 26.92 | 25.75 |
| Energy: 1,000 kWh @ (17.23 + 0.606 Fiona) ¢ | 178.36 |
| Subtotal | 204.11 |
| HST 15% (no provincial rebate since 1 Jul 2026) | 30.62 |
| **Total** | **234.72 → 23.47 ¢/kWh** |

Uncertainties:

- **The Fiona adder.** I derived 0.606 ¢/kWh from the $6.06 difference in Maritime Electric's own benchmark bill. I
  could not reach the order text itself (irac.pe.ca refused the connection).
- **A pending ECAM increase.** In December 2025 Maritime Electric applied to raise ECAM to 1.949 ¢/kWh from
  1 Mar 2026. The 31 Jul 2026 benchmark shows it was not in effect then, and I could not verify its status since. If
  it were approved, the bill would rise by about +1.7 ¢ all-in.

### CA-SK — SaskPower residential (E01 urban / E03 rural), effective 2026-02-01

Source: SaskPower *Residential Rates*
([PDF](https://www.saskpower.com/-/media/SaskPower/Accounts-and-Services/Rates/Service-Rates/Power-Supply-Rates/Report-Rates-Residential.ashx)):
$31.16/month + 15.476 ¢/kWh for both codes. The rates are net of "any taxes or surcharges". SaskPower's
[sample residential bill](https://www.saskpower.com/accounts/billing/your-power-bill/how-to-read-your-bill/residential)
shows a 10% municipal surcharge and 5% GST, and no PST.

| Item | CAD |
|---|---:|
| Basic monthly charge | 31.16 |
| Energy 1,000 kWh @ 15.476 ¢ | 154.76 |
| Subtotal | 185.92 |
| Municipal surcharge, blended 6% (assumption: 10% cities, 5% towns/villages, 0 rural) | 11.16 |
| GST 5% on charges | 9.30 |
| **Total** | **206.37 → 20.64 ¢/kWh** |

A Regina-type city (10%) comes to 21.38 ¢, and rural to 19.52 ¢. Two parts are assumptions: the 6% blend, and that
GST is not charged on the surcharge. Taxing the surcharge would add 0.06 ¢. Saskatoon's core is served by Saskatoon
Light & Power, not SaskPower.

### CA-AB — Rate of Last Resort, Edmonton and Calgary (weighted 1.6 Calgary : 1.1 Edmonton)

RoLR is the default supply for anyone without a retail contract. Its energy price is fixed for 2025–26. Competitive
fixed contracts in 2026 cost about 7.8–8.25 ¢ for energy, against RoLR's 12 ¢, so contract customers pay several
¢/kWh less. EPCOR's historical-rates page lists them.

**Edmonton.** EPCOR Energy Alberta RoLR price schedule, effective 1 Jul 2026
([PDF](https://www.epcor.com/content/dam/epcor/documents/rates/regulated-rate-tariffs/2026-07-edmonton-regulated-rate-tariff.pdf)).
EDTI 2026 interim DAS-R and SAS-R tariffs, riders G (Balancing Pool, +0.130 ¢), J (SAS true-up, −0.016 ¢) and K
(transmission deferral, +0.103 ¢ from 1 Oct 2026), and the City of Edmonton franchise fee of 1.388 ¢/kWh (all on
[EPCOR's tariffs page](https://www.epcor.com/ca/en/ab/edmonton/account/rates/special-fees-charges/electricity-tariffs.html)).

| Item | CAD |
|---|---:|
| RoLR energy 1,000 kWh @ 12.01 ¢ | 120.10 |
| RoLR administration $0.230/day | 7.00 |
| Distribution $0.72856/day | 22.16 |
| Distribution 1.783 ¢/kWh | 17.83 |
| Transmission 4.050 ¢/kWh | 40.50 |
| Riders G + J + K = +0.217 ¢/kWh | 2.17 |
| Local access (franchise) fee 1.388 ¢/kWh | 13.88 |
| Subtotal | 223.64 |
| GST 5% | 11.18 |
| **Total** | **234.82 → 23.48 ¢/kWh** |

**Calgary.** ENMAX Energy interim 2026 RoLR residential schedule: 12.06 ¢/kWh + $0.4134/day
([PDF](https://assets.enmax.com/api/public/content/516f331f11314de58342afacbb98bc1e?v=52c9f5c0)). ENMAX Power D100
distribution tariff "in effect as of April 1, 2026", with DAS/SAS from AUC Decision 30299-D01-2025
([PDF](https://assets.enmax.com/api/public/content/267403ea7dc446518a54d1a3fc13d39b?v=e6ddec2a)). The City of
Calgary local access fee for 2025–26 is a fixed 1.5507 ¢/kWh
([calgary.ca](https://www.calgary.ca/our-finances/facts/franchise-fee-update.html)).

| Item | CAD |
|---|---:|
| RoLR energy 1,000 kWh @ 12.06 ¢ | 120.60 |
| RoLR administration $0.4134/day | 12.57 |
| Distribution $0.769463/day | 23.40 |
| Distribution 1.5477 ¢/kWh | 15.48 |
| Transmission 3.8996 ¢/kWh | 39.00 |
| Riders: Balancing Pool +0.1290 ¢, quarterly TAC −0.1826 ¢ (Q3 2026), TAC deferral +0.0483 ¢ | −0.05 |
| Local access fee 1.5507 ¢/kWh | 15.51 |
| Subtotal | 226.51 |
| GST 5% | 11.33 |
| **Total** | **237.83 → 23.78 ¢/kWh** |

The Q3 2026 TAC rider (AUC Disposition 30883-D01-2026) comes from a search snippet, because media.auc.ab.ca refused
the download. The Q4 (1 Oct 2026) value is not published in the schedule I could reach. Either way it moves the total
by about ±0.2 ¢. Weighted result: (1.6 × 23.78 + 1.1 × 23.48) / 2.7 = **23.66 ¢/kWh**.

## Licence

Every source is a utility tariff, a regulator's order or rate report, or a municipal fee notice. These are public
regulatory documents, and the numbers in them are facts. No source carries an open licence, and none was needed. I
could not read the OEB site's own terms of use (oeb.ca refused the connection), and none of the documents
used states any terms specific to them. So the CSV records "utility tariff (public regulatory document; rates are
facts)" for all eight rows.

## Things not verified

- **PE.** The status of the March 2026 ECAM application, and the text of UE26-07 (the adder is derived).
- **AB.** The Q4 2026 ENMAX TAC rider. EDTI's 2026 DAS/SAS rates are still interim.
- **SK.** The share of customers paying each surcharge rate, and the GST treatment of the surcharge.
- **MB.** The GST basis of the city tax.
- **Hosts I could not reach.** newfoundlandpower.com, pub.nl.ca (pub.nf.ca worked), oeb.ca (I used Wayback copies of
  the 17 Oct 2025 report and backgrounder), irac.pe.ca and maritimeelectric.com (I used Wayback copies), and
  media.auc.ab.ca.
