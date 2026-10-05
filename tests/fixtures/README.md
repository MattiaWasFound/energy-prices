# Recorded fixtures

Real responses, recorded once, so the parsers are tested against what the
sources actually send. Tests never reach the network (`tests/conftest.py`).

| File | What it is | Where it came from |
|---|---|---|
| `eds_dayahead_2026-10-04.json` | Energi Data Service `DayAheadPrices`, 2026-10-04 and -05, DK1 DK2 DE NO2 SE3 SE4, 15-minute | Recorded 2026-10-04 from api.energidataservice.dk |
| `ecb_eurofxref_2026-10-02.xml` | ECB euro reference rates for 2026-10-02 | Recorded 2026-10-04 from ecb.europa.eu |
| `frankfurter_v2_rates_eur_2026-10-04.json` | Frankfurter v2 rates, base EUR | Recorded 2026-10-04 from api.frankfurter.dev |
| `eds_dayahead_2026-10-05.json` | The same, for 2026-10-05 only: the cross-check against ENTSO-E | Recorded 2026-10-05 from api.energidataservice.dk |
| `entsoe_se3_2026-10-05.xml` | ENTSO-E A44, SE3, 15-minute, A03 with omitted repeats (91 points), one negative price | Recorded 2026-10-05 from web-api.tp.entsoe.eu |
| `entsoe_de-lu_2026-10-05.xml` | ENTSO-E A44, DE-LU, two auctions (sequence 2 EXAA first, then 1 SDAC) | Recorded 2026-10-05 |
| `entsoe_no3_2026-10-05.xml` | ENTSO-E A44, NO3, 15-minute, the same curve sent twice without a sequence | Recorded 2026-10-05 |
| `entsoe_ch_2026-10-05.xml` | ENTSO-E A44, CH, hourly | Recorded 2026-10-05 |
| `entsoe_ack_ie-sem_2026-10-05.xml` | ENTSO-E "No matching data found" acknowledgement (IE-SEM has published nothing since 2026-09-29) | Recorded 2026-10-05 |

Re-record with `tools/record_fixtures.py`; it also writes Energi Data Service,
ECB and Frankfurter files, which are only kept when a test uses them.
