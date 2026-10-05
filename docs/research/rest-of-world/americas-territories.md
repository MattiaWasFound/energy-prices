# Group D (Americas north / Caribbean territories): household electricity price, October 2026

Territories: AW BQ CW SX BL MF GP MQ KY TC BM GL PM. All figures were fetched 2026-10-04.
Consumption is 300 kWh/month unless a typical household use was sourced (BQ 208, KY 1158).

## AW Aruba: AWG 0.3848/kWh (medium)
N.V. ELMAR residential rate, "effective as of the November 2024 bill month" and still the current page:
access charge AWG 12.50/month; energy 0.3431 (first 500 kWh), 0.3531 (501-1000), 0.4645 (>1000).
300 kWh: 300 x 0.3431 = 102.93, plus 12.50, gives 115.43. Divided by 300: **0.3848**.
ELMAR's annotated sample bill ("Understanding your statement") has only fixed charge and usage lines,
with no separate tax or fuel line, so the rates are treated as all-in. Caveat: the rate is from 2024 and
there is no 2026 confirmation beyond the live page. Source: https://www.elmar.aw/payment-&-billing/rates

## BQ Caribbean Netherlands: USD 0.6742/kWh, Bonaire headline (medium)
ACM sets maximum tariffs. The variable usage tariff is reset on 1 Jan and adjusted on 1 Jul for fuel.
- **Bonaire (WEB)**: from 1 Jul 2026 the ACM max variable tariff is USD 0.5021/kWh (Jan-Jun 0.3868); Pagabon prepaid 0.8518
  (ACM/UIT/681851, https://www.acm.nl/system/files/documents/beschikking-variabel-gebruikstarief-web-per-1-juli-2026.pdf).
  ACM max fixed charge 2026: 1x25A USD 51.33/mo, 3x25/3x35A 72.85
  (https://www.acm.nl/system/files/documents/beschikking-distributietarieven-elektriciteit-2026-web.pdf).
  WEB actually charges USD 35.85/mo for standard connections up to 3x35A from 1 Jul 2026 (down from 47.80), using
  extra subsidy from the EZ/KGG and I&W ministries (https://www.bonaire.nu/nieuws/consument/91879/web-verlaagt-vaste-tarieven-stroomprijs-stijgt).
  Typical use: 2500 kWh/yr (208.33 kWh/mo), the average in the BES ministerial regulation cited by ACM. Rijksdienst CN also says
  "approximately 210 kWh" per average household.
  208.33 x 0.5021 = 104.60, plus 35.85, gives 140.45. Divided by 208.33: **0.6742**. At 300 kWh: 0.6216.
- **Saba (SEC)**: ACM max variable from 1 Jul 2026 is USD 0.5465 (https://www.acm.nl/system/files/documents/beschikking-variabel-gebruikstarief-sec-per-1-juli-2026.pdf).
  SEC and the Public Entity keep 0.4792 through end-2026, sharing the difference
  (https://saba-news.com/saba-electric-customers-to-receive-temporary-tariff-relief-through-2026/).
  ACM fixed max: 3.2 kVA USD 34.28, 7.7 kVA 82.49. From March 2026 the subsidy covers 100% of 3.2 kVA and 60% of 7.7 kVA
  (https://www.bes-reporter.com/news/energy/88095/electricity-relief-for-saba-but-high-energy-costs-still-bite).
  3.2 kVA: **0.4792**. 7.7 kVA at 208 kWh: (32.996 + 99.83) / 208.33 = 0.638.
- **Sint Eustatius (STUCO)**: ACM max variable from 1 Jul 2026 is USD 0.3809 (https://www.acm.nl/system/files/documents/beschikking-variabel-gebruikstarief-stuco-per-1-juli-2026.pdf).
  ACM fixed max: 3.2 kVA USD 28.97/mo (https://www.acm.nl/system/files/documents/beschikking-distributietarieven-elektriciteit-2026-stuco.pdf).
  I could not find the subsidised fixed charge STUCO actually bills. Range: 0.3809 (fixed fully subsidised) to
  (28.97 + 79.35) / 208.33 = 0.520 (no subsidy). Low confidence.
- Caveats: whether ABB (BES consumption tax) applies to electricity was not verified. The variable tariff moves again on 1 Jan 2027.

## CW Curaçao: XCG 0.7133/kWh (medium)
Aqualectra domestic (01) tariffs valid as of 1 Oct 2026 (basic + fuel component, fuel reset monthly):
up to 250 kWh 0.3129 + 0.3827 = 0.6956; 250-350 kWh 0.4192 + 0.3827 = 0.8019; over 350 kWh 0.8461.
The site's own calculator JS confirms the blocks are incremental.
300 kWh: 250 x 0.6956 = 173.90, plus 50 x 0.8019 = 40.10, gives 214.00. Divided by 300: **0.7133**.
There is no fixed or meter charge on the rates page or in the calculator, and the prepaid Pagatinu rates match postpaid.
Caveat: I did not confirm whether OB (6%) sits inside these tariffs or is added on the bill. The Selikor waste tax is collected
on the same invoice but is not electricity, so it is excluded. Source: https://www.aqualectra.com/rates/

## SX Sint Maarten: XCG 0.74/kWh (low)
GEBE publishes no tariff sheet; its site only mentions a "fuel clause".
- Base rate is XCG 0.25/kWh, "unchanged since 2011", from the 2025 BTP SXM / RAC government-commissioned tariff evaluation
  as reported in https://stmaartennews.com/news/how-rising-energy-costs-impact-households-in-st-maarten/ (June 2026).
- Fuel clause is XCG 0.49/kWh from 10 Jul 2026, per a reader letter (https://stmaartennews.com/letters-to-the-editor/gebe-overcharges/, Sep 2026).
0.25 + 0.49 = **0.74** (energy only).
Excluded and unverified: any monthly fixed/meter charge and any turnover tax (TOT) on the bill. The fuel clause changes
monthly and is disputed (an ACP petition, and the government designated BTP as supervisor in May 2026). Low confidence.

## BL Saint-Barthélemy: EUR 0.2039/kWh (high)
EDF Archipel Guadeloupe Tarif Bleu résidentiel TTC for St-Barthélemy, valid 1 Aug 2026, Base 6 kVA:
subscription 159.60 EUR/yr (13.30/mo), energy 15.96 c/kWh. The TTC includes CTA, CSPE 2.25 c/kWh and the local electricity tax of
10% for 3-6 kVA. There is no VAT.
13.30 + 300 x 0.1596 = 61.18. Divided by 300: **0.2039**.
Source: https://www.edf.gp/sites/sei_gp/files/2026-08/Tarif_Bleu_residentiel_TTC_Guadeloupe_St_Barthelemy_01082026.pdf

## MF Saint-Martin (French): EUR 0.2119/kWh (high)
Same EDF grid structure, valid 1 Aug 2026, Base 6 kVA: 159.60 EUR/yr, 16.76 c/kWh TTC. The TTC includes CTA, CSPE 2.25 c/kWh,
taxe territoriale (0.25-0.75 c/kWh) and TGCA 4% on the TTC. There is no VAT.
13.30 + 300 x 0.1676 = 63.58. Divided by 300: **0.2119**.
Source: https://www.edf.gp/sites/sei_gp/files/2026-08/Tarif_Bleu_residentiel_TTC_Guadeloupe_St_Martin_01082026.pdf

## GP Guadeloupe: EUR 0.2377/kWh (high)
EDF Tarif Bleu résidentiel TTC, Guadeloupe excluding St-Barth and St-Martin, valid 1 Aug 2026, Base 6 kVA: 175.56 EUR/yr (14.63/mo),
18.89 c/kWh. The TTC includes CTA 15% of the fixed delivery part, accise 3.062 c/kWh, OMR 1.5%, TVA 8.5%, and the "rémanence d'octroi de mer"
0.5383 c/kWh inside the HT energy price.
14.63 + 300 x 0.1889 = 71.30. Divided by 300: **0.2377**.
Source: https://www.edf.gp/sites/sei_gp/files/2026-08/Tarif_Bleu_residentiel_TTC_Guadeloupe_01082026.pdf
CRE (16 Jul 2026 press release) states that in the ZNI all residential customers are on TRVE "au même niveau hors taxes qu'en France
métropolitaine. La fiscalité varie selon les territoires": https://www.cre.fr/fileadmin/Documents/Communiques_de_presse/2026/260716_CP_TRVE_Aout_2026.pdf
(deliberation 2026-147: https://www.cre.fr/fileadmin/Documents/Deliberations/2026/260715_2026-147_TRVE.pdf).
Mainland comparison: Base 6 kVA HT 13.61 c/kWh + 143.28 EUR/yr. TTC mainland 20.01 c/kWh + 190.32 EUR/yr.

## MQ Martinique: EUR 0.2384/kWh (high)
EDF Martinique Tarif Bleu résidentiel TTC valid 1 Aug 2026, Base 6 kVA: 175.56 EUR/yr, 18.96 c/kWh. Same taxes as GP
(TVA 8.5%, OMR 1.5%, accise, CTA), with a ROM of 0.6026 c/kWh.
14.63 + 300 x 0.1896 = 71.51. Divided by 300: **0.2384**.
Source: https://www.edf.mq/sites/sei_mq/files/2026-08/Tarif_Bleu_residentiel_TTC_Martinique_01082026.pdf
Note: the Aug 2026 deliberation removes the Base option only for "Bleu +" (>36 kVA) overseas. Residential Base 6 kVA remains;
the 9-36 kVA Base powers are being phased out.

## PM Saint-Pierre-et-Miquelon: EUR 0.2110/kWh (high)
EDF SPM Tarif Bleu résidentiel TTC, Saint-Pierre, valid 1 Aug 2026, Base 6 kVA: 159.60 EUR/yr, 16.67 c/kWh. The TTC includes CTA and
accise 3.062 c/kWh. There is no VAT. Check: HT 13.61 + 3.062 = 16.67.
13.30 + 300 x 0.1667 = 63.31. Divided by 300: **0.2110**.
Sources: https://www.edf.pm/sites/sei_pm/files/2026-08/Tarif_Bleu_residentiel_TTC_SPM_01082026.pdf ;
Miquelon grid (identical): https://www.edf.pm/sites/sei_pm/files/2026-08/Tarif_Bleu_residentiel_TTC_SPM_Miquelon_01082026.pdf ;
HT grid: https://www.edf.pm/sites/sei_pm/files/2026-08/bleu_residentiel_saint_pierre_et_miquelon.pdf
Caveat: households in a cold climate likely use more than 300 kWh. The per-kWh price is barely sensitive to that.

## KY Cayman Islands (Grand Cayman, CUC): KYD 0.3316/kWh (medium)
Rate R from 1 Jun 2026 (URCO-approved), per the CUC news release of 3 Jul 2026 (fetched from cuc-cayman.com press releases):
facilities charge CI$6.96/mo; energy charge 0.1387/kWh; licence and regulatory fee 0.0076/kWh on consumption over 1000 kWh.
Pass-through rates (https://www.cuc-cayman.com/fuel-cost) for October 2026: fuel cost 0.242491/kWh, fuel duty "-" (waived), renewables 0.005880.
The government Electricity Assistance Programme caps the fuel charge at CI$0.18/kWh on the first 2000 kWh for residential customers
using 101-3500 kWh. It was extended with the duty waiver to end-2026 (https://www.caymancompass.com/2026/09/29/government-extends-fuel-duty-waiver-through-end-of-year/).
Typical use: 1158 kWh/mo, CUC's 2025 average residential consumption.
6.96 + 1158 x 0.1387 (160.61) + 1158 x 0.18 (208.44) + 1158 x 0.00588 (6.81) + 158 x 0.0076 (1.20) = 384.02.
Divided by 1158: **0.3316**.
Check: the Compass example for September (1200 kWh) gives 398.23 with the cap, and my formula reproduces 398.23 exactly.
Without the cap (October fuel rate): 0.3941/kWh, about 0.407 with duty restored. There is no VAT in Cayman.
Caveat: the cap is temporary and income/usage-limited. Island Energy (Cayman Brac) tariffs were not priced.

## TC Turks and Caicos (Providenciales, Pelican Energy TCI, ex-FortisTCI): USD 0.48/kWh (medium)
FortisTCI was sold to Vision Ridge and renamed Pelican Energy TCI in Sept 2025.
The bill is kWh x electric rate plus kWh x fuel factor, with no fixed charge
(https://energymatters.pelicanenergytci.com/wp-content/uploads/2025/09/Understanding-Electricity-Bill_090225-1.pdf).
Residential electric rates come from the utility's bill estimator (https://www.pelicanenergytci.com/billestimate): Providenciales 0.26 if ≤300 kWh,
otherwise 0.275; Grand Turk 0.273/0.289; South Caicos 0.25/0.264. The fuel factor is authenticated monthly by the Energy and Utilities
Commissioner. August 2026 update: Providenciales/North/Middle Caicos 0.2771 (from 0.3017).
The TCIG Fuel Factor Relief Program caps the fuel factor at USD 0.22/kWh for eligible residential customers (3-month average bill below
$1,500), July-October 2026 (https://www.pelicanenergytci.com/ratecap).
300 kWh: 0.26 + 0.22 = **0.48** (eligible). Unsubsidised: 0.5371. Above 300 kWh: 0.495 capped, 0.5521 uncapped.
There is no VAT in TCI. The cap expires after October 2026 bills, so the price will likely jump back toward 0.54.

## BM Bermuda (BELCO): BMD 0.4159/kWh (high)
RA Bermuda-approved residential rates from 1 Aug 2026: energy blocks 0.14520 (0-250 kWh), 0.25611 (251-700), 0.39504 (700+).
Fuel adjustment rate 14.226 c/kWh from 1 Oct 2026. RA fee 0.00556/kWh. Graduated facilities charge tier 1 (0-10 kWh/day) BMD 31.33,
tier 2 (10-15) 47.00.
300 kWh: 250 x 0.1452 = 36.30, plus 50 x 0.25611 = 12.81, plus FAR 42.68, plus RA fee 1.67, plus GFC 31.33, gives 124.78.
Divided by 300: **0.4159**.
300 kWh/30 days is exactly 10 kWh/day, the tier 1/2 boundary. On a 31-day bill it is tier 1. With tier 2 the price is 0.4682.
There is no VAT/GST on the bill. Source: https://belco.bm/know-your-rate-and-bill/

## GL Greenland (Nukissiorfiit): DKK 2.0833/kWh (high)
Prisblad nr. 39, valid from 1 Jan 2026 and still linked as current. The el tariff for kundegruppe 1 (ordinary customers) is DKK 2.00/kWh in every
one of the 71 listed localities (Bilag A). The meter subscription is DKK 25.00/month.
300 x 2.00 = 600, plus 25, gives 625. Divided by 300: **2.0833**.
The price page says prices are set by Naalakkersuisut and are "ens for private, uanset hvor i landet man bor".
Greenland has no VAT (moms), and the prisblad mentions none.
Sources: https://nukissiorfiit.gl/da/kundeservice/priser/ ;
https://nukissiorfiit.gl/wp-content/uploads/2025/12/DK-Bilag-a-Prisblad-nr.-39-01.01.2026-.pdf

---

## Currency
- AW: **AWG** (Aruban florin). ELMAR bills in Afl./AWG.
- CW, SX: **XCG** (Caribbean guilder). It replaced ANG on 31 March 2025 in the Curaçao-Sint Maarten monetary union. Since 1 April 2026,
  NAf can be exchanged only at the CBCS, until 2055 (CBCS release reproduced at https://stmaartennews.com/banking/naf-now-only-exchangeable-at-cbcs/).
  Aqualectra's rate table is in XCG.
- BQ: **USD** (all ACM tariffs are in USD).
- BL, MF, GP, MQ, PM: **EUR**.
- KY: **KYD** (CUC bills in CI$).
- TC: **USD**.
- BM: **BMD** (pegged 1:1 to USD).
- GL: **DKK**.

## Zone candidates
- BQ: the three islands are separate systems with separate ACM decisions. Bonaire 0.674 USD/kWh (at 208 kWh), Saba 0.479
  (3.2 kVA, fixed fully subsidised), Sint Eustatius 0.38-0.52. This spread is about 1.3-1.8x, so it is not quite 2x. Bonaire is the
  headline (by far the most populous of the three). The islands are well known as separate units, so the list is short and recognisable if zones
  are ever wanted.
- GP vs BL vs MF: different ISO codes already. Same TRVE HT, different taxes: 0.204-0.238 EUR/kWh. No 2x difference.
- TC: island differences are small. Fuel factors and base rates vary about 5-10% between Providenciales, Grand Turk and South Caicos.
- KY: Cayman Brac/Little Cayman (Island Energy) not priced. Small population, so not a zone candidate.
- GL: Nukissiorfiit tariff is uniform nationwide (confirmed, 2.00 DKK/kWh in all 71 localities). There are no zones.
- PM: Saint-Pierre and Miquelon grids are identical.

## Gaps
- SX: no published GEBE tariff. Base rate and fuel clause come from news reports. Fixed charge and turnover tax are unknown, so low confidence.
- BQ Sint Eustatius: STUCO's actual (subsidised) fixed charge is unknown, so it is shown as a range. ABB applicability to BES electricity is unverified.
- CW: unclear whether OB is included in Aqualectra's published tariffs (believed to be all-in, unconfirmed).
- AW: the tariff date is Nov 2024. The page is current, but there is no 2026 confirmation of unchanged rates.
- KY / TC: headline prices include temporary government fuel caps (KY to end-2026, TC to Oct 2026 bills). Unsubsidised: KY 0.394, TC 0.537.
- No commercial tables (GlobalPetrolPrices etc.) were consulted, even as a sanity check.
