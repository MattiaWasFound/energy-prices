# asia-south-west: household electricity price per kWh (October 2026)

Countries: Southern Asia AF BD BT IN IR LK MV NP PK; Western Asia AE AM AZ BH IL IQ JO KW LB OM PS QA SA SY YE.
Figures in `asia-south-west.csv`.

How the research was done: sources are official sites, read via archived copies on
web.archive.org where a site blocked automated access. No
commercial tables were used. "Read via archive" means the numbers were seen on an archived copy of the
official page.

## Southern Asia

**AF, 2.5 AFN/kWh (medium).** DABS "Kabul Breshna tariffs from 1395 to Present" (image on
https://main.dabs.af/static/16): residential 0-200 kWh 2.5, 201-400 3.75, 401-700 6.25, 701-2000 8.75,
>2000 10 AFN/kWh. At 200 kWh (low-income default): 200 x 2.5 = 500 AFN, so 2.5. At 300 kWh, if blocks are
marginal: 500 + 100 x 3.75 = 875, so 2.92. No taxes or meter rent shown. No change seen in DABS news since
Aug 2024. Kabul only; supply limited and mostly imported.

**BD, 7.72 BDT/kWh (medium).** BERC order of 3 Jun 2026 (from bill month June 2026), corrected 4 Jun 2026:
lifeline 0-50 4.63, 0-75 5.26, 76-200 8.50, 201-300 9.10, 301-400 9.62, 401-600 15.01, >600 17.35 Tk/kWh
(telescopic), demand charge 42 Tk/kW/month. Typical use 138 kWh = BPDB FY22-23 domestic sales / 3,388,588
domestic consumers (BPDB zones only). 75 x 5.26 + 63 x 8.50 = 930.0, + 84 (2 kW, assumed) = 1,014.0, + 5% VAT
= 1,064.7 Tk, so 7.72. With 1 kW 7.40; at 200 kWh 8.09. VAT and sanctioned load not seen on the order.
Correction PDF: https://objectstorage.ap-dcc-gazipur-1.oraclecloud15.com/n/axvjbnqprylg/b/V2Ministry/o/office-bpdb/2026/5/4eb054d9-34eb-4cf5-be6f-a7e1c25be406.pdf

**BT, 1.97 BTN/kWh (medium).** BPC LV tariff since 1 Nov 2024, extended by an ERA interim order of
1 Jul 2025 while the 2025-28 application is pending: Block I 0-100 kWh 1.28 Nu (free for rural homes and
0-200 for highlanders), Block II >100 kWh 2.66. No fixed charge on LV (ERA Tariff Determination
Regulation 2025). 200 kWh (no sourced typical figure): 100 x 1.28 + 100 x 2.66 = 394 Nu, so 1.97. Rural:
266 Nu, so 1.33. At 300 kWh 2.20. GST status unknown.

**IN, 3.06 INR/kWh (medium), national figure, no zones.** Method: CEA "Electricity Tariff & Duty and
Average Rates of Electricity Supply in India", March 2026 (https://cea.nic.in/wp-content/uploads/fs___a/2026/08/Book_2026-1.pdf),
Table 1(a): each state's all-in domestic rate at 1 kW / 100 kWh per month (energy + fixed charge per kWh +
electricity duty). 100 kWh is the CEA's standard level and close to the all-India average of 109 kWh per
household connection (CEA General Review 2025: 369,059.5 GWh household sales / 281,715,538 connections =
1,310 kWh/yr). State on-bill subsidies were applied using the CEA's state-by-state subsidy list (pp. 39-57),
checking against each state's tariff schedule whether the table rate is before or after subsidy. Then
weighted by household connections per state (urban/rural split for six states by Census 2011 rural share;
Maharashtra 83% MSEDCL / 17% Mumbai utilities, estimated). Results: weighted 5.78 before subsidies, 3.06
after; consumption-weighted 5.52 / 3.02; median 3.21. At 100 kWh, 26.5% of households live where the bill
is zero (Karnataka Gruha Jyothi, Bihar 125 units, Rajasthan 100 units, Punjab 300/month, Delhi 200 units,
Jharkhand 200 units, Himachal 125 units); Tamil Nadu (1.18) and Madhya Pradesh (1.00) are near-free.
Sensitivity to enrolment in registration-based schemes gives a range of 3.0-3.6. Excludes monthly
fuel/power-purchase adjustment surcharges and FY2026-27 tariff orders (not yet consolidated).

**IR, 2,200 IRR/kWh (low).** No official 1405 (2026/27) rial schedule could be reached (tavanir.org.ir,
moe.gov.ir refuse or challenge). From Khabaronline reports quoting Tavanir/Ministry officials: price is set
against a monthly consumption "pattern" (normal zone 200 kWh, 300 in June-Sept; tropical zones up to 3,000
in hot months); below pattern 0.15 x supply cost, pattern to 1.5x pattern 0.5x, to 2.5x 2.5x, above 5x.
1404 rates ~139 toman/kWh to 100 kWh and 162 toman to 200 kWh (https://www.khabaronline.ir/news/2062066);
bills up to 40% higher year on year in 1405. 200 kWh, normal zone, October: 100 x 1,390 + 100 x 1,620 =
301,000 IRR, x 1.0-1.4 = 301-421k, + 10% electricity levy + 10% VAT = 361-506k IRR, so 1,800-2,500,
headline 2,200 IRR/kWh. Subscription fee, insurance and fuel-cost lines not quantified.

**LK, 20.58 LKR/kWh (high).** PUCSL tariff effective 11 May 2026 (Annex 2,
https://www.pucsl.gov.lk/wp-content/uploads/2026/05/Annex-2-Approved-Tariff-Tabel_May-2026.pdf), kept by
the July 2026 decision ("continue with the existing end-user electricity tariffs",
https://www.pucsl.gov.lk/wp-content/uploads/2026/07/Full-Decision-on-Electricity-Tariffs-July-2026.pdf).
Domestic 0-60 kWh category: 0-30 at 5 (fixed 80), 31-60 at 9 (fixed 210). 61-180 category: 0-60 at 14,
61-90 at 20 (fixed 400), 91-120 at 28 (fixed 1,000), 121-180 at 44 (fixed 1,500). Above 180: all 180 at
32.50, rest at 100, fixed 2,500. Typical use 69 kWh = CEB Statistical Digest 2025
(https://www.ceb.lk/front_img/img_reports/1783568926SD-2025-Finalized-(Web-Edition).pdf): 5,079 GWh over
6,142,601 domestic accounts. 60 x 14 + 9 x 20 = 1,020 + 400 fixed = 1,420 LKR, so 20.58. No tax line on the
PUCSL calculator (https://www.pucsl.gov.lk/calculator/js/calculator.js). Steep around the 60 kWh step: at
60 kWh it is 10.50. CEB's 2025 average domestic revenue was 24.14 LKR/kWh.

**MV, 1.42 MVR/kWh (low).** URA tariffs page (updated March 2026, https://www.ura.gov.mv/en/electricity-tariffs):
domestic 0-100 1.25, 101-400 1.50, 401-500 2.66, 501-600 3.20, >600 3.83 MVR/kWh, same in Malé and all atolls.
300 kWh: 125 + 300 = 425 MVR, so 1.42. Low because URA also shows a fuel-surcharge rule (0.03 MVR/kWh per
0.10 MVR/litre above 8.00) that could add over 1 MVR/kWh if households pay it, which was not confirmed;
GST unknown; STELCO's site blocked automated access.

**NP, 8.63 NPR/kWh (medium).** ERC bill calculator (https://www.erc.gov.np/electricity-calculator, rates
labelled "ERC approved FY 2081/82"), 15A single-phase: 0-20 4.00, 21-30 6.50, 31-50 8.00, 51-250 9.50,
>250 11.00 NPR/kWh, plus a monthly demand charge set by the slab of total use (100 for 51-100 kWh, 125 for
101-250). Typical use 80 kWh = NEA annual report 2025/26: 5,169 GWh domestic sales / 5,372,615 domestic
consumers. 20 x 4 + 10 x 6.5 + 20 x 8 + 30 x 9.5 = 590 + 100 = 690, so 8.63. At 200 kWh 9.28. 5A
households (about 48%) pay 7.31-8.06; the ERC calculator and NEA's own tariff PDF
(https://nea.org.np/uploads/shares/Tarrif_rates/Consumer_Tarrif_data.pdf) disagree on whether the first
20 units are free. VAT believed nil, not verified.

**PK, 18.89 PKR/kWh (medium).** NEPRA uniform tariff, SRO 279(I)/2026 of 12 Feb 2026 (calendar-year 2026
tariff, adds residential fixed charges); also on https://iesco.com.pk/tariff-guide. Protected: 1-100 kWh
10.54 (fixed 200 Rs/kW/month), 101-200 13.01 (fixed 300), with the previous-slab benefit. Unprotected
1-100 22.44 ... 101-200 28.91 (fixed 300) ... >700 47.20, whole consumption at the slab rate. Sept 2026
bills add FCA +2.0581 and quarterly adjustment +0.5194 Rs/kWh. Typical 126 kWh = 51,675 GWh / 34,274,946
residential consumers (government figures in NEPRA's Feb 2026 decision); 59% of residential consumers are
protected, so the headline is a protected household: 100 x 10.54 + 26 x 13.01 = 1,392.26 + 300 fixed (1 kW,
assumed) + 126 x 2.5775 = 324.77, = 2,017.03, + 18% GST = 2,380.09, so 18.89. Unprotected 200 kWh / 2 kW
household: 40.70. Unverified: sanctioned load, that electricity duty and PTV fee are gone, whether the
Rs 3.23 debt-service surcharge is inside the rates. Uniform rates also apply to K-Electric.

## Western Asia

Gulf choice of tariff: AE, KW and QA use the expatriate tariff (expatriate households are the majority);
BH uses the citizens' tariff (62.6% of private households are Bahraini, census 2020); OM and SA have
nationality-independent tariffs.

**AE, 0.31 AED/kWh (medium).** Expatriate tariffs. Typical use 1,600 kWh/month = DEWA 2025 statistics
booklet: 19,252 GWh over 1,003,334 residential accounts (includes villas). Dubai (DEWA slab tariff, read via
archive): 23/28/32/38 fils in 2,000 kWh slabs + fuel surcharge 6 fils (Sept 2026, monthly) + meter charge 5
+ 5% VAT: (1,600 x 0.29 + 5) x 1.05 = 492.5 AED, so 0.308 (0.322 at 300 kWh). Abu Dhabi ADDC (2024 page,
read via archive): expat apartment 26.8 fils to 20 kWh/day, then 30.5, + 5% VAT, so 0.305. EtihadWE
(https://www.etihadwe.ae/en/About/Pages/Tariff.aspx): 23/28/32/38 fils + 5 fils surcharge + VAT, so 0.294.
All three within 0.29-0.31, so 0.31 is used without weighting. Nationals pay 6.7-7.5 fils in Abu Dhabi and
the northern emirates. Sharjah (SEWA) tariff not found. Housing/knowledge fees on DEWA bills excluded.

**AM, 48.48 AMD/kWh (medium).** PSRC decision 478-N (2021) as amended by 466-N of 30 Dec 2025; table
valid from 1 Feb 2026, VAT included, unchanged since Feb 2022 (https://psrc.am/content/el_energy_tariffs;
ENA https://www.ena.am/Info.aspx?id=11&lang=2): day/night <=200 kWh 46.48/36.48, 201-400 48.48/38.48,
>400 53.48/43.48; socially vulnerable 29.99/19.99. No fixed charge. 300 kWh at the day rate of its
category: 48.48. If tiers are marginal: (200 x 46.48 + 100 x 48.48)/300 = 47.15; with 1/3 night use 45.15.

**AZ, 0.0927 AZN/kWh (high).** Tariff Council decision 19 of 29 Dec 2024 (from 2 Jan 2025): 0-200 kWh
8.4 qəpik, 201-300 10.0, >300 15.0, incl. VAT, marginal; decision 9 of 30 Dec 2025 adds 1.00 AZN/month from
1 Jan 2026. 300 kWh: 200 x 8.4 + 100 x 10 = 2,680 qəpik = 26.80 + 1.00 = 27.80 AZN, so 0.0927. Nakhchivan
not checked.

**BH, 0.0040 BHD/kWh (medium).** EWA tariff page (updated 2 Aug 2026): Bahraini single account 3 fils to
3,000 kWh, 9 to 5,000, 16 to 7,000, 32 above; non-Bahraini and extra accounts 32 fils flat. BD 1 monthly
admin fee (EWA bill guide). Typical 3,400 kWh = EWA 2025 domestic sales 9,384 GWh / 228,972 private
households (census 2020; overstated as households have grown). 3,000 x 0.003 + 400 x 0.009 + 1 = 13.6 BD,
so 4.0 fils (6.3 fils at 300 kWh). Expatriate households pay ~32 fils + VAT, about 9x more. VAT treatment of
utility bills not confirmed (absorbed by government since 2020 per press; bill guide lists no VAT line).

**IL, 0.754 ILS/kWh (medium).** Electricity Authority tariff book July 2026 (read via archive): household
tariff 53.83 agorot/kWh before VAT (54.51 in Jan 2026) + capacity 6.18 ILS/kVA/year + consumer-service
charges 9.97 + 15.60 ILS for a single-phase meter (header says per month). 300 kWh: 161.49 + 4.74 (9.2 kVA)
+ 25.57 = 191.80 x 1.18 VAT = 226.32 ILS, so 0.754 (0.70 if the service charges are per two-month bill).
Eilat VAT 0%; ~10% of households use private suppliers 5-7% cheaper.

**IQ, 10 IQD/kWh (high).** Ministry of Electricity tariff and calculator (read via archive, July 2025;
ministry denied increases Dec 2025 and May 2026): residential 10 IQD/kWh up to 1,500 kWh/month, no fixed
charge or VAT found. Any normal consumption gives 10. Grid supply is rationed; most households also pay
neighbourhood generators (~20,000 IQD per amp per month) that are not in this figure. Unconfirmed
3,000 IQD/bill fee would add ~5 IQD/kWh at 300 kWh.

**JO, 0.045 JOD/kWh (high).** EMRC bill calculator (April 2022 structure): subsidised (Jordanian) household
50 fils 1-300 kWh, 100 fils 301-600, 200 fils above, minus 2 JOD support at 201-600 kWh; + meter rent 0.2
JOD + "rural fils" 1 fil/kWh; fuel clause 0; no VAT. 300 kWh (EMRC 2023: 8,856 GWh / 2.53M subscribers =
291 kWh): 15 - 2 + 0.2 + 0.3 = 13.5 JOD, so 0.045. Non-subsidised (non-Jordanians) 120 fils, 0.122 all-in.
TV fee (1 JOD) and municipal waste fee on the bill excluded as not electricity.

**KW, 0.005 KWD/kWh (medium).** Ministry of Electricity and Water 2017 tariff infographics
(mew.gov.kw/assets/images/Tariff/1-6.jpg): investment-sector (rented apartment) rate raised to 5 fils from
22 Aug 2017; private housing, and Kuwaitis in investment flats without another home, kept the old
subsidised rate (2 fils, value not confirmed). 62% of private households are non-Kuwaiti (register census
2021, table 113: 515,879 of 832,569). Flat, no VAT, no fixed charge found. In many flats electricity is
included in the rent.

**LB, 0.255 USD/kWh (medium).** EDL tariff (notice https://www.edl.gov.lb/news.php?nid=429; unchanged to
2030 in EDL's Dec 2025 plan): 10 US cents first 100 kWh, 27 cents above, + 0.25 USD per amp per month +
fixed monthly fee, + 11% VAT. 300 kWh, 20 A: 10 + 54 + 5 = 69 USD x 1.11 = 76.59, so 0.255 (0.233 at 200
kWh). About 22,850 LBP/kWh at 89,500. Stamp duty excluded. EDL supplies ~6-8 h/day; private generators
(MoEW guide Sep 2026: 52,840 LBP/kWh in cities, ~0.59 USD, plus a fixed per-amp fee) cover the rest, so
the real household average is higher than the grid price.

**OM, 0.0147 OMR/kWh (high).** APSR decision 44/2024 (from 1 Jan 2025), Nama Supply residential tariff PDF
(read via archive), still linked as the approved tariff in 2026: primary account (any customer, up to two
accounts per Civil/Resident ID) 14 baisa to 4,000 kWh, 18 to 6,000, 32 above; additional accounts 22/26/32;
citizens' national-subsidy rate 10/13/20. VAT 5% (electricity not exempt or zero-rated in the VAT Law).
14 x 1.05 = 14.7 baisa at any use to 4,000 kWh. May-Aug summer discount not applicable in October.

**PS, 0.669 ILS/kWh (medium).** PERC: cabinet decision of 5 Mar 2025 (https://perc.ps/perc/wp-content/uploads/2025/03/tariff25.pdf):
1-160 kWh 0.5103, 161-250 0.5500, 251-400 0.6344, 401-600 0.6782, >600 0.7498 ILS/kWh; daily minimum charge
0.34 ILS for credit meters; excl. 16% VAT. 300 kWh: 162.87 + 10.20 = 173.07 x 1.16 = 200.76, so 0.669.
Prepaid meters 0.63-0.64. West Bank excl. Jericho/Jordan Valley (slightly cheaper). Gaza has no functioning
grid tariff.

**QA, 0.11 QAR/kWh (high).** Kahramaa tariff web service behind
https://www.km.qa/CustomerService/Pages/Tariff.aspx, flat and villa categories: 0.11 QAR to 2,000 kWh,
0.13 to 4,000, 0.18 to 15,000, 0.26 above (supersedes the 2015 0.08/0.09/0.10 scheme). No VAT, no fixed
charge. Expatriate tariff; Qatari households can apply for exemption (free).

**SA, 0.245 SAR/kWh (medium).** SERA consumption tariff (read via archive, Feb 2025): residential 0.18 SAR
to 6,000 kWh, 0.30 above, same for citizens and expatriates; meter fee SAR 10 (up to 60 A breaker, ECRA
2018 tariff). 300 kWh (no sourced typical figure): 54 + 10 = 64 x 1.15 VAT = 73.6, so 0.245; 0.218 at 1,000
kWh. Citizens receive cash support through the Citizen Account, off-bill.

**SY, 8.0 SYP/kWh (medium).** Ministry of Energy decision 687 (30 Oct 2025) as reported by SANA
(https://sana.sy/locals/2553528/): two-month cycle, 6 new SYP/kWh for the first 300 kWh, 14 above (600 and
1,400 old pounds). 200 kWh/month = 400 per cycle: 300 x 6 + 100 x 14 = 3,200, so 8.0. Fixed fees and stamp
unknown; decision text not seen.

**YE, not priced (gap).** No PEC tariff for Aden or Sana'a found. The only verified price is Taiz's
local-authority cap for private diesel networks, 900 YER/kWh from May 2026 (hybrid 560-750, solar 300-400),
disputed by operators (https://www.yemenmonitor.com/Details/ArtMID/908/ArticleID/171088). Not national.

## Currency

- **LB: USD.** EDL's tariff is set in US dollars and bills show the LBP equivalent at the Banque du Liban
  rate (89,500 LBP/USD); payable in either. Source: EDL notice https://www.edl.gov.lb/news.php?nid=429.
  Generator prices are set in LBP.
- **SY: SYP (new pound).** The new Syrian pound (1 new = 100 old) came in on 1 Jan 2026 (Decree 293/2025);
  old notes stopped being exchanged on 30 Jul 2026 (Wikipedia "Syrian pound"). SANA quotes tariffs in new
  pounds. Whether ISO 4217 assigned a new code is unverified; SYP is used.
- **IR: IRR.** Bills are in rials; prices are commonly quoted in toman (1 toman = 10 IRR). Multiple exchange
  rates exist. A law to drop four zeros has reportedly passed, unverified.
- **PS: ILS.** PERC tariffs are stated in shekels (tariff PDF above).
- **YE: YER, two separate note series.** New rial in government areas (Aden, Taiz, ~1,560-1,630/USD); old
  rial in Houthi areas (Sana'a, ~530/USD). Source: Sana'a Center Yemen Review, Oct-Dec 2025 and Apr-Jun 2026.
- **IQ: IQD; AF: AFN** (USD circulates, but DABS bills in AFN). **BT: BTN** (pegged 1:1 to INR).
  **MV: MVR** (USD-pegged; residential bills in MVR).
- BHD, KWD, OMR, JOD are divided into 1,000 fils/baisa, so 0.005 KWD is 5 fils.

## Zone candidates

- **IQ, strong:** Kurdistan Region (Erbil, Sulaymaniyah, Duhok, Halabja; ~6.4M people) pays 72 IQD/kWh for
  1-400 kWh (Runaki, from 14 May 2025), against 10 IQD in federal Iraq, about 7x.
- **IR, summer only:** tropical zones (Khuzestan, Hormozgan, Bushehr, Sistan-Baluchestan) have hot-month
  patterns up to 3,000 kWh against 300 in Tehran. At 600 kWh in summer a Tehran household pays well over 2x
  per kWh. At typical use outside summer the rates are similar.
- **IN:** state spread is far above 2x (after subsidy 0 in seven states to 8.11 in Maharashtra at 100 kWh;
  before subsidy 1.80 to 8.80), but India is not zoned: the file carries one national figure.
- **YE:** government and Houthi areas would qualify, but only one side has a price.
- **SY:** north-east (AANES) and north-west have separate operators; not quantified.
- Not regional, but 2x+ differences by nationality or household type, worth a note: BH citizens ~4 fils vs
  expats ~36 fils (9x); QA free for Qataris vs 0.11 QAR; KW 2 vs 5 fils; AE nationals 6.7-7.5 fils vs 23-30.5;
  JO subsidised 0.045 vs non-Jordanian 0.122 JOD; PK protected 18.89 vs unprotected 40.70 PKR.

## Gaps

- **YE:** no national or PEC tariff found; only a disputed Taiz private-network price. Not priced.
- **IR:** no official 1405 rial schedule reachable; figure is an estimate from news reports (low).
- **MV:** whether households pay the fuel surcharge, and GST (low).
- Smaller open points: SEWA (Sharjah) tariff; Bahrain VAT treatment; Kuwait 2 fils rate unconfirmed;
  Israel service-charge period; Lebanon stamp duty; Syria fixed fees; Iraq per-bill fee; Pakistan and
  Bangladesh sanctioned load; Nepal current-rate date; Bhutan and Saudi typical consumption (defaults used);
  Armenia tier mechanics; Afghanistan provinces; India FY2026-27 orders and fuel surcharges.
