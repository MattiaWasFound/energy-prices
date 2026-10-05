# Zones for five more countries, and the thirteen averages (2026-10-05)

**Question.** `rest-of-world/` named MX, KZ, IQ, SO and KN as meeting the zone
rule and left 13 places on regional or global averages. Should those five get
zones, and can the 13 be priced after all?

**How.** Three researchers followed `method.md`: `mexico`, `zones` (KZ, IQ,
SO, KN) and `averages`. Their records are `mexico.md`, `zones.md` and
`averages.md`; the rows as delivered are in `rows/`. Downloaded pages and PDFs
(about 180 MB for Mexico) are not kept here.

**Decided.**
- KZ (20 regions), IQ (2), SO (7) and KN (2) got static zones; each national
  row was dropped so the average is the population-weighted zone mean.
- MX got no zones: at each tariff zone's typical use the yearly price spans
  only 1.17 to 1.35 MXN/kWh, short of the 2x rule. Its national row is now
  1.327 MXN/kWh at 140 kWh a month. The zone rows are ready in
  `rows/mexico/` should that change; the zone rule says no.
- SJ (Svalbard Energi, 1.20 NOK) and CF (ENERCA average, 83 XAF, low) were
  priced. The CF research row cited a mismatched World Bank URL; the import
  cites the 2022 CAR project document instead.
- YE stays on the regional average, documented (README "Known gaps";
  `averages.md`). VA copies Italy's row. SO and LB are priced in USD.
- The seven uninhabited territories get an `educated-guess` price rather than
  an average: GS the Falklands' 0.35 GBP, the rest 0.50 EUR, the remote-island
  diesel range. KP (North Korea) gets `no-published-price`, with the reason.
  PN stays on the average (its 2013 tariff can't be verified).

**Rerun.** `rows/zones/build.py` regenerates the KZ/IQ/SO/KN rows;
`rows/mexico/calc.py` reproduces `rows/mexico/results.txt` (its input pages are
not kept here; the rates are typed into the script). Import country rows with
`tools/import_prices.py`; zone rows are copied into `config/zones.csv` and
`config/static_prices.csv`.
