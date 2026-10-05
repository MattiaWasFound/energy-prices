# Reference data for the household electricity price job

Researched 2026-10-04. Every sample named below was fetched that day; the copies are not kept here.

Context: the output JSON is published, so every source has to allow **public redistribution of derived
values**.

---

## 1. Exchange rates

Target: every current tender currency used for household billing. CLDR gives **153 distinct currencies** across the
249 ISO 3166-1 codes plus XK (see section 4). Coverage below is measured against those 153, from the samples
fetched today.

| Source | URL | Coverage of the 153 | Update | Key | Licence / terms |
|---|---|---|---|---|---|
| **Frankfurter v2** (blend of 104 central banks and official sources) | `https://api.frankfurter.dev/v2/rates?base=USD` (add `&expand=providers` for provenance, `&providers=ECB` for a single source) | **153/153** (165 quotes in total, including metals and XDR) | daily (142 of 165 quotes dated 2026-10-04, the rest 2026-10-02) | none | Code MIT. Data: "Frankfurter doesn't own the rates, so it can't give you rights the provider doesn't. If a provider publishes terms of use, they apply." Also: "Blended rates are Frankfurter's own calculation, not an official rate from any institution." FAQ: "Is the API free for commercial use? Yes. The rates themselves fall under each provider's terms." https://frankfurter.dev/license/ |
| Frankfurter v1 (ECB only) | `https://api.frankfurter.dev/v1/latest?base=USD` | 30 | ECB working days | none | Deprecated but "remains available indefinitely". ECB terms apply. |
| **ECB euro reference rates** | `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml` | **30/153** | about 16:00 CET on TARGET days | none | "When such information is distributed or reproduced, it must appear accurately and the ECB must be cited as the source." Rates are "for information purposes only". https://www.ecb.europa.eu/services/using-our-site/disclaimer/html/index.en.html |
| **open.er-api.com** (ExchangeRate-API, open access) | `https://open.er-api.com/v6/latest/USD` | 152/153 (no KPW); 166 codes | daily (`time_next_update_utc` in the payload) | none | Attribution is required: `<a href="https://www.exchangerate-api.com">Rates By Exchange Rate API</a>` (https://www.exchangerate-api.com/docs/free). The terms forbid redistribution: "This license does not permit re-distribution of our data." and "data gathered from our API cannot be re-distributed - caching is for customer end-use only." https://www.exchangerate-api.com/terms. Rate limit: no throttling at about one request an hour; a client that exceeds the limit is blocked for 20 minutes. |
| fawazahmed0/exchange-api | `https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json`, fallback `https://latest.currency-api.pages.dev/v1/currencies/usd.json` | 153/153 (339 codes including crypto) | daily | none | Repo licence CC0-1.0, but it **does not name its upstream sources**, so the CC0 grant covers the repo and not necessarily the rates. **Data-quality failure seen today:** SYP = 13,009 per USD, the pre-2026 pound. Syria dropped two zeros on 2026-01-01 and kept the code SYP; the other sources show about 122. KPW is 900 here against 130 elsewhere. |
| IMF representative rates | `https://www.imf.org/external/np/fin/data/rms_mth.aspx?SelectDate=YYYY-MM-DD&reportType=REP` (HTML) | about 50 to 60 currencies | daily, published with a lag | none | IMF terms: content is "All Rights Reserved". Personal, noncommercial use only, "without any right to resell, redistribute, compile, or create derivative works". "For any potential commercial reuse of IMF Data, please email copyright@imf.org" (https://www.imf.org/en/about/copyright-and-terms; the page returns 403 to bots, so these quotes come from search snippets). **Not usable.** |
| World Bank `PA.NUS.FCRF` (official rate, LCU per USD, period average) | `https://api.worldbank.org/v2/country/all/indicator/PA.NUS.FCRF?format=json&mrv=1` | 186 economies with a value | **annual**; latest is 2025 (updated 2026-07-13) | none | CC BY 4.0 (https://datacatalog.worldbank.org/public-licenses). Too stale for daily conversion. Useful only as a sanity bound. |
| Fed H.10 | `https://www.federalreserve.gov/datadownload/Output.aspx?rel=H10&series=60f32914ab61dfab590e0e470153e3ae&lastobs=10&filetype=csv&label=include&layout=seriescolumn` | 23 | weekly release of daily noon rates | none | "Unless otherwise indicated, information on the Board's website is in the public domain and may be copied and distributed without permission." (https://www.federalreserve.gov/disclaimer.htm). Coverage is too small. |
| UN operational rates of exchange | https://treasury.un.org/operationalrates/default.php | nearly all currencies | monthly | none | UN site terms: "personal, non-commercial use, without any right to resell or redistribute". Use only as a manual cross-check. |

### Recommendation

- **Primary: Frankfurter v2** (`/v2/rates?base=EUR&expand=providers`). It is the only free, keyless source that covers
  all 153 billing currencies with traceable official provenance. It also excludes outliers: today it dropped Cuba's
  BCC "informal market rate" of 695 and kept the official 24, and it dropped BOI/CBKKW's 102k for LBP and kept BDL's
  89,500.
  Licence position: every number is a central-bank reference rate. Most providers publish no terms, and the ones that
  do (ECB, BoE, BoC, RBA and others) allow reuse with attribution. The output file publishes **converted prices, not a
  rate table**, which is a derived work. To stay clean:
  1. credit "Exchange rates: Frankfurter (frankfurter.dev), from central-bank reference rates" in the output metadata;
  2. if the output file also carries the rate used per currency, keep that to the one rate per currency actually used.
     Do not publish a full FX feed.
  The project can be self-hosted (`docker run lineofflight/frankfurter`) if the public instance disappears.
- **Fallback for the 30 major currencies: ECB eurofxref-daily.xml.** Its licence is unambiguous (cite the ECB). If
  Frankfurter is down, convert the ECB-covered currencies and carry the last good Frankfurter rate for the rest, with
  a `rate_date` per currency. Persist the last good rates in the repo or job state for this.
- **Do not use open.er-api.com.** Its terms forbid redistribution, and a public file of prices converted daily at its
  rates comes close to that. Its required attribution link would also have to go on "the pages you're using these
  rates with".
- **Do not use fawazahmed0.** The rates have unknown provenance and today's SYP is 100x wrong.
- Per-currency staleness guard: Frankfurter returns a `date` per quote. Flag any quote more than about 7 days older
  than the run.

### Tricky currencies (what the sources say today, per USD)

- **CUP (Cuba):** the official rate is 24. The BCC's floating "informal market" rate, published since 2025-12-19, is
  695. Households pay UNE in CUP. Converting at 24 overstates the USD price roughly 29x compared with the street rate.
  Decide explicitly, or flag Cuba as "official rate".
- **LBP (Lebanon):** BDL 89,500, which is the rate at which EDL's USD-indexed tariffs are billed.
- **VES (Venezuela):** BCV 866.6. **ZWG (Zimbabwe):** only BDI and NBP quote it, at 26.85. **SSP:** only BDI and
  NBP. **IRR:** sources spread from 1.31M to 1.76M (official and market tiers). **BWP:** 13.04 to 14.14 across
  providers. The blend gives 13.59, against 14.17 on open.er-api.
- **SYP:** post-redenomination, about 122. Make sure any historical tariff in old SYP is divided by 100.

Samples: `ecb-eurofxref-daily.xml`, `frankfurter-latest.json` and `frankfurter-currencies.json` (v1),
`frankfurter-v2-v2_rates.json` (EUR base), `frankfurter-v2-v2_rates_base_USD.json`,
`frankfurter-v2-rates-usd-expand-providers.json`, `frankfurter-v2-v2_currencies.json`,
`frankfurter-v2-v2_providers.json` (104 providers, each with `terms_url`), `open-er-api-usd.json`, `fawaz-usd.json`,
`fawaz-usd-pagesdev.json`, `fawaz-currencies.json`, `worldbank-PA.NUS.FCRF-sample.json`, `fed-h10-sample.csv`,
`imf-rms-sample.html`.

---

## 2. ISO 3166-1 alpha-2 list (249 codes, plus XK)

| Source | URL | Count | Licence |
|---|---|---|---|
| **Debian iso-codes** (recommended) | https://salsa.debian.org/iso-codes-team/iso-codes/-/raw/main/data/iso_3166-1.json | 249 | `REUSE.toml`: `path = "data/*json"`, `SPDX-License-Identifier = "LGPL-2.1-or-later"`. Shipping the JSON as a data file is fine. LGPL only places obligations on modifications of the library itself, so keep the file unmodified and add XK in code. |
| datasets/country-codes (DataHub) | https://raw.githubusercontent.com/datasets/country-codes/main/data/country-codes.csv | 249 | "licensed by its maintainers under the Public Domain Dedication and License" (PDDL). Bundles M49 regions, ISO 4217 and the UNTERM names. Auto-updated (last commit 2026-10-01). The README warns: "ISO makes the list of alpha-2 country codes available for internal use and non-commercial purposes free of charge." |
| ISO OBP | https://www.iso.org/obp | n/a | Not machine-readable for reuse, and the ISO terms restrict it. Skip. |

The code list itself is a set of facts and every open source republishes it. Use Debian as the canonical list and
append `XK` (Kosovo, a user-assigned code also used by Eurostat, the EU and CLDR).

Files: `iso_3166-1.debian-iso-codes.json`, `country-codes.datasets.csv`.

---

## 3. World regions: UN M49

- **Official page:** https://unstats.un.org/unsd/methodology/m49/overview/. The "Download" buttons are client-side
  DataTables exports. The full table is embedded in the HTML as `<table id="downloadTableEN">`, so the job (or a
  one-off script) can parse the page. There is no static CSV URL. I parsed it into **`m49-unsd-overview-en.csv`**:
  248 rows with columns Global/Region/Sub-region/Intermediate codes and names, M49 code, ISO alpha-2/alpha-3,
  LDC/LLDC/SIDS, and Developed/Developing. Raw page: `m49-overview.html`.
- **Licence:** the page carries only the generic UN site terms (https://www.un.org/en/about-us/terms-of-use): "for
  the User's personal, non-commercial use, without any right to resell or redistribute them or to compile or create
  derivative works therefrom". In practice M49 is a public statistical standard and is republished widely; for
  example, datasets/country-codes republishes it under PDDL. Two lower-risk options: vendor the mapping (codes to
  region names, a list of facts) in the repo and publish only region names and averages with the citation
  "regions: UN M49"; or take the same columns from the PDDL `country-codes.csv`.
- **Gaps compared with ISO 3166-1 plus XK:**
  - **TW**: not in M49. Assign Asia (142), Eastern Asia (030). datasets/country-codes does the same.
  - **XK**: not in M49 (it is within Serbia's entry). Assign Europe (150), Southern Europe (039), with RS, ME, MK, AL.
  - **AQ Antarctica**: listed, but under "World" only, with no region. Exclude it from regional averages.
  - Every other ISO code (BV, HM, GS, IO, TF, UM, PS, AX, SJ and so on) has a full region in M49.
- Choice of level: M49 sub-regions are uneven. "Latin America and the Caribbean" is one sub-region, while "Northern
  America" is separate. Regions (5) or sub-regions (17) are the usual choice for averages.
- **Alternative with a clean licence: World Bank regions**, CC BY 4.0, from
  `https://api.worldbank.org/v2/country?format=json&per_page=400`. It
  has 7 regions and 217 economies including XK, but it **misses 34 ISO codes, including TW** and most territories.
  M49 is the better fit.

A draft joined table (not kept here) had 250 rows with the M49 region, the TW/XK overrides, CLDR
currencies, the datasets/country-codes currency, and whether Frankfurter v2 covers the currency.

---

## 4. Country to ISO 4217 billing currency

| Source | URL | Licence | Notes |
|---|---|---|---|
| **CLDR supplemental `currencyData`** (recommended) | JSON: https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/cldr-core/supplemental/currencyData.json · XML: https://raw.githubusercontent.com/unicode-org/cldr/main/common/supplemental/supplementalData.xml | Unicode License v3, a permissive MIT-style licence ("All other content in this repo is released under UNICODE LICENSE V3"; only the UTS #35 spec text is restricted) | CLDR 48. Each territory lists currencies with `_from`/`_to`/`_tender`. "Current" means no `_to` and `_tender` not equal to `false`. Includes **XK** (EUR). |
| ISO 4217 List One (SIX, the maintenance agency) | https://www.six-group.com/dam/download/financial-information/data-center/iso-currrency/lists/list-one.xml | No explicit reuse licence. A free public download from the maintenance agency. | Published 2026-09-17. 280 entries, keyed by **country name**, not by code, so it needs name matching. Good as an audit of CLDR. |
| datasets/country-codes `ISO4217-currency_alphabetic_code` | (see section 2) | PDDL | Comma-separated when there are several (for example NA = "NAD,ZAR"). |
| Debian `iso_4217.json` | https://salsa.debian.org/iso-codes-team/iso-codes/-/raw/main/data/iso_4217.json | LGPL-2.1+ | Currency names and codes only, with no country mapping. |

Running the CLDR rule over 250 codes gives exactly one current tender currency for 242 of them, and **153 distinct
currencies**. The cases that need an explicit pick (hardcode a small override table in the job):

| Code | CLDR / SIX say | Bill households in | Note |
|---|---|---|---|
| BG | EUR from 2026-01-01; BGN ended 2026-01-31 (SIX: EUR) | **EUR** | Eurostat NAC for 2025 semesters is still **BGN**. Convert before mixing it with 2026 data (fixed rate 1.95583). |
| HR | EUR from 2023-01-01 | EUR | Already EUR in Eurostat. |
| ME, XK | EUR (unilateral use) | EUR | Eurostat NAC = EUR for both. |
| AD, MC, SM, VA | EUR (monetary agreements) | EUR | |
| EC, SV | USD (SIX also lists SVC for SV) | USD | |
| PA | PAB + USD | **USD** (PAB is pegged 1:1, coins only) | |
| ZW | ZWG (from 2024-06-25) + USD | **ZWG**, with USD widely used | ZESA tariffs are set in ZWG, and prepaid power can be bought in USD. FX coverage of ZWG is thin (2 providers). |
| VE | VES (VED tender=false) | VES | |
| LB | LBP | LBP | EDL tariffs are USD-indexed and billed in LBP at the BDL rate (89,500). |
| CU | CUP | CUP | See the FX tier problem above. |
| HT | HTG + USD | HTG | |
| BT | BTN + INR | BTN (pegged to INR) | |
| LS / NA / SZ | LSL+ZAR / NAD+ZAR / SZL | LSL / NAD / SZL (all 1:1 with ZAR) | |
| PS | ILS + JOD (SIX: "No universal currency") | **ILS** | Electricity comes from IEC/JDECO and is billed in ILS. |
| AQ | none (CLDR XXX, tender=false; SIX: "No universal currency") | none | Emit null. |
| CK, NU, PN, TK | NZD | NZD | |
| BV, HM, GS, IO, TF, UM | NOK, AUD, GBP, USD, EUR, USD | (none: no resident households) | Emit null or "no household market" rather than a price. |
| CW, SX | XCG (Caribbean guilder, from 2025-03-31; ANG ended 2025-06-30) | XCG | |
| SL | SLE (SLL ended 2023-12-31) | SLE | |
| SY | SYP (redenominated 100:1 on 2026-01-01, same code) | SYP | |
| KI, NR, TV | AUD | AUD | |
| FM, MH, PW, TL, BQ | USD | USD | |

File: `cldr-currencyData.json`, `cldr-supplementalData.xml`, `iso4217-six-list-one.xml`, `iso_4217.debian-iso-codes.json`.

---

## 5. Ember: European wholesale electricity prices

- **Page:** https://ember-energy.org/data/european-wholesale-electricity-price-data/
- **Download URLs** (as linked from the page today; the old `https://storage.googleapis.com/emb-prod-bkt-publicdata/public-downloads/price/outputs/…` paths still serve the same files, same Last-Modified, so either works):
  - monthly: https://files.ember-energy.org/public-downloads/price/outputs/european_wholesale_electricity_price_data_monthly.csv
  - daily: https://files.ember-energy.org/public-downloads/price/outputs/european_wholesale_electricity_price_data_daily.csv
  - hourly: https://files.ember-energy.org/public-downloads/price/outputs/european_wholesale_electricity_price_data_hourly.zip (a compiled file plus one file per country)
- **Format:** CSV, `Country,ISO3 Code,Date,Price (EUR/MWhe)`. Monthly rows are dated on the first of the month. The
  current month is partial: `2026-10-01` exists today.
- **Method (quoted):** "Hourly data is sourced from ENTSO-e, EMR (UK), SEMOpx (Ireland). Missing values are
  interpolated from nearby values. This data is then aggregated to produce average daily and monthly values per
  country, weighted by load. In countries with multiple exchanges … the average is taken." Multi-zone countries (NO,
  SE, DK, IT) get **one load-weighted national price**, not a price per bidding zone.
- **Licence:** "All content is released under a Creative Commons Attribution Licence (CC-BY-4.0)." (site footer).
  Credit "Ember" and link the dataset.
- **Update frequency:** the page says "Updated monthly". In practice the file is refreshed far more often: the daily
  CSV has `Last-Modified: Fri, 02 Oct 2026 09:12:27 GMT` and runs to 2026-10-01 for most countries (2026-09-30 for
  DK, IE, IT, SE and GB). Treat it as roughly daily, without a guarantee. For the current day-ahead price use
  ENTSO-E directly.
- **Coverage: 32 countries.** AT, BE, BG, HR, CZ, DK, EE, FI, FR, DE, GR, HU, IE, IT, LV, LT, LU, NL, NO, PL, PT,
  RO, SK, SI, ES, SE, CH, GB (from 2016-06), RS (from 2016-12), ME (from 2023-04), MK (from 2023-05), and **AL (new,
  from 2026-07)**. Most start in 2015. **Not covered:** CY, MT, IS, BA, XK, MD, UA, TR, GE, LI.
- Mapping: the files use ISO3 (`GRC`, `GBR`) and need converting to alpha-2. Eurostat uses `EL` and `UK`, so map
  those too.

Files: `ember-european_wholesale_electricity_price_data_monthly.csv` (4,037 rows),
`ember-european_wholesale_electricity_price_data_daily.csv` (121,948 rows), `ember-page.html`.

---

## 6. Eurostat household electricity prices

- **Dataset `nrg_pc_204`:** "Electricity prices for household consumers - bi-annual data" (from 2007, Regulation (EU)
  2016/1952). Dimensions `freq, siec, nrg_cons, unit, tax, currency, geo, time`. Band DC = `nrg_cons=KWH2500-4999`.
  `tax` ∈ {`I_TAX` all taxes and levies included, `X_VAT` excluding VAT and other recoverable taxes, `X_TAX`
  excluding taxes and levies}. `currency` ∈ {`EUR`, `NAC`, `PPS`}. Unit `KWH` (price per kWh).
- **`nrg_pc_204_c`:** "Electricity prices components for household consumers". This is **annual** (`freq=A`),
  latest 2025. Components: `NRG_SUP` energy and supply, `NETC` network, `TAX_FEE_LEV_CHRG`, `VAT`, `TAX_RNW`,
  `TAX_CAP`, `TAX_ENV`, `TAX_NUC`, the `*_ALLOW` allowances, and `OTH`. Use it when the add-on has to be split into
  network and taxes.
- **API (JSON-stat 2.0, no key):**
  ```
  https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nrg_pc_204?format=JSON&lang=EN&nrg_cons=KWH2500-4999&unit=KWH&tax=I_TAX&tax=X_VAT&tax=X_TAX&currency=NAC&currency=EUR&lastTimePeriod=1
  ```
  Repeat a parameter to select several values. Use `lastTimePeriod=N` or `sinceTimePeriod=2025-S1`. The flat index
  is row-major over `id`/`size`, and flags are in `status` (`e` estimated, `p` provisional).
  **SDMX-CSV** (easier to parse):
  ```
  https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/nrg_pc_204/S.E7000.KWH2500-4999.KWH.I_TAX+X_VAT+X_TAX.NAC+EUR.?format=SDMX-CSV&startPeriod=2025-S1
  ```
  Columns: `DATAFLOW,LAST UPDATE,freq,siec,nrg_cons,unit,tax,currency,geo,TIME_PERIOD,OBS_VALUE,OBS_FLAG,CONF_STATUS`.
  Components dataset: `.../data/nrg_pc_204_c?format=JSON&lang=EN&nrg_cons=KWH2500-4999&sinceTimePeriod=2024`.
- **Latest semester available now: `2025-S2`** (`OBS_PERIOD_OVERALL_LATEST`, data updated 2026-09-24). 2026-S1 is
  not out yet; Eurostat usually publishes S1 in late October or November.
- **Licence:** https://ec.europa.eu/eurostat/help/copyright-notice. "Reuse of statistical data, metadata,
  publications, and other dissemination tools published on this website for commercial or non-commercial purposes
  is authorised provided the source is acknowledged." This rests on Commission Decision 2011/833/EU. The editorial
  content is under CC BY 4.0.
- **Geo codes:** Eurostat uses `EL` (Greece) and `UK`, and includes `XK`. Aggregates are `EU27_2020` and `EA`.

### Countries with a band-DC value in 2025-S2 (all three tax levels, NAC and EUR)

**Have values (38 plus 2 aggregates):** EU27_2020 and EA (EUR only), BE, BG, CZ, DK, DE, EE, IE, EL, ES, FR, HR (p),
IT, CY, LV, LT, LU, HU, MT (p), NL, AT (I_TAX and X_VAT flagged e), PL, PT, RO, SI, SK, FI, SE, LI, NO, BA, ME, MD,
MK, GE, AL (e), RS, TR, XK.

**No value in 2025-S2:** **IS** (it had 2025-S1: 29.31 ISK, 0.2019 EUR), **UK** (no data since it left), **UA**
(no data in 2024-25).

EUR, all taxes, 2025-S2, per kWh (spot check): DE 0.3869 · IE 0.4042 · DK 0.3312 · BE 0.3499 · CZ 0.3217 · AT
0.3272 · IT 0.2966 · FR 0.2561 · ES 0.2669 · NL 0.2558 · SE 0.2711 · NO 0.1922 · PL 0.2709 · RO 0.2893 · HU 0.1082
· BG 0.1355 · MT 0.1282 · XK 0.0877 · TR 0.0636 · GE 0.0731.

Pitfalls for the "add-on = X_VAT − wholesale" method:
- **X_TAX > X_VAT** in IE, LU, NL, AT (X_TAX only) and NO. Since 2021, allowances and subsidies are counted as negative
  taxes, so "taxes" can be net negative. Do not assume I_TAX ≥ X_VAT ≥ X_TAX.
- MD has I_TAX ≈ X_VAT ≈ X_TAX (2025-S1 identical). HU, BG, MK, GE and AL have X_VAT = X_TAX, which means no non-VAT
  taxes are reported.
- RO NAC rose from 0.96 to 1.47 RON between S1 and S2 2025 (the price cap ended on 2025-07-01). This shows the
  semester baseline can go stale fast.
- BG NAC is in **BGN** for 2025. Bulgaria bills in EUR from 2026.

Files: `eurostat-nrg_pc_204-DC-sample.json` (2024-S1 to 2025-S2, all tax and currency levels),
`eurostat-nrg_pc_204-DC-latest.json` (`lastTimePeriod=1`, NAC and EUR), `eurostat-nrg_pc_204-DC-sdmx.csv`,
`eurostat-nrg_pc_204_c-DC-sample.json` (components, 2024 to 2025).

---

## Attribution block for the output file

```
"sources": {
  "fx": "Frankfurter (frankfurter.dev): blended central-bank reference rates; ECB euro reference rates (ecb.europa.eu)",
  "wholesale": "Ember, European wholesale electricity price data (CC BY 4.0)",
  "retail_baseline": "Eurostat nrg_pc_204, band DC (source: Eurostat)",
  "regions": "UN M49 standard country or area codes",
  "currencies": "Unicode CLDR (Unicode License v3)"
}
```
