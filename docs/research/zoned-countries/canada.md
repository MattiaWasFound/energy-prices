# Canada household electricity prices by province/territory, researched 2026-10-04

Purpose: inputs for a household electricity price estimator. The figures are all-in residential prices in CAD per kWh
for a household using **1,000 kWh/month**: energy, delivery, fixed charges spread over 1,000 kWh, riders, sales
taxes, and any rebate that appears on the bill. The rows are in `config/static_prices.csv`. Raw pulls are not kept here.

**Bottom line.** No single openly licensed source covers all 13 jurisdictions with current, tax-inclusive, correct
numbers. The closest is the CER Market Snapshot of 2026-03-04, which covers all 13 at 1,000 kWh, excludes taxes and
uses rates as of about Nov 2025. Its licence is not OGL, and its Yukon and NWT figures leave out the riders. I used
CER as the backbone where it checks out. Where it doesn't, or where a utility has changed rates since, I replaced the
figure with the utility's own current tariff. Then I added each jurisdiction's tax rule.

---

## 1. Result (1,000 kWh/month, taxes included)

| Zone | Name | ¢/kWh ex-tax | Tax treatment applied | **¢/kWh all-in** | As of | Confidence |
|---|---|---:|---|---:|---|---|
| CA-AB | Alberta | 23.3 (RoLR) | GST 5% | **24.5** | 2026-08 | medium |
| CA-BC | British Columbia | 13.68 | GST 5% (PST exempt) | **14.4** | 2026-04 | medium |
| CA-MB | Manitoba | 10.95 | PST 7% + municipal 2.5% + GST 5% | **12.6** | 2026-01 | medium-high |
| CA-NB | New Brunswick | 19.07 | HST 15% minus 10% provincial rebate on kWh charges | **20.3** | 2026-04 | medium-high |
| CA-NL | Newfoundland and Labrador | 17.34 | HST 15% | **19.9** | 2026-07 | medium |
| CA-NS | Nova Scotia | 21.14 | HST 14%, provincial part rebated → 5% | **22.2** | 2026-05 | medium-high |
| CA-NT | Northwest Territories | 39.40 | GST 5% | **41.4** | 2026-07 | medium-high |
| CA-NU | Nunavut | 37.47 (winter, subsidised) | GST 5% | **39.3** | 2026-10 | medium-low |
| CA-ON | Ontario | 16.45 (net of OER) | HST 13% on pre-OER amount, OER 23.5% | **19.2** | 2025-11 | medium |
| CA-PE | Prince Edward Island | 19.81 | HST 15% | **22.8** | 2026-07 | medium-low |
| CA-QC | Quebec | 8.54 | GST 5% + QST 9.975% | **9.8** | 2026-04 | high |
| CA-SK | Saskatchewan | 18.50 | GST 5% + municipal surcharge (about 6% on average) | **20.5** | 2026-02 | medium |
| CA-YT | Yukon | 24.96 (with winter relief) | GST 5% | **26.2** | 2026-10 | low |

The population-weighted average of these 13 figures, using the 2026-07-01 populations from section 5, is
**17.2 ¢/kWh**.

How each figure was built. All arithmetic is at 1,000 kWh/month.

- **AB.** I took Hydro-Québec's Apr 2025 tax-included figures for Calgary (24.05) and Edmonton (23.10), both on the
  Rate of Last Resort. I weighted them 1.6 : 1.1 by city size, then scaled by StatCan CPI electricity for Alberta
  from 2025-04 to 2026-08 (209.0 → 216.2, ×1.0345). The RoLR energy charge is fixed for 2025–26 (EPCOR 12.01 ¢,
  ENMAX 12.06 ¢), so the drift is delivery charges. Customers on a competitive fixed contract pay less: CER's lowest
  readily available option is 18.71 ex-tax, about **19.6** with GST. Alberta has no single "average" price. RoLR is
  the default tariff, so I kept it here for consistency with the other provinces.
- **BC.** CER 13.186 (BC Hydro tiered rate, 2025) × 1.0375 for the 1 Apr 2026 bill increase, + GST. Hydro-Québec's
  Vancouver figure is a bit lower (12.60 ex-tax, Apr 2025). The $1.90/month Metro Vancouver transit levy is
  excluded.
- **MB.** CER 10.954 already uses the Manitoba Hydro rates of 1 Jan 2026 (+4.0% interim, PUB). That matches
  Hydro-Québec's 10.53 × 1.04. Taxes are for a customer without electric heat, the same assumption Hydro-Québec uses
  for Winnipeg. Customers with electric heat pay PST 1.4% and municipal tax 0.5%, about **11.7** all-in.
- **NB.** NB Power schedule N-1, effective 2026-04-14. Service charge $30.82 urban / $33.82 rural (I used the
  average), plus 15.39 ¢ base + 0.45 ¢ variance charge = 15.84 ¢/kWh. That is 19.07 ex-tax. Since Jan 2025 the
  province rebates "the provincial portion of the HST (10%) on electricity consumption" (kWh, not the service
  charge). The result is 190.72 × 1.15 − 15.84 = 203.49, i.e. 20.35 ¢. CER's 15.20 for NB doesn't fit NB Power's
  published charges and looks like an error.
- **NL.** CER 16.951 (Newfoundland Power, Jul 2025) × 1.023 for the 1 Jul 2026 average increase, + HST 15%.
- **NS.** NS Power Standard Residential rate from 1 May 2026 (+3.1%): $20.08/month + 19.128 ¢/kWh. Nova Scotia
  rebates the provincial part of HST on residential energy (Your Energy Rebate Program), so the net tax is 5%. CER
  chose the cheaper Time-of-Day rate (16.10 ex-tax). Few customers are on it.
- **NT.** Naka Power Yellowknife (Snare zone) schedule of 1 Jul 2026: $18 + 23.72 ¢ base, Rider R +8.199% on base,
  Rider F (NTPC purchased power) 10.84 ¢, franchise tax 2.464%, then GST. As a check, the schedule's own TPSP
  "Snare Zone (Yellowknife) reference rate" is 36.50 ¢/kWh, which equals 23.72 × 1.08199 + 10.84. CER's 25.52 is
  only $18 + 23.72 ¢ with no riders, so it understates NT by about 35%.
- **NU.** QEC's non-government residential rate is 74.94 ¢/kWh (interim since 1 Apr 2025). The Nunavut Electricity
  Subsidy Program pays 50% on the first 1,000 kWh in Oct–Mar (first 700 kWh in Apr–Sep) and covers the $36 service
  charge. In winter that gives 37.47 ex-tax, matching CER exactly. In summer it is about **51.1** all-in, and the
  12-month average is about **45.2**. Public-housing tenants (about 57% of homes) pay 6 ¢/kWh and are excluded. I
  could not verify whether the final 2025–26 rates or a Fuel Stabilization Rider change this.
- **ON.** CER 16.454 is the lowest-cost RPP plan (TOU, tiered or ULO), including delivery, regulatory charges and
  Global Adjustment, net of the Ontario Electricity Rebate. It is averaged over Hydro One 45% / Toronto Hydro 25% /
  Alectra 30%. HST applies to the bill before OER. So the all-in figure = net × (1.13 − 0.235)/(1 − 0.235), using
  the 23.5% OER in force since 1 Nov 2025. If CER actually used Nov 2024 prices with the 13.1% OER, the result would
  be 18.9. Cross-check: Hydro-Québec's Apr 2025 tax-included figures, scaled by CPI Ontario, give Toronto 18.8 and
  Ottawa 17.4. RPP prices reset again on **1 Nov 2026**, so update this figure then.
- **PE.** CER 19.805 (Maritime Electric, Mar 2025; urban $24.57 + 17.23 ¢ for the first 2,000 kWh), + HST 15%. The
  10% PEI Government Energy Rebate on the first 2,000 kWh ended **30 Jun 2026**. Neither CER nor Hydro-Québec had
  included it, so the pre-July bill was about 10% lower on energy. IRAC Order UE26-07 (Fiona cost recovery,
  effective 1 Aug 2026) adds an unverified ~2%. It is not included.
- **QC.** 8.29 ex-tax in Apr 2025 (Hydro-Québec and CER agree) × 1.03 for the 1 Apr 2026 Rate D increase (3%) +
  GST/QST.
- **SK.** CER 17.894 (SaskPower, 1 Apr 2025) + 3.9% on the energy charge from 1 Feb 2026. I assumed an energy charge
  of about 15.5 ¢ (assumption), giving about 18.50 ex-tax. Taxes: GST, plus SaskPower's municipal surcharge, which
  is about 10% in cities and 0 in rural areas. I used a blended +6%. Regina-type urban is about 21.3, rural about
  19.4.
- **YT.** ATCO Electric Yukon's own example at 1,000 kWh: $314 ex-GST from 1 Apr 2026, after the winter rebates
  ended and YEC Riders J/J1 rose. Rider F goes to 1.0 ¢ on 1 Oct 2026 (+$6.22). From Oct 2026 to Mar 2027 the
  expanded Affordability Rate Relief is "25% of electricity charges for the first 1,500 kWh". The maximum is $106 per
  month Oct–Dec 2026 and $112 per month Jan–Mar 2027. I pro-rated it to about $71 at 1,000 kWh (my estimate), so the
  relief amount and its GST basis are the uncertain parts. Without relief, Apr–Sep 2026 is **33.0** all-in. The
  12-month average is about **30**. CER's 13.60 is the base rate schedule without riders J/J1/R, which more than
  doubles base. Don't use it.

## 2. Sources and licences

| Source | Coverage | Basis | Licence (quoted) |
|---|---|---|---|
| **CER Market Snapshot, "How much do your neighbours across Canada pay for electricity?"**, released 2026-03-04. [link](https://www.cer-rec.gc.ca/en/data-analysis/energy-markets/market-snapshots/2026/market-snapshot-how-much-do-your-neighbours-across-canada-pay-for-electricity.html) | All 13; 750 / 1,000 / 1,500 kWh | "excluding all taxes"; "Including distribution charges and direct subsidies"; "lowest-cost rate structure available"; rates "as of November 2025"; one representative utility each | **Not OGL.** CER [terms](https://www.cer-rec.gc.ca/en/terms-conditions.html): "you may reproduce the materials in whole or in part for non-commercial purposes … without charge or further permission" with attribution; "you may not reproduce materials … for the purposes of commercial redistribution without prior written permission". The chart is Power BI. |
| **Hydro-Québec, "Comparison of Electricity Prices in Major North American Cities" 2025** (rates of 1 Apr 2025). [PDF](https://www.hydroquebec.com/data/documents-donnees/pdf/comparaison-prix-2025-en.pdf) | 12 Canadian cities (10 provinces; no territories) | 1,000 kWh/month; separate summary tables with and without taxes; Appendix C lists the taxes | **Proprietary.** Hydro-Québec [terms](https://www.hydroquebec.com/terms-confidentiality.html): "all Digital Platform content is also Hydro‑Québec property … If you wish to use, copy, translate, publish or distribute such content, you must obtain Hydro‑Québec's prior written authorization." Hydro-Québec's *open data* uses CC BY-NC 4.0 ([licence page](https://www.hydroquebec.com/documents-data/open-data/licence.html)), but this report is not in that portal. The 2026 edition (rates of 1 Apr 2026) is not out yet; the 2025 edition was deposited in Q4 2025. |
| **Statistics Canada CPI, table 18-10-0004-01**, product "Electricity", monthly to 2026-08. [table](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401) | 10 provinces + Whitehorse + Yellowknife (no Iqaluit) | Index (2002=100), taxes included | [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence) (OGL-style, attribution). |
| **CER Canada's Energy Future 2026, end-use prices** ([open.canada.ca](https://open.canada.ca/data/en/dataset/07c42deb-9435-43b9-a416-7ce316f3893d), CSV `end-use-prices-2026.csv`) | All 13, residential electricity, yearly | Modelled. Unit not stated in the data dictionary (probably real 2025 $/GJ). NU is unsubsidised. | **Open Government Licence – Canada**. Cross-check only; see section 4. |
| Utility tariffs: NB Power, NS Power, Naka Power, QEC, ATCO Electric Yukon, Manitoba Hydro | single jurisdictions | current schedules | Public regulatory documents with no open licence. I use only the facts (rates). |

Things that turned out not to exist: StatCan has no ¢/kWh table by province. Table 18-10-0204-01 is a selling-price
*index*. The CER provincial/territorial energy profiles have no residential prices. NRCan has no current all-province
residential ¢/kWh series.

## 3. Changes in 2025–2026 (the reason most figures moved)

- **Federal consumer carbon charge removed on 1 Apr 2025.** It had no direct effect on electricity, which was never
  charged. The exception is Saskatchewan: SaskPower stopped passing on its federal carbon charge on 1 Apr 2025, and
  SK CPI electricity fell 6.8% that month (206 → 192). CER/Hydro-Québec SK figures already reflect this.
- **ON:** On 1 Nov 2025 RPP prices rose (TOU 9.8 / 15.7 / 20.3 ¢, tiered 12.0 / 14.2 ¢, ULO 3.9 / 39.1 ¢) and the
  **OER went from 13.1% to 23.5%** to offset it. Bills net of OER barely moved. Tax-included prices rose because HST
  applies before OER (ON CPI +4.6% in Nov 2025). The next reset is 1 Nov 2026.
- **AB:** The Rate of Last Resort replaced the RRO on 1 Jan 2025, fixed at about 12.0 ¢ for 2025–26. The Restructured
  Energy Market is due mid-2027.
- **BC:** BC Hydro bills +3.75% on 1 Apr 2025 and +3.75% on 1 Apr 2026.
- **QC:** Rate D +3% on 1 Apr 2025 and on 1 Apr 2026 (residential increases capped at 3%).
- **MB:** +4.0% on 1 Jan 2026 (interim, then final in the PUB order of March 2026).
- **SK:** +3.9% on 1 Feb 2026, and another 3.9% requested for 1 Feb 2027.
- **NB:** Provincial 10% HST-equivalent rebate on residential kWh charges since Jan 2025. NB Power +4.29% on
  14 Apr 2026 (energy 14.76 → 15.39 ¢).
- **NS:** HST cut from 15% to 14% on 1 Apr 2025. Residential energy is net 5% after the YERP rebate. NS Power +3.1%
  on 1 May 2026.
- **PE:** PEI Government 10% Energy Rebate (first 2,000 kWh) ended 30 Jun 2026, replaced by the income-tested PEI
  Essentials Benefit. Fiona cost adjustment from 1 Aug 2026 (IRAC UE26-07). *Note:* PE CPI electricity was still
  flat in Jul–Aug 2026 (179.0). That is odd if the rebate ended, so the CPI may lag or treat the rebate differently.
  I did not resolve this.
- **NL:** Newfoundland Power about +7% on 1 Jul 2025 and +2.3% on 1 Jul 2026, after the province cut the July 2026
  increase.
- **YT:** Winter Electrical Affordability Rebate (−3.377 ¢) and Affordability Rate Relief (−2.674 ¢) ended
  31 Mar 2026. Riders J/J1 rose. The bill at 1,000 kWh went up 33.8% (Whitehorse CPI 228 → 305). The expanded relief
  (25% on the first 1,500 kWh) runs Oct 2026 to Mar 2027. Rider F rises on 1 Oct 2026.
- **NT:** NTPC GRA increases are passed through in Rider F, which was raised on 1 Jul 2026.
- **NU:** QEC interim rates from 1 Apr 2025: energy 67.33 → 74.94 ¢, service charge $18 → $36 (covered by NESP).

## 4. Cross-check table (¢/kWh at 1,000 kWh/month)

| Zone | HQ Apr-2025 ex-tax | HQ Apr-2025 incl. tax | CER ~Nov-2025 ex-tax | EF2026 "2026" (÷ 2.778, if $/GJ) | This file, all-in |
|---|---:|---:|---:|---:|---:|
| AB | 22.90 Cgy / 22.00 Edm | 24.05 / 23.10 | 18.71 (fixed contract) | 16.6 | 24.5 |
| BC | 12.60 | 13.43 | 13.19 | 13.1 | 14.4 |
| MB | 10.53 | 12.07 | 10.95 | 12.3 | 12.6 |
| NB | 16.61 | 20.84 (inconsistent with its own ex-tax figure ×1.15) | 15.20 (suspect) | 20.1 | 20.3 |
| NL | 15.59 | 17.92 | 16.95 | 18.2 | 19.9 |
| NS | 20.48 | 21.50 | 16.10 (TOD) | 21.6 | 22.2 |
| NT | — | — | 25.52 (no riders) | 27.8 | 41.4 |
| NU | — | — | 37.47 | 72.7 (unsubsidised) | 39.3 |
| ON | 15.57 Tor / 14.35 Ott | 17.90 / 16.50 | 16.45 | 15.8 | 19.2 |
| PE | 19.69 | 22.64 | 19.81 | 23.3 | 22.8 |
| QC | 8.29 | 9.53 | 8.29 | 10.4 | 9.8 |
| SK | 17.89 | 20.58 | 17.89 | 23.4 | 20.5 |
| YT | — | — | 13.60 (no riders) | 14.8 | 26.2 |

Hydro-Québec's Canadian tax-inclusive figures use one city each (Appendix C taxes): Montréal GST + QST; Calgary and
Edmonton GST; Charlottetown, Moncton, St. John's HST 15%; Halifax 5% (net of the provincial rebate); Ottawa and
Toronto HST 13%; Regina 10% municipal + GST; Vancouver $1.90 levy + GST; Winnipeg PST 7% + municipal 2.5% + GST
(non-electric heat).

## 5. Population for weighting: StatCan 17-10-0009-01, 2026-07-01 (Q3 2026, latest)

Source: [table 17-10-0009-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901), Statistics Canada
Open Licence.

| Zone | Population | Share |
|---|---:|---:|
| CA-NL | 552,462 | 1.32% |
| CA-PE | 182,989 | 0.44% |
| CA-NS | 1,103,419 | 2.64% |
| CA-NB | 883,522 | 2.11% |
| CA-QC | 9,067,114 | 21.69% |
| CA-ON | 16,262,121 | 38.91% |
| CA-MB | 1,517,379 | 3.63% |
| CA-SK | 1,278,402 | 3.06% |
| CA-AB | 5,101,050 | 12.20% |
| CA-BC | 5,710,598 | 13.66% |
| CA-YT | 50,356 | 0.12% |
| CA-NT | 45,904 | 0.11% |
| CA-NU | 43,091 | 0.10% |
| Canada | 41,798,407 | 100% |

## 6. Is there a published national average?

There is **no official one.** StatCan, CER and NRCan do not publish a national average residential ¢/kWh. The CER
2026 snapshot gives only a range: "roughly $83 to $375 per month" at 1,000 kWh. Hydro-Québec's "AVERAGE" row
(25.28 ¢ incl. tax) covers its 21 North American cities, US included, so it is not a Canadian figure. Commercial
sites publish unofficial ones, for example [energyhub.org](https://www.energyhub.org/electricity-prices/) (about
19.2 ¢, 2023) and [GlobalPetrolPrices](https://www.globalpetrolprices.com/Canada/electricity_prices/). Their method
and licence are unclear, so treat them as low confidence.

Derived here: the population-weighted average of section 1 is **17.2 ¢/kWh all-in**. Weighting by residential
customers or by kWh would give a different number, because QC homes use much more electricity. Weighting by
consumption would pull the average down.

## 7. Caveats

- Every figure is for one representative utility or tariff per jurisdiction, not a customer-weighted provincial
  average. This matters most for AB (competitive retail), ON (about 60 local distributors), SK (SaskPower vs
  Saskatoon Light & Power) and NT/NU (community zones, subsidies).
- 1,000 kWh/month is above the median in AB and ON (where homes heat with gas) and below it in QC and MB (where many
  heat with electricity). Fixed charges make ¢/kWh higher at lower use. CER's 750 / 1,500 kWh values are on the
  CER snapshot page.
- Seasonal subsidies make YT and NU figures depend on the month. The CSV gives the Oct 2026 (winter) value, and the
  `includes` column states the summer value and the 12-month average.
- Not re-fetched or unverified: the exact BC Hydro 2026 tariff, the exact SaskPower energy-charge split, the
  Maritime Electric Aug 2026 adjustment, the QEC final rates and FSR, and the GST basis of the Yukon relief.
