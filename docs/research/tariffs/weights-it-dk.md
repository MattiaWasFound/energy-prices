# Population weights per day-ahead bidding zone: Italy and Denmark

Compiled 2026-10-04 from official statistics. Weights = zone population / national
population, rounded to 4 decimals (each column sums to exactly 1.0000 after rounding).

## Italy

### Zone configuration (in force since 1 January 2021, unchanged as of October 2026)

| Zone | Regions |
|---|---|
| NORD | Valle d'Aosta, Piemonte, Liguria, Lombardia, Trentino-Alto Adige, Veneto, Friuli-Venezia Giulia, Emilia-Romagna |
| CNOR | Toscana, Marche |
| CSUD | Lazio, Umbria, Abruzzo, Campania |
| SUD | Molise, Puglia, Basilicata |
| CALA | Calabria |
| SICI | Sicilia |
| SARD | Sardegna |

The 2021 reform moved Umbria from CNOR to CSUD, not into CNOR. It also replaced the Rossano production pole with the new
physical zone Calabria. ARERA deliberation 103/2019/R/eel, point 1 of the decision:
"prevedendo lo spostamento dell'Umbria dalla zona Centro Nord alla zona Centro Sud e
l'introduzione della zona Calabria con soppressione del polo di produzione limitata di
Rossano". Point 2 adds: "abbia effetti dal 1 gennaio 2021".

- Terna zone page (maps only, no text list): https://www.terna.it/it/sistema-elettrico/mercato-elettrico/zone-mercato
  (English: https://www.terna.it/en/electric-system/electricity-market/market-zones).
  The page labels the current map "la nuova configurazione zonale" against the zones "in vigore fino al 31 dicembre 2020".
- ARERA 103/2019/R/eel: https://www.arera.it/fileadmin/allegati/docs/19/103-19.pdf
  (landing page https://www.arera.it/atti-e-provvedimenti/dettaglio/19/103-19)

Text source: Terna, Codice di Rete, Allegato A.24 "Individuazione zone della rete rilevante", Rev. 05, January 2021,
section 4 (https://download.terna.it/terna/A%2024%20individuazione%20zone%20della%20rete%20rilevante_8d887e8354fd2b9.pdf).
ARERA 473/2023/R/eel still cites Rev. 5 as in force; Terna's Cronoprogramma (Delibera 362/2024) puts the next zonal
review at 2030-01-01.

### Population (ISTAT, resident population at 1 January 2026, provisional estimate)

Source: ISTAT demo.istat.it, "Popolazione residente per età e sesso al 1° gennaio 2026 (stima)".
- Dataset page: https://demo.istat.it/app/?i=POS&l=it
- Regional file: https://demo.istat.it/data/posas/POSAS_2026_it_Regioni.zip (file dated 2026-03-30; totals are the age 999 rows)
- Italy total: 58,942,828

| Region | Population 2026-01-01 |
|---|---:|
| Piemonte | 4,255,006 |
| Valle d'Aosta | 122,554 |
| Lombardia | 10,065,694 |
| Trentino-Alto Adige | 1,090,818 |
| Veneto | 4,857,460 |
| Friuli-Venezia Giulia | 1,193,496 |
| Liguria | 1,511,988 |
| Emilia-Romagna | 4,477,009 |
| Toscana | 3,659,222 |
| Umbria | 850,627 |
| Marche | 1,479,832 |
| Lazio | 5,709,444 |
| Abruzzo | 1,267,222 |
| Molise | 285,940 |
| Campania | 5,568,703 |
| Puglia | 3,865,277 |
| Basilicata | 525,281 |
| Calabria | 1,827,571 |
| Sicilia | 4,775,194 |
| Sardegna | 1,554,490 |

### Weights

| Zone | Population | Weight |
|---|---:|---:|
| NORD | 27,574,025 | 0.4678 |
| CNOR | 5,139,054 | 0.0872 |
| CSUD | 13,395,996 | 0.2273 |
| SUD | 4,676,498 | 0.0793 |
| CALA | 1,827,571 | 0.0310 |
| SICI | 4,775,194 | 0.0810 |
| SARD | 1,554,490 | 0.0264 |
| Total | 58,942,828 | 1.0000 |

Unrounded: NORD 0.467810, CNOR 0.087187, CSUD 0.227271, SUD 0.079340, CALA 0.031006, SICI 0.081014, SARD 0.026373.

Caveat: the zones follow the grid, not administrative borders exactly. Mapping whole regions to zones is the standard approximation and matches how Terna and ARERA describe the zones.

CSV source line:

```
ISTAT demo.istat.it POSAS resident population by region 2026-01-01 (provisional, https://demo.istat.it/data/posas/POSAS_2026_it_Regioni.zip); Terna zone map since 2021-01-01 (https://www.terna.it/it/sistema-elettrico/mercato-elettrico/zone-mercato; ARERA 103/2019/R/eel: Umbria CNOR->CSUD, Calabria new zone)
```

### Do Italian households pay the zonal price?

One national price. Since 2025-01-01 buy bids on the day-ahead market are formally valued at zonal prices, but a
transitional equalisation component brings every purchase back to the "PUN Index GME", the purchase-volume-weighted
mean of the zonal prices (GME notice 2024-04-18; ARERA Delibera 304/2024/R/eel). ARERA's July 2026 annual report
announces a gradual move to full zonal pricing, with no date set. The job's population-weighted mean of the seven
zones approximates the volume-weighted PUN Index.

## Denmark

Zones: DK1 = Jutland and Funen (west of the Great Belt) = Region Nordjylland + Region Midtjylland + Region Syddanmark.
DK2 = Zealand, Lolland-Falster, Møn and Bornholm = Region Hovedstaden (which includes Bornholm) + Region Sjælland.

Source: Statistics Denmark, StatBank table FOLK1A, "Population at the first day of the quarter", latest quarter 2026Q3 (1 July 2026). The table was updated 2026-08-10.
- StatBank: https://www.statbank.dk/FOLK1A
- API query used: https://api.statbank.dk/v1/data/FOLK1A/CSV?OMR%C3%85DE=000,081,082,083,084,085&Tid=2026K3&lang=en

| Region | Population 2026Q3 | Zone |
|---|---:|---|
| Region Nordjylland | 593,299 | DK1 |
| Region Midtjylland | 1,385,488 | DK1 |
| Region Syddanmark | 1,244,118 | DK1 |
| Region Hovedstaden | 1,949,336 | DK2 |
| Region Sjælland | 859,458 | DK2 |
| All Denmark | 6,031,699 | |

| Zone | Population | Weight |
|---|---:|---:|
| DK1 | 3,222,905 | 0.5343 |
| DK2 | 2,808,794 | 0.4657 |
| Total | 6,031,699 | 1.0000 |

Unrounded: DK1 0.534328, DK2 0.465672.

Minor edge cases, all negligible: Samsø and Anholt are in Midtjylland and are DK1. Christiansø is outside any municipality and has under 100 residents.

CSV source line:

```
Statistics Denmark StatBank FOLK1A population by region 2026Q3 (2026-07-01, https://www.statbank.dk/FOLK1A); DK1 = Nordjylland+Midtjylland+Syddanmark, DK2 = Hovedstaden+Sjælland
```
