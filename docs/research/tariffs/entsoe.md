# ENTSO-E Transparency Platform: day-ahead prices (A44), state as of 2026-10-04

Researched 2026-10-04. The authoritative docs are now the Transparency Platform knowledge base
(Zendesk, `transparencyplatform.zendesk.com`) and the official Postman collection. The old
`transparency.entsoe.eu/content/static_content/.../Guide.html` user guide was moved there.
The KB articles quoted below, the Terms of Use, the open-data list and the curveType spec were
saved as snapshots on the day; the copies are not kept here.

Key references:
- KB sitemap for API integration: https://transparencyplatform.zendesk.com/hc/en-us/articles/15692855254548 (updated 2026-09-24)
- Postman API docs (official): https://documenter.getpostman.com/view/7009892/2s93JtP3F6
- Official XML examples repo: https://gitlab.entsoe.eu/transparency/xml-examples
- entsoe-py (reference Python client, MIT): https://github.com/EnergieID/entsoe-py (read at commit `0cae4006`, 2026-09-04)

---

## 1. Endpoint, auth, request, limits, errors

### Base URL
- **Production: `https://web-api.tp.entsoe.eu/api`**. HTTPS only.
  Source: KB "Request Endpoint", https://transparencyplatform.zendesk.com/hc/en-us/articles/15696677194644 (updated 2026-09-21).
- Test (IOP): `https://web-api.tp-iop.entsoe.eu/api`. It holds less data, and needs an account on `https://iop-transparency.entsoe.eu/`.
- **No newer endpoint or API migration was announced for 2025-2026.** The 2023-2025 "migration to a newer
  technology" (TP "R3") changed the backend and the response content but kept the URL. Energy Prices
  [12.1.D] were migrated on **2024-10-04**. See KB "Migration of Transparency Platform data items",
  https://transparencyplatform.zendesk.com/hc/en-us/articles/30195539966865. User-visible effects:
  `curveType` A03 by default, decimals allowed, and rate limiting per token instead of per IP.
- The legacy path `https://transparency.entsoe.eu/api` no longer serves the API. Probed on
  2026-10-04, it returns `200 text/html` (the new website SPA). `transparency.entsoe.eu` is now the
  new website, formerly `newtransparency.entsoe.eu`.
- Live probe on 2026-10-04 without a valid token: `401`, `Content-Type: text/xml`, and an
  Acknowledgement document containing "Authentication failed." So the endpoint was up.

### Token
- GET: query parameter **`securityToken=<uuid>`**. Parameter names are case-sensitive.
  Source: KB "Get Method", https://transparencyplatform.zendesk.com/hc/en-us/articles/15854521447188
- POST (XML `StatusRequest_MarketDocument` body): HTTP header `SECURITY_TOKEN: <token>`.
  Source: KB "Post Method", https://transparencyplatform.zendesk.com/hc/en-us/articles/15854497223188
- A missing, invalid or suspended token returns HTTP 401. You regenerate the token yourself if it leaks.
  Source: https://transparencyplatform.zendesk.com/hc/en-us/articles/15854491895828

### Day-ahead price request (Energy Prices, TR art. 12.1.D)
From the Postman collection, item "Market / 12.1.D Energy Prices" ([M] = mandatory, [O] = optional):

| param | value | notes |
|---|---|---|
| `documentType` | `A44` | [M] Price Document |
| `in_Domain` | bidding-zone EIC | [M] |
| `out_Domain` | same EIC | [M] must equal in_Domain |
| `periodStart` | `yyyyMMddHHmm` (UTC) | [M] e.g. `202610032200` |
| `periodEnd` | `yyyyMMddHHmm` (UTC) | [M] |
| `contract_MarketAgreement.type` | `A01` | [O] A01 = day-ahead, A07 = intraday. **Send A01.** Without it you may also get intraday-auction series (A07) for zones that publish them. entsoe-py always sends A01. |
| `classificationSequence_AttributeInstanceComponent.position` | `1` | [O] Selects the auction when a zone has more than one. **For DE-LU and AT, 1 = SDAC and 2 = the EXAA 10:15 auction.** entsoe-py sends `1` only for DE_LU and AT. |
| `offset` | `0`, `100`, ... | [O] Zero-based paging over TimeSeries, 100 per response |
| `curveType` | `A01` / `A03` | [O] "A01 = Sequential fixed block; A03 = Variable sized blocks (**default**)". Documented in Postman but could not be tested before the token arrived, so A03 expansion is implemented anyway. |

- `timeInterval=2026-10-03T22:00Z/2026-10-04T22:00Z` is an alternative to periodStart/periodEnd. KB: https://transparencyplatform.zendesk.com/hc/en-us/articles/12783280128404
- All times are UTC. A CET delivery day D is `(D-1)T23:00Z .. DT23:00Z` in winter and `(D-1)T22:00Z .. DT22:00Z` in summer.
- For 12.1.D **the response is always whole delivery days**. A window that touches part of a day returns the whole day, in the time zone the platform uses for that area. That is "in general the area's own time zone, with exceptions due to regional arrangements". All SDAC zones observed, including SE3 and LV, use the CET/CEST market day (start `22:00Z`/`23:00Z`). Take day boundaries from the response's `timeInterval`, not from your own assumption.
  KB: https://transparencyplatform.zendesk.com/hc/en-us/articles/12786736668180 and https://transparencyplatform.zendesk.com/hc/en-us/articles/12786431986964

Example (DK1, delivery day 2026-10-04 CEST):
```
GET https://web-api.tp.entsoe.eu/api?documentType=A44&in_Domain=10YDK-1--------W&out_Domain=10YDK-1--------W&contract_MarketAgreement.type=A01&periodStart=202610032200&periodEnd=202610042200&securityToken=<TOKEN>
```
A successful response is `200`, `Content-Type: text/xml`, `Content-Disposition: inline; filename="Energy_Prices_202407272200-202407282200.xml"`. Those headers come from the Postman example response.

### Limits
- **Query size:** at most 1 year per request for Day Ahead Prices 12.1.D, and **at most 100 TimeSeries per XML response**. Page with `offset`.
  KB "API Query Size Limit": https://transparencyplatform.zendesk.com/hc/en-us/articles/15854536354964. Postman 12.1.D description.
- **Rate limit:** **400 requests per minute per token.** It is counted per token, not per IP; R3 does no IP banning. Going over gives `429` and a temporary token ban, lifted automatically after about 10 minutes. Several nodes sharing one token are counted together. ENTSO-E suggests client throttling at about 6-7 requests per second.
  KB "API Rate Limit Part 1": https://transparencyplatform.zendesk.com/hc/en-us/articles/12783148966036 (updated 2026-09-01)
- **Timeout:** 300 s per request. KB "API Rate Limit Part 2": https://transparencyplatform.zendesk.com/hc/en-us/articles/12783223209876
- **Publication timing:** TR art. 12.1.D requires publication "no later than one hour after gate closure". SDAC results normally arrive shortly after about 12:45-13:00 CET on D-1. KB: https://transparencyplatform.zendesk.com/hc/en-us/articles/16647234190100

### Errors: `Acknowledgement_MarketDocument`
Namespace `urn:iec62325.351:tc57wg16:451-1:acknowledgementdocument:7:0`. The reason is in `Reason/code` (always `999` for API rejections) and `Reason/text`.
HTTP codes, from KB "Query Response": https://transparencyplatform.zendesk.com/hc/en-us/articles/15727773247124

| HTTP | Reason code | meaning |
|---|---|---|
| **200** | 999 | **No matching data found** (a valid query with no data). You must sniff the body; the status is 200, not 4xx. |
| 400 | 999 | Invalid query attributes or parameters: missing or duplicate params, wrong case, more than 1 year, more than 100 TimeSeries |
| 401 | 999 | Missing or invalid token. Live body text: `Authentication failed.` |
| 429 | - | Too many requests |

Real no-data body text: `No matching data found for Data item ENERGY_PRICES and interval 2024-10-26T21:00:00.000Z/2024-10-26T21:00:00.000Z`.
Rejection reasons are listed at https://transparencyplatform.zendesk.com/hc/en-us/articles/15854332833300.
entsoe-py matches these substrings: `No matching data found`, `check you request against dependency tables`, `amount of requested data exceeds allowed limit`, and `requested data to be gathered via the offset parameter exceeds the allowed limit`.

---

## 2. Response XML format (`Publication_MarketDocument`)

- **Namespace (current):** `urn:iec62325.351:tc57wg16:451-3:publicationdocument:7:3`. Every real response from 2024-10 to 2026-04 that I found uses 7:3. Older captures and the official example use `...:7:0`. **Match on the local element name and ignore the namespace version.**
- Structure, with an annotated official template at gitlab `Market/Energy Prices [12.1.D] - XSD7:3.xml`:

```
Publication_MarketDocument
  mRID, revisionNumber, type=A44, sender/receiver (10X1001A1001A450 = ENTSO-E), createdDateTime
  period.timeInterval/{start,end}          # union of all days returned, UTC "YYYY-MM-DDTHH:MMZ"
  TimeSeries (1..n)                        # one per delivery day x auction(sequence) [x currency]
    mRID                                   # just a counter 1..n
    auction.type      A01 (implicit)
    businessType      A62 (spot price)
    in_Domain.mRID / out_Domain.mRID       # zone EIC, codingScheme="A01"
    contract_MarketAgreement.type  A01 day-ahead | A07 intraday
    currency_Unit.name   EUR (PLN series also exist for PL, see gotchas)
    price_Measure_Unit.name  MWH           # price is currency per MWh
    classificationSequence_AttributeInstanceComponent.position   # optional; present for DE-LU/AT
    curveType  A03 (current default) | A01
    Period (1..n)
      timeInterval/{start,end}             # one delivery day, UTC
      resolution  PT15M | PT30M | PT60M
      Point (1..n)
        position       1-based
        price.amount   decimal, may be negative; may be ABSENT (see below)
```

- **Multiple TimeSeries per document are normal:**
  - one per delivery day (a 2-day query gives 2 TimeSeries, as in the CH sample)
  - one per auction sequence (DE-LU and AT return seq 1 and seq 2; the DE-LU sample has 4 TimeSeries for 2 days)
  - possibly one per currency (PL)
  - historically one per resolution
  Group by `(zone, contract, sequence, currency, resolution)` before you build a series.
- **Timestamp of a point:** `Period.timeInterval.start + (position-1) * resolution`, in UTC. This is DST-safe: a 23-hour day has 92 PT15M or 23 PT60M slots, a 25-hour day has 100 or 25. Expected slot count = `(end-start)/resolution`.
- **curveType A01 (sequential fixed blocks):** every position from 1 to N is present. A missing position is a gap.
- **curveType A03 (variable sized blocks):** **only positions where the value changes are sent.** Each point's value holds until the next point's position. The last point holds until `Period.end`, so trailing positions can be missing too. Expand by forward-filling over positions 1..N. Spec: "THE INTRODUCTION OF DIFFERENT TIME SERIES POSSIBILITIES (CURVETYPE)" v1.4, §3 and §4.3: https://eepublicdownloads.entsoe.eu/clean-documents/EDI/Library/cim_based/Introduction_of_different_Timeseries_possibilities__curvetypes__with_ENTSO-E_electronic_document_v1.4.pdf. KB: https://transparencyplatform.zendesk.com/hc/en-us/articles/30262342482961. Since R3 the API returns A03 "for all data items".
  - Real gaps in the samples:
    - NO3 2024-10-18 PT60M: 22 points for 24 hours; positions 15 and 19 missing
    - SE3 2026-04-14 PT15M: 95 of 96; position 29 missing
    - DE-LU 2025-11-01 seq 2: 91 of 96
  - **A `Point` with a `position` but no `price.amount`** means there is no value from that position on, until the next point. The official template says that to cancel a publication you "resubmit... with curveType A03 and remove `<price.amount>`". I saw this shape in a third-party file (`devskill-org/ems`, not saved because it looks synthetic). Map it to NULL, not to the previous value.
  - Disjoint Periods inside one TimeSeries are gaps (spec §5). Never fill across Periods, and never read a missing value as 0.
- entsoe-py does the same expansion: `S.reindex(pd.date_range(start, end-delta, freq=delta)).ffill()` when curveType is A03 (`entsoe/series_parsers.py`).

Minimal expansion. I tested it against every saved sample; each one expands to 96, 24 or 92 slots per day as expected:
```python
step = {"PT15M": 15, "PT30M": 30, "PT60M": 60}[resolution]          # minutes
n = int((end - start).total_seconds() // (step * 60))
pts = {int(p.position): (float(p.amount) if p.amount is not None else None) for p in points}
last = None
for pos in range(1, n + 1):
    if pos in pts: last = pts[pos]
    elif curve_type == "A01": last = None          # A01: a missing position is a real gap
    yield start + timedelta(minutes=step * (pos - 1)), last
```

### 15-minute MTU in day-ahead (SDAC)
- **SDAC switched to a 15-minute MTU on trading day 2025-09-30, for delivery day 2025-10-01** (from `2025-09-30T22:00Z`), in all SDAC bidding zones and across borders. The go-live was successful.
  Sources:
  - Nord Pool / MCSC: https://www.nordpoolgroup.com/en/message-center-container/newsroom/exchange-message-list/2025/q3/market-coupling-steering-committee-confirms-go-live-of--15-minute-mtu-in-sdac-on-trading-day-30-september-2025-for-delivery-day-1-october-2025/
  - APG: https://markt.apg.at/en/news-press/sdac-go-live-of-15-minute-market-time-unit-in-day-ahead-market-coupling-successful-as-of-september-30-2025/
  - entsoe-py hard-codes `QUARTER_MTU_SDAC_GOLIVE = 2025-10-01 Europe/Amsterdam`.
- **SEM (IE-SEM) day-ahead moved to a 30-minute MTU on the same date** (first delivery 2025-10-01): https://www.semopx.com/market-messages/mcsc-revised-go-live-date-sdac-15min-mtu-sem-dam-30min-mtu
- What publishes which resolution now:
  - **PT15M:** every SDAC zone, i.e. Nordic, Baltic, CWE/Core, Iberia, Italy, GR, RO, BG, HR, SI, HU, PL, CZ, SK. Before 2025-10-01 they were PT60M.
  - **PT30M:** IE-SEM.
  - **PT60M:** CH. Switzerland is not in SDAC; it runs its own EPEX CH auction, and a real Nov 2025 sample is still hourly.
  - **Non-SDAC Balkan and UA auctions (RS, ME, MK, AL, XK, UA): resolution not verified.** Key off the `resolution` element.
  - **DE-LU and AT:** before go-live, seq 1 (SDAC) was PT60M and seq 2 (EXAA) was PT15M. Now **both are PT15M**, so **the sequence is the only way to tell SDAC from EXAA.**
- ENTSO-E's resolution-change report (https://eepublicdownloads.blob.core.windows.net/tp-reporting-exports/ChangesToPublicationResolution.xlsx, refreshed 2026-10-04) has no rows for 12.1.D. Its 12.1.E "Daily" net-position rows show the switch at `2025-09-30T22:00Z` for CWE/Core/RO/BG/HR/SI, at `2025-09-29T22:00Z` for Nordic and Baltic, and at `2025-12-31T23:00Z` for HU. Treat dates around the switch as possibly mixed. Never infer the resolution from the date.

---

## 3. Bidding zones with day-ahead prices

EIC codes come from **ENTSO-E's own KB "Area List with Energy Identification Code (EIC)"**, https://transparencyplatform.zendesk.com/hc/en-us/articles/15885757676308 (updated 2026-09-21). Each one is cross-checked against entsoe-py `entsoe/mappings.py` (commit `0cae4006`) and Electricity Maps' `ENTSOE.py` (master, 2026-10-02), and all three agree.

Status:
- **R** = reliably populated, SDAC, EUR
- **R\*** = populated, non-SDAC local auction (zone list from Electricity Maps' Oct-2026 `ENTSOE_DAY_AHEAD_AUCTIONS` allowlist, PR #8870: https://github.com/electricitymaps/electricitymaps-contrib/pull/8870). Verify once you have a token.
- **E** = empty or not published

| id | EIC | ISO country(ies) | auction | resolution now | status |
|---|---|---|---|---|---|
| **Nordic** |||||
| SE1 | 10Y1001A1001A44P | SE | SDAC | PT15M | R |
| SE2 | 10Y1001A1001A45N | SE | SDAC | PT15M | R |
| SE3 | 10Y1001A1001A46L | SE (+AX: Åland prices = SE3) | SDAC | PT15M | R |
| SE4 | 10Y1001A1001A47J | SE | SDAC | PT15M | R |
| NO1 | 10YNO-1--------2 | NO | SDAC | PT15M | R |
| NO2 | 10YNO-2--------T | NO | SDAC | PT15M | R |
| NO3 | 10YNO-3--------J | NO | SDAC | PT15M | R |
| NO4 | 10YNO-4--------9 | NO | SDAC | PT15M | R |
| NO5 | 10Y1001A1001A48H | NO | SDAC | PT15M | R |
| DK1 | 10YDK-1--------W | DK | SDAC | PT15M | R |
| DK2 | 10YDK-2--------M | DK | SDAC | PT15M | R |
| FI | 10YFI-1--------U | FI | SDAC | PT15M | R |
| **Baltic** |||||
| EE | 10Y1001A1001A39I | EE | SDAC | PT15M | R |
| LV | 10YLV-1001A00074 | LV | SDAC | PT15M | R |
| LT | 10YLT-1001A0008Q | LT | SDAC | PT15M | R |
| **Central / Western** |||||
| DE-LU | 10Y1001A1001A82H | DE, LU | SDAC = seq 1; EXAA = seq 2 | PT15M | R (filter seq=1) |
| AT | 10YAT-APG------L | AT | SDAC = seq 1; EXAA = seq 2 | PT15M | R (filter seq=1) |
| BE | 10YBE----------2 | BE | SDAC | PT15M | R |
| NL | 10YNL----------L | NL | SDAC | PT15M | R |
| FR | 10YFR-RTE------C | FR | SDAC | PT15M | R |
| CH | 10YCH-SWISSGRIDZ | CH (+LI) | EPEX CH (not SDAC) | PT60M | R\* (sample Nov 2025) |
| PL | 10YPL-AREA-----S | PL | SDAC | PT15M | R (EUR + PLN series) |
| CZ | 10YCZ-CEPS-----N | CZ | SDAC | PT15M | R |
| SK | 10YSK-SEPS-----K | SK | SDAC | PT15M | R |
| HU | 10YHU-MAVIR----U | HU | SDAC | PT15M | R |
| SI | 10YSI-ELES-----O | SI | SDAC | PT15M | R |
| HR | 10YHR-HEP------M | HR | SDAC | PT15M | R |
| **Southern** |||||
| ES | 10YES-REE------0 | ES | SDAC | PT15M | R |
| PT | 10YPT-REN------W | PT | SDAC | PT15M | R |
| IT-NORD | 10Y1001A1001A73I | IT | SDAC | PT15M | R |
| IT-CNOR | 10Y1001A1001A70O | IT | SDAC | PT15M | R |
| IT-CSUD | 10Y1001A1001A71M | IT | SDAC | PT15M | R |
| IT-SUD | 10Y1001A1001A788 | IT | SDAC | PT15M | R |
| IT-CALA | 10Y1001C--00096J | IT | SDAC | PT15M | R (zone exists since 2021-01-01) |
| IT-SICI | 10Y1001A1001A75E | IT | SDAC | PT15M | R |
| IT-SARD | 10Y1001A1001A74G | IT | SDAC | PT15M | R |
| GR | 10YGR-HTSO-----Y | GR | SDAC | PT15M | R |
| **South-East / Balkan** |||||
| RO | 10YRO-TEL------P | RO | SDAC | PT15M | R |
| BG | 10YCA-BULGARIA-R | BG | SDAC | PT15M | R |
| RS | 10YCS-SERBIATSOV | RS | SEEPEX | ? | R\* |
| ME | 10YCS-CG-TSO---S | ME | BELEN | ? | R\* |
| MK | 10YMK-MEPSO----8 | MK | MEMO | ? | R\* |
| AL | 10YAL-KESH-----5 | AL | ALPEX | ? | R\* |
| XK | 10Y1001C--00100H | XK (Kosovo; not an official ISO code) | ALPEX | ? | R\* |
| BA | 10YBA-JPCC-----D | BA | none (no day-ahead market) | - | E |
| **East** |||||
| UA | 10Y1001C--000182 (BZN\|UA-IPS) | UA | UA market operator (OREE) DAM | ? | R\*. Electricity Maps uses UA-IPS for prices. `10Y1001C--00003F` (BZN\|UA) is the other UA BZN code, and is what entsoe-py's `UA` maps to; try both. Currency not verified. |
| MD | 10Y1001A1001A990 | MD | OPEM DAM (live since delivery 2025-12-11, prices in MDL) | ? | E/unverified. Not in Electricity Maps' list. MD data is also excluded from ENTSO-E's CC-BY list. |
| **Islands** |||||
| IE-SEM | 10Y1001A1001A59C | IE, GB-NIR (ISO: IE + GB) | SEMOpx (not SDAC) | PT30M | R\* |
| GB | 10YGB----------A | GB (excl. NIR) | N2EX / EPEX GB | - | **E since 2021-06-15**: GB publication on the TP stopped after Brexit, and only history before then is available. Use Elexon/Nord Pool/EPEX for GB. |

Not covered or out of scope:
- CY (`10YCY-1001A0003J`), MT (`10Y1001A1001A93C`), TR (`10YTR-TEIAS----W`; use EPİAŞ; TR data is excluded from CC-BY), GE (`10Y1001A1001B012`), RU, BY: no usable A44 day-ahead prices.
- Legacy or virtual zones you must **not** use for current data:
  - DE-AT-LU `10Y1001A1001A63L` (split 2018-10-01)
  - IT-Brindisi, IT-Foggia, IT-Priolo, IT-Rossano (abolished 2021-01-01)
  - IT-GR, IT-North-AT/CH/FR/SI, IT-SACOAC/SACODC, IT-Malta, NO1A, NO2A, DK1A, DK1-NO1, NO2NSL, GB(IFA)/GB(IFA2)/GB(ElecLink) (interconnector or virtual BZNs)
  - Country or control-area codes such as DE `10Y1001A1001A83F`, IT `10YIT-GRTN-----B`, SE `10YSE-1--------K`, NO `10YNO-0--------C`, DK `10Y1001A1001A65H`, LU `10YLU-CEGEDEL-NQ`, IE `10YIE-1001A00010` and NIE `10Y1001A1001A016` are not price zones. Query the BZN code instead (e.g. DE-LU for DE and LU).

Caveat: R\* means "a maintained open-source parser fetches this zone from ENTSO-E A44 as of 2026-10". This could not be confirmed before the token arrived (§6 has the live check). The check was a one-day probe per zone.

---

## 4. Saved sample documents (verbatim)

All of them are real API responses except where noted. The price values in them are ENTSO-E TP data under the TP Terms of Use (see §5). Each was a copy of a repo test fixture, pinned to a commit; the copies are not kept here, the pinned sources are below.

| file | what it shows | source (pinned) | repo licence |
|---|---|---|---|
| `entsoe_sample_PT15M_SE3_2026-04-14.xml` | **Current SDAC 15-min**, ns 7:3, 1 TimeSeries, A03 with one compressed position (29) | https://github.com/gangwalrachit/gridlog/blob/3bb5037d70ff3cbe351bf14eeb32467a02647e54/fixtures/se3_da_2026-04-14.xml | MIT |
| `entsoe_sample_PT15M_DE-LU_2seq_2025-10-31_2025-11-01.xml` | **Post-go-live DE-LU: 4 TimeSeries = 2 days x seq 1 (SDAC) and seq 2 (EXAA), all PT15M**, A03 gaps | https://github.com/openhab/openhab-addons/blob/7616f4d542d054753b0b991c15eefe4e6f0fb907/bundles/org.openhab.binding.entsoe/src/test/resources/response-PT15M.xml | EPL-2.0 |
| `entsoe_sample_PT60M_CH_2025-11-26_2025-11-27.xml` | **PT60M after go-live** (CH, non-SDAC), 2 TimeSeries for 2 days | https://github.com/openhab/openhab-addons/blob/7616f4d542d054753b0b991c15eefe4e6f0fb907/bundles/org.openhab.binding.entsoe/src/test/resources/response-PT60M.xml | EPL-2.0 |
| `entsoe_sample_PT60M_A03gaps_NO3_2024-10-18.xml` | **curveType A03 with omitted repeats** (22 points for 24 h; positions 15 and 19 omitted) | https://github.com/frodegill/elspot/blob/ca52d290c7976230a04d87ae9f878f2bbc5aff78/src/tests/curvetype_a03.xml | GPL-3.0 |
| `entsoe_sample_PT15M_AT_seq2_2024-07-28_official_postman.xml` | **Official ENTSO-E** example response (AT, seq 2 = EXAA, PT15M, 95 of 96 points), captured 2024-10-01 | Postman collection, item "12.1.D Energy Prices", saved response "AT (28/07/2024)": https://documenter.getpostman.com/view/7009892/2s93JtP3F6. Extracted from the collection JSON `https://documenter.gw.postman.com/api/collections/7009892/2s93JtP3F6?segregateAuth=true&versionTag=latest` | ENTSO-E documentation, no explicit licence |
| `entsoe_sample_ack_no_data.xml` | **"No matching data found"** acknowledgement for ENERGY_PRICES (served with HTTP 200) | https://github.com/mikahozz/gohome/blob/97beb075374088dac077560ccd991670ac5e7d2d/integrations/spot/mock/noData_200.xml | MIT |
| `entsoe_sample_ack_401_auth_failed.xml` | 401 acknowledgement, "Authentication failed." | captured live by me, 2026-10-04, with a dummy token | n/a |

There is also an official annotated *template* (a provider upload example, one point, not a real response) at https://gitlab.entsoe.eu/transparency/xml-examples/-/blob/main/Market/Energy%20Prices%20[12.1.D]%20-%20XSD7:3.xml (no licence stated).

---

## 5. Token registration, and the licence for re-publishing

### Getting a token
From KB "How to get security token?", https://transparencyplatform.zendesk.com/hc/en-us/articles/12845911031188 (updated 2026-09-28):
1. Register at https://transparency.entsoe.eu/: **Sign In → Register**, fill in the form, then verify the account with the link sent by email. Use https://iop-transparency.entsoe.eu/ for the test environment.
2. Email **`transparency@entsoe.eu`** with the subject **`RESTful API access`** and **your registered email address in the body**.
3. Wait for the confirmation email. It is **"granted within 3 working days"**.
4. Log in, go to **My Account**, then **Generate token**. Generating again replaces the old token and shows a warning first. The token is a UUID.
5. Use it as `securityToken`.

Known open issue (KB "List of known TP issues", ticket 9469652, created 2026-09-09, status **Hold**): accounts not synchronised between Keycloak and the TP show "Unexpected error" in My Account, so no token can be generated, or the API answers "Invalid security token". If that happens, reply to the support email or open a ticket. Source: https://transparencyplatform.zendesk.com/hc/en-us/articles/51106751516945

### Can we publish ENTSO-E day-ahead prices in a file?
Sources:
- KB "Legal Terms and Conditions": https://transparencyplatform.zendesk.com/hc/en-us/articles/40921911218961 (updated 2026-09-22)
- Terms of Use, version 29/03/2023 (current): https://transparencyplatform.zendesk.com/hc/article_attachments/40921869376401
- "List of data available for free re-use", version 18/10/2023 (current): https://transparencyplatform.zendesk.com/hc/article_attachments/40921869379729

- ENTSO-E publishes a **list of data items that are open data under CC-BY 4.0**, re-usable "for any purpose" with attribution and an indication of changes. **Energy Prices [12.1.D] (day-ahead prices) are NOT on that list.** The list covers 6.1.b-e, 9.1, 10.1.a/b, 11.1.a/b, 11.4, 12.1.a/b/c, **12.1.g**, 13.1.a-c and balancing items, but has no 12.1.d (I also checked for 12.1.e, 12.1.f and 14/16). It also excludes all MD and TR data.
- So day-ahead prices fall under the general **Terms of Use §3.1**. The data user must:
  - use the data in good faith;
  - **mention the ENTSO-E Transparency Platform as the source**;
  - not use the ENTSO-E name in a way that suggests sponsorship or endorsement;
  - **"not cause prejudice to the copyright or related right on a Transparency Platform Data, which may be owned by the concerned Primary Owner of Data. In case of a risk to cause prejudice to said right, the Data User shall seek the prior agreement of the holder."**
  For 12.1.D the primary owners and data providers are the **power exchanges (NEMOs: Nord Pool, EPEX SPOT, OMIE, GME, ...) or TSOs**. §5.1 says TP data "may be subject to copyright owned by the Primary Owner of Data", and rights are "not sub-licensable or transferrable".
- In practice, many open projects republish these prices. But **the TP terms give no CC-BY grant for day-ahead prices.** Republishing raw price series in a public file carries a residual risk toward the NEMOs, who sell this data commercially. Options, from safest to least safe:
  1. Ask `transparency@entsoe.eu` (and/or the relevant NEMO) for written permission.
  2. Publish only derived aggregates (e.g. daily or monthly averages) with clear attribution: "Source: ENTSO-E Transparency Platform, Energy Prices [12.1.D]; values aggregated/modified."
  3. Publish raw values with attribution and accept the risk.
  This is a reading of the documents, not legal advice.

---

## 6. Live check with our own token, 2026-10-05

The token arrived on 2026-10-05, about a day after the request email of
2026-10-04. Same day, `tools/record_fixtures.py --day 2026-10-05` and a full
`generate` run:

- **29 of the 30 configured countries came back live.** The exception is
  Ireland: IE-SEM (`10Y1001A1001A59C`) returns the "No matching data found"
  acknowledgement for every day after 2026-09-29 (found by bisecting
  2026-09-15 to 2026-10-01). Data for 2026-09-15 and earlier is there. The job
  falls back to the country table for IE, as designed, and picks the live
  price up again on its own once SEM data reappears.
- **ENTSO-E and Energi Data Service agree.** For SE3 and DE-LU the 96
  quarter-hours match to within 0.00001 EUR/MWh (rounding), so the two
  sources are interchangeable for the areas both cover. This is now a test.
- **NO3 and PL send the same curve twice**, as TimeSeries mRID 1 and 2, with
  no sequence element and identical points. Collapsing them is harmless. If
  they ever differ, the later series wins, which would need a look.
- **DE-LU lists sequence 2 (EXAA) first**, starting at 200.00 against SDAC's
  161.27 on the day, so taking the first series would be visibly wrong.
- **SE3 had 91 points for 96 quarters** (A03 omissions) and one negative
  price, -5.05 EUR/MWh.

The recordings replace the fixtures borrowed from open-source projects; see
`tests/fixtures/README.md`.

## Gotchas
- **"No data" is HTTP 200** with an `Acknowledgement_MarketDocument`. Branch on the root element name, not on the status code. Auth errors are 401 with an XML ack, not HTML.
- **Always expand A03.** Missing positions repeat the previous value, including at the end of the Period. A Point with no `price.amount` is a NULL, and disjoint Periods are gaps. Never fill missing values with 0.
- **DE-LU and AT return two auctions.** Request or filter `classificationSequence_AttributeInstanceComponent.position=1` for SDAC. Since 2025-10-01 both sequences are PT15M, so a resolution filter no longer separates them. Single-auction zones omit the sequence element, so treat a missing one as seq 1. For DE-LU and AT, ENTSO-E's own template says that when a provider omits it, the sequence is derived from resolution (PT60M = 1, PT15M = 2). That rule only applies to data from before go-live.
- **Send `contract_MarketAgreement.type=A01`**, so that intraday-auction (A07) series published under A44 are not mixed in.
- **Group TimeSeries by (sequence, resolution, currency).** PL has published PLN series next to the EUR ones, and the same day can appear more than once. Filter `currency_Unit.name == "EUR"`, or store the currency.
- **Resolution varies by zone and date:** PT60M before 2025-10-01, PT15M for SDAC after, PT30M for IE-SEM after, PT60M for CH. A mixed backfill window gives mixed resolutions, so store the resolution per row.
- **Whole days come back.** Responses snap to the area's market day (CET/CEST for SDAC zones, even FI/Baltics/GR/RO/BG). Use the returned `timeInterval`. Request in UTC `yyyyMMddHHmm` and handle 92/100-slot DST days.
- **Namespace version drifts** (7:0 → 7:3). Parse by local name.
- **Limits:** 1 year per request, 100 TimeSeries per response (page with `offset`), 400 requests per minute **per token across all your machines** (429 means about a 10-minute ban), 300 s timeout.
- **Use EIC BZN codes, not country codes:** DE → `10Y1001A1001A82H` (DE-LU), IE/NIR → `10Y1001A1001A59C`, SE/NO/DK/IT need their sub-zones. Legacy zones (DE-AT-LU, IT-Brindisi, ...) return only history.
- **GB has had no data since 2021-06-15. BA has no day-ahead market. MD/UA/Balkan zones are unverified or local-currency risks.** Probe each zone for one recent day before relying on it.
- **Licence:** day-ahead prices are *not* on ENTSO-E's CC-BY 4.0 list. Attribute the "ENTSO-E Transparency Platform" and check permission before publishing raw series.
- `https://transparency.entsoe.eu/api` is dead (it serves HTML). Use `https://web-api.tp.entsoe.eu/api`.
- Token issuance can be blocked by the open Keycloak sync issue (Sep 2026). Budget for more than the nominal 3 working days.
