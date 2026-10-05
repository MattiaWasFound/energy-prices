# Zones for KZ, IQ, SO and KN (researched 2026-10-05)

Group `zones` of the October 2026 research (`method.md`). It starts from the
`rest-of-world/` notes (`asia-east.md`, `asia-south-west.md`,
`gapfill-africa-gaps.md`, `americas-caribbean-east.md`), checks them, and turns
the four zone candidates into config rows. The price definition and source
rules are those of `rest-of-world/method.md`.

Files:

- `zones.csv` (`country,id,name,area,weight,weight_source`) and
  `static_prices.csv` (`country,zone,price,currency,as_of,source,licence,note`),
  one price row per zone.
- `build.py` writes both CSVs from the figures below and prints each
  country's weighted mean and max/min ratio. Rerun: `python3 build.py`.
- The two PDFs read in full (BGS Somalia report, Somali Public Agenda
  Bosaso brief) are cited below; copies are not kept here.

Summary:

| Country | zone_label | Zones | Range | Max/min | Weighted mean | National row |
|---|---|---|---|---|---|---|
| KZ | Регион | 20 (17 oblasts + 3 cities) | 23.86–45.51 KZT | 1.91 | 33.99 KZT | drop |
| IQ | المنطقة | 2 (Kurdistan Region, rest of Iraq) | 10–82.74 IQD | 8.3 | 20.28 IQD | drop |
| SO | Gobol | 7 (Banaadir, 5 member states, Somaliland) | 0.41–1.00 USD | 2.4 | 0.72 USD | drop |
| KN | Island | 2 (St Kitts, Nevis) | 0.70–1.57 XCD | 2.2 | 0.92 XCD | drop |

All four existing national rows describe one place only (KZ is a midpoint of
two cities, IQ is federal Iraq, SO is Mogadishu, KN is St Kitts). None is a
published national average, so each should be dropped and the country average
left to the weighted zone mean. The US is the only case with a published
national figure worth keeping, and none of these four has one.

## KZ Kazakhstan: 20 regions, tier 2 incl. VAT

**Zones.** These are the 17 oblasts plus the three cities of republican
significance (Astana, Almaty, Shymkent). Ids are the ISO 3166-2 codes, which
became numeric on 2022-11-29: KZ-71 Astana, KZ-75 Almaty, KZ-79 Shymkent,
KZ-10 … KZ-63 for the oblasts. The method's example "KZ-ALA" is the pre-2022
letter code. Names are the official Russian forms, as on the bill (bills are
bilingual Kazakh/Russian, and the existing RU zones use Russian). The three
oblasts created in 2022 have official Russian names in Kazakh spelling:
"область Абай", "область Жетісу", "область Ұлытау". zone_label is
**Регион**, not "Область", because three of the zones are cities.

**Price.** Each regional supplier sells to households at a flat price per kWh
with 16% VAT (since 2026-01-01). There is no standing charge. Households with
meters are on three volume tiers. The method asks for tier 2 at typical use,
and that holds up: Astana-REK's tiers (no electric stove) are 0–70 kWh at
24.81, 70–140 at 33.74 and above 140 at 42.18. At 200 kWh/month the bill is
70×24.81 + 70×33.74 + 60×42.18 = 6,629.30 KZT, or 33.15 per kWh, against a
tier 2 rate of 33.74. Tier 2 is therefore used everywhere.

Sources, in order of preference:

- **Supplier pages (high):**
  - Astana-REK, 33.74 from 2026-07-01
    (https://astrec.kz/abonentam/tarify-dlia-fizicheskih-lits).
  - AZhK Energosbyt, which serves both Almaty city and Almaty oblast, from
    2026-09-12 (https://www.esalmaty.kz/ru/home-tariffs; vlast.kz). Tiers are
    29.55 / 39.23 / 49.04 excluding VAT, or 34.28 / **45.51** / 56.89
    including it. The unified household rate is 37.92 including VAT; the rest-of-world
    research used that rate.
- **zhkh24.kz regional table (medium):** tier 2 including VAT without an
  electric stove, for all 20 regions, collected 2026-08-17
  (https://zhkh24.kz/ru/articles/skolko-stoit-svet-v-raznyh-regionah-kazahstana-tarify-dlya-naseleniya-v-2026-godu).
  It is a housing-sector news site compiling the suppliers' rates, and its
  Astana figure (33.74) matches the supplier page exactly.
- **Rises on 1 October 2026.** These are applied by scaling the August tier 2
  by the ratio of the new to the old household base rate. In every region
  checked, tier 2 is 1.20 × the base household rate, so the scaling holds.
  - Atyrau: base 22.29 to 24.52 excluding VAT (+10.0%), so 31.03 → **34.13**
    (digitalbusiness.kz, inform.kz).
  - Pavlodar: base 21.63 to 22.71 (+5.0%), so 30.11 → **31.61**
    (digitalbusiness.kz).
  - West Kazakhstan: household rate 29.04 to 30.49 (+5.0%), so 33.69 →
    **35.37** (bes.media). This one is low confidence: 29.04 excluding VAT
    does not reconcile with zhkh24's August 33.69 including VAT (which is
    29.04 × 1.16 exactly, so 33.69 may be the base rate rather than tier 2).
    The true tier 2 could be about 40–42.
- **Pending, not applied:**
  - Astana-REK applied to raise its limit price from 32.74 to 38.98 excluding
    VAT from 2026-10-01; no approval was found (bes.media, tengrinews).
  - North Kazakhstan asked for about +15% (qaz-media.kz).
  - The cause is national: the Single Buyer's renewables cost went from 13 to
    16 KZT/kWh on 2026-07-15. More regions will follow this autumn, so
    re-check in a few months.

**Prices.** The range is from North Kazakhstan 23.86 to Almaty city and oblast
45.51, so max/min is 1.91. Roughly: the north, east and west are 24–28; the
south and the cities 30–37; Akmola, Kostanai and Almaty 39–46. This is just
under the 2x rule. It is kept because the method and the `rest-of-world/` research already chose
to zone KZ, and Almaty (19% of the population with its oblast) sits at the top.

**Weights.** Bureau of National Statistics population at 1 Dec 2024, from the
table in ru.wikipedia "Административно-территориальное деление Казахстана".
That gives one consistent date. The July 2026 figures in the press cover only
10 of the 20 regions, with the same shares within about 0.5 point (Almaty
2.37M, Turkestan 2.15M, Astana 1.68M). The weighted mean is **33.99 KZT**,
close to the rest-of-world research's 33.0 midpoint.

**National row.** Drop it. The 33.0 row is the midpoint of two cities, not a
national figure, and the weighted mean replaces it.

## IQ Iraq: Kurdistan Region against the rest of Iraq

**Zones: two, not governorates.** Inside each region the tariff is uniform:
KRG MoE Runaki in all four Kurdistan governorates, and the federal Ministry of
Electricity in the other 15. Governorates would add 19 rows with only two
prices.

- **IQ-KR** is the ISO 3166-2 code for the Kurdistan Region, the parent of
  IQ-AR, IQ-SU and IQ-DA. Halabja has no ISO code yet.
- **IQ-FED** is our own code for the 15 federal governorates.

Names are in Arabic, an official language in both regions, so the list reads
in one script: "إقليم كوردستان" and "محافظات العراق الأخرى" ("Iraq's other
governorates"). The Kurdish (Sorani) name "هەرێمی کوردستان" may be what Runaki
bills print; see the open questions. zone_label is **المنطقة** ("area" or
"region"). "الإقليم" would be wrong for the federal part.

**IQ-KR: 82.74 IQD, medium confidence.**

- Runaki household blocks from 14 May 2025: 72 IQD for 0–400 kWh, 108 for
  401–800, 175 for 801–1,200, 265 for 1,201–1,600, 350 above. No fixed charge
  or VAT was found (964media, 2025-05-14).
- Typical use: KRG MoE reported in February 2026 that half of Runaki
  households used under 853 kWh on a billing cycle of about 45 days. That is
  about 570 kWh/month, and the median bill (73,000 IQD) is consistent with
  monthly blocks (964media 45190; gov.krd is behind Cloudflare and was not
  readable).
- At 570 kWh: 400×72 + 170×108 = 47,160 IQD, or **82.74 IQD/kWh**. At 400 kWh
  or less it is 72. The winter cycle was described as unusually cold, so the
  yearly median may be a bit lower, but Iraqi summers drive use up as well.
- Runaki 24-hour supply reached more than 90% of the region in 2026
  (Kurdistan24). The remaining households are still on the old KRG tariff plus
  generators.
- Temporary relief such as the 20% e-payment credit is left out.

**IQ-FED: 10 IQD, high confidence, unchanged from the rest-of-world research.** This is the
Ministry of Electricity flat 10 IQD/kWh up to 1,500 kWh. The ministry denied
increases in December 2025 and May 2026. It is the grid price only: most
federal households also pay neighbourhood generators (about 20,000 IQD per
amp per month), which no tariff covers.

**Weights.** From the final 2024 census (Feb 2025): Kurdistan Region
6,519,129 of 46,118,793, or **0.1414**. Another report gives 6.37M for the
region, which would be 0.138. Weighted mean: **20.28 IQD**.

**National row.** Drop it. 10 IQD is only federal Iraq. The weighted mean
(20.3) is what a nationwide figure should show.

## SO Somalia: Banaadir, five member states, Somaliland

**Zones.** Each city has its own private grid, and residents know their
member state.

| id | name | main city and provider | price USD/kWh | as_of | source |
|---|---|---|---|---|---|
| SO-BN | Banaadir (Muqdisho) | Mogadishu, BECO | 0.41 | 2023 | BGS 2025, Fig. 2 |
| SO-JUB | Jubaland | Kismayo | 0.90 | 2023 | BGS 2025, Fig. 1 |
| SO-SWS | Koonfur Galbeed | Baidoa | 0.70 | 2023 | BGS 2025, Fig. 1 |
| SO-HIR | Hirshabeelle | Jowhar, Beledweyne | 1.00 | 2023 | BGS 2025, Fig. 1 |
| SO-GAL | Galmudug | Galkayo south, Dhusamareb | 1.00 | 2023 | BGS 2025, Fig. 1 |
| SO-PUN | Puntland | Bosaso, PEPCO | 0.79 | 2025-08 | Somali Public Agenda brief 36/2025 |
| SO-SML | Somaliland | Hargeisa | 0.59 | 2025-12 | Ministry of Energy and Minerals decision |

- SO-BN is the ISO 3166-2 region code. The member states have no ISO code, so
  they get our own ids.
- Names are in Somali, the language of bills and of daily use. "Koonfur
  Galbeed" is South West State and "Hirshabeelle" the Somali spelling.
  Somaliland is named plainly as "Somaliland", with no status word.
- zone_label is **Gobol** ("region"). The member states are "dowlad goboleed",
  which is too long for a picker.

**Notes per zone:**

- **Banaadir.** BGS's BECO chart gives the household price as $0.46 in 2022
  and $0.41 in 2023, with the note "minimum for business $0.30, maximum for
  household $0.41". The $0.36 in its Figure 1, which the rest-of-world research used, is the
  all-customer average. The household rate is used here. No BECO price after
  2023 was found.
- **Jubaland, South West, Hirshabelle, Galmudug.** Only the 2023 state
  averages exist (BGS Figure 1, credited to Shuraako and the National
  Transformation Plan 2025). No city provider's current price was found. These
  rows are low confidence.
- **Puntland.** The method says to use the main city. Bosaso is the largest
  city and the commercial hub; after a merger it is served by one company,
  PEPCO, at $0.79 (SPA, Aug 2025). Garowe, the capital, is about $0.59. BGS's
  2023 state average is $1.00.
- **Somaliland.** The government set $0.59 for every city except Berbera from
  2025-12-01, down from $0.73 (set June 2022). It is tied to subsidised fuel
  for power companies (geeska.com, somalilandcurrent.com). It is a press
  report of a ministry decision; the decision document itself was not found.
  Medium confidence.

**Currency.** Everything is priced in USD, Somaliland included: its government
tariff is set in USD. Nowhere was a utility found billing in SOS or SLSH. How
Somaliland households actually pay (USD mobile money or shillings at the
day's rate) was not checked. Note that `countries.csv` lists SO as
**SOS** while the price rows are USD. That was already so for the national
row, so check that the build accepts a static row in a
currency other than the country's.

**Fixed charges.** None were itemised. The providers sell a flat per-kWh price,
with connection and meter fees paid upfront, so the prices hold at any use.

**Weights.** OCHA Somalia subnational population estimates for 2025, for the
18 pre-1991 regions (via en.wikipedia "Regions of Somalia"; OCHA's HDX
dataset is CC BY-IGO), mapped to states:

- Jubaland: Gedo, Lower Juba, Middle Juba.
- South West: Bay, Bakool, Lower Shabelle.
- Hirshabelle: Hiran, Middle Shabelle.
- Galmudug: Galguduud plus ½ Mudug.
- Puntland: Bari, Nugal, ½ Mudug, ½ Sool, ½ Sanaag.
- Somaliland: Awdal, Maroodi Jeex, Togdheer, ½ Sool, ½ Sanaag.

The halves are a rough neutral split of contested or divided regions. Las
Anod (SSC-Khaatumo, since 2025 part of the federal Northeast State) belongs
to neither priced zone and is not modelled. The resulting weights are
Banaadir 0.169, Jubaland 0.137, South West 0.181, Hirshabelle 0.081,
Galmudug 0.083, Puntland 0.165, Somaliland 0.184. Weighted mean: **0.72 USD**.
For comparison, BGS's 2023 national average is 0.81.

**National row.** Drop it. The current 0.36 is Mogadishu's all-customer
average and makes Somalia look half as expensive as it is.

## KN Saint Kitts and Nevis: two islands

**Zones.** KN-K St Kitts (SKELEC) and KN-N Nevis (NEVLEC), the ISO 3166-2
state codes. The names are in English. zone_label is **Island**.

**The open question from the rest-of-world research: is SKELEC's fuel variation charge still
subsidised? Yes, as of June 2026.** SKELEC's November 2022 notice says the
FVC is shown on the bill and credited back in full by the government. On 18
June 2026, Energy Minister Konris Maynard, who is responsible for SKELEC,
said: "It costs more for SKELEC to purchase fuel than for them to charge you
and us for the electricity." He said residential tariffs remain below the fuel
cost of production, with the government subsidising the difference
(WINN FM, https://www.winnmediaskn.com/nevis-premier-says-cap-on-fuel-surcharge-to-be-removed-due-to-continued-global-volatility/).
This is a minister's statement reported by the press, not a SKELEC notice,
and no current FVC value was found. It is enough to move St Kitts from low
to medium confidence. The 2022 measure that halves bills for customers under
200 kWh was not re-checked; it does not affect a 300 kWh bill.

**KN-K St Kitts: 0.70 XCD, medium confidence.** SKELEC's posted tariff dates
from January 2011. At 300 kWh: energy 50×0.59 + 100×0.65 + 150×0.68 = 196.50,
plus a demand charge of EC$13 per 15 A of fuse rating (one unit assumed),
gives 209.50, or **0.698**. With a 60 A service it is 0.83. There is no VAT on
electricity.

**KN-N Nevis: 1.57 XCD, medium confidence.** At 300 kWh: NEVLEC energy
50×0.65 + 75×0.70 + 175×0.75 = 216.25, plus a standing charge of 18.00 above
250 kWh, plus the fuel surcharge 300×0.79 = 237.00, gives EC$471.25, or
**1.571**. The surcharge came back in June 2026 at 0.69 and is 0.79 in
NEVLEC's September 2026 bill guide. It changes monthly.

**Weights.** From the 2022 Population and Housing Census summary report
(CARICOM statistics): St Kitts 38,138 and Nevis 13,182 of 51,320, giving
0.7431 and 0.2569. Weighted mean: **0.92 XCD**. Max/min is 2.24.

**National row.** Drop it. The 0.70 row is St Kitts alone. The weighted mean
(0.92) includes Nevis's reinstated surcharge.

## What could not be settled

1. **KZ, Astana's October rise.** Astana-REK applied for +19% on the limit
   price from 2026-10-01. If it was approved, Astana's tier 2 would be about
   40 instead of 33.74. North Kazakhstan asked for +15%, and other regions are
   likely to follow the July rise in the Single Buyer's cost.
2. **KZ, West Kazakhstan's tier 2.** zhkh24's 33.69 looks like the base rate
   including VAT, not tier 2. The true tier 2 may be about 42.
3. **KZ, tier thresholds.** It is unclear whether the tier thresholds are per
   account (as Astana-REK's page reads) or per registered resident (as
   zhkh24 says). If they are per person, a family's blended price is lower
   than tier 2.
4. **IQ, bill language and typical use.** It is not known whether Runaki bills
   print Kurdish, Arabic or both. That decides whether IQ-KR should read
   "هەرێمی کوردستان". The 570 kWh figure comes from one winter billing cycle;
   no yearly mean was found.
5. **SO, prices after 2023.** Four of the seven SO prices are 2023 survey
   averages: no current provider tariff for Kismayo, Baidoa, Jowhar or
   Galkayo, and no BECO price after 2023. The weights split contested regions
   50/50.
6. **SO, currency.** `countries.csv` says SOS but households are billed in
   USD. Either the country's currency should become USD or the build must
   accept the USD rows.
7. **KN, St Kitts.** The 2026 FVC value and a SKELEC-side confirmation of the
   subsidy were not found, and the reading of the demand charge per 15 A of
   fuse rating is still ambiguous.

## Sources

- zhkh24.kz regional table: https://zhkh24.kz/ru/articles/skolko-stoit-svet-v-raznyh-regionah-kazahstana-tarify-dlya-naseleniya-v-2026-godu
- Astana-REK: https://astrec.kz/abonentam/tarify-dlia-fizicheskih-lits
- AZhK Energosbyt: https://www.esalmaty.kz/ru/home-tariffs
- vlast.kz on the September rise: https://vlast.kz/novosti/70802-v-almaty-i-almatinskoj-oblasti-s-12-sentabra-povysatsa-tarify-na-elektroenergiu.html
- Rises from 1 October: https://digitalbusiness.kz/2026-10-01/chto-podorozhaet-v-kazahstane-s-1-oktyabrya-2026-goda/
  and https://www.inform.kz/ru/noviy-tarif-na-elektroenergiyu-utverdili-v-atirauskoy-oblasti-35f83c09
- West Kazakhstan: https://bes.media/news/v-zko-s-1-oktyabrya-podnimut-tarif-na-elektroenergiyu-dlya-naseleniya/
- Astana application: https://bes.media/news/elektrichestvo-v-astane-mozhet-podorozhat-s-oktyabrya-skolko-pridetsya-platit-zhitelyam/
- North Kazakhstan request: https://qaz-media.kz/v-srednem-na-15-hotyat-podnyat-tarif-na-elektrichestvo-v-sko/
- KZ population (BNS, 1 Dec 2024): https://ru.wikipedia.org/wiki/Административно-территориальное_деление_Казахстана
- KZ ISO codes: https://en.wikipedia.org/wiki/ISO_3166-2:KZ
- Runaki tariff: https://en.964media.com/35966/
- Runaki median bill: https://en.964media.com/45190/
- Runaki coverage: https://www.kurdistan24.net/en/story/924374
- Iraq Ministry of Electricity calculator: https://web.archive.org/web/20250709013453/https://moelc.gov.iq/?calculation
- Iraq 2024 census: https://peregraf.com/en/news/10297 and https://ina.iq/en/local/43822-planning-minister-announces-final-results-of-national-population-census.html
- Iraq ISO codes: https://en.wikipedia.org/wiki/ISO_3166-2:IQ
- BGS Somalia report: https://bgs.so/wp-content/uploads/2025/10/Navigating-Non-Technical-Barriers-to-Affordable-Electricity-in-Somalia.pdf
- Somali Public Agenda Bosaso brief: https://somalipublicagenda.org/wp-content/uploads/2025/08/SPA_Governance_Briefs_36_2025_ENGLISH1.pdf
- Somaliland tariff cut: https://www.geeska.com/en/somaliland-cuts-electricity-tariffs-ease-energy-costs
- OCHA regional populations: https://en.wikipedia.org/wiki/Regions_of_Somalia
- SKELEC tariff: https://www.skelec.kn/wp-content/uploads/2024/09/ElectricityTariffStructure-Jan2011-scaled.jpg
- SKELEC FVC notice: https://www.skelec.kn/skelec-bills-will-now-show-the-value-of-the-fuel-variation-charge/
- WINN FM, June 2026: https://www.winnmediaskn.com/nevis-premier-says-cap-on-fuel-surcharge-to-be-removed-due-to-continued-global-volatility/
- NEVLEC rates: https://www.nevlec.com/residential/your-bill/electricity-rates/
- NEVLEC bill guide: https://www.nevlec.com/wp-content/uploads/2026/09/UnderstandingYourResidentialBill.png
- KN 2022 census: https://statistics.caricom.org/wp-content/uploads/2025/11/SKN-Census-Report-2021-2022.pdf

Commercial tables (GlobalPetrolPrices and others) were not used.
