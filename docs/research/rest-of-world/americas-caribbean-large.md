# Group B (Caribbean): household electricity price, October 2026

Countries: CU DO HT JM PR BS TT BB. Researched 2026-10-04. Prices are in the currency households are billed in, all on-bill charges and taxes included, divided by the stated monthly consumption.

## CU Cuba: 1.44 CUP/kWh at 300 kWh (medium)

Source: Council of Ministers Acuerdo 9810/2024, Gaceta Oficial Extraordinaria No. 10, 2024-03-01, in force 2024-03-01
(https://www.gacetaoficial.gob.cu/sites/default/files/goc-2024-ex10_0.pdf). UNE's "Marco Legal y Regulatorio" page
(https://www.unionelectrica.cu/marco-regulatorio/) still lists it as the residential tariff.

Blocks are incremental and priced in CUP/kWh: 0-100 0.33 · 101-150 1.07 · 151-200 1.43 · 201-250 2.46 · 251-300 3.00 · 301-350 4.00 · ... · 501-600 11.50 · ... · >5000 25.00.

- At 300 kWh: 100×0.33 = 33.00; 50×1.07 = 53.50; 50×1.43 = 71.50; 50×2.46 = 123.00; 50×3.00 = 150.00. Total 431.00 CUP, which is **1.437 CUP/kWh**.
- At 200 kWh: 33.00 + 53.50 + 71.50 = 158.00 CUP, which is 0.79 CUP/kWh. I found no source for typical household use, so I used the 300 kWh default. Use 200 kWh if a later pass sources it.
- There is no fixed charge, and no tax appears on the bill.
- Caveats: I found no 2025-26 revision, but I could not confirm that none exists. Supply is heavily rationed (long blackouts). The tariff is far below cost.

## DO Dominican Republic: 7.33 DOP/kWh at 300 kWh (high)

Source: the BTS-1 tariff set by SIE, as published monthly by Edesur. The September 2026 sheet is at
https://www.edesur.com.do//media/25qjllpm/tarifa-septiembre-2026.xlsx, listed on https://www.edesur.com.do/enlaces-empresa/tarifa-electrica/. October 2026 is not yet published. Edenorte's page (https://www.edenorte.com.do/tarifas/) confirms that BTS-1 is the residential tariff for loads under 10 kW. The SIE site itself is behind a Cloudflare block.

BTS-1 for September 2026:
- Fixed charge: RD$42.10 for 0-100 kWh, RD$128.59 above 100 kWh.
- Energy, incremental blocks per kWh: 0-200 RD$6.05 · 201-300 RD$8.59 · 301-700 RD$12.89 · >700 RD$13.09.

At 300 kWh: 128.59 + 200×6.05 (1,210.00) + 100×8.59 (859.00) = RD$2,197.59, which is **7.325 DOP/kWh**.

Caveats:
- ITBIS is not charged on residential electricity. That is from my own knowledge and was not verified this round.
- Municipal public-lighting fees appear on some bills and are not included.
- The tariff is heavily subsidised by the state.

## HT Haiti: 0.20 USD/kWh (equivalent), at 200 kWh, 2017 (low; placeholder)

- No EDH tariff schedule could be retrieved: edh.ht does not resolve, and the regulator ANARSE (https://anarse.gouv.ht/) publishes no tariff tables.
- The only figure found is from the World Bank Renewable Energy for All PAD (2017-10, CC BY 3.0 IGO): "average electricity tariffs range from US$0.20 per kWh (for residential customers) to US$0.30 per kWh for industrial and commercial customers"
  (http://documents.worldbank.org/curated/en/606711509156039620/pdf/Haiti-Renewable-Energy-for-All-Project-PAD-10052017.pdf).
- EDH bills in HTG. The HTG figure behind that USD equivalent is unknown, and the gourde has since lost most of its value against the USD. Do not convert.
- Grid supply runs a few hours a day where it exists. Most households' effective cost is generator or solar.
- ANARSE's 2023 report mentions a 60% increase in 2023 for NRECA's Caracol (north) mini-grid customers. That is not EDH.

## JM Jamaica: 58.5 JMD/kWh at 165 kWh (medium)

Source: OUR media release of 2025-12-15
(https://our.org.jm/wp-content/uploads/2025/12/Media-Release-JPS-Customers-to-See-Moderate-Bill-Adjustments.pdf). It says the average residential customer uses **165 kWh/month**, and that this customer's bill of about J$9,000 rises by about J$655 (7%) on December 2025 bills. That gives about J$9,655 / 165 = **58.5 JMD/kWh**, all in.

Cross-check against the last full Rate 10 schedule I could retrieve, JPS Rate Schedules 2023, approved by OUR effective 2023-08-09
(https://www.jpsco.com/wp-content/uploads/2023/10/JPS-RATE-SCHEDULE-2023-O-Full-Page-25.6x35cm.pdf):

| Component | Basis | J$ |
|---|---|---|
| Customer charge | 603.54 per month | 603.54 |
| Energy, first 100 kWh | 100 × 8.31 | 831.00 |
| Energy, next 65 kWh | 65 × 23.86 | 1,550.90 |
| Fuel charge | about 29.8/kWh × 165 (December 2025, press-reported) | about 4,920 |
| IPP charge | about 11/kWh × 165 (press-reported) | about 1,850 |
| GCT | 7% on energy charges, plus FX adjustment | |
| **Total** | | **about J$9,700+** |

This is consistent with OUR's figure.

Caveats:
- jpsco.com blocks automated fetches, so I could not get the 2025/26 annually adjusted non-fuel rates.
- Fuel and IPP charges change monthly. Post-Hurricane Melissa deferred costs are being recovered through 2026.
- A J$26.776/kWh fuel rate for August 2026 appeared only in a search snippet and is unverified.

## PR Puerto Rico: 0.339 USD/kWh at 800 kWh (high)

Source: NEPR Resolución y Orden of 2026-09-30, docket NEPR-MI-2020-0001, the quarterly factors for Oct-Dec 2026
(https://energia.pr.gov/wp-content/uploads/sites/7/2026/09/20260930-MI20200001-Resolucion-y-Orden.pdf).

Approved from 2026-10-01:

| Factor | Oct-Dec 2026 | Jul-Sep 2026 |
|---|---|---|
| FCA | 0.173576 USD/kWh | 0.114070 |
| PPCA | 0.045090 USD/kWh | 0.051748 |
| FOS (fuel-oil subsidy clause) | 0.020822 | |
| Riders: CILT | 0.007386 | |
| Riders: SUBA-HH | 0.014338 | |
| Riders: SUBA-NHH | 0.000865 | |
| Riders: EE | 0.000853 | |

- Pension rider: a fixed $10.89/month for GRS since 2026-01, per LUMA's revised motion of 2025-11-25 in NEPR-AP-2023-0003 (https://energia.pr.gov/wp-content/uploads/sites/7/2025/11/20251125-AP20230003-LUMAs-Revised-Motion.pdf).
- NEPR's Anejo 4 gives the bill for a non-subsidised GRS residential customer at 800 kWh: **$270.86, i.e. $0.33858/kWh**, up from $228.59 ($0.28574) in Jul-Sep 2026.
- Variable part at 800 kWh: (0.218665 + 0.023442) × 800 = $193.69. The remaining $77.17 is customer charge, base energy, pension and provisional riders.
- 800 kWh is NEPR's reference household. I could not retrieve LUMA's tariff sheets (lumapr.com returns 403), so I did not recompute at 300 kWh. The fixed charges (about $15+) would push the 300 kWh figure somewhat above $0.34.
- Residential electricity carries no IVU.

## BS Bahamas: 0.225 BSD/kWh at 300 kWh (medium)

Sources:
- Base tariff: BPL's Equity Rate Adjustment, effective for bills after 2024-07-01 (https://www.bplco.com/new-tariff-rates-information-era/). Base energy is 0-200 kWh **0.00**, 201-800 kWh 11.95c, >800 14.95c. The fuel charge is the average minus 2.5c for the first 800 kWh and plus 1.5c above. VAT applies only to bills over $400.
- Customer charge of $3.36/month for residential: from https://www.bplco.com/services/home-generators/, the "understand your bill" page (undated).
- Fuel charge of 17.4c up to 800 kWh (21.4c above): the latest BPL publishes, for Dec 2025-Feb 2026 (https://www.bplco.com/fuel-charge-update/). It includes the government rebate that began in July 2025 (unrebated rate 18.5c).

At 300 kWh: 3.36 + 0 + 100×0.1195 (11.95) + 300×0.174 (52.20) = $67.51, which is **0.225 BSD/kWh**. No VAT, since the bill is under $400.

Caveats:
- Fuel charges for Mar-Oct 2026 are not posted. The Tribune (2026-06-04) cites an all-in range of 33-39 c/kWh and a fuel charge "more than 21 cents", which suggests the 2026 fuel charge is higher than 17.4c. This is the reason for medium rather than high confidence.
- Bahamian households use far more than 300 kWh (about $4,800/yr average bill per the Tribune). At 800 kWh the same tariff gives 0.268.

## TT Trinidad and Tobago: 0.373 TTD/kWh at 627 kWh (medium)

Source: RIC Final Determination 2023-2028, Table 1 "Tariffs for 2023"
(https://www.ric.org.tt/wp-content/uploads/2023/11/RICs-Final-Determination-for-the-Electricity-Transmission-and-Distribution-Sector-of-Trinidad-and-Tobago-2023-2028.pdf). The RIC press advertisement (https://www.ric.org.tt/wp-content/uploads/2023/10/Regulated-Industries-Commission-Tariffs-for-2023-2024_v2.pdf) confirms the bills.

Residential, billed monthly:
- Customer charge TT$7.50.
- Energy blocks: 1-200 kWh 0.28 · 201-700 0.40 · 701-1400 0.54 · >1400 0.68.

The RIC states that average residential use is **627 kWh/month**, with a bill of TT$234.30:
7.50 + 200×0.28 (56.00) + 427×0.40 (170.80) = TT$234.30, which is **0.374 TTD/kWh**.

At 300 kWh: 7.50 + 56.00 + 40.00 = TT$103.50 (0.345/kWh), matching the RIC table.

Caveats:
- The Determination excludes VAT. I treated residential electricity as VAT-free (zero-rated) but did not verify this. T&TEC's own tariff page (https://ttec.co.tt/default/tariffs-2) is stale, still showing 2009 rates, and says "All Rates subject to VAT".
- I found no annual tariff adjustment after 2023.
- There is no fuel pass-through; generation is gas-based and subsidised.

## BB Barbados: 0.647 BBD/kWh at 300 kWh (medium)

Sources:
- Base tariff: the BL&P Domestic Tariff (https://support.blpc.com.bb/support/solutions/articles/42000057422-domestic-tariff).
  - Customer charge $12/month in the 151-500 kWh band.
  - Base energy: first 150 kWh $0.160, next 350 $0.196, next 1000 $0.225, over 1500 $0.254.
  - Fuel clause adjustment on all kWh.
  - VAT on everything.
- FCA for Aug and Sep 2026: **37.5253 c/kWh** (https://www.blpc.com.bb/fuel-clause-adjustment/). Earlier 2026: Jan/Feb 28.99, Mar/Apr 35.83, May-Jul 39.75.

At 300 kWh, before VAT: customer charge 12.00 + base 150×0.160 (24.00) + 150×0.196 (29.40) + FCA 300×0.375253 (112.58) = $177.98.

VAT under BRA guidance OGC 07/2024 (https://bra.gov.bb/attachment?file=Attachments%2FOGC+No.+072024+GUIDANCE+NOTE+Re+VAT+on+the+Supply+of+Eletricity.pdf&name=Value+Added+Tax%3A+the+Supply+of+Electricity):
- 7.5% on the first 250 kWh, including the customer charge: (12 + 24 + 100×0.196 + 250×0.375253) = 149.41 × 7.5% = 11.21.
- 17.5% on the rest: (50×0.196 + 50×0.375253) = 28.56 × 17.5% = 5.00.

Total $194.18, which is **0.647 BBD/kWh**.

Caveats:
- BRA's last published extension of the 7.5% rate runs to 2025-03-31. A press summary of the March 2026 budget says the 7.5% cap continues, but I did not confirm that from a primary source. If it has lapsed (17.5% on everything), the price is 0.697.
- The March 2026 budget had the government absorb 50% of any FCA increase above the March 2026 level for three months from 2026-04-01 (EY budget summary: https://www.ey.com/content/dam/ey-unified-site/ey-com/en-bb/documents/ey-bb-budget-summary-2026-17032026.pdf). It is unclear whether the published FCA is gross or net of that absorption, or whether the absorption was extended.
- The 10% prompt-payment discount on customer and base charges is excluded.
- The Domestic Tariff page is dated 2022-09. The FTC rejected BL&P's 2023 rate increase, so the base rates are believed current.

## Currency

- **CU, CUP (Cuban peso)**: households are billed in CUP by UNE under the Acuerdo 9810/2024 table. The Banco Central de Cuba publishes three official segments (https://www.bc.gob.cu/tasas-de-cambio):
  - Segment III, the floating official rate, showed **USD 1 = 695.00 CUP** on 2026-10-04.
  - Segments I (state-entity fixed rate) and II are not shown in the static page. From my own knowledge (unverified this round) they are historically 24 and 120 CUP/USD.
  - The informal rate is different again.
  - Any USD conversion of the Cuban price depends heavily on which rate is used. At Segment III, 1.44 CUP is about USD 0.002/kWh.
- **DO, DOP**.
- **HT, HTG**: EDH bills in gourdes. The only figure found is a USD equivalent from 2017, so it is not comparable without the underlying HTG tariff.
- **JM, JMD**: fuel and IPP charges are USD-linked, and non-fuel charges are FX-indexed, but bills are in JMD.
- **PR, USD**.
- **BS, BSD**: pegged 1:1 to USD.
- **TT, TTD**.
- **BB, BBD**: pegged 2:1 to USD, so 0.647 BBD is about USD 0.32.

## Zone candidates

- None that qualify. All eight have a single national tariff for households:
  - DO: one SIE tariff for Edesur, Edenorte and Edeeste.
  - BS: BPL has uniform rates across islands, cross-subsidised at about $50m/month per the Tribune, 2026-06.
  - JM, PR, TT, BB: single utility.
- Haiti is the only place with real regional divergence. Isolated EDH grids, the NRECA Caracol grid in the north, and private mini-grids (WB PAD: US$0.55-0.80/kWh) differ widely from Port-au-Prince EDH. That is not a short list of recognised regions with sourced prices, so it is not proposed.
- In the Bahamas, Grand Bahama is served by a separate private utility, Grand Bahama Power Co., not BPL. Its tariff was not researched and may differ. Flag for a later pass, though GB is about 13% of the population.

## Gaps

- **HT**: no current EDH tariff obtainable (site down, regulator publishes none). Only a 2017 World Bank USD-equivalent placeholder, low confidence.
- **JM**: the current (2025/26) Rate 10 non-fuel schedule could not be fetched (jpsco.com blocks bots). The OUR average-bill figure was used instead.
- **PR**: no 300 kWh computation, because LUMA tariff sheets return 403. The NEPR 800 kWh reference bill was used.
- **BS**: BPL has not posted fuel charges after Feb 2026, and Grand Bahama Power was not covered.
- **BB**: the status of the 7.5% VAT relief and of the FCA absorption after Jun 2026 is unconfirmed.
- **TT**: the VAT treatment of residential electricity is unverified, as is whether any post-2023 annual adjustment happened.
- **CU**: there is no official typical-consumption figure. I also cannot rule out a 2025-26 tariff change.
