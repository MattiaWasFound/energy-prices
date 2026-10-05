# west-a: NG, GH, CI, SN, BF

Consumption basis: 300 kWh/month for the lower-middle-income countries (NG, GH, CI, SN), 200 kWh/month for low-income BF (the method's defaults). No sourced household-only average was found, except a Senegal proxy, noted below.

## NG Nigeria

- **Sources:** NERC monthly MYTO supplementary orders.
  - July 2025 orders for all 11 DisCos, e.g. https://nerc.gov.ng/wp-content/uploads/2025/08/IE_July_2025_064.pdf (and AEDC_..._059 through YEDC_..._069).
  - September 2026 order for PHED: https://nerc.gov.ng/wp-content/uploads/2026/09/PHED_HOLDCO_YSS_September_2026_097.pdf (a scan; I OCR'd it). Its table runs "Jul 2024 - Sep 2026" and says Bands A and B-E "shall remain frozen" at the July 2024 and Dec 2022 rates.
  - NERC Q1-2026 report: https://nerc.gov.ng/wp-content/uploads/2026/07/2026_Q1-Report.pdf ("end-user tariffs ... frozen at rates payable in July 2024").
  - The Presidency said on 27 Jul 2026 that there will be no 2026 tariff rise for any band: https://www.legit.ng/business-economy/energy/1721712-presidency-announces-decision-reported-electricity-tariff-increase-bands/
- **Structure:** a flat ₦/kWh rate set by service band (A-E, by hours of supply on the customer's feeder). Lifeline R1 (≤50 kWh) pays ₦4.00. There is no fixed charge for Non-MD customers.
- **Bands (Non-MD, ₦/kWh, before VAT):**
  - **The 2024 Band A change:** Band A went to 225.00 in Apr 2024, 206.80 in May 2024, and has been 209.50 at every DisCo since Jul 2024.
  - **Band B:** 61.00-68.96.
  - **Band C:** 45.80-56.91, median 52.51 (YEDC).
  - **Bands D/E:** 31.24-41.21 at ten DisCos; YEDC D is 50.01.
- **Which band households are on:** NERC (Vice-Chairman Oseni, April 2024) said Band A is about 15% of the ~12 million customers, e.g. https://www.channelstv.com/2024/04/03/breaking-fg-increases-electricity-tariff-for-band-a-customers/ So the majority (~85%) are on Bands B-E. I found no published split across B-E, so I use the middle band, Band C.
- **Arithmetic:** 52.51 × 1.075 (VAT 7.5%) = **₦56.45/kWh**. This is the same at any consumption level.
- **Range:**
  - Bands D/E: 33.58-53.76.
  - Band B: 65.58-74.13.
  - Band A: 225.21.
- **Caveats:**
  - The VAT treatment of household electricity under the Nigeria Tax Act 2025 (in force 2026) was not re-verified. 7.5% VAT is the DisCo billing practice under the Finance Act 2019.
  - About 41% of customers are unmetered (Q1-2026 report: 59.13% metered) and pay capped estimated bills.

## GH Ghana

- **Source:** the PURC publication of electricity tariffs dated 22 Sep 2026, effective 1 Oct 2026: https://www.purc.com.gh/attachment/67864-20261001121001.pdf
  - It keeps the Q3 rates unchanged (0% adjustment). The Q3 rise was 3.49% from 1 Jul 2026.
- **Residential tariff:**
  - **Lifeline:** 0-30 kWh at 89.9315 GHp, exclusive, with a 213 GHp service charge.
  - **Other residential:** 0-300 kWh at 203.7509 GHp/kWh, then 301+ kWh at 269.2235 GHp/kWh.
  - **Service charge for other residential:** 1,073.09 GHp/month.
- **Levies:**
  - Public Lighting Levy 3% and National Electrification Scheme Levy 2% of the electricity charge (Act 1135; https://www.taxlawgh.com/ghana-energy-sector-levies).
  - VAT: the 15% VAT (with NHIL and GETFund) on non-lifeline residential use was suspended by the government in Feb 2024 (https://www.graphic.com.gh/news/general-news/govt-officially-suspends-vat-on-electricity.html). So no VAT is included.
- **Arithmetic at 300 kWh:**
  1. Energy: 300 × 2.037509 = 611.25
  2. Service charge: + 10.73
  3. Levies: + 5% × 611.25 = 30.56
  4. Total: GHS 652.55, / 300 = **GHS 2.1752/kWh**
- **Caveats:**
  - I applied the levies to the energy charge only. Applying them to the service charge too would add about GHS 0.002/kWh.
  - The VAT suspension is open-ended, so it could be reinstated.

## CI Côte d'Ivoire

- **Sources:**
  - CIE's tariff page: https://www.cie.ci/particuliers/tarifs-electricite. It shows HT/TVA/TTC columns. CIE's site links Arrêté interministériel n°1355/MMPE/MFB of 27 Dec 2023 as the current tariff order.
  - The ANARE-CI price page, for structure and definitions: https://anare.ci/le-marche/prix-de-lelectricite/
    - It says the prime fixe for Domestique Général is per kVA.
    - It says RTI and the communal tax are charged per kWh.
    - It says the social tariff is for 5A subscriptions with an average of ≤200 kWh per bimester.
    - It says that in 2020, 48% of low-voltage customers were on Domestique Général.
- **Why Domestique Général:** at 300 kWh/month (600 kWh per two-month bill) a household is not eligible for the social tariff. So I used Domestique Général 10A (2.2 kVA).
- **Arithmetic per two-month bill (Abidjan):**
  1. Block 1 (≤180 h × 2.2 kVA = 396 kWh): 396 × 73.66 HT = 29,169.36
  2. Block 2: 204 × 63.84 HT = 13,023.36
  3. Prime fixe: 1,371.22 × 2.2 = 3,016.68
  4. TVA 18% on energy + prime fixe: 8,137.69
  5. Rural electrification fee (REF): 100 + 1.06 × 600 = 736
  6. RTI fee (the TV/radio levy): 2 × 600 = 1,200
  7. Household-waste removal tax, Abidjan: 2.50 × 600 = 1,500
  8. Total: 56,783.10 XOF, / 600 = **94.64 XOF/kWh**
- **Variants:**
  - Other communes (waste tax 1.00/kWh): 93.14.
  - If the prime fixe is per subscription rather than per kVA: 91.40.
  - Social 5A tariff at 75 kWh/month: about 57.
- **Caveats:**
  - The CIE page shows no effective date. I assumed Jan 2024, from the Dec 2023 arrêté. No 2025-2026 change was found, but none was ruled out, so medium confidence.
  - The CIE page is inconsistent on the RTI line: it shows "2,00" for some tariffs and "2 000" for others. I took 2 per kWh, as in ANARE's worked example.

## SN Senegal

- **Sources:**
  - CRSE Décision n°2025-140 of 26 Dec 2025, the Senelec tariff grid in force from 1 Jan 2026: https://www.crse.sn/wp-content/uploads/2026/03/Grille-tarifaire-Senelec-a-compter-du-01012026-1.pdf. The CRSE electricity page shows the same grid for Jan-Jun 2026.
  - Senelec key figures: https://www.senelec.sn/qui-sommes-nous/chiffres-cles/. In 2025, 1,889,696 of 2,527,726 customers were prepaid (Woyofal), about 75%.
  - The tax code (CGI 2025, https://www.dgid.sn/storage/docs/CGI-2025.pdf):
    - Electricity supplied to a household whose consumption does not exceed the social tranche is VAT-exempt.
    - A household above the social tranche pays VAT on its whole consumption.
    - The VAT rate is 18% (art. 369).
- **DPP tariff (FCFA/kWh, tax-exclusive, includes the 0.7 FCFA/kWh rural electrification levy):**
  - 0-150 kWh: 82.00
  - 151-250 kWh: 136.49
  - Over 250 kWh: 159.36
  - Prepaid bills the third tranche at the second-tranche rate.
  - There is no fixed premium for DPP.
- **Arithmetic at 300 kWh (prepaid):**
  1. 150 × 82.00 + 150 × 136.49 = 32,773.5
  2. × 1.18 TVA = 38,672.7
  3. / 300 = **128.91 XOF/kWh**
- **Variants:**
  - Postpaid at 300 kWh: 150 × 82 + 100 × 136.49 + 50 × 159.36 = 33,917, × 1.18 / 300 = 133.41.
  - Sourced proxy for typical use: Senelec low-voltage sales of 3,800.5 GWh over 2.52 million low-voltage customers is about 125 kWh/month (this includes small businesses). At that level a household stays in tranche 1 and pays 82.00 TVA-exempt. That is a large sensitivity.
- **Caveats:**
  - The billing period for the tranches is not stated in the grid. Postpaid bills are bimonthly; I treated the tranches as monthly, as for prepaid.
  - I assumed the "tranche sociale" for VAT is tranche 1 (set by a finance ministry arrêté I did not see).
  - A municipal tax said to appear on Senelec bills was not verified and is not included.

## BF Burkina Faso

- **Sources:**
  - Arrêté interministériel n°2023-382/MEMC/MEFP/MDICAPME of 29 Sep 2023, SONABEL grid applicable from 1 Oct 2023 (scan; read from the image): https://www.arse.bf/wp-content/uploads/2025/09/N°2023-2023-382-Arrete-Interministeriel-MEMC-MEFP-MDICAPME-portant-fixation-des-tarifs-de-vente-de-lenergie-electrique-par-la-Societe-Nationale-dElectricite-du-Burkina-SONABEL.pdf
  - The ARSE 2024 activity report (https://www.arse.bf/wp-content/uploads/2025/08/Rapport-dactivite-2024.pdf) confirms this grid is in force for urban SONABEL sales. No later change appears on the ARSE site, which as of Sep 2026 is only opening a tariff-methodology review.
- **Low-voltage domestic tariffs:**
  - **Type A, social, 1-3A:** 0-75 kWh at 75, 76-100 at 128, over 100 at 138; redevance 1,132/month.
  - **Type B1, normal single-phase, 5-15A:** 0-50 kWh at 96, 51-200 at 102, over 200 at 109; redevance 457/month; prime fixe 355 per ampere per month.
- **Arithmetic at 200 kWh, B1 10A:**
  1. Energy: 50 × 96 + 150 × 102 = 20,100
  2. Redevance: + 457
  3. Prime fixe: + 3,550
  4. Total: 24,107, / 200 = **120.54 XOF/kWh**
  - On 5A: 111.66.
- **Caveats:**
  - Taxes are not included. I could not confirm whether these kWh prices are HT, or whether TVA, a TV fee or an electrification levy is added to domestic bills: sonabel.bf refused connections. Low confidence.
  - Rural COOPEL areas use a separate 2009 arrêté.

## Currency notes

- **NG:** NGN.
- **GH:** GHS. PURC publishes tariffs in pesewas (GHp); 100 GHp = 1 GHS.
- **CI, SN, BF:** XOF, the West African CFA franc, pegged at 655.957 per EUR.

None of these countries is dollarised or has dual exchange rates.

## Zone candidates

- **NG:**
  - The 2x+ gap is between service bands, not regions. Band A pays ₦225.21 and Bands B-E pay ₦33.58-74.13 incl. VAT, and the bands are set feeder by feeder within every DisCo. So it does not map to regions.
  - **A zone split by DisCo is not warranted.**
    - The same-band spread across DisCos is at most about 1.6x, at Band D: 31.24 at Ikeja vs 50.01 at YEDC. All other DisCos' Band D is 31.24-41.20.
    - Band A is identical everywhere.
  - **Watch item:** under the Electricity Act 2023, several states now regulate their own markets (e.g. Enugu; Gombe moved in Jan 2026 per NERC's Q1 report). State tariffs may diverge later.
- **GH:** none (one national tariff).
- **CI:** none. The only regional difference is the waste tax, 2.50 vs 1.00 XOF/kWh.
- **SN:** none. Rural concessions are harmonised to Senelec rates (82.00 base).
- **BF:** none known.

## Gaps

- **BF:** taxes and levies on domestic bills are unverified, so the price excludes them (low confidence).
- **SN:** the municipal tax is unverified and excluded.
- **NG:** there is no public split of households across Bands B-E. Band C was chosen as the middle band, and this choice moves the figure by roughly ±35%.
