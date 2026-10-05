# Zoned countries: the United States, Canada and Russia (2026-10-04)

**Question.** Where do per-region household prices come from for the United
States, Canada and Russia, and what does each figure include?

| File | Topic |
|---|---|
| `us-household-taxes.md` | The state-by-state check of taxes households pay on top of EIA's price, the rule for what is added, and the corrections it found |
| `us-eia.md` | What EIA's residential average price includes (energy, delivery, fixed charges, franchise fees; most likely not household sales tax), licence (public domain), lag (~2 months) |
| `canada.md` | Canadian provinces and territories at 1,000 kWh/month, taxes and on-bill rebates included: sources compared (CER snapshot, Hydro-Québec comparison, utility tariffs, Statistics Canada CPI), 2025-26 changes, population |
| `canada-tariffs.md` | The eight rows rebuilt from utility tariffs, with each bill calculation |
| `russia.md` | Russian household tariffs per federal subject from 2026-10-01: FAS order 1130/25 caps, regional orders, Rosstat cross-check, the tariff choice, the excluded occupied territories |

**Decided.**
- **US:** EIA's monthly state figures are fetched on every run; the country
  average is EIA's own national figure. EIA's revenue includes taxes the
  utility pays but most likely not those levied on the household, so
  `config/household_taxes.csv` adds per state the sales tax, consumer
  excises (Illinois, DC, Virginia per kWh) and a typical local or city utility
  tax (an estimate). It was verified state by state against statutes and
  revenue departments on 2026-10-04 (four parallel passes; notes per row).
  Utility-level taxes already in rates (Ohio, Pennsylvania, Hawaii,
  Washington's state tax) are left out to avoid counting them twice. The
  national figure gets the states' taxes weighted by residential kWh sold:
  July 2026 $0.1831 -> $0.1898.
- **Canada:** no published national average exists, so the country average
  weights the 13 provinces and territories by Statistics Canada population at
  2026-07-01. Every row is computed from the utility's own published tariff
  (a public regulatory document; rates are facts). Eight rows first came from
  the CER snapshot (non-commercial terms) and Hydro-Québec's comparison (all
  rights reserved); `canada-tariffs.md` rebuilds them, each within 4.2% of
  the old figure. Ontario's row is due again after the 1 November reset.
- **Russia:** the standard urban single-rate tariff for homes without electric
  stoves (first consumption range; above-norm in the five regions with a
  social norm), VAT included. Only subjects with an ISO 3166-2:RU code. Crimea,
  Sevastopol and the occupied Donetsk, Luhansk, Zaporizhzhia and Kherson
  regions are left out, though the regulator lists them. The country average
  weights the 83 regions by Rosstat population at 1 January 2025 (no 2026
  regional estimate was published): 7.10 RUB/kWh. Rosstat's own all-household
  average was 5.46 in August 2026, before the 11.3% October rise and including
  cheaper rural and electric-stove tariffs.

**Rerun.** Russian tariffs change every 1 October: redo `russia.md`'s table
from the FAS caps and the regional orders it cites. The build script and raw
downloads used for the 2026 rows are not kept here.
