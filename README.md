# energy-prices

The household electricity price per kWh, all taxes and fees included, for
every country, in one JSON file rebuilt every day:

- **Data:** <https://mattiawasfound.github.io/energy-prices/v1/prices.json>
- **Format:** [`schema/prices.schema.json`](schema/prices.schema.json), also at
  <https://mattiawasfound.github.io/energy-prices/v1/prices.schema.json>
- **Map:** <https://mattiawasfound.github.io/energy-prices/>, every country and
  how its price was worked out

A client downloads the file once per session, picks a country (and for a few
countries a zone), and reads the price for the current time. Nothing runs per
request, there is no API key and no rate limit.

Coverage today: 250 countries and territories. 29 European countries are live,
in 15-minute slots from the day-ahead auction; 211 come from published
regulator, utility or statistics tables; 2 take their region's average; 7
uninhabited territories carry a labelled guess; North Korea has no price.
Every entry says which, in its `basis`. An example output is in
[`samples/`](samples/).

**These are rough household figures, not tariffs.** A real bill depends on
the supplier, the contract, the consumption and local fees. Check an entry's
`basis` and its source before relying on it.

## Run it locally

```
uv sync
ENTSOE_TOKEN=… EIA_API_KEY=… uv run python -m energyprices generate --out out
bin/verify
```

`generate` fetches, builds, validates and writes `out/prices.json`. It reads
the previous `out/prices.json` first, so a failed source carries its entries
forward. Without `ENTSOE_TOKEN` it still runs: the areas Energi Data Service
carries (DK1, DK2, DE-LU, NO2, SE3, SE4) are live and the rest fall back.

Options:

- `--now 2026-10-05T12:00:00Z` pretends it is that time.
- `--fail entsoe,eds,eia,fx` simulates failing sources, to see carry-forward work.

Exit status 1 means validation failed and nothing was written; the problems
are listed on stderr. Every carried-forward or fallen-back entry is listed on
stderr too.

`bin/verify` runs the tests: parsers against recorded fixtures, the build
rules against a small test config in `tests/config/`, the schema itself, and
the shipped `config/` tables' cross-checks. CI runs the same command.

## Browse a file

`uv run python tools/browse.py` writes `out/browse.html`: one self-contained
page (no network) with a world map coloured by how each country is priced or
by its price now, the live 15-minute series per country and zone, how each
figure was computed (add-on, VAT, weights, sources), and "What the research
found": the cards come from [`docs/findings.md`](docs/findings.md), one tagged
section per finding, parsed by the tool (the page lays them out; it never
renders markdown). The page source is `browse/index.html`; the published copy
is the site's front page. The map
is Natural Earth via world-atlas 50m (ISC licence, `browse/LICENSE-world-atlas`),
matched to ISO codes through `browse/iso-numeric.csv` (datasets/country-codes, PDDL).

## How a price is decided

`energyprices/build.py` resolves every country through one chain and records
the step in the entry's `basis`:

1. **`day-ahead`** (precision `live`), where `config/areas.csv` lists a
   bidding area for the country. Per slot:
   `(spot + add-on) × (1 + VAT)`, in the country's currency, with spot
   converted from EUR/MWh at today's rate. A support scheme
   (`support_threshold`, `support_share`) first takes its share of spot above
   the threshold, which is how Norway's strømstøtte is modelled. A country
   with several areas gets the population-weighted mean of its areas' final
   prices. `flat` is the mean of the last complete delivery day.
   When the sources fail, the entry from the previous file is carried forward,
   its series trimmed to start today (or dropped once it no longer reaches
   today, leaving `flat`).
2. **`country-table`**: `config/static_prices.csv`. Also used for a live
   country listed in `settings.toml` `table_instead_of_live`.
3. **`regional-average`**: the mean, in EUR, of the countries in the same
   UN M49 sub-region that resolved at step 1 or 2.
4. **`global-average`**: the mean of every country that resolved at 1 or 2.

Two lists in `settings.toml` skip the chain, for places with no published
household price. Both have no zones, stay out of the regional and global
means, and carry a `reason` (English, for display) that the client should show:

- **`educated-guess`** (precision `estimated`), from `[educated_guess]`: a
  price, its currency and the reason it is defensible. Used where nobody lives:
  South Georgia takes the Falklands' price, and the six other uninhabited
  territories take about what remote islands on diesel pay (0.50 EUR).
- **`no-published-price`** (precision `none`), from `[no_published_price]`:
  no `flat` at all, where even a guess would mislead. Only North Korea: its
  fees are not per kWh, and its official won rate is about 500 times the
  market's. A client must handle an entry without a price.

### Known gaps

- **Yemen stays on the Western Asia average, on purpose.** A Sana'a household
  pays about 300 rials/kWh on the public grid (an Aden household 19), but Yemen
  has two rials under one code, YER, and the rate the job gets (Frankfurter,
  about 266 per euro) matches neither: the Sana'a old rial trades near 600
  per euro and the Aden new rial near 1,800. Imported, 300 YER would read as
  €1.13 instead of about €0.50 and lift the Western Asia mean. The euro value
  of Yemen's average is right; its figure in YER is converted at the same
  wrong rate, so it is too low in local terms. Revisit if a source publishes
  a usable YER rate, or if config gains a pinned rate per currency.
- **Ireland** is priced from the table while ENTSO-E publishes nothing for
  the Irish market (since 2026-09-29); it goes live again on its own.
- **Official exchange rates** flatter prices where the street rate is far
  weaker (Cuba, Turkmenistan, Myanmar, Venezuela, Iran, Lebanon, Syria); see
  `docs/findings.md`.

Delivery days run 00:00 to 24:00 Central European time for every European
zone, so a series starts at 22:00 or 23:00 UTC and a day has 92, 96 or 100
quarter-hours. Gaps of up to two hours inside a day are filled by carrying
the previous slot forward; a longer gap makes the day incomplete.

Before anything is written, `energyprices/validate.py` checks the schema, the
size limit, that every configured country is present, that every currency has
a rate, that every series starts at today's delivery day and ends on a day
boundary, and that every price is inside the bounds in `settings.toml`.

## Config tables

All in `config/`, all hand-maintained, cross-checked by `config.load()` so a
bad edit fails before any fetch.

| File | One row per | Columns |
|---|---|---|
| `countries.csv` | country in the file | `code` (ISO 3166-1 alpha-2, or XK), `name`, `currency` (ISO 4217, what households are billed in), `region` (UN M49 sub-region), `zone_label` (empty unless the country has zones) |
| `areas.csv` | live bidding area and country | `area`, `country`, `weight` (population share within the country; a country's weights sum to 1), `weight_source`, `entsoe_eic`, `eds_area` (Energi Data Service backup, if it carries the area) |
| `zones.csv` | zone shown in the client, in display order | `country`, `id`, `name`, `area` (live zones) or `weight` + `weight_source` (static zones) |
| `tariffs.csv` | live country, plus area overrides | `scope` (country code, or an area id whose non-empty fields override the country row), `currency`, `addon` (per kWh, excl. VAT), `vat` (fraction), `support_threshold`, `support_share`, `fixed_energy` (the energy price an option uses in place of spot), `source`, `as_of`, `confidence`, `note` |
| `static_prices.csv` | country or zone with a published price | `country`, `zone` (empty for the country), `price` (per kWh, all-in), `currency`, `as_of` (YYYY-MM), `source`, `licence`, `note` |
| `household_taxes.csv` | US state (zones of a `fetched_static` country) | `zone`, `rate` (state tax on the household bill), `local_rate` (typical local or city utility tax, an estimate), `per_kwh` (a per-kWh consumer tax, USD), `note` (statute), `confidence`. Added to EIA's price, which excludes taxes levied on the household; utility-level taxes already in rates are left out |
| `settings.toml` | | `[[options]]` (prices the user can pick, e.g. Norgespris), `table_instead_of_live`, `fetched_static` (countries whose table rows a source supplies at run time: the US from EIA), sanity `bounds` |

### Add a country

1. Add a row to `countries.csv`.
2. If a published household price exists, add a `static_prices.csv` row with
   its source, month and licence. Otherwise the country takes its region's
   average.
3. For live prices: add its bidding area(s) to `areas.csv` with population
   weights and a tariff row to `tariffs.csv`.
4. `bin/verify`, then `generate`.

### Add zones to a country

Zones are config only. Set the country's `zone_label`, then add `zones.csv`
rows in display order:

- **Live zones** name an area from `areas.csv`. The country average is the
  population-weighted mean of the areas, using the `areas.csv` weights.
- **Static zones** leave `area` empty and need a `static_prices.csv` row per
  zone. The country average is the country's own `static_prices.csv` row if
  there is one (the US uses its published national average), otherwise the
  zones' mean weighted by the `weight` column.

The rule for adding zones: well-populated regions differ in price by roughly
two times or more, and there is a short list of regions residents recognise.

### Update the static table

`uv run python tools/eurostat.py --period 2026-S1` prints fresh Eurostat rows
for every European country and the add-on baseline for every live country.
Paste the rows you want into `static_prices.csv`; keep the non-Eurostat rows
(their `source` says where they came from). The `VA` row is a copy of the `IT` row
(Vatican City is supplied from the Italian grid): update both together. Eurostat publishes each semester
about nine months after it ends.

`uv run python tools/import_prices.py rows.csv` imports researched rows (the
columns are in the tool's docstring) as country rows, replacing the existing
ones for those countries.

### Add-ons and VAT (live countries)

Each live country's add-on is Eurostat's household price excluding VAT (band
DC, 2 500 to 4 999 kWh a year) minus the same semester's mean wholesale price
(Ember), plus the tax and levy changes since that semester. The derivation and
the per-country changes are in the `source` and `note` columns of
`tariffs.csv`. The `note` column of `tariffs.csv` shows the arithmetic for each row. Because the
baseline is an average over the band, it includes standing charges spread per
kWh; it is a rough household figure, not a tariff.

### Options the user can pick (Norgespris)

A country can carry `options`: alternative prices the client offers beside the
default, each repeating the country's average and zones with the same ids.
`settings.toml` `[[options]]` declares them. The one today is Norway's
Norgespris: the NO tariff row's `fixed_energy` (0.40 NOK excl. VAT) in place
of spot, plus the add-on and VAT (none in NO4), labelled `country-table`.
The default stays spot with strømstøtte. About 59% of Norwegian households
had chosen Norgespris by August 2026 (Elhub).

### Regulated countries

In several live countries households are on regulated tariffs that do not
follow the day-ahead price (BG, CH, FR, HR, HU, MK, ME, PL, RS, SK). Their
add-ons come out small or negative, because the regulated price sits near or
below wholesale. Listing a country in `table_instead_of_live` prices it from
`static_prices.csv` instead.

## Sources

| Source | Used for | Licence | Updates |
|---|---|---|---|
| ENTSO-E Transparency Platform, A44 day-ahead prices | live prices, every European bidding zone | ENTSO-E terms of use: name the "ENTSO-E Transparency Platform" as source. Day-ahead prices are not on its CC BY list; the power exchanges own them. This file publishes household prices derived from them | daily, ~13:00 CET for the next day |
| Energi Data Service (Energinet) `DayAheadPrices` | backup for DK1, DK2, DE-LU, NO2, SE3, SE4 | Energinet's terms of use for Energi Data Service (attribution); not confirmed in writing yet, and the prices themselves come from the exchanges, as with ENTSO-E | daily, with the auction |
| ECB euro reference rates | exchange rates for the ~30 currencies it quotes | reuse with the ECB cited as source | TARGET working days ~16:00 CET |
| Frankfurter v2 | exchange rates for every other currency | code MIT; each rate under its central bank's terms (frankfurter.dev/license) | daily |
| US EIA API v2 `electricity/retail-sales`, residential | US national average and the 50 states plus DC, fetched every run, plus `household_taxes.csv` (the national figure gets the states' taxes weighted by residential kWh sold); a failure carries the previous US entries forward | US government work, public domain | monthly, about two months behind |
| Eurostat nrg_pc_204 | static European prices; add-on baseline | reuse authorised with the source acknowledged | twice a year |
| Ember European wholesale prices | add-on baseline (wholesale mean) | CC BY 4.0 | monthly (in practice near daily) |
| Utility tariffs (13 Canadian utilities), FAS order 1130/25 and regional tariff orders (Russia), state tax statutes (US) | Canadian provinces, Russian regions, US household taxes | public regulatory documents and official acts; rates are facts | yearly (Russia every 1 October, Ontario every 1 November) |
| Regulator and utility tariffs for the rest of the world (about 190 documents, one per row of `static_prices.csv`) | every country outside Europe and the zoned three | public regulatory documents; rates are facts; a few CC BY national datasets (ACCC, MBIE) | per row |
| National regulators and statistics (ElCom, Ofgem, ANRE, ERE, Ukraine's PSO act) | static rows outside Eurostat or newer than it | per row in `static_prices.csv` | per row |
| SCB, Elhub, ISTAT, Statistics Denmark | population weights | per row in `areas.csv` | yearly |

## Publishing

`.github/workflows/publish.yml` runs every day at 12:20 UTC, after the
day-ahead results (published about 13:00 Central European time in winter, an
hour earlier in UTC terms in summer), on every push to `main`, and on demand
from the Actions tab. It downloads the published `prices.json` first,
so a failed source carries the previous entries forward, then runs
`generate`, builds the map page, and deploys `site/` to GitHub Pages:

| Path | What |
|---|---|
| `/` | the map page (`tools/browse.py`) |
| `/v1/prices.json` | the data |
| `/v1/prices.schema.json` | the schema |

If validation fails the run fails and the previous deployment stays up. Each
run also re-enables its own workflow, because GitHub disables scheduled
workflows in a public repository after 60 days without a commit.

### API keys

The job needs two keys, stored as repository secrets (Settings, Secrets and
variables, Actions):

- **`ENTSOE_TOKEN`.** Register at <https://transparency.entsoe.eu> and verify
  the email. Then email `transparency@entsoe.eu` with the subject "RESTful API
  access" and your registered email address in the body. Access comes within
  about three working days; then generate the token under My Account Settings.
- **`EIA_API_KEY`.** Register at <https://www.eia.gov/opendata/register.php>;
  the key arrives by email.

They never go into the repository, a log or the output file;
`energyprices/http.py` keeps request URLs (which carry the ENTSO-E token) out
of every error message.

## Licence

The code is MIT ([`LICENSE`](LICENSE)). The data (`prices.json` and the tables
in `config/`) is CC BY 4.0: credit "energy-prices" with a link to this
repository, and pass on the source credits below, which their own terms
require. In particular, day-ahead prices come from the ENTSO-E Transparency
Platform (name it as the source), exchange rates from the ECB and
Frankfurter, and US prices from the US EIA. The map is Natural Earth via
world-atlas (ISC).
