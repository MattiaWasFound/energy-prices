# Nordic household electricity price inputs (SE, NO, FI, DK), researched 2026-10-04

Purpose: inputs for a household electricity price estimator. Each figure has a source and the date it was read.
**[UNVERIFIED]** marks a number found only in a secondary source (a retailer blog, a news summary or a search
snippet), or one that conflicts with another source. Raw pulls are not kept here.

---

## 1. Population and household weights per bidding zone

### Sweden (SE1–SE4)

No official source publishes population per elområde. There are two derivations below. They agree to within
about 1 percentage point.

**A. Recommended for household weighting: SCB metering points for permanent dwellings, 2024 (direct data).**
SCB table `EN0105A/UttagspSNI2007Ar` ("Antal uttagspunkter fördelat på användningsområde och elområde", latest
year 2024, published 2025-10-08). This is the sum of five categories: småhus over 10 MWh, småhus up to 10 MWh,
flerbostadshus with direct delivery over 5 MWh, flerbostadshus with direct delivery up to 5 MWh, and kollektivleveranser.
Holiday homes are excluded.
API: `https://api.scb.se/OV0104/v1/doris/sv/ssd/START/EN/EN0105/EN0105A/UttagspSNI2007Ar`
Browse: https://www.statistikdatabasen.scb.se/pxweb/sv/ssd/START__EN__EN0105__EN0105A/

| Zone | Residential metering points (2024) | Weight |
|---|---:|---:|
| SE1 | 141,879 | 0.0335 |
| SE2 | 307,744 | 0.0726 |
| SE3 | 2,898,052 | 0.6840 |
| SE4 | 889,566 | 0.2099 |
| Total | 4,237,241 | 1.0000 |

Caveat: one building-level kollektivleverans meter serves many flats, and there are only 10,073 of them. Most flats
have their own meter (2.03 M points in "flerbostadshus ≤5 MWh"), so the error is small.

**B. Population: SCB municipal population mapped to zones (derived).**
Source: SCB `BE0101A/BefolkManadCKM`, population for 2026M07 (published 2026-09-07). Riket = **10,613,531**.
Area definitions come from sv.wikipedia "Elområden i Sverige" (https://sv.wikipedia.org/wiki/Elomr%C3%A5den_i_Sverige),
Selectra SE2 (https://selectra.se/elpris/elomraden/elomrade-2-se2) and Värnamo Energi
(https://www.varnamoenergi.se/elomraden). The zone borders follow the grid, not municipal lines. SVT reports
that the border cuts through Oskarshamn (https://www.svt.se/nyheter/lokalt/smaland/nya-elomraden-grans-genom-oskarshamn).
So this mapping is approximate:
- SE1 = Norrbotten + Skellefteå
- SE2 = rest of Västerbotten + Jämtland + Västernorrland + northern Gävleborg (Ljusdal, Hudiksvall, Nordanstig,
  Bollnäs, Ovanåker, Söderhamn) + Älvdalen, Orsa, Mora
- SE4 = Skåne + Blekinge + Kronoberg + Kalmar except Västervik/Vimmerby/Hultsfred + Halmstad, Laholm, Hylte,
  Falkenberg + Värnamo, Gislaved, Gnosjö, Vaggeryd, Sävsjö, Vetlanda
- SE3 = the rest

| Zone | Population (Jul 2026, derived) | Weight |
|---|---:|---:|
| SE1 | ~324,000 | 0.0306 |
| SE2 | ~736,000 | 0.0693 |
| SE3 | ~7,264,000 | 0.6844 |
| SE4 | ~2,289,000 | 0.2157 |

**Use weights A** (SE1 .0335 / SE2 .0726 / SE3 .6840 / SE4 .2099) to weight households. Use B to weight people.

### Norway (NO1–NO5)

**A. Recommended: Elhub household metering points per price area (direct data, current boundaries).**
Source: the Elhub open-data API, dataset `CONSUMPTION_PER_GROUP_MBA_HOUR`, consumption group `household`. Hour read:
2026-09-27 12:00, dataset lastUpdated 2026-10-03.
`https://api.elhub.no/energy-data/v0/price-areas?dataset=CONSUMPTION_PER_GROUP_MBA_HOUR&startDate=2026-09-27T12:00:00%2B02:00&endDate=2026-09-27T13:00:00%2B02:00`
Elhub assigns each metering point to its price area as of today. Past boundary moves therefore need no handling here
(NO3/NO5 interface redefined 2017; Mel power plant moved NO3→NO5 in 2022, see https://snl.no/NO5_-_norsk_prisomr%C3%A5de_for_str%C3%B8m
and https://www.statnett.no/en/for-stakeholders-in-the-power-industry/news-for-the-power-industry/statnett-adjusts-the-interface-between-the-central-norway-and-western-norway-bidding-zones/).

| Area | Household metering points | Weight | Implied population (weight × 5,627,400) |
|---|---:|---:|---:|
| NO1 Øst | 1,125,212 | 0.4192 | ~2.36 M |
| NO2 Sørvest | 637,249 | 0.2374 | ~1.34 M |
| NO3 Midt | 413,499 | 0.1541 | ~0.87 M |
| NO4 Nord | 246,790 | 0.0920 | ~0.52 M |
| NO5 Vest | 261,206 | 0.0973 | ~0.55 M |
| Total | 2,683,956 | 1.0000 | |

The same API call also returns cabin (fritidsbolig) points. On 2026-08-31: NO1 111,246, NO2 107,086, and so on.

**B. Cross-check: SSB population for 2026 mapped by county and municipality (derived).**
SSB table 07459, 1 Jan 2026, total **5,627,400** (https://data.ssb.no/api/v0/no/table/07459/). Area descriptions
come from SNL (https://snl.no/prisomr%C3%A5der_for_str%C3%B8m). Assumptions:
- NO1 = Østfold, Akershus, Oslo, Innlandet except Lesja/Dovre/Skjåk/Lom, Buskerud except Hallingdal and Numedal, plus Røros
- NO2 = Vestfold, Telemark, Agder, Rogaland, Sunnhordland (Etne, Sveio, Bømlo, Stord, Fitjar, Kvinnherad, Tysnes), plus Numedal/Kongsberg
- NO5 = the rest of Vestland except Nordfjord, plus Hallingdal
- NO3 = Møre og Romsdal, Trøndelag except Namdal and Røros, Nordfjord, plus Lesja/Dovre/Skjåk/Lom
- NO4 = Nordland, Troms, Finnmark, plus Namdal

Result: NO1 0.424, NO2 0.243, NO3 0.137, NO4 0.094, NO5 0.102. This is close to A. NO3 comes out about 1.7 pp lower
than A, which suggests some of the municipalities assigned to NO5 or NO1 above are actually in NO3. The A weights
avoid this mapping error.

**Use weights A** (NO1 .4192 / NO2 .2374 / NO3 .1541 / NO4 .0920 / NO5 .0973).

---

## 2. Norway: Norgespris

### Terms (NVE "Dette er Norgespris", page updated 2026-03-27: https://www.nve.no/reguleringsmyndigheten/kunde/stroem/dette-er-norgespris/)
- **Price: 40 øre/kWh excl. VAT, the same everywhere.** That is 50 øre incl. 25 % VAT. Households in **Nordland,
  Troms and Finnmark** pay no VAT on electricity, so they pay 40 øre. "40 vs 50" is therefore not a north/south price
  split. It is the VAT exemption. Note that the VAT-exempt area is Nordland, Troms and Finnmark, which is not
  identical to NO4: NO4 also includes the Namdal part of Trøndelag, which pays VAT.
- **Cap:** 5,000 kWh/month per metering point for a dwelling (bolig) and 1,000 kWh/month for a cabin (fritidsbolig).
  Consumption above the cap is settled at spot. District-heating households have a separate scheme
  (https://www.regjeringen.no/no/aktuelt/norgespris-og-stromstonad-til-husholdninger-som-bruker-fjernvarme/id3094397/).
  Retailers cite a 4,500 kWh fjernvarme figure: **[UNVERIFIED]**.
- **How it is settled:** the customer keeps their ordinary supply contract and pays spot plus markup to the supplier.
  The grid company credits or debits the difference between spot and 40 øre for each hour on the nettleie bill.
  When spot is below 40 øre, the customer pays the difference to the state. The supplier markup and fees still apply.
- **Start:** ordering opened 2025-09-24 and the scheme took effect 2025-10-01.
- **Binding:** from the order date to **31 Dec 2026**, with a 14-day cancellation right.
- **Who:** households, ordered per metering point by the customer (minside.elhub.no, or via the grid company). It
  applies to the home and to cabins. It is **instead of** strømstøtte: you cannot have both.
- **2027:** the agreement does not roll over, so customers must re-order. Elhub (https://elhub.no/stromkunde/norgespris,
  read 2026-10-04) says: "Pris for 2027 er ikke klar enda, og det er foreløpig ikke mulig å bestille." The scheme is
  approved through 2029-12-31, and price and terms can change each year
  (Polar Kraft, 2026-08-26: https://www.polarkraft.no/aktuelt/norgespris-viderefores-i-2027-dette-vet-vi-sa-langt/).
  The 2027 price will come with Statsbudsjett 2027 (October 2026). It is not known as of 2026-10-04.

### Uptake: share of households on Norgespris
Elhub's live statistics page is https://elhub.no/data-og-innsikt/statistikk-for-norgespris. Its charts are JS-rendered
and could not be read here. The figures below are Elhub numbers republished with dates.

| Date (data) | NO1 | NO2 | NO3 | NO4 | NO5 | All | Source |
|---|---:|---:|---:|---:|---:|---:|---|
| ~2025-10-09 | – | 48 % | – | – | – | ~30 % of households nationally | VG 2025-10-10 https://www.vg.no/nyheter/i/KMOa4M/skyhoeye-septemberpriser-gjorde-norgespris-loennsomt-i-soer |
| 2026-01-07 | 53 % | 68 % | 1.9 % | 0 % | 48 % | 56.9 % of households in the south (NO1+2+5) | NRK 2026-01-10 https://www.nrk.no/norge/bare-57-prosent-har-valgt-norgespris-der-det-lonner-seg-1.17722186 |
| 2026-01-20 | 60 % of meters in the south (NO1+2+5) cover >70 % of household consumption; NO3+NO4 <14,000 meters, <2.5 % of consumption | | | | | | Elhub analysis PDF, https://elhub.no/artikler/hvor-mye-av-stromforbruket-er-knyttet-til-norgespris |
| **2026-08-31** | **64.95 %** (727,503) | **77.36 %** (489,528) | **46.12 %** (189,480) | **0.21 %** (504) | **65.05 %** (168,527) | 1,575,542 households + 245,945 cabins = 1,821,487 meters; Elhub: 59.92 % of all eligible meters | Fortum, updated 2026-09-04, citing Elhub https://www.fortum.com/no/strom/blogg/sa-mange-har-valgt-norgespris |
| 2026-09-04 | 66.35 % | 77.51 % | 47.79 % | ~500 hh | 64.44 % | – | Fortum, updated 2026-09-10 https://www.fortum.com/no/strom/blogg/slik-har-norgespris-slatt-ut-sa-langt-i-ar |

Notes:
- **National household share, derived:** on 2026-08-31, 1,575,542 households had Norgespris against about 2.66–2.68 M
  household meters (Elhub API, section 1). That is **≈ 59 %**. Excluding NO4 it is about 65 %.
- **The share differs strongly by area.** It was high in NO2 and nearly zero in NO4. NO4 spot prices have been far
  below 40 øre, so Norgespris would cost customers there money. NO3 rose from about 2 % in January to about 46–48 %
  by September, after high NO3 prices in 2026 (see also https://trondelagitall.no/artikkel/hoye-strompriser-sa-langt-i-2026-gjor-flere-velger-norgespris).
- The two Fortum snapshots disagree slightly for NO5 (65.05 % on Aug 31, 64.44 % on Sep 4). The denominators
  probably differ. Treat values as ±1 pp.
- Uptake rises with consumption. In the south, January 2026: 77 % of households using over 16 MWh/yr, 62 % of those
  using 8–16 MWh, and 42 % of those using under 8 MWh (Elhub PDF). This matters for a consumption-weighted estimate:
  **the share of household kWh on Norgespris is higher than the share of households** (about 70 % vs 60 % in January).
- Suggested estimator shares as of autumn 2026: NO1 0.66, NO2 0.775, NO3 0.48, NO4 0.002, NO5 0.645. Weighted with
  the section 1 household weights, that gives ≈ 0.59 nationally.

---

## 3. Norway: strømstøtte for households on spot (2026)

Sources: hvakosterstrommen.no (updated 2026-01-10, https://www.hvakosterstrommen.no/artikler/slik-fungerer-stromstotten);
Elinett (https://www.elinett.no/news/stroemstoetteordningen-viderefoeres-i-hele-2026-innslaget-endres-fra-75-til-77-oere);
Ishavskraft (https://www.ishavskraft.no/om/aktuelt/alt-om-stromstotten-i-2026). Official overview:
https://www.regjeringen.no/no/tema/energi/strom/regjeringens-stromtiltak/id2900232/ (returned 403 to the fetcher).

- **Threshold:** 77 øre/kWh excl. VAT (96.25 øre incl. VAT) from 2026-01-01. It was 75 øre in 2025.
- **Coverage:** 90 % of the spot price above the threshold.
- **Settlement:** **hour by hour**, on the hourly area spot price. The day-ahead market has used 15-minute MTUs since
  2025-10-01. Retailers still describe the support as hourly, which presumably means the hourly average of the
  quarter-hour prices: **[UNVERIFIED]**.
- **Cap:** 5,000 kWh/month per metering point. It covers the home only, not cabins, unless someone lives permanently
  in the cabin.
- **Paid by:** the grid company, as a deduction on the nettleie invoice. It is automatic.
- **Still exists alongside Norgespris:** yes, through at least 2026-12-31. A household has either strømstøtte (the
  default) or Norgespris, never both.
- **2027:** not settled as of 2026-10-04. It depends on Statsbudsjett 2027.

**Household energy price per hour h (øre/kWh). Let VAT = 0.25, or 0 in Nordland, Troms and Finnmark:**

```
support_h  = 0.90 × max(0, spot_h_exVAT − 77)            # applies to the first 5,000 kWh in the month
spot customer:
  price_h  = (spot_h + markup − support_h + grid_energy_h + elavgift + enova) × (1 + VAT)
Norgespris customer (consumption ≤ cap):
  price_h  = (40 + markup + grid_energy_h + elavgift + enova) × (1 + VAT)
plus the monthly fixed costs: grid capacity charge (kapasitetsledd) + supplier monthly fee, each × (1 + VAT)
```

For example, at 150 øre spot ex VAT, the support is 0.9 × 73 = 65.7 øre, so the net energy price is 84.3 øre ex VAT.
Above the threshold the household pays 77 + 10 % × (spot − 77).

---

## 4. Norway and Sweden: taxes, grid fees, markups (2026)

### Norway
- **VAT:** 25 %. Households in **Nordland, Troms and Finnmark** are exempt on electricity and nettleie
  (Elhub https://elhub.no/artikler/hva-inngar-i-mine-stromutgifter; NVE page above). By population that is
  489,778 people, 8.7 % of Norway (SSB 2026).
- **Elavgift (forbruksavgift) 2026:** **7.13 øre/kWh excl. VAT**, one rate for the whole year. It was 12.53 øre at
  the end of 2025, and 16.93 earlier in 2025. The reduced rate is 0.60 øre/kWh, for industry and similar users.
  **Households and public administration in Finnmark and the Nord-Troms municipalities Karlsøy, Kvænangen, Kåfjord,
  Lyngen, Nordreisa, Skjervøy and Storfjord are exempt (0 øre).**
  Source: Stortingsvedtak om avgift på elektrisk kraft for 2026, §1 and §3a, https://lovdata.no/dokument/STV/forskrift/2025-12-18-2760/KAPITTEL_1;
  Avgiftssatser 2026, https://www.regjeringen.no/no/tema/okonomi-og-budsjett/skatter-og-avgifter/skatte-og-avgiftssatser/avgiftssatser-2026/id3121982/
- **Enova-avgift:** **1.0 øre/kWh, still charged in 2026.** The government proposed abolishing it from 2026-01-01,
  and Elhub's Aug-2025 page said "blir fjernet i 2026". But Elvia's tariff from 2026-07-01 still lists
  "Enova-avgift 1,0 øre/kWh" (https://www.elvia.no/nettleie/alt-om-nettleiepriser/ny-pris-for-privatkunder-fra-1.-juli-2026).
  Treat it as 1.0 øre. **[Conflicting sources; Elvia's live tariff taken as authoritative]**
- **Typical nettleie for households, 2026.** Example: Elvia, the largest DSO (NO1), from 2026-07-01:
  - Energy component excl. taxes: 28.99 øre/kWh day (weekdays 06–22) and 16.99 øre/kWh night/weekend. Incl.
    elavgift, Enova and VAT that is 46.40 and 31.40 øre/kWh. Before 2026-07-01 the incl.-tax figures were 36.40 and 26.40.
  - Capacity charge (kapasitetsledd), incl. VAT, based on the average of the 3 highest hourly peaks on different
    days in the month: 0–2 kW 150 kr/mo, 2–5 kW 250, 5–10 kW 420, 10–15 kW 585, 15–20 kW 755.
    A typical house sits in the 5–10 kW step (≈ 336 kr/mo excl. VAT). A typical flat sits in the 2–5 kW step.
  - Machine-readable tariffs for every DSO: https://kraftsystemet.no/fri-nettleie/tariffer/elvia.html (and other DSOs
    under /tariffer/). Lnett 2026 tariff booklet: https://www.l-nett.no/getfile.php/131569206-1764934863/Tariffhefte%20fra%201.%20januar%202026.pdf
  - Rule of thumb: the energy component is **~15–30 øre/kWh excl. taxes**, and the fixed part is **~150–420 kr/mo
    excl. VAT** for flats and houses. One secondary summary gives an NVE national average of "56.0 øre/kWh incl.
    fees for 20,000 kWh/yr"; its year and basis are unclear: **[UNVERIFIED]**. NVE's nettleie statistics:
    https://www.nve.no/reguleringsmyndigheten/regulering/nettvirksomhet/nettleie/nettleie-for-forbruk/
- **Supplier markup (spot contracts):** typically 0–5 øre/kWh plus 0–50 kr/mo. **[UNVERIFIED, general market knowledge]**
  Forbrukerrådet's comparison: https://www.forbrukerradet.no/strompris/spotpriser/

### Sweden
- **VAT:** 25 % on everything, including the energy tax.
- **Energiskatt 2026:** **36.0 öre/kWh excl. VAT (45.0 incl.)** from 2026-01-01, down 7.9 öre. There was no change
  during the year. **Reduced rate in 46 northern municipalities: 26.4 öre excl. VAT (33.0 incl.)**, a reduction of
  9.6 öre. The 46 are all of Norrbotten, Västerbotten and Jämtland, plus Sollefteå, Ånge, Örnsköldsvik, Ljusdal,
  Torsby, Malung-Sälen, Mora, Orsa and Älvdalen. Their population is ≈ 815,800, 7.7 % of Sweden (SCB Jul 2026, own
  sum). Most of SE1 and roughly half of SE2 are in this list.
  Source: Energimarknadsbyrån, updated 2026-10-01, https://www.energimarknadsbyran.se/el/dina-elavtal-och-kostnader/fakturering-och-betalning/elrakningen/energiskatt/
  The municipality list comes from general knowledge and its count matches the 46 stated: **[verify against Skatteverket's
  list]**. Elbot's "36.0 incl. VAT" is wrong.
- **Typical elnät transfer fee for 2026, incl. VAT:**
  - Ellevio (Stockholm and others), from 2026-06-01: 26 öre/kWh. Fixed fee 450 kr/mo (16 A) or 590 kr/mo (20 A).
    The effektavgift was removed (https://www.ellevio.se/abonnemang/elnatspriser/hus/).
  - Vattenfall Eldistribution: 44.5 öre/kWh, fixed fee 5,775 kr/yr for a villa on 16 A.
  - E.ON Energidistribution: 91.75 öre/kWh, fixed fee 226.25 kr/mo on 16 A.
  - Ei median, villa 16 A at 5,000 kWh: 4,678 kr/yr excl. VAT, about 94 öre/kWh all-in excl. VAT.
  - Source for the last three: elpris24.se, 2026-09-24, https://elpris24.se/kunskap/elnatsavgift/ **[secondary]**
  - Rule of thumb: **variable 20–90 öre/kWh incl. VAT (~16–73 excl.)**, with ~25–45 öre excl. VAT as a central value.
    Fixed fees run ~150–600 kr/mo for houses and ~100–250 kr/mo for flats.
- **Supplier markup (rörligt pris):** typically 2–8 öre/kWh excl. VAT plus 0–50 kr/mo. Examples: Vattenfall 7.0 öre
  + 45 kr/mo; Tibber 6.0 öre + 49 kr; E.ON 6.0 öre + 40 kr. **[secondary, search summary]**
- **Support schemes in 2026:**
  - A one-off **elstöd** for Jan–Feb 2026 consumption: 14 öre/kWh in SE1/SE2, 26 in SE3, 29 in SE4, capped at
    10,000 kWh per metering point. Försäkringskassan paid it in June 2026 (https://selectra.se/bidrag-och-stod/elstod-2026).
  - A standby **högkostnadsskydd** from Nov 2025 through 2026, triggered if the monthly mean spot price in a zone
    exceeds 1.50 SEK/kWh (Bixia: https://www.bixia.se/press/nyheter/2025/regeringen-infor-sankt-energiskatt-och-nytt-hogkostnadsskydd).
    The exact compensation formula is **[UNVERIFIED]**. For a monthly estimator, model it as nothing unless the zone's
    month average is above 150 öre.

---

## 5. Finland and Denmark (2026)

### Finland
- **VAT:** 25.5 % (since 2024-09-01).
- **Electricity tax class I (households):** **2.325 c/kWh excl. VAT (≈ 2.918 c incl.)** from 2026-04-01. That is
  energy tax 2.24 plus a huoltovarmuusmaksu of 0.085, raised from 0.013. Before April it was 2.253 c excl. VAT
  (2.83 incl.). Source: halpasahko.com (https://halpasahko.com/sahkon-hinnan-muodostuminen/), matched by
  sahkotanaan.fi / grivolt. **[UNVERIFIED against vero.fi, whose rate pages returned 404]** One site
  (porssisahkonhinta.net, 2026-05-18) gives "2.53 c incl. VAT", which conflicts with this. Treat it as an outlier.
- **Grid fee (siirto), 2026, incl. 25.5 % VAT:** the energy fee is **2.8–5.9 c/kWh** and the basic fee is
  4.6–44 €/mo, across 77 DSOs. Urban examples: Helen 4.44 c + 6.01 €/mo; Vantaan Energia 3.10–3.30 c + 5.70–6.00 €/mo.
  Rural examples: Järvi-Suomen Energia 2.89 c + 44.44 €/mo; PKS 3.89 c + 42.04 €/mo (3×25 A).
  Central value: **~3.5 c/kWh + ~10–20 €/mo**, or about 3.0 c/kWh excl. VAT.
  Source: https://www.porssisahkonhinta.net/blogi/sahkon-siirtohinnat-yhtioittain/ (2026-05-18) **[secondary]**
- **Retailer margin on spot (pörssisähkö):** typically 0.2–0.6 c/kWh plus 2–5 €/mo. **[UNVERIFIED]**

### Denmark
- **VAT:** 25 % on everything.
- **Elafgift 2026–2027: cut to 0.8 øre/kWh excl. VAT (1.0 øre incl.)**, from 72.7 øre in 2025. The cut runs from
  2026-01-01 to 2027-12-31. **Verified:** Energi Data Service DatahubPricelist charge `EA-001 Elafgift` = 0.008
  DKK/kWh, valid 2026-01-01 to 2028-01-01. Skat: https://skat.dk/erhverv/afgifter-paa-varer-og-ydelser-punktafgifter/nyhedsbrev-afgifter/midlertidig-nedsaettelse-af-elafgiften-i-2026-og-2027
  Bill: https://www.retsinformation.dk/eli/ft/202512L00024
- **Energinet tariffs (excl. VAT, flat across all hours):** the transmission nettarif is **4.3 øre** and the systemtarif
  is **7.2 øre**, total **11.5 øre/kWh in 2026**. For 2027 the figures are 5.6 + 4.9 = 10.5 øre.
  Source: Energi Data Service, charge codes `40000` and `41000`, GLN 5790000432752; Energinet/Ritzau
  (https://via.ritzau.dk/pressemeddelelse/14552884/elforbrugernes-tarif-bliver-naeste-ar-115-ore-og-falder-dermed-med-15-procent).
  An Energinet "systemabonnement 187 kr/yr" figure appeared only in a search summary: **[UNVERIFIED]**.
- **DSO nettarif C (households), 2026, DKK/kWh excl. VAT.** These are time-of-use tariffs by hour of day, from
  Energi Data Service DatahubPricelist (https://api.energidataservice.dk/dataset/DatahubPricelist), read 2026-10-04.
  Time bands: lavlast 00–06, normal (høj) 06–17 and 21–24, spidslast 17–21.

  | DSO (area) | Period | 00–06 | 06–17, 21–24 | 17–21 | Flat 24 h mean |
  |---|---|---:|---:|---:|---:|
  | Radius (DK2 Copenhagen/N. Zealand), `DT_C_01` | 2025-10-01 → 2026-03-31 | 0.0976 | 0.2929 | 0.8788 | 0.342 |
  | | 2026-04-01 → 2026-09-30 (summer) | 0.1062 | 0.1593 | 0.4141 | 0.189 |
  | | 2026-10-01 → 2027-03-31 (winter) | 0.1062 | 0.3185 | 0.9556 | 0.372 |
  | Cerius (DK2 rest of Zealand), `30TR_C_ET` | 2025-10-01 → 2026-03-31 | 0.1065 | 0.3194 | 0.9582 | 0.373 |
  | | 2026-04-01 → 2026-09-30 | 0.1153 | 0.1730 | 0.4498 | 0.205 |
  | | 2026-10-01 → 2027-03-31 | 0.1153 | 0.3460 | 1.0380 | 0.404 |
  | N1 (DK1 North/Central Jutland), `CD` | 2026-01-01 → 2026-03-31 | 0.0879 | 0.2636 | 0.7907 | 0.308 |
  | | 2026-04-01 → 2026-09-30 | 0.0879 | 0.1318 | 0.3426 | 0.156 |
  | | 2026-10-01 → 2026-12-31 | 0.0879 | 0.2636 | 0.7907 | 0.308 |

  Monthly subscriptions (net abo C forbrug, excl. VAT): N1 28.12 DKK/mo, Cerius 48.25 DKK/mo. Radius was not pulled.
  Other DSOs (TREFOR, Konstant, Dinel, and others) fall within a 24 h mean of ~0.08–0.49 DKK/kWh.
  A typical household has a load-weighted mean about 10–15 % above the flat 24 h mean, because evening use lands in
  the spidslast band. That percentage is **[estimate]**.
- **Supplier markup (spot products):** typically 0–10 øre/kWh plus 0–40 DKK/mo. **[UNVERIFIED]**
- **DK household price per hour (DKK/kWh):**
  `(spot_h + markup + DSO_tariff_h + 0.115 + 0.008) × 1.25`, plus subscriptions × 1.25.

---

## Quick-reference summary (excl. VAT unless stated)

| | VAT | Energy/electricity tax | Grid variable (typical) | Other per-kWh levies | Support |
|---|---|---|---|---|---|
| NO | 25 % (0 % in Nordland, Troms, Finnmark) | 7.13 øre (0 in Finnmark and N-Troms households) | ~17–29 øre (Elvia night/day) | Enova 1.0 øre | strømstøtte 90 % above 77 øre, hourly, ≤5,000 kWh/mo; **or** Norgespris 40 øre fixed (≤5,000 kWh/mo home, 1,000 cabin) |
| SE | 25 % | 36.0 öre (26.4 in 46 northern municipalities) | ~20–75 öre | – | högkostnadsskydd above 1.50 SEK/kWh monthly mean (standby); one-off Jan–Feb 2026 elstöd |
| FI | 25.5 % | 2.325 c (from 2026-04-01) [unverified vs vero.fi] | ~2.2–4.7 c | – | none |
| DK | 25 % | 0.8 øre (2026–27) | DSO ToU 0.09–1.04 DKK (C) | Energinet 11.5 øre | none |

