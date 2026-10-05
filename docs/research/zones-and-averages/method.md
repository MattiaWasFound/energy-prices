# Research method: five more zoned countries and the thirteen averages (October 2026)

This is the instruction sheet the three researchers worked from, kept as written
except for paths. Their answers are `mexico.md`, `zones.md` and `averages.md`.

Zones were wanted for the five countries `rest-of-world/` named as clear zone
candidates (MX, KZ, IQ, SO, KN), and a fresh attempt at the thirteen places
that fall back to a regional or global average (AQ, BV, CF, GS, HM, IO, KP, PN,
SJ, TF, UM, VA, YE). Background: the project README's sections "How a price is
decided", "Config tables" and "Add zones to a country"; the method in
`rest-of-world/method.md`, whose source rules apply unchanged; and the
countries' notes in `rest-of-world/` (their "Zone candidates" and "Gaps"
sections already hold numbers and URLs: start from them, verify, don't redo).

The price: what a typical household pays per kWh, all taxes and fees included,
fixed charges spread per kWh at a stated monthly consumption, on-bill subsidies
applied, in the currency households are billed in. Show the arithmetic. No
commercial tables (GlobalPetrolPrices, Statista, comparison sites) except as a
sanity check. Unverified means low confidence, not a guess.

## Zones (groups `mexico` and `zones`)

The zone rule: well-populated regions differ in household price by roughly 2x
or more, and residents recognise a short list of regions. The client shows the
list under the country's `zone_label` and the user picks one. Per country:

- `zones.csv` rows: `country,id,name,area,weight,weight_source`, `area` empty.
  `id` is the ISO 3166-2 code where the zone is an ISO subdivision (KZ-ALA,
  KN-K), else `<CC>-<SHORT>` in capitals, explained in the notes. `name` is
  what residents call it, in the language they read on their bill (as RU uses
  Russian). `weight` is the zone's share of the country's population (or of
  households), summing to 1, with its source.
- `static_prices.csv` rows, one per zone: `country,zone,price,currency,as_of,source,licence,note`,
  `source` being the arithmetic plus ` | ` and URLs, `note` starting with the
  confidence and the consumption used.
- The `zone_label` (the word for "region" as residents would read it, e.g.
  "Prisområde", "Oblast'").
- Whether the country's existing national row should stay as the country
  average or be dropped so the average becomes the weighted zone mean. Say why.
- A short list of what you could not settle.

Country notes:

- **MX** (own group). CFE domestic tariffs 1, 1A to 1F are assigned by
  locality from summer temperature, and the gap is about 3x in summer. Decide
  between zones by tariff letter (printed on every bill) and zones by state
  (better known, but several states mix tariffs); recommend one with reasons.
  Prices are seasonal: give each zone's price over a whole year at that zone's
  typical consumption (summer months use more), and record the summer and
  winter figures in the note. Weights: households per tariff if CFE or SENER
  publish it, else population by locality mapped to tariffs. Note the DAC
  tariff and the 8% border IVA and how you treated them.
- **KZ.** Oblasts plus the three cities of republican significance; tariffs
  are set per region (zhkh24.kz, regional utilities, KREM orders). Almaty rose
  in September 2026. Tiered tariffs: use tier 2 at typical use, or say why not.
- **IQ.** Kurdistan Region (Runaki, 72 IQD for 1-400 kWh since May 2025)
  against federal Iraq (10 IQD block). Decide whether the zones are the two
  regions or governorates; two is likely right.
- **SO.** Banadir/Mogadishu and the federal member states (Jubaland,
  South West, Hirshabelle, Galmudug, Puntland) plus Somaliland, which runs its
  own utilities and which residents treat as its own region; name it
  neutrally ("Somaliland"). Private providers per city: use the main city's
  provider for each zone. Prices are billed in USD in most places; say where not.
- **KN.** St Kitts (SKELEC) and Nevis (NEVLEC). The open question from
  `rest-of-world/`: does SKELEC still have its fuel variation charge subsidised?
  Settle it if any source does.

## Averages (group `averages`)

Each of the thirteen gets one of:

- a country row in the `rest-of-world/` CSV format
  (`country,price,currency,as_of,consumption_kwh_month,includes,source_url,licence,confidence,note`),
  imported later with `tools/import_prices.py`; or
- "no household price": why (uninhabited, research staff only, military base,
  no published tariff), and whether a different fallback would be more honest
  than the UN M49 regional mean it gets now (for example the supplying
  country's price for VA, Norway's Longyearbyen tariff for SJ), with a
  recommendation.

Notes: SJ has about 2,500 residents in Longyearbyen with a local utility (the
lokalstyre). PN has about 40 residents on a diesel grid run by the island
government. VA is supplied from the Italian grid. CF (ENERCA), YE (Aden grid
against private generators in Sana'a, about 40x apart: pick what a typical
household pays and explain) and KP (probably nothing published) were gaps in
`rest-of-world/`; see `gapfill-africa-gaps.md`, `gapfill-world-gaps.md`,
`asia-east.md`.

## Output, every group

- `<group>.csv` (or `zones.csv` + `static_prices.csv` for the zone groups),
- `<group>.md`: per country the arithmetic, sources, caveats, and the
  decisions asked for above.
