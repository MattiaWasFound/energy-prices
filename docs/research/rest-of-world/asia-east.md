# asia-east: household electricity price per kWh (researched 2026-10-04)

Group: Central Asia (KG KZ TJ TM UZ), Eastern Asia (CN HK JP KP KR MN MO TW), South-eastern Asia (BN ID KH LA MM MY PH SG TH TL VN).
Figures are all-in per kWh at the stated monthly consumption, in the billing currency. Rows and sources: `asia-east.csv`.
Limitation: several items were confirmed only by direct fetches or the Wayback Machine (tepco.co.jp and clp.com.hk are Akamai-blocked). Those items are marked lower confidence.

## Central Asia

### KG Kyrgyzstan: 1.64 KGS/kWh (300 kWh/month, medium)
Order No.103 of 2026-04-24, valid from 1 May 2026: 1.64 som/kWh up to 700 kWh/month, 2.94 above (was 1.37 / 2.60). 300 kWh is all in block 1: 300 x 1.64 = 492 som. No fixed charge on NESK's tariff page. economist.kg says approved rates are "listed without taxes"; if 12% VAT plus ~2% sales tax were added on the bill the figure would be ~1.87. Not settled. Low-income families pay 0.50 up to 700 kWh. Planned yearly May increases to ~3.4 som by 2030.
Sources: https://nesk.kg/ru/abonentam/tarif/ , https://www.tazabek.kg/news:2460545 , https://bulak.kg/2026/05/02/v-kyrgyzstane-s-1-maya-vstupili-v-silu-novye-tarify-na-elektroenergiyu , https://economist.kg/enierghietika/2026/03/28/skolko-budiet-stoit-eliektrichiestvo-v-kyrghyzstanie-s-1-maia-2026-ghoda-tarify/

### KZ Kazakhstan: 33.0 KZT/kWh (300 kWh/month, medium)
Prices are set per regional supplier; flat per-kWh, 16% VAT (from 2026-01-01) included, no standing charge. Astana-REK household average 28.12 KZT with VAT (valid 2026-07-01 to 2027-06-30); Almaty Alatau Zharyk standard household rate 37.92 with VAT from 2026-09-12 (optional three-tier 34.28 / 45.51 / 56.89). 33.0 is the midpoint of the two largest cities, a "national-ish" figure, not a weighted average.
Sources: https://www.esalmaty.kz/ru/home-tariffs , https://vlast.kz/novosti/70802-v-almaty-i-almatinskoj-oblasti-s-12-sentabra-povysatsa-tarify-na-elektroenergiu.html , https://kz.kursiv.media/2026-08-27/kaye-zhitelyam-astany-otvetili-podorozhaet-li-elektroenergiya-do-koncza-goda/ , https://zhkh24.kz/ru/articles/skolko-stoit-svet-v-raznyh-regionah-kazahstana-tarify-dlya-naseleniya-v-2026-godu

### TJ Tajikistan: 0.4137 TJS/kWh (300 kWh/month, medium)
Single household rate 41.37 diram/kWh from 2026-02-01 (government decree approved 2025-12-29; was 35.36 from April 2025). Flat: 300 x 0.4137 = 124.11 TJS. Industrial rate above 10,000 kWh/month. No fixed charge found; VAT inclusion not stated (decree tariffs are normally the billed price). Decree text not fetched; figures from news citing it.
Sources: https://interfax.com/newsroom/top-stories/115538/ , https://asiaplus.news/en/2025/12/29/electricity-and-heating-rates-to-change-in-tajikistan-likely-to-increase/

### TM Turkmenistan: 0.025 TMT/kWh (300 kWh/month, low)
Decree of 2017-10-10 (effective 2017-11-01): 2.50 manat per 100 kWh including VAT, for use above the then-free allowance; free allowances were abolished in 2019, so all household use is presumably billed at this rate. 300 x 0.025 = 7.50 TMT. No later revision found, none ruled out.
Source: https://turkmenistan.gov.tm/en/post/9220/new-charges-for-gas-electricity-housing-and-communal-transport-and-communications-services

### UZ Uzbekistan: 733.33 UZS/kWh (300 kWh/month, high)
Cabinet resolution PKM-243 of 2026-05-15, effective 2026-06-01: up to 200 kWh 650 sum, 201-500 900, 501-1,000 1,100, 1,001-5,000 1,600, 5,001-10,000 1,900, above 2,200 (half rates for apartment blocks with electric cooking). 200 x 650 + 100 x 900 = 220,000 / 300 = 733.33. No fixed charge. VAT believed included in residential tariffs, not stated explicitly. Previous (May 2025): 600 / 800 / 1,000.
Sources: https://www.spot.uz/ru/2026/05/15/energy-tariffs-up/ , https://asiaplus.news/en/2026/05/19/uzbekistan-to-raise-electricity-and-gas-rates/ , https://www.gazeta.uz/ru/2025/04/30/tariffs/

## Eastern Asia

### JP Japan: 36.8 JPY/kWh (260 kWh/month, medium)
TEPCO EP "平均モデル" (従量電灯B 30A, 260 kWh/month, incl. basic charge, fuel-cost adjustment, renewable levy and 10% consumption tax): JPY 9,561 for October 2026 usage (November bill), the first month after the national 電気・ガス料金支援 subsidy (3.50 JPY/kWh in the August-September 2026 bills) ended. 9,561 / 260 = 36.77 JPY/kWh.
Across the ten regional utilities the standard-household bill for October 2026 usage ranges from JPY 7,970 (Hokuriku, lowest) to JPY 10,752 (Okinawa, highest); a ~1.5x gap does not meet the zone rule. TEPCO serves the Kanto area (~1/3 of Japanese households) and sits in the middle of the range, so it stands in for the national typical household. Hokuriku/Hokkaido/Kyushu models historically assume 230-250 kWh, so per-kWh the range is roughly 34-41 JPY.
Caveat: TEPCO's own page (tepco.co.jp/ep/private/fuelcost2/new/) was Akamai-blocked; the 9,561 figure is from the 29 Sep 2026 ten-utility announcement as reported by Kyodo/8and; the model definition (従量電灯B 30A, 260 kWh, tax and levy included) was read from the archived TEPCO page.

Sources: https://www.tepco.co.jp/ep/private/fuelcost2/new/index-j.html (model definition, read via Wayback) , https://8and.jp/2026/10/01/10%E6%9C%88%E3%81%AE%E9%9B%BB%E6%B0%97%E4%BB%A3%E3%81%8C%E5%A4%A7%E6%89%8B10%E7%A4%BE%E3%81%9D%E3%82%8D%E3%81%A3%E3%81%A6%E9%81%8E%E5%8E%BB%E6%9C%80%E9%AB%98%E3%81%AB%E3%80%80%E6%9D%B1%E4%BA%AC/ (TEPCO JPY 9,561) , https://tokyonewsmedia.com/archives/28563 (range 7,970-10,752)

### KR South Korea: 192.5 KRW/kWh (300 kWh/month, low-voltage residential, non-summer, medium)
KEPCO 주택용 저압 (Oct-Jun tiers): base charge 1,600 (201-400 kWh band); energy 200 x 120.0 = 24,000 + 100 x 214.6 = 21,460; 기후환경요금 9 x 300 = 2,700; 연료비조정 +5 x 300 = 1,500 (kept at +5 for Q4 2026). Subtotal 51,260. VAT 10% = 5,126; 전력산업기반기금 2.7% (since Jul 2025) = 1,380. Total ~57,760 KRW -> 192.5 KRW/kWh.
300 kWh is the method's default (KEPCO's 4-person reference is ~307 kWh in shoulder months; sources quote 270-350 kWh by season). Apartments on 주택용 고압 pay less (105.0/174.0/242.3 KRW/kWh, base 730/1,260/6,060), about 165 KRW/kWh at the same use. Summer (Jul-Aug) tiers widen to 300/450 kWh. TV licence fee (2,500 KRW) collected on the bill is excluded. Climate rate (9 KRW) not re-verified for 2026 beyond secondary sources.

Sources: https://cyber.kepco.co.kr/ckepco/front/jsp/CY/E/E/CYEEHP00101.jsp (KEPCO tariff table) , https://www.dailian.co.kr/news/view/1692747/4%EB%B6%84%EA%B8%B0-%EC%A0%84%EA%B8%B0%EC%9A%94%EA%B8%88-%EB%8F%99%EA%B2%B0%EC%97%B0%EB%A3%8C%EB%B9%84-%EC%A1%B0%EC%A0%95%EB%8B%A8%EA%B0%80-2026 (Q4 2026 freeze, +5 KRW) , https://www.electimes.com/news/articleView.html?idxno=334694 (fund 3.7% -> 2.7%)

### CN China: 0.55 CNY/kWh (300 kWh/month, low)
No national tariff: each province sets three-tier residential prices (tariffs are VAT-inclusive, no fixed charge). Verified examples: Beijing (fgw.beijing.gov.cn via english.beijing.gov.cn) tier 1 <=240 kWh 0.4883, tier 2 241-400 0.5383, tier 3 >400 0.7883 -> at 300 kWh: 240 x 0.4883 + 60 x 0.5383 = 149.49 CNY = 0.498 CNY/kWh. Shanghai tier 1 (0-3,120 kWh/year) 0.617, tier 2 ~0.667-0.677, tier 3 ~0.917-0.977 -> ~0.62 at 300 kWh.
The national figure 0.55 is a judgement inside the band of populous provinces' tier-1/tier-2 rates (most 0.48-0.62); it is not from an official national average I could fetch this round. Treat as low confidence until an NEA/CEC residential average is pulled.

Sources: https://english.beijing.gov.cn/livinginbeijing/housing/202005/t20200513_1895841.html (Beijing DRC tiers) , https://localshanghai.com/shanghai-utility-bills-electricity-water-gas-foreigner/ (Shanghai tiers, secondary)

### HK Hong Kong: 1.43 HKD/kWh (275 kWh/month, CLP, medium-high)
CLP residential tariff from 1 Jan 2026 (bimonthly blocks): 275 kWh/month = 550 kWh per bimonthly bill. Energy charge 400 x 94.5 + 150 x 107.9 = 53,985 cents; fuel cost adjustment 45.0 c/kWh (from 1 Aug 2026, latest published; annual forecast 39.4) x 550 = 24,750 cents; no energy-saving rebate (>400 units). Total HK$787.35 / 550 = 1.432 HKD/kWh. No VAT/sales tax in HK.
275 kWh/month is the government's "typical three-member household" (info.gov.hk 18 Nov 2025). HK Electric (Hong Kong Island and Lamma, ~590k customers vs CLP ~2.8M) gives HK$352.1 for 275 kWh in Jan 2026 = 1.280 HKD/kWh. A special fuel rebate of 8 c/kWh for eligible residential customers ran Aug-Oct 2026 (eligibility not confirmed, not applied). Monthly FCA changes move the figure by a few cents.

Sources: CLP tariff table (Wayback copy fetched, original Akamai-blocked) https://www.clp.com.hk/content/dam/clphk/documents/tariff-adjustment-2026/Tariff%20Table%20-%20English_Update.pdf , CLP FCA page https://www.clp.com.hk/en/help-support/bills-payment-tariffs/fuel-cost-adjustment , https://www.info.gov.hk/gia/general/202511/18/P2025111800787.htm , HK Electric https://www.hkelectric.com/documents/en/MediaResources/PressReleases/Documents/20251118_pre_TR%202026_final_website.pdf

### KP North Korea: gap
No published household tariff, regulator or statistics office; household electricity is state-allocated, rationed and intermittent; any charge is nominal in KPW at a meaningless official rate. No openly licensed dataset covers it.

### MO Macao: 1.41 MOP/kWh (250 kWh/month, high)
CEM tariff A1 (Executive Decree 105/2022), CEM's own worked example: demand charge 6.9 kVA 18.80 + 250 x 0.963 = 240.75 + tariff clause adjustment 250 x 0.36 (Q3 2026, from 22 Jul 2026) = 90.00 + government tax 0.75 x sqrt(6.9) = 2.00 -> MOP 351.55 / 250 = 1.406 MOP/kWh. Q4 2026 TCA is set around 22 Oct 2026. Households with <=120 kWh/month for six months get tariff A2 (0.858, no demand charge).

Sources: https://www.cem-macau.com/en/customer-service/billing-service/tariff-group-a , https://www.cem-macau.com/en/customer-service/billing-service/tariff-clause-adjustment

### MN Mongolia: 248.95 MNT/kWh (220 kWh/month, high)
ERC central/southern grid table (covers Ulaanbaatar; in the regulator's 2026 upload folder), standard meter: up to 150 kWh 184 MNT, 150-300 269, above 300 299, plus monthly base charge 3,360 MNT; rates exclude 10% VAT and include a 13.48 MNT/kWh renewables levy. 220 kWh/month is the ERC's published average household use. (150 x 184 + 70 x 269 + 3,360) x 1.10 = 54,769 MNT / 220 = 248.95. The same method on the Nov 2024 tariff reproduces ERC's published 52,107 MNT example bill exactly. Exact 2026 effective month not found (as_of set to 2026-01).
Sources: https://erc.gov.mn/mn/tariff-center , https://admin.erc.gov.mn/uploads/files/2026/tarif/tuv2.jpg , https://erc.gov.mn/en/news/1033 , https://montsame.mn/en/read/356054

### TW Taiwan: 2.28 TWD/kWh (345 kWh/month annual average, medium)
Taipower residential (non-TOU) progressive tariff, tax-inclusive (5% business tax in the rate), no fixed charge. Taipower (1 Jun 2026): 2025 average household use 308 kWh/month non-summer, 418 kWh summer, ~345 kWh annual. Focus Taiwan (11 May 2026, from Taipower): average bill NT$638/month non-summer, NT$1,084/month summer.
Annual: (8 x 638 + 4 x 1,084) / (8 x 308 + 4 x 418) = 9,440 / 4,136 = 2.28 TWD/kWh. Non-summer alone 638/308 = 2.07; summer 1,084/418 = 2.59. Summer tiers: <=120 kWh 1.78, 121-330 2.55, 331-500 3.80, 501-700 5.14, 701-1000 6.44, >1000 8.86 (bimonthly billing doubles the bands). Non-summer tier-2 rate (~2.26) is inferred from the NT$638 average, not read from the schedule.

Sources: https://www.taipower.com.tw/2764/2804/2805/69043/normalPost (Taipower, 1 Jun 2026) , https://focustaiwan.tw/business/202605110005

## South-eastern Asia

### BN Brunei: 0.038 BND/kWh (1,000 kWh/month, low)
DES residential tariff (since 2012-01, still published): 1-600 kWh B$0.01, 601-2,000 B$0.08, 2,001-4,000 B$0.10, above B$0.12; no GST, no standing charge. 600 x 0.01 + 400 x 0.08 = B$38 / 1,000 = 0.038. The tariff is certain; 1,000 kWh/month is an unsourced estimate of typical (high, air-conditioned) Brunei use, and the result is very sensitive to it: 0.010 at <=600 kWh, 0.052 at 1,500, 0.059 at 2,000.
Source: https://www.des.gov.bn/electricity-tariff/

### ID Indonesia: 1,517 IDR/kWh (200 kWh/month, medium)
PLN R-1 1,300-2,200 VA non-subsidised: Rp1,444.70/kWh flat; no VAT for households up to 6,600 VA; postpaid has no standing charge (40-hour minimum = 52 kWh at 1,300 VA, not binding). PPJ (street-lighting tax) set by each regency, max 10% (Law 1/2022): 1,444.70 x 1.05 = 1,517 with an assumed 5% (range 1,479 at 2.4% to 1,589 at 10%; the 5% is a midpoint, not a sourced rate). Q4 2026 tariffs not announced by 1 Oct, Q3 rates carry over. Other classes: 450 VA subsidised 415, 900 VA subsidised 605, 900 VA non-subsidised 1,352, >=3,500 VA 1,699.53.
Sources: https://money.kompas.com/read/2026/10/01/134318126/tarif-listrik-per-kwh-oktober-2026-cek-daftar-harga-semua-golongan , https://finance.detik.com/energi/d-8687317/daftar-tarif-listrik-yang-berlaku-per-1-oktober-2026

### KH Cambodia: 610 KHR/kWh (200 kWh/month, medium)
EAC Decision 032/2026 (approved 2026-01-29) for EDC, residential: 1-10 kWh 380, 11-50 480, 51-200 610, above 200 730 riel/kWh. The Khmer wording ("users who use 51 to 200 kWh per month") reads as one rate for the whole bill: 200 kWh -> 610. If stepped: 114,500 riel = 572.5. No residential fixed charge found; VAT treatment not verified. Decision 034/2026 applies the same residential rates to licensed private distributors on the national grid.
Source: https://eac.gov.kh/uploads/tariff_decides/2026/032_សរ_26_Decision_on_consumer_tariff_for_EDC_2026_17_province_20260205074557.pdf

### LA Laos: ~1,100 LAK/kWh (200 kWh/month, low)
EDL raises tariffs monthly under a 2025-2029 roadmap: August 2026 0-25 kWh tier LAK 807, >1,500 kWh tier 1,946 (Dec 2026 targets 850 / 2,086); household prices +91.5% y/y in July 2026. Nov 2025 subsidy cut the transmission fee for <=300 kWh households from 260 to 109 kip/kWh; from the Sep 2026 bill, use up to 300 kWh is exempt from 10% VAT (VAT still on the maintenance fee). The middle tiers (26-150, 151-300 kWh) were not found, so 1,100 is a bracketed estimate (~1,000-1,200), not a computed bill. Needs the EDL tariff notice.
Sources: https://laotiantimes.com/2026/09/11/laos-exempts-residential-electricity-use-up-to-300-kwh-from-vat/ , https://laotiantimes.com/2026/08/10/laos-considers-vat-exemption-to-subsidize-electricity-for-low-income-households/ , https://laotiantimes.com/2025/11/19/lao-government-rolls-out-usd-10-million-electricity-subsidy/

### MM Myanmar: 112.5 MMK/kWh (200 kWh/month, low)
MOEP household tariff from 2024-09-01 (cabinet approval 5 Jul 2024), unchanged as of Feb 2026: 1-50 kWh 50, 51-100 100, 101-200 150, above 200 300 kyat. Stepped: 2,500 + 5,000 + 15,000 = 22,500 / 200 = 112.5 (150 if whole-bill). Meter/service fee and any tax unknown. Sources are news, not a ministry document. Load-shedding until a 500 MW LNG plant came online in Jan 2026; grid access far from universal.
Sources: https://elevenmyanmar.com/news/moep-announces-electricity-rate-increase-effective-sept-1 , https://elevenmyanmar.com/news/power-rationing-ends-as-supply-rises-household-tariffs-unchanged

### MY Malaysia: 0.2193 MYR/kWh (300 kWh/month, Peninsular TNB, high)
TNB domestic tariff (structure from July 2025): energy 27.03 + capacity 4.55 + network 12.85 = 44.43 sen x 300 = RM133.29; energy efficiency incentive (251-300 kWh band) -22.5 sen x 300 = -RM67.50 -> RM65.79 / 300 = 0.2193. At 300 kWh nothing else applies: KWTBB 1.6% only above 300 kWh; AFA (+3.61 sen Oct 2026), RM10 retail charge and 8% SST only above 600 kWh (raised to 800 kWh Sep-Dec 2026). At 600 kWh: 266.58 - 54.00 + KWTBB 3.40 = RM215.98 = 0.360 MYR/kWh. 300 kWh is the method's default (no official typical figure found); the steep incentive makes the result sensitive to it.
Sources: https://www.mytnb.com.my/tariff/index.html (rates.js, calculator-newDomestic.js) , https://www.st.gov.my/jadual-elektrik-baharu-lebih-236-juta-pengguna-domestik-semenanjung-nikmati-kadar-lebih-adil , https://misif.org.my/wp-content/uploads/2025/06/202507-Elec-Tariff.pdf , https://paultan.org/2026/10/01/tnb-bill-afa-rate-october-2026-set-at-3-61-sen-kwh/

### PH Philippines: 14.7424 PHP/kWh (200 kWh/month, high)
Meralco overall rate for a typical 200 kWh household, September 2026 (advisory 2026-09-11), ~PHP 2,948/month. All-in: generation, transmission, system loss, distribution, supply and metering, universal charges, FIT-All, VAT, local taxes, lifeline subsidy; residential refunds (1.0139/kWh) applied. October 2026 advisory not yet published. (October 2025: 13.3182.)
Sources: https://company.meralco.com.ph/news-and-advisories/lower-rates-september-2026 , https://company.meralco.com.ph/news-and-advisories/higher-rates-october

### SG Singapore: 0.3116 SGD/kWh (flat, high)
SP Group regulated household tariff 1 Oct-31 Dec 2026: 28.59 cents/kWh before 9% GST (energy 22.18 + network 6.10 + market/other), 31.16 cents with GST. Flat per-kWh tariff, no standing charge, so consumption does not matter. U-Save rebates (HDB households only, quarterly credits) not applied; open-electricity-market retailers sell below the regulated tariff for ~half of households.
Sources: https://www.spgroup.com.sg/about-us/media-resources/news-and-media-releases/Electricity-Tariff-Revision-for-the-Period-1-July-to-30-September-2027 (title: "Electricity Tariff Revision for the Period 1 October to 31 December 2026", dated 30 Sep 2026; the URL slug is SP Group's) , https://www.ema.gov.sg/consumer-information/electricity/buying-electricity/buying-at-regulated-tariff

### TH Thailand: 3.8846 THB/kWh (300 kWh/month, high)
New household structure from the September 2026 bills (PEA and MEA): Type 1.1.2 (>150 kWh): 0-200 kWh 3.0000, 201-400 4.1584, >400 4.3583; service charge 24.62 THB/month; Ft 16.23 satang/kWh for Sep-Dec 2026 (ERC, 23 Jul 2026); VAT 7%. 200 x 3.0000 + 100 x 4.1584 = 1,015.84 + Ft 48.69 + 24.62 = 1,089.15 x 1.07 = 1,165.39 THB / 300 = 3.8846 (3.5154 at 200 kWh). Uniform national tariff.
Sources: https://www.pea.co.th/sites/default/files/users/user34/attachments/Electricity_Tariff_SEP_2026_3.pdf , https://www.erc.or.th/web-upload/200xf869baf82be74c18cc110e974eea8d5c/202607/m_news/9090/3458/file_download/4381ae6dc8f34f40cbf163099dd2f8c4.pdf , https://www.thansettakij.com/social-biz/668978

### TL Timor-Leste: 0.113 USD/kWh (200 kWh/month, low)
EDTL tariff per Ministerial Diploma 1/2017 (as reported by ADB): first 20 kWh $0.05, above $0.12; no VAT; no fixed charge found for prepaid meters. 20 x 0.05 + 180 x 0.12 = $22.60 / 200 = 0.113 (0.12 if prepaid households pay a flat rate). EDTL cost ~$0.42/kWh, so all households are subsidised. Not confirmed unchanged since 2017; EDTL/regulator sites unreachable.
Source: https://www.adb.org/sites/default/files/linked-documents/49177-002-ssa.pdf

### VN Vietnam: 2,662 VND/kWh (300 kWh/month, medium)
EVN residential 6-tier tariff, Decision 1279/QD-BCT (effective 2025-05-10), still billed per 2026 secondary sources: 0-50 1,984; 51-100 2,050; 101-200 2,380; 201-300 2,998; 301-400 3,350; >400 3,460 (before VAT). 50 x 1,984 + 50 x 2,050 + 100 x 2,380 + 100 x 2,998 = 739,500 x 1.08 (VAT, temporarily 8%, reportedly to 31 Dec 2026) = 798,660 / 300 = 2,662 (2,374 at 200 kWh). Decision 14/2025/QD-TTg sets a 5-tier frame; under it 300 kWh would be 2,650, <1% different. A 2026 adjustment could not be ruled out.
Sources: https://www.cskh.evnspc.vn/TraCuu/ThongTinGiaDien , https://datsolar.com/gia-dien-dan-dung/

## Currency
- TL Timor-Leste: USD (dollarised; EDTL bills in US dollars; centavo coins are local but the unit of account is USD). Source: ADB document above.
- MO Macao: MOP (CEM bills in patacas; HKD circulates widely but is not the billing currency). Source: CEM tariff page.
- HK Hong Kong: HKD.
- KH Cambodia: KHR (EAC tariffs are in riel although USD is widely used day to day). Source: EAC Decision 032/2026.
- TM Turkmenistan: TMT; official rate pegged at 3.50 TMT/USD since 2015, street rate roughly 10x weaker, so any USD conversion depends on the convention chosen.
- MM Myanmar: MMK; the central bank reference rate (~2,100 MMK/USD) is well below the market rate (believed roughly double; not verified).
- KP North Korea: KPW, official rate meaningless; no price anyway.
- BN Brunei: BND (at par with SGD by currency agreement).

## Zone candidates
- KZ Kazakhstan: yes, close to 2x. Tier-2 household rates with VAT (zhkh24.kz, Aug 2026): North Kazakhstan 23.86, Mangystau 23.98, Abai/East 24.29, Shymkent 29.88, Astana 33.74, Akmola 39.13, Kostanai 41.99, Almaty city+region 42.42 (before the September rise; Almaty standard rate now 37.92, tiered up to 45-57). Max/min 1.78 in August, ~1.9 after Almaty's increase. Regions are well recognised (oblasts + 3 cities). Possible split: South/Almaty + Kostanai/Akmola (~38-45) vs North/West/East (~24-28).
- CN China: borderline, probably below 2x for well-populated provinces. Verified: Beijing tier 1 0.4883 (0.498 at 300 kWh), Shanghai tier 1 0.617. From memory only, unverified: lowest tier-1 rates ~0.38-0.39 (Qinghai, Xinjiang), highest ~0.62-0.68 (Shanghai, Shenzhen). Max/min ~1.6-1.8x, and the cheapest provinces are thinly populated. Provinces are well recognised; worth a dedicated pass with each provincial DRC table if zones are considered.
- MM Myanmar: the national grid tariff is uniform, but off-grid private suppliers charge 2,700-3,600 kyat/kWh (Ye township, https://elevenmyanmar.com/news/electricity-tariff-in-ye-township-raised-to-3600-kyats-per-unit-starting-april-1), >20x the grid rate. It is a grid/off-grid split, not a list of regions, so probably not a zone in the method's sense.
- Not candidates (checked): JP (~1.5x across 10 utilities, below the zone rule); MY (Peninsular 21.9 / Sabah 23.0 / Sarawak 25.0 sen at 300 kWh); PH (utilities ~11.2-15.0 PHP/kWh, ~1.34x; from a comparison site, low confidence); MN (other grids <=14% lower); HK (CLP 1.43 vs HK Electric 1.28); ID (national tariff, PPJ <=10%); TH, VN, KH, UZ, KG, TJ, TW, KR (national tariffs).

## Gaps
- KP North Korea: no published household tariff or dataset (see above). Not priced.
- LA Laos: priced only as a low-confidence bracket; EDL's middle tiers (26-300 kWh) not found (EDL site is a JS app with no reachable tariff page).
- Partial, flagged low/medium: TM (2017 decree, no later confirmation), TL (2017 tariff), BN (typical consumption unknown), MM (stepped vs whole-bill, meter fee), CN (no official national average), ID (PPJ rate assumed), KG/TJ/KH (VAT treatment), JP (10-utility national average not assembled; TEPCO model used).
