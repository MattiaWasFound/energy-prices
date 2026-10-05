# Research method: household electricity price per country (October 2026)

This is the instruction sheet the regional researchers worked from. Their
answers are the other files in this folder.

Goal: for each country or territory in a regional group, ONE figure: what a
typical household pays per kWh of electricity, all taxes and fees included
(energy, delivery, fixed/standing charges spread per kWh at the stated monthly
consumption, VAT/sales tax, levies; on-bill subsidies applied), in the currency
households are billed in, as current as possible.

Method, in order of preference:
1. The national regulator's or the dominant utility's published residential
   tariff (a public regulatory document; rates are facts). Compute the monthly
   bill at a stated typical consumption (the country's typical household use
   where it can be sourced, else 200 kWh/month for low-income countries and
   300 kWh/month otherwise; say which), add fixed charges and taxes, divide by
   kWh. For block tariffs this matters: show the arithmetic.
2. An official statistics office or regulator average residential price per kWh.
3. An openly licensed international dataset (e.g. a World Bank or
   regional-regulator table under CC BY).

No commercial tables: GlobalPetrolPrices, IEA paid data, Statista,
CallMePower, energy comparison sites. They may be used only to sanity-check,
never as the source.

Output per group:
- `<group>.csv` with columns
  `country,price,currency,as_of,consumption_kwh_month,includes,source_url,licence,confidence,note`
  (`as_of` = YYYY-MM the tariff is valid from or the data month; `licence` =
  the source's actual terms, or "utility/regulator tariff (public regulatory
  document; rates are facts)"; `confidence` high/medium/low). These are in
  `rows/`.
- `<group>.md`: per country a few lines of arithmetic and caveats, then three
  short sections:
  - "Currency": the ISO 4217 code households are billed in, where it is not
    obvious (dollarised economies, dual rates: CU, VE, LB, ZW, SS, IR, SY...),
    with a source.
  - "Zone candidates": any country where well-populated regions differ in
    household price by roughly 2x or more AND residents recognise a short list
    of regions (e.g. states or provinces). Named with the numbers, not built.
  - "Gaps": countries that could not be priced, and why.

Uninhabited territories are skipped (no price needed). Anything unverified is
marked low confidence rather than guessed. Every figure cites a real URL.
