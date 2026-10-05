# Russia: household electricity tariffs by federal subject, researched 2026-10-04

Purpose: one regulated household tariff per ISO 3166-2:RU subject, plus population weights, for a household
electricity price estimator. Output: 83 rows, now in `config/zones.csv` and `config/static_prices.csv`. Raw pulls and the
build script are not kept here.

## 0. The 2026 indexation was on 1 October, not 1 July

Russia moved the annual household tariff change from 1 July to **1 October 2026**. FAS said this gives regions
time to adopt every regulated tariff decision. There were two steps in 2026:

| Date | Change | Source |
|---|---|---|
| 2026-01-01 | **+1.7%** in every region. This passed through the VAT rise from 20% to 22% (Federal Law 425-FZ of 28.11.2025; Government order 3413-r of 25.11.2025). | https://www.bigpowernews.ru/news/document122770.phtml |
| 2026-10-01 | **+11.3%** on average for households (the Ministry of Economic Development forecast). Most regional base tariffs rose 11.1-11.3%. Some rose more: Krasnoyarsk +15.5%, Irkutsk +16.7%, Khakassia +11.2%. | https://www.eprussia.ru/news/base/2025/1978969.htm , https://www.sravni.ru/novost/2026/9/5/tarify-zhkh-povysyat-s-1-oktyabrya-razmer-indeksaczii-po-regionam/ |
| 2027, 2028 | The forecast is +8.6% and +9.1%, also from 1 October. | eprussia (above) |

So `valid_from` is **2026-10-01**. The current regional tariffs mostly run 01.10.2026-31.12.2026. They will be
superseded by the 2027 decisions, expected from 1 October 2027. FAS has already published the 2027 caps
(https://realtagil.ru/zhkh/fas-utverdila-predelnye-tarify-na-elektroenergiyu-dlya-naseleniya-na-2027-god/,
not read).

## 1. Sources used

### A. Backbone: FAS order No. 1130/25 of 19.12.2025 (the only official table covering every region)
"О предельных минимальных и максимальных уровнях тарифов на электрическую энергию (мощность), поставляемую
населению и приравненным к нему категориям потребителей, по субъектам Российской Федерации на 2026 год".
- Registered with the Ministry of Justice on 29.01.2026 (No. 85120), in force from 30.01.2026. It replaced order
  790/25 of 10.10.2025, which was recalculated for the 22% VAT.
- Text: https://www.garant.ru/products/ipo/prime/doc/413442354/.
  Mirror: https://normativ.kontur.ru/document?moduleId=1&documentId=504219 . The official publication portal
  (publication.pravo.gov.ru) API timed out.
- Content: min and max levels in kopecks/kWh **including VAT**, for 01.01-30.09.2026 and 01.10-31.12.2026.
  - **Table 1** has five regions with a **social consumption norm**, giving within-norm and above-norm levels:
    Zabaykalsky, Krasnoyarsk, Vladimir, Nizhny Novgorod and Oryol.
  - **Table 2** has one level per region for the other 85 rows. These include the occupied Ukrainian territories
    and Baikonur.
- For most regions min and max differ by 1 kopeck, so the cap is in effect the tariff.
- **Licence:** an official act of a federal executive body is not a copyright object under Civil Code RF
  art. 1259(6), so the numbers are free to reuse. garant.ru's own site terms restrict copying of its materials
  (its editorial wrapper, not the act).
- The FAS level corresponds to the **base tariff**: urban, no electric stove, no 0.7 reducing coefficient, first
  consumption range. Checked in section 3.

### B. Actual regional decisions (the tariffs people pay)
These are set by each region's tariff body (РЭК, комитет or служба по тарифам). There is no consolidated
machine-readable feed. The regional bodies' sites often block non-Russian IPs; kamgov.ru, for example, returns a
geo-block page. So the 2026-10-01 figures were checked one region at a time, through the regional body or
guaranteeing supplier where reachable, otherwise through regional media quoting the order. Each CSV row names
the URL it rests on.

### C. Rosstat cross-check, machine-readable
**Средние потребительские цены**, August 2026:
https://rosstat.gov.ru/storage/mediabank/sred_potreb_cen_08-2026.xlsx . The relevant items:
- 9471 "Электроэнергия в квартирах без электроплит за минимальный объем потребления, за 100 кВт·ч"
- 9472 the above-minimum-volume price
- 9473 and 9474 the with-electric-stove prices
- 9475 "Услуги по снабжению электроэнергией", an all-category average

The August 2026 value of item 9471 **equals the FAS Jan-Sep max (±1 kop) in 70+ of the 83 regions**. So regions
price at the cap, and the Oct-Dec cap is a sound proxy where the Oct figure could not be read directly.

Exceptions in the Rosstat file:
- Krasnoyarsk and Irkutsk are above the cap (see below).
- Zabaykalsky is below it (4.48 vs 4.72).
- For Primorye, Buryatia, Kamchatka, Magadan and Chukotka, Rosstat suppresses the no-stove figure ("...") or shows
  the electric-stove rate.

Rosstat site terms: public official statistics. Reuse with attribution is customary; no formal open licence was
found. The rosstat.gov.ru TLS chain uses the Russian Mintsifry CA, which macOS does not trust, so curl needed `-k`.

## 2. Which tariff is in the CSV (tariff_type)

- **Single-rate** (одноставочный, круглосуточный), not day/night zones.
- **Urban population, houses not equipped with electric stoves** (in practice gas-stove flats). Urban
  electric-stove/electric-heating homes and rural population get a reducing coefficient of 0.7-0.9 and are
  excluded.
- **First consumption range** where a region has volume ranges. Since 2025 most regions have three ranges. The
  first range is up to 3,900 kWh/month in many regions, but some set it lower: 1,000-1,600 kWh for flats in Perm,
  Komi, Arkhangelsk, Lipetsk and Volgograd, and 2,000 for Irkutsk flats. The upper ranges (often 1.5-2x the first)
  apply only to very high consumption, such as mining or electric-heated houses. A normal household is always in
  range 1.
- **Social-norm regions** (the 5 in FAS Table 1): the CSV carries the **above-norm** tariff.
  This is the marginal price of a kWh for a typical household, because norms are small. Examples: 50 kWh/person/month
  in Nizhny Novgorod, 65 in Zabaykalsky, 110 for one person or 75 per person in Krasnoyarsk. The within-norm
  tariff is noted below. Caveat: for a whole-bill average in these regions, blend the two. For example, a household
  of 2 using 250 kWh in Nizhny Novgorod pays 6.19 on the first 100 kWh and 10.00 on the rest, about 8.48 on average.
- **VAT is included.** The FAS levels and the regional household tariffs are stated "с учетом НДС"; households
  pay the published figure. The VAT rate has been 22% since 2026-01-01.

## 3. Verification and confidence

`confidence` in the CSV means:
- **high (29 regions):** the 2026-10-01 figure was read on a fetched page (regional body, supplier or media
  quoting the order) and agrees with the FAS cap, or is the regional body's own figure.
- **medium:** one of three cases:
  - (a) a search snippet or a single secondary source that agrees with the FAS cap within 1 kop.
  - (b) no Oct-2026 page could be read, so the value is the FAS Oct-Dec max. These rows have source_url = the
    FAS order. The proxy is backed by Rosstat's Aug-2026 price equalling the Jan-Sep cap.
  - (c) the special cases below.
- **low:** none were kept. Where snippets conflicted with the cap and with Rosstat, the FAS cap was used and the
  row marked medium (b). Examples: a snippet of 6.80 for Udmurtia against a cap of 6.41, and 6.80 for Bryansk
  against 6.56.

Rows filled from the FAS cap without a direct Oct-2026 read (medium b):
RU-BRY Bryansk Oblast, RU-KGD Kaliningrad Oblast, RU-KHM Khanty-Mansi Autonomous Okrug - Yugra, RU-KL Republic of Kalmykia, RU-KR Republic of Karelia, RU-MUR Murmansk Oblast, RU-NEN Nenets Autonomous Okrug, RU-NGR Novgorod Oblast, RU-PNZ Penza Oblast, RU-TYU Tyumen Oblast, RU-UD Udmurt Republic, RU-YAN Yamalo-Nenets Autonomous Okrug, RU-YEV Jewish Autonomous Oblast.

## 4. Special cases

- **Irkutsk (RU-IRK), the cheapest:** base 2.10 rub/kWh from 01.10.2026, up from 1.80. The second range (to 6,000
  kWh/month for houses) is 4.30 and the third is 7.97. Electric-heated houses pay 1.47 up to 7,020 kWh in the
  heating season. Source: the Irkutsk tariff service order 79-716-спр of 29.12.2025, via Irkutskenergosbyt
  (https://sbyt.irkutskenergo.ru/for-population/tariffs-and-consumption-standards/tariffs/).
  - The base exceeds the FAS cap of 2.00. The cap seems to apply to a blended level once the 1.47 rural/heating
    rate is counted. Rosstat Aug-2026 (1.80) matches the Jan-Sep base.
  - The low price comes from the Angara hydro cascade. The steep upper ranges were introduced in 2023-24 against
    crypto-mining.
- **Khakassia (RU-KK), second cheapest:** 3.67 for urban gas-stove homes in the first range (up to 3,900
  kWh/month), from 3.30. The second range is 4.84 and the third 9.91; the reduced-coefficient homes pay
  2.57/3.39/6.94. Source: Goskomtarif order 7-э of 29.12.2025 (https://r-19.ru/news/obshchestvo/188563/). Sayano-Shushenskaya hydro.
- **Other low-tariff regions:**
  - Dagestan 4.45; Chechnya 4.62. Both have high losses and non-payment, and their tariffs are held down.
  - Murmansk 4.70 (Kola nuclear and hydro).
  - Novosibirsk 4.64.
  - Tyumen, KhMAO and YaNAO 4.77 each (one FAS level for the Tyumen "matryoshka").
  - Krasnoyarsk 4.77 within its social norm.
- **Krasnoyarsk (RU-KYA):** the social-norm region with the widest FAS corridor (1.71-4.49 within norm), which
  reflects the isolated Norilsk/Taimyr systems. The Krasnoyarsk city tariff for no-electric-stove homes is 4.77
  within the norm and **7.76 above it** (from 4.13 and 6.65, +15.5%). These exceed the FAS max levels of 4.49 and
  7.24. Rosstat Aug-2026 shows 4.13 and 6.65, so the media figures are consistent. Source:
  https://ngs24.ru/text/gorod/2026/09/05/76626695/ . Electric-stove homes pay 3.34 within the norm and 5.43 above.
- **Other social-norm regions:**

  | Region | Within norm | Above norm (in CSV) | Source |
  |---|---:|---:|---|
  | Zabaykalsky | 5.25 | 6.95 | chita.ru, verified |
  | Vladimir | 7.84 (FAS cap; media 7.83) | 9.38 (FAS) | |
  | Nizhny Novgorod | 6.19 | 10.00 | |
  | Oryol | 6.64 (FAS) | 9.17 (FAS) | |
- **Far East equalisation (выравнивание тарифов ДФО):** since 2017 the Far Eastern Federal District's
  non-price/isolated zones get prices equalised toward the national average. This is financed by a capacity
  surcharge paid by wholesale buyers in the price zones (Federal Law 35-FZ art. 23.3 and Government decree 895).
  It mainly concerns business tariffs. Household tariffs there are set regionally and subsidised from regional
  budgets in isolated zones.
  - **Chukotka (12.84) and Yakutia (10.92)** remain the most expensive in Russia.
  - Magadan 8.46, Kamchatka 6.24, Sakhalin 6.88, Primorye 6.46, Khabarovsk 7.67.
  - **Kamchatka** has a FAS corridor (2.78-9.09) rather than a point. The 6.24 figure applies to
    Petropavlovsk-Kamchatsky/Yelizovo, from 5.68 in Jan-Sep.
  - In Yakutia, Chukotka and Kamchatka the regulated tariff in isolated settlements can differ from the base.
- **Seasonal tariffs:** several regions widen the first-range threshold in the heating season for electric-heated
  houses: Irkutsk, Khakassia and Primorye (7,020 kWh Sept-May), and Perm (3,900 kWh). There is no seasonal
  variation for the standard urban gas-stove flat in the CSV.
- **Moscow (RU-MOW):** 8.90 with no volume ranges. Electric-stove homes pay 8.46 and rural/СНТ 8.28. Order of the
  city's economic policy department ДЭПиР-ТР-407/25 of 24.12.2025.
- **Highest base tariffs:** Chukotka 12.84 and Yakutia 10.92. Next come the above-norm figures for Nizhny
  Novgorod (10.00) and Vladimir (9.38), then Moscow Oblast 9.32, Moscow 8.90, Altai Republic 8.85 and NAO 8.77.

## 5. Population weights

- Source: Rosstat, "Оценка численности постоянного населения на 1 января 2025 г. и в среднем за 2024 г."
  (https://rosstat.gov.ru/storage/mediabank/OkPopul_Comp2025_Site.xlsx, published 14.03.2025, sheet "Всего",
  column "на 1 января 2025 г.").
- **This is the latest regional 1 January estimate Rosstat has published.** The Rosstat demography page
  (https://rosstat.gov.ru/folder/12781, read 2026-10-04) has no file for 1 January 2026. Rosstat has restricted
  demographic releases since 2025. A national figure of 146.03 M for 1 Jan 2026 circulates in secondary sources
  but is unverified, and no regional breakdown was found.
- Coverage: Rosstat's Russia total of 146,119,928 includes occupied Crimea and Sevastopol and excludes the other
  occupied territories. The 83 rows here sum to **143,659,377**.
- Arkhangelsk and Tyumen use the "без автономных округов" rows, so NAO, KhMAO and YaNAO are not double-counted.

**Population-weighted mean of the CSV tariff: 7.10 rub/kWh** (83 subjects, urban no-stove base). This
uses above-norm values for the 5 social-norm regions; with within-norm values instead it is 6.92 rub/kWh.

## 6. National average household price (Rosstat)

| Item, Russian Federation | Value | Period | Source |
|---|---:|---|---|
| Electricity in flats without electric stoves, minimum volume (item 9471) | **5.947 rub/kWh** (594.70 per 100 kWh) | Aug 2026 (before the 1 Oct indexation) | sred_potreb_cen_08-2026.xlsx |
| same, above minimum volume (9472) | 6.148 | Aug 2026 | same |
| with electric stoves, minimum volume (9473) | 4.485 | Aug 2026 | same |
| "Услуги по снабжению электроэнергией", all households (9475) | 5.455 (monthly); 5.48 (weekly, 28 Sep 2026) | Aug / Sep 2026 | same; https://rosstat.gov.ru/storage/mediabank/nedel_sred_cen.xlsx |

The September and October 2026 monthly files were not yet published on 2026-10-04. Applying +11.3% gives an
estimated Oct-2026 national no-stove average of about 6.62 rub/kWh (derived, not a Rosstat figure). This CSV's
population-weighted mean (6.92 with within-norm values) runs about 4-5% higher, because Rosstat weights by its
own consumer-price basket rather than by population, and the rows here are urban base rates. Rosstat's 9471
national figure is weighted by Rosstat's own consumer-price weights, not population.

## 7. Excluded rows (present in the FAS order, deliberately not in the CSV)

- **Occupied Ukrainian territories:** Republic of Crimea (FAS 5.45), Sevastopol (5.71), the so-called "DNR"
  (2.89), "LNR" (2.86), and the Zaporizhzhia (3.78) and Kherson (3.67) "oblasts". For DNR/LNR/Zaporizhzhia/Kherson
  FAS allowed about +50% from 1 Oct 2026. None of these has an ISO 3166-2:RU code.
- **Baikonur** (7.83): leased from Kazakhstan, not a federal subject.

## 8. Per-region notes

Sorted by tariff. Source URL per row is in the CSV.

| zone | name | rub/kWh | confidence | note |
|---|---|---:|---|---|
| RU-IRK | Irkutsk Oblast | 2.10 | high | 1st range up to 3900 kWh/month (houses) / 2000 (flats); exceeds FAS cap 2.00; Irkutsk tariff service order 79-716-spr of 29.12.2025 |
| RU-KK | Republic of Khakassia | 3.67 | high | Goskomtarif Khakassia order 7-e of 29.12.2025; 1st range up to 3900 kWh/month |
| RU-DA | Republic of Dagestan | 4.45 | high |  |
| RU-CE | Chechen Republic | 4.62 | high | 1st range; FAS cap 4.63 |
| RU-NVS | Novosibirsk Oblast | 4.64 | medium | 4.18 -> 4.64; FAS cap 4.65 |
| RU-MUR | Murmansk Oblast | 4.70 | medium | FAS cap for 01.10-31.12.2026; Rosstat Aug-2026 price equals the Jan-Sep cap |
| RU-KHM | Khanty-Mansi Autonomous Okrug - Yugra | 4.77 | medium | FAS cap for 01.10-31.12.2026; Rosstat Aug-2026 price equals the Jan-Sep cap |
| RU-TYU | Tyumen Oblast | 4.77 | medium | FAS cap for 01.10-31.12.2026; Rosstat Aug-2026 price equals the Jan-Sep cap |
| RU-YAN | Yamalo-Nenets Autonomous Okrug | 4.77 | medium | FAS cap for 01.10-31.12.2026; Rosstat Aug-2026 price equals the Jan-Sep cap |
| RU-ORE | Orenburg Oblast | 5.19 | medium | 1st range; snippet |
| RU-CHE | Chelyabinsk Oblast | 5.38 | medium | snippet |
| RU-BA | Republic of Bashkortostan | 5.55 | high | 1st range |
| RU-CU | Chuvash Republic | 5.60 | medium | snippet; FAS cap 5.61 |
| RU-KGN | Kurgan Oblast | 5.68 | high | 1st range up to 1200 kWh |
| RU-TY | Tyva Republic | 5.81 | medium | 1st range up to 3900 kWh; aggregator page fetched |
| RU-PNZ | Penza Oblast | 5.86 | medium | FAS cap for 01.10-31.12.2026; Rosstat Aug-2026 price equals the Jan-Sep cap |
| RU-KEM | Kemerovo Oblast (Kuzbass) | 5.97 | medium | 1st range; snippet |
| RU-SAR | Saratov Oblast | 6.03 | high | 1st range up to 3900 kWh |
| RU-TOM | Tomsk Oblast | 6.07 | medium | 1st range up to 3900 kWh; order 6-683 of 29.12.2025; snippet |
| RU-KR | Republic of Karelia | 6.10 | medium | FAS cap for 01.10-31.12.2026; Rosstat Aug-2026 price equals the Jan-Sep cap |
| RU-IN | Republic of Ingushetia | 6.14 | high | FAS cap 6.15 |
| RU-MO | Republic of Mordovia | 6.15 | medium | 1st range up to 1200 kWh; snippet |
| RU-KAM | Kamchatka Krai | 6.24 | medium | FAS cap is a corridor 2.78-9.09; 5.68 Jan-Sep (matches Rosstat Aug-2026) -> 6.24; search snippet |
| RU-ME | Mari El Republic | 6.25 | medium | 1st range up to 1200 kWh; snippet |
| RU-ULY | Ulyanovsk Oblast | 6.27 | medium | 1st range; snippet only for gas-stove value |
| RU-YAR | Yaroslavl Oblast | 6.30 | high | 1st range up to 3900 kWh |
| RU-AMU | Amur Oblast | 6.31 | high | 1st range up to 3900 kWh; FAS cap 6.32 |
| RU-YEV | Jewish Autonomous Oblast | 6.32 | medium | FAS cap for 01.10-31.12.2026; Rosstat Aug-2026 price equals the Jan-Sep cap |
| RU-UD | Udmurt Republic | 6.41 | medium | FAS cap for 01.10-31.12.2026; Rosstat Aug-2026 price equals the Jan-Sep cap |
| RU-LIP | Lipetsk Oblast | 6.42 | medium | 1st range up to 1635 kWh; snippet |
| RU-PRI | Primorsky Krai | 6.46 | medium | snippet; Rosstat Aug-2026 4.65 is the electric-stove rate |
| RU-TA | Republic of Tatarstan | 6.47 | high |  |
| RU-KRS | Kursk Oblast | 6.52 | high | Kursk decree 86 of 25.12.2025; FAS cap 6.53 |
| RU-KB | Kabardino-Balkar Republic | 6.53 | medium | snippet; FAS cap 6.54 |
| RU-BRY | Bryansk Oblast | 6.56 | medium | FAS cap for 01.10-31.12.2026; Rosstat Aug-2026 price equals the Jan-Sep cap |
| RU-TVE | Tver Oblast | 6.62 | high | 1st range up to 3800 kWh; REC order 578-np of 26.12.2025 |
| RU-ROS | Rostov Oblast | 6.66 | medium | 1st range; snippet |
| RU-KIR | Kirov Oblast | 6.68 | medium | economically justified rate quoted; FAS cap 6.69 |
| RU-VOR | Voronezh Oblast | 6.69 | medium | 1st range; snippet |
| RU-SMO | Smolensk Oblast | 6.73 | high | decree 439 of 30.12.2025 |
| RU-BEL | Belgorod Oblast | 6.79 | high |  |
| RU-TAM | Tambov Oblast | 6.80 | medium | 1st range up to 3900 kWh; snippet |
| RU-BU | Republic of Buryatia | 6.85 | medium | order RST 1/30 of 24.12.2025; snippet |
| RU-SAK | Sakhalin Oblast | 6.88 | high | FAS cap 6.89 |
| RU-SAM | Samara Oblast | 6.95 | high | FAS cap 6.96 |
| RU-ZAB | Zabaykalsky Krai | 6.95 | high | ABOVE social norm (65 kWh/person); within norm 5.25 |
| RU-KC | Karachay-Cherkess Republic | 6.97 | medium | 1st range up to 3900 kWh; snippet |
| RU-SE | Republic of North Ossetia-Alania | 6.97 | medium | snippet; FAS cap 6.98 |
| RU-PER | Perm Krai | 6.98 | high | 1st range up to 1000 kWh (urban); FAS cap 6.99 |
| RU-KGD | Kaliningrad Oblast | 7.01 | medium | FAS cap for 01.10-31.12.2026; Rosstat Aug-2026 price equals the Jan-Sep cap |
| RU-ALT | Altai Krai | 7.07 | high | 1st range up to 3900 kWh; FAS cap 7.08 |
| RU-OMS | Omsk Oblast | 7.08 | medium | snippet; FAS cap 7.09 |
| RU-SVE | Sverdlovsk Oblast | 7.15 | medium | 1st range; ranges 7.15/10.23/13.47 |
| RU-LEN | Leningrad Oblast | 7.44 | medium | 1st range; committee order 587-p of 19.12.2025; snippet |
| RU-VGG | Volgograd Oblast | 7.49 | medium | 1st range up to 1500 kWh; snippet |
| RU-NGR | Novgorod Oblast | 7.52 | medium | FAS cap for 01.10-31.12.2026; Rosstat Aug-2026 price equals the Jan-Sep cap |
| RU-KOS | Kostroma Oblast | 7.54 | medium | 1st range up to 3900 kWh; snippet |
| RU-TUL | Tula Oblast | 7.60 | medium | 1st range up to 1200 kWh; snippet; FAS cap 7.61 |
| RU-PSK | Pskov Oblast | 7.65 | medium | 1st range; snippet |
| RU-KHA | Khabarovsk Krai | 7.67 | medium | snippet; one conflicting snippet |
| RU-KYA | Krasnoyarsk Krai | 7.76 | medium | ABOVE social norm, no electric stove; within norm 4.77; exceeds FAS caps 7.24/4.49; Jan-Sep values 6.65/4.13 match Rosstat Aug-2026 |
| RU-IVA | Ivanovo Oblast | 7.88 | medium | 1st range up to 1000 kWh; snippet |
| RU-SPE | Saint Petersburg | 7.88 | high | gas stoves, 1st range |
| RU-STA | Stavropol Krai | 7.90 | high | 1st range up to 3900 kWh |
| RU-KO | Komi Republic | 7.97 | medium | 1st range up to 1200 kWh; snippet |
| RU-RYA | Ryazan Oblast | 8.06 | medium | snippet |
| RU-VLG | Vologda Oblast | 8.10 | high |  |
| RU-AST | Astrakhan Oblast | 8.21 | high | 1st range up to 1200 kWh |
| RU-AD | Republic of Adygea | 8.31 | high |  |
| RU-KDA | Krasnodar Krai | 8.31 | high | 1st range |
| RU-KLU | Kaluga Oblast | 8.32 | medium | 1st range up to 1200 kWh; snippet; URL truncated in search result |
| RU-ARK | Arkhangelsk Oblast | 8.39 | medium | 1st range up to 1200 kWh; snippet |
| RU-KL | Republic of Kalmykia | 8.42 | medium | FAS cap for 01.10-31.12.2026; Rosstat Aug-2026 price equals the Jan-Sep cap |
| RU-MAG | Magadan Oblast | 8.46 | high | order 36-2/e of 22.12.2025; electric stove/rural 5.92; FAS cap 8.47 |
| RU-NEN | Nenets Autonomous Okrug | 8.77 | medium | FAS cap for 01.10-31.12.2026; Rosstat Aug-2026 price equals the Jan-Sep cap |
| RU-AL | Altai Republic | 8.85 | high | 1st range up to 3900 kWh |
| RU-MOW | Moscow | 8.90 | high | DEPR Moscow order DPR-TR-407/25; no volume ranges |
| RU-ORL | Oryol Oblast | 9.16 | medium | ABOVE social norm; within norm 6.64; snippet; FAS caps 9.17/6.64 |
| RU-MOS | Moscow Oblast | 9.32 | medium | 1st range; search snippet |
| RU-VLA | Vladimir Oblast | 9.38 | medium | ABOVE social norm = FAS cap; within norm cap 7.84 (media 7.83); Rosstat Aug-2026 7.04/8.43 = Jan-Sep caps |
| RU-NIZ | Nizhny Novgorod Oblast | 10.00 | medium | ABOVE social norm (50 kWh/person); within norm 6.19; snippet |
| RU-SA | Sakha (Yakutia) Republic | 10.92 | medium | snippet; FAS cap 10.93 |
| RU-CHU | Chukotka Autonomous Okrug | 12.84 | medium | snippet; = FAS cap; highest in Russia |
