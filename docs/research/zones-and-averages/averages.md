# The thirteen averages: AQ BV CF GS HM IO KP PN SJ TF UM VA YE (October 2026)

Research for the zones-and-averages round (`method.md`). After the `rest-of-world/` research,
these thirteen places got no published household price. They fell back to their UN M49 region's
mean, or for AQ to the global mean. Each gets either a country row (in `averages.csv`, the
`rest-of-world/` format, for `tools/import_prices.py`) or "no household price", with a
recommendation on the fallback.

What each one shows today (`out/prices.json`, generated 2026-10-04):

| | Fallback today | Shows | In EUR |
|---|---|---|---|
| AQ | global average | 0.2258 USD | 0.201 |
| BV | South America mean | 1.81 NOK | 0.168 |
| CF | Middle Africa mean | 65.0 XAF | 0.099 |
| GS | South America mean | 0.1425 GBP | 0.168 |
| HM | Australia and New Zealand mean | 0.494 AUD | 0.305 |
| IO | Eastern Africa mean | 0.192 USD | 0.171 |
| KP | Eastern Asia mean | 17.8 KPW | 0.121 |
| PN | Polynesia mean | 0.610 NZD | 0.305 |
| SJ | Northern Europe mean | 3.14 NOK | 0.290 |
| TF | Eastern Africa mean | 0.171 EUR | 0.171 |
| UM | Micronesia mean | 0.441 USD | 0.393 |
| VA | Southern Europe mean | 0.176 EUR | 0.176 |
| YE | Western Asia mean | 24.5 YER | 0.092 |

## Summary

| | Result | Recommendation |
|---|---|---|
| SJ | **1.20 NOK/kWh**, high | Import the row. |
| YE | **300 YER/kWh** (Sana'a grid, old rials), low | Import only together with a YER exchange-rate fix (see YE). |
| CF | 83 XAF/kWh (2017 all-customer average), low | Import the row: it is the country's own figure and nothing newer exists. |
| VA | No household price | Use Italy's price as a proxy (ready row below). |
| PN | No verifiable tariff | Keep the Polynesia mean. It is within about 15% of the only (unverified) tariff. |
| KP | No per-kWh price | Show no price if the client can. Otherwise keep the mean and accept that it is fiction. |
| AQ BV GS HM IO TF UM | No residents | Keep the current fallback, or show nothing. No proxy mechanism. |

## SJ Svalbard and Jan Mayen: 1.20 NOK/kWh (high)

Svalbard Energi AS is Longyearbyen's municipal utility (owned by the lokalstyre). Its notice
was updated 2025-09-25:
households and holiday homes pay **1.20 kr/kWh from 1 October 2025**, "lik pris per kWt, uavhengig
forbruksmengde", including the fastledd (fixed charge) that used to be billed separately. Before
that the price was 3.20 kr/kWh plus about 10.50 kr/day. At 300 kWh/month that was 3.20 + 10.50 × 30.4 / 300 =
**4.26 kr/kWh**, so the reduction is about 72%. A state grant (NOK 4.7m for the first period) pays for it, and
the notice says the aim is a price in line with mainland households.

- Source: https://www.svalbard-energi.no/stoette-til-reduserte-stroempriser-for-husholdninger-i-longyearbyen.6729844-586879.html
- Continuation: the revised national budget of 12 May 2026 proposes a "Svalbardpris" for electricity and
  district heating in 2026 (NOK 9.3m to Svalbard Energi). The stated aim is that the electricity price keeps matching
  what an example household on Norgespris pays on the mainland
  (https://www.nrk.no/tromsogfinnmark/regjeringen-foreslar-egen-svalbardpris-pa-strom-og-fjernvarme-1.17880993;
  the regjeringen.no page refused automated fetches). Svalbard Energi's district-heating notice of
  1 July 2026 (https://www.svalbard-energi.no/?id=6749211) cuts heating to 0.60 kr/kWh, which shows the scheme is
  running. I found no 2026 change to the 1.20 electricity price.
- Taxes: Svalbard is outside the Norwegian VAT area (merverdiavgiftsloven § 1-3), and the notice says
  the 1.20 is the whole price per kWh. So it is all-in as billed. The notice does not mention
  elavgift explicitly.
- Sanity check: mainland Norgespris is 40 øre excl. VAT (50 øre incl.) plus nettleie, which lands near
  1.2 kr. That is consistent.
- Consumption: the price is flat, so the 300 kWh in the row is nominal. Longyearbyen homes are heated by
  district heating, so their electricity use is lower than on the mainland.
- Coverage: Longyearbyen has about 2,500 of Svalbard's roughly 2,900 residents. Barentsburg (Trust
  Arktikugol's coal-mining settlement, a few hundred people, company-supplied) and Jan Mayen (station staff) have no published price.
  The row stands for the territory. That is reasonable, since Longyearbyen is where almost everyone lives.

## YE Yemen: 300 YER/kWh, Sana'a grid in old rials (low), and an exchange-rate problem

**Which price a typical household pays.** Yemen has two grids and two kinds of rial:

- **Areas under the Sana'a authorities** hold most of the population (commonly put at about two-thirds or
  more; I did not fetch a source for this share). The public grid there is run by the Public Electricity
  Corporation under the Sana'a Ministry of Electricity and Energy. It sells at regulated prices close to the
  private-generator level and is billed in old (pre-2016) rial notes:
  - Nov 2023: private commercial stations were capped at 257 YER/kWh (Saba, https://www.saba.ye/en/news3281568.htm,
    found in `rest-of-world/`).
  - Sep 2024: the public grid got tiers of 230 YER/kWh for 1-2,999 kWh per half-month, falling to 170 for very
    large users (Yemen Eco, 2024-09-05, https://yemeneco.org/archives/81651). Households are all in the first tier.
  - Then 250, and from about October 2026 **300 YER/kWh** (Khabar, 2026-10-01,
    https://www.khabaragency.net/news253684.html). The reason given is fuel prices, a rise of about 20%.
    Khabar is hostile to the Sana'a authorities, I have not seen the decision text, and the
    effective date is not given.
- **Government (Aden) areas**: the Ministry's July 2026 memorandum keeps the residential grid tariff at
  **19 YER/kWh** up to 1,000 kWh/month (https://south24.net/news/newse.php?nid=5623, found in `rest-of-world/`). These are new
  rials, about 1,520-1,630 per USD. That is about US$0.012/kWh, but supply is a few hours a day, collection is 20-66%, and
  households fill the gaps with private generators (Taiz's cap for private diesel networks is 900 new YER/kWh, May 2026).

The row uses **300 YER/kWh at 200 kWh/month**: 200 × 300 = 60,000 old YER, about US$112 at about 535 old
YER/USD, so about **US$0.56/kWh**. I chose it because it is the grid price where most households live, and it is close to
what private supply costs there. The Aden 19 YER is a real tariff but nearly symbolic. The gap
between the two is about 40-50x in real terms. A Yemeni reading "300 YER" will recognise it as the Sana'a price.

**Exchange-rate problem; decide before importing.** Both rials carry the ISO code YER. The pipeline's
YER rate comes from Frankfurter: **266.5 YER per EUR, about 237 per USD** (live query 2026-10-05). That matches
neither market. The Sana'a old rial is about 535/USD (about 600/EUR) and the Aden new rial about 1,600/USD
(about 1,800/EUR); sources in the Currency sections of `rest-of-world/asia-south-west.md` and `rest-of-world/gapfill-world-gaps.md`. Figures in
YER display correctly, because the conversion cancels when a price's currency is the country's currency.
Every EUR conversion is wrong, though:

- 300 YER becomes €1.13 in the pipeline, against about €0.50 at the Sana'a rate. As a resolved country, YE would also enter the
  Western Asia mean and raise it by about €0.06/kWh for no real reason.
- The current fallback shows 24.5 YER (the Western Asia mean of €0.092 × 266.5). At the rates households actually face, that is
  €0.04 in Sana'a or €0.014 in Aden.

Options:

- (a) Import the row together with a pinned YER rate of about 600/EUR (the Sana'a old-rial rate, matching
  the price), if config allows a per-currency override. This is the recommendation.
- (b) Import the row but keep YE out of the regional means.
- (c) Leave YE on the average and note the problem.

Without (a) or (b), importing distorts other countries' fallbacks.

## CF Central African Republic: 83 XAF/kWh (low)

A fresh attempt, in French and English, found no current ENERCA residential schedule:

- enerca-rca.com still redirects to an unrelated site.
- ARSEC has no publications online.
- No press article with a tariff grid exists.

The World Bank documents remain the only source. The 2019 Emergency Electricity Supply and Access PAD gives an
ENERCA average tariff of 83 XAF/kWh (US$0.14, 2017). The 2022 PARSE PAD
(https://documents1.worldbank.org/curated/en/824551653593686389/pdf/Central-African-Republic-First-Phase-of-the-Electricity-Sector-Strengthening-and-Access-Project.pdf)
restates "Average Tariff US$14 cents/kWh" against a supply cost of US$0.20, and notes many flat-rate customers. One search
result described "tariffs unchanged since 1994". That came from a Republic of Congo document (E2C), not CAR, so I did not use it.

Recommendation: **import the row**. It is an all-customer average, not a household schedule, and its tax treatment
is unknown, so it is low confidence. Still, it is the country's own utility figure, restated in 2022, and
nothing newer exists. The Middle Africa mean it would replace is 65 XAF, so the change is modest. The rest-of-world research
left it out as "not residential-specific". That is a fair reason to keep the low confidence, but not to
prefer a regional mean.

## VA Vatican City: no household price; use Italy as proxy

Nothing new beyond the rest-of-world research (`gapfill-europe-small.md`). The Vatican is supplied from the Italian grid
(ACEA) under the Lateran arrangements and the Governorate pays. Its few hundred residents live in service
housing and are not billed per kWh on any published tariff. Many Vatican employees in fact live in
Rome and pay Italian tariffs.

Recommendation: a proxy row with **Italy's price**. The power is Italian, and the nearest real household
price is the one across the street. The current Southern Europe mean (€0.176) is about 40% below Italy (€0.297), for
no reason. Ready row (it has to be refreshed when Italy's Eurostat row is):

```
VA,0.2966,EUR,2025-12,,"proxy: Italy's household price (Eurostat nrg_pc_204 2025-S2 band DC, all taxes); Vatican residents are not billed on a published tariff",https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_204/default/table,"Eurostat: reuse authorised, source acknowledged",low,"No Vatican household tariff exists: supply comes from the Italian grid and the Governorate pays; Italy's price is used as the nearest real household price"
```

If the client can show "price as Italy" more cleanly (an alias to IT's resolved entry, which would also follow
Italy's live price), that is better than a copied row. It would be a code change, though, for one country, and SJ no longer needs one.

## PN Pitcairn: no verifiable tariff; keep the Polynesia mean

- About 40 residents. The island government runs a low-voltage grid from diesel generators, 06:00-22:00. There are 26 household
  accounts, the average household uses **320 kWh/month**, and households take 61% of the island's 150,000 kWh/year. The source is SPC
  RFQ 20/036, 2020, the solar PV hybrid design study
  (https://www.pcreee.org/sites/default/files/proc_notice/files/RFQ%2020_036-%20DESK%20STUDY%20TO%20DESIGN%20THE%20PITCAIRN%20ISLAND%20SOLAR%20PV%20HYBRID%20SYSTEM.pdf),
  which mentions "billing data" but gives no tariff.
- The only tariff seen is a 2013 schedule quoted in a search-engine summary: NZ$0.60 up to 210 units, 0.85 for
  211-250, 0.90 above 250. Its source page (an eng-tips forum thread) refused fetches, so it is
  unverified. At 320 kWh: 210 × 0.60 + 40 × 0.85 + 70 × 0.90 = 223 NZ$, which gives **0.70 NZD/kWh**.
- Wikipedia (uncited) says every home now has a solar system that covers over 95% of household use, so the
  2013 grid tariff may hardly apply any more.
- No government.pn tariff notice was found.

Recommendation: **keep the Polynesia mean (0.61 NZD)**. It is within about 15% of the unverified 2013 figure, and
a row resting on a source I could not open would be a guess with a URL. If a number is preferred
of its own, the 0.70 NZD above at low confidence is the candidate.

## KP North Korea: no per-kWh price

- Asiapress survey, 2026-09-08 (https://www.asiapress.org/rimjin-gang/2026/09/society-economy/price-survey-6/),
  from four cities in Ryanggang and North Hamgyong:
  - The **basic electricity charge is 650 won/month** everywhere, for 2-2.5 hours of supply a day.
  - Households that want about 6 more hours a day pay 25,000-30,000 won/month.
  - Appliances carry ownership fees.
  - Market rate: 10,000 won is about US$0.15 (2026-08-28), so about 66,700 KPW/USD.
- Meters are rare outside Pyongyang. The last per-kWh rates reported are Pyongyang 2017: 35 won/kWh, 350 above 100 kWh
  (RFA, https://www.rfa.org/english/news/korea/power-meters-11072017112708.html).
- There is no consumption figure, so no per-kWh price can be computed.

The currency is the second problem. The pipeline's KPW rate is the official one, about 146/EUR. The market rate is about
75,000/EUR, a 500x gap. Today's fallback shows 17.8 KPW/kWh. That is meaningless in won (a household pays 650 won a
month for its basic supply) and meaningless in EUR.

Recommendation: **no household price**. If the client can show "no published price", use that for KP.
Otherwise keep the Eastern Asia mean, but know that it is fiction. A won figure from the survey would be just as wrong
once converted at the official rate.

## AQ BV GS HM IO TF UM: no residents, no household price

- **AQ** Antarctica: research stations only, with power from each station's own generators.
- **BV** Bouvet Island (Norway): uninhabited.
- **GS** South Georgia and the South Sandwich Islands (UK): British Antarctic Survey and government staff at King Edward
  Point and Bird Island, no households.
- **HM** Heard Island and McDonald Islands (Australia): uninhabited.
- **IO** British Indian Ocean Territory: the Diego Garcia military base and contractors. There are no permanent
  residents; the Chagossians were removed. The UK–Mauritius sovereignty agreement does not change the
  price question.
- **TF** French Southern Territories: research and military staff at Kerguelen, Crozet and Amsterdam, and the
  Scattered Islands. No households.
- **UM** US Minor Outlying Islands:
  - Wake: military and contractors.
  - Midway: Fish and Wildlife staff.
  - Palmyra: Nature Conservancy staff.
  - The rest: uninhabited.

Nobody buys household electricity in any of these, so every number is invented. The administering
country's price (NO, GB, AU, FR, US) is no more true than the regional mean, though it is easier to defend
than BV and GS sitting in "South America" or IO and TF in "Eastern Africa".

Recommendation: **show "no household price"** for these seven if the client and `validate.py` allow a country
without a price. Otherwise **keep the current fallback** and don't build a proxy mechanism for places nobody
lives. Not worth the code.

## Open questions

1. YE: the YER exchange rate. Does config allow pinning a per-currency rate (about 600/EUR for the old rial), or should
   YE stay out of the regional means? Import the YE row only with one of the two.
2. Can a country carry no price at all ("no published price")? That is the honest answer for KP and the
   seven uninhabited territories. If not, they keep their means.
3. VA: a copied Italy row (ready above) or an alias to Italy's entry (code)?
4. KP's KPW rate has the same problem as YER, a 500x gap between official and market. It does not matter while KP has no row.
5. Unverified here:
   - SJ: whether Svalbardpris 2026 moved the 1.20 (no notice found).
   - YE: the date the 300 took effect, and the population share.
   - PN: the 2013 tiers.
