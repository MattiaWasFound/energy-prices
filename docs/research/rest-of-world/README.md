# The rest of the world (2026-10-04)

**Question.** One household price per kWh, all taxes and fees included, for
every country not covered by `tariffs/` and `zoned-countries/` (193 codes, many
of them small territories), from sources whose licence allows republishing.

**Method.** `method.md` is the method every regional researcher followed: the
regulator's or dominant utility's published residential tariff, computed at a
stated monthly consumption (the country's own typical use where sourced, else
200 kWh for low-income and 300 kWh for other countries), with fixed charges and
taxes; else an official statistics or regulator average; never a commercial
table (GlobalPetrolPrices, IEA, Statista and comparison sites were at most a
sanity check). Six regional groups ran in parallel, then a gap-fill pass for
what the first pass could not reach.

**Files.** One write-up per group (arithmetic per country, then Currency,
Zone candidates and Gaps); `rows/` holds every research CSV as imported with
`tools/import_prices.py`. South America and Oceania came back as rows only:
their sources and confidence are in `rows/south-america-oceania.csv`.

**Result at the time.** 234 of 250 countries resolved from a published price
(plus 3 live and the rest averaged). Left on the regional or global average:
the uninhabited territories (AQ BV GS HM IO TF UM SJ, and PN with about 50
people), and four places with no usable figure: Central African Republic (only
a 2017 all-customer average exists), North Korea (no published tariff), Vatican
City (residents are not billed per kWh) and Yemen (the only grid tariff is in
Aden rials while the exchange-rate source quotes the Sana'a rate, and most
households buy from private generators). `zones-and-averages/` revisits these.

**Regional averages.** The fallback uses UN M49 regions (the intermediate region
where M49 has one, else the sub-region), as the plain mean in EUR of the
countries in it that resolved from live data or a table; Taiwan is placed in
Eastern Asia and Kosovo in Southern Europe. The global average is the plain mean
of every resolved country.

**Zone candidates found (named, not built, as the method asks):**

- **Mexico:** CFE's climate-zone tariffs (1 to 1F) differ about 3x in summer
  at the same consumption, and households in hot zones are subsidised.
- **Kazakhstan:** about 1.9x between the north and west (about 24 KZT) and
  Almaty, Kostanai and Akmola (38 to 45 KZT).
- **Iraq:** the Kurdistan Region pays about 7x the federal rate.
- **Somalia:** Mogadishu about 0.36 USD against about 1.00 in member states.
- **St Kitts and Nevis:** about 2.2x between the two islands since Nevis
  restored its fuel surcharge.
- Possible, unverified: Argentina (Buenos Aires against provincial utilities),
  China (provincial spread about 1.6 to 1.8x).

**Exchange-rate conventions to know about.** The job converts at official
reference rates (ECB, Frankfurter). That understates the euro price in
countries with a much weaker street rate: Cuba (official 24 CUP/USD, floating
695), Turkmenistan (about 10x), Myanmar, Venezuela, Iran, Lebanon (EDL bills in
USD, so the row is in USD), Syria (the redenominated pound).

**Rerun.** Re-research a country with the same method, write rows in its
format, and import them with `tools/import_prices.py <file.csv>`.
