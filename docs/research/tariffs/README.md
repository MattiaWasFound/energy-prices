# Sources, add-ons, VAT and weights for the live countries (2026-10-04)

**Question.** What does a household in each European country pay per kWh, as
"day-ahead spot + fixed add-on, times VAT", and where do the inputs come from?

**What was done.** Parallel research on 2026-10-04, one file per topic:

| File | Topic |
|---|---|
| `entsoe.md` | ENTSO-E API as of 2026: endpoint, A44 format, auction sequences, 15/30/60-minute zones, EIC codes, token procedure, licence |
| `reference.md` | Exchange-rate sources and licences (ECB + Frankfurter chosen), ISO 3166 list, UN M49 regions, currencies, Ember, Eurostat |
| `nordic.md` | SE/NO zone weights (SCB, Elhub), Norgespris terms and uptake, strømstøtte, Nordic taxes and grid fees |
| `weights-it-dk.md` | Italy and Denmark zone weights (ISTAT, Statistics Denmark); Italian households pay the national PUN Index |
| `tax-changes-group1..6.md` | Per country: VAT on household electricity in 2026, tax and levy changes since 2025, spot exposure, non-EU prices |

**How the add-on was derived.** `tools/eurostat.py --period 2025-S2` prints
Eurostat's household price excluding VAT (band DC) minus Ember's mean wholesale
price over the same months, per country, in national currency. Then each
`config/tariffs.csv` row adds the changes since that semester from the
tax-changes files, skipping changes the 2025-S2 baseline already contains
(Romania's cap ending 2025-07, Norway's 2025 elavgift steps, part of Croatia's
2025-11 rise, half of Serbia's 2025-10 rise). The arithmetic is in each row's
`note`.

Results that need judgement:

- **Negative or near-zero add-ons** in HU, RS, ME, MK, BG, HR: households are on
  regulated prices at or below wholesale. The average comes out right; the
  slot-to-slot variation does not exist for those households.
- **Norway's** Eurostat baseline (1.31 NOK) is high next to a bottom-up estimate
  for a typical 16 MWh home (~0.6 NOK): band DC is a small consumer, whose
  fixed charges spread over fewer kWh. Kept for consistency with every other
  country.
- **Denmark** checks out bottom-up: 0.63 DKK against ~0.65 from elafgift 0.008 +
  Energinet 0.115 + DSO ToU mean ~0.3 + subscriptions and supplier markup.
- **Portugal's** VAT is the effective rate (14.8%, Eurostat ratio), because the
  6% band covers the first kWh of a typical bill.
- **Switzerland, Montenegro, North Macedonia** have no complete Ember or Eurostat
  pair; see their rows.

**Decided.** Live prices for every zone the sources cover, with a
`table_instead_of_live` switch in `config/settings.toml` for the regulated
countries, left empty. Norway defaults to spot with strømstøtte; Norgespris is
an option the user can pick (README, "Options the user can pick").

**Rerun.** `uv run python tools/eurostat.py --period <YYYY-Sn>` for the
baseline; the research itself is a dated snapshot and is redone by hand.
Bulky downloads (Ember daily CSV, M49 HTML, CLDR XML, sample API responses)
are not kept here.
