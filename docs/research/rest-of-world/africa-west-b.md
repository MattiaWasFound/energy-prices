# west-b: BJ, TG, NE, ML, MR, GM, GN, GW

Consumption basis: 200 kWh/month for World Bank low-income countries (TG, NE, ML, GM, GW) and 300 kWh/month for lower-middle-income ones (BJ, MR, GN). No country-specific typical household use was sourced. All XOF countries bill in FCFA (XOF). Prices are per kWh, all on-bill items included.

## BJ Benin

- Sources:
  - SBEE tariff page: https://sbee.bj/particuliers/tarifications/. Postpaid BT: social 88 FCFA/kWh if consumption is under 20 kWh in 30 days. Otherwise 0-250 kWh at 125 and above 250 kWh at 148. Prime fixe 500 FCFA/kVA/month. Prepaid is a flat 125 + 500 FCFA/kVA.
  - On-bill taxes, from the January 2021 tariff change (decree 2020-328) as reported in https://daabaaru.bj/benin-hausse-du-prix-de-lelectricite-de-la-sbee-les-associations-de-consommateurs-informes-sur-les-nouveaux-tarifs/: TVA 18%, taxe électricité 2 FCFA/kWh, contribution électrification rurale 3 FCFA/kWh.
  - The ARE decision of 13 Oct 2025 keeps the BT1 grid (88/125/148) for 2026-2027: https://lamarinabj.com/index.php/2025/10/20/tarifs-de-lelectricite-au-benin-la-sbee-obtient-le-feu-vert-de-lare-pour-2026-2027/
- Structure: above 20 kWh the social price is lost, so all kWh go into the 125 block. That is how the SBEE page and the GitHub calculator (https://github.com/Bull1016/calculateur-facture-electricite) read it.
- Bill at 300 kWh, 3 kVA subscription (assumed):
  - Energy: 250 x 125 + 50 x 148 = 38,650
  - Prime fixe: 3 x 500 = 1,500
  - TVA: 18% x 40,150 = 7,227
  - Levies: 5 x 300 = 1,500
  - Total 48,877 FCFA, which gives **162.92 FCFA/kWh**.
- Caveats:
  - If the first 20 kWh stayed at 88 (as some third-party guides say), the price would be 158.96.
  - Prepaid BT (flat 125 + 500/kVA, same taxes assumed) at 300 kWh: 37,500 + 1,500 + 7,020 TVA + 1,500 levies = 47,520, which gives 158.40. No official prepaid share was found.
  - The subscribed kVA is an assumption; each extra kVA adds about 2 FCFA/kWh.
  - It is unclear whether SBEE's published 88 already contains the 2 F taxe électricité, since the decree says 86.
  - Confidence: medium.

## TG Togo

- Source: CEET tariff page https://services.ceet.tg/informations-utiles, per Arrêté interministériel N°072/MMRE/MEF/MPDC/MCACL of 24 March 2025, in force 5 May 2025 (+12.5% average). Prices are HT.
- VAT and EP rules, from CEET "Bon à savoir" (https://services.ceet.tg/bon-a-savoir) and the Togo CGI social-tranche exemption (https://investirautogo.tg/media/CGI%20(art.%20308%20-%20399).pdf):
  - TVA 18% applies to energy and redevance puissance.
  - The first 100 kWh/month are VAT-exempt for residential customers with ≤2.2 kVA.
  - The redevance éclairage public (EP) is 5 FCFA/kWh (raised from 1 to 5 in March 2019) and carries no TVA.
- Grid:
  - Prepaid (Cash Power), domestic, <2.2 kVA: 0-30 kWh 70; 31-120 kWh 88; 121-350 kWh 123; >350 kWh 145. No monthly fixed charges for <2.2 kVA (≥2.2 kVA pays 600/kVA + 500 + 500).
  - Postpaid, <2.2 kVA: 60 / 93 / 130, plus 250 + 500 + 500 FCFA/month.
- Bill at 200 kWh, prepaid <2.2 kVA (the common household meter):
  - Energy: 30 x 70 + 90 x 88 + 80 x 123 = 19,860
  - TVA: 18% x (19,860 - 8,260 exempt first 100 kWh) = 2,088
  - EP: 5 x 200 = 1,000
  - Total 22,948 FCFA, which gives **114.74 FCFA/kWh**.
- Postpaid <2.2 kVA at 200 kWh gives about 125.4 FCFA/kWh.
- Caveats:
  - No official prepaid/postpaid customer split was found.
  - The taxe d'habitation is collected through CEET bills (https://www.togofirst.com/fr/finances-publiques/1301-9240-togo-la-taxe-d-habitation-passe-sur-les-factures-d-electricite-de-la-ceet). It is a property-occupancy tax collected half-yearly, not an electricity charge, so it is excluded.
  - Confidence: medium-high, rendered as "medium" in the CSV.

## NE Niger

- Source: the regulator ARSE's NIGELEC bill simulator, https://arse.ne/simulateur-facture-nigelec/. Its JavaScript carries the tariff codes and the tax rules.
- The 2018 tariff structure (decree 2017-796) is still in force: ARSE says tariff increases have not been applied since 2022, per the World Bank / M300 Niger energy compact https://thedocs.worldbank.org/en/doc/aa1c1df323bc70ef9a9b0b0aa7ba8144-0010012025/original/M300-AES-Compact-Niger.pdf.
- Structure:
  - Social (3 kW, ≤50 kWh): 59.45 FCFA/kWh, prime 250.
  - Code 331 BT ménage (3 kW): 0-150 kWh 68.37; 151-300 kWh 89.82; >300 kWh 127.27; prime fixe 1,278/month; taxe d'habitation 200.
  - TVA 19%, with the first 150 kWh exempt.
  - Taxe kWh 2 F/kWh; ORTN (radio-TV) 3 F/kWh.
- Bill at 200 kWh, 3 kW ménage:
  - Energy: 150 x 68.37 = 10,255 and 50 x 89.82 = 4,491, total 14,746
  - TVA: 19% x 4,491 = 853.29
  - Prime fixe: 1,278
  - Taxe kWh: 400
  - ORTN: 600
  - Taxe d'habitation: 200
  - Total 18,077 FCFA, which gives **90.39 FCFA/kWh**.
- Caveats:
  - On prepaid, prime and taxe d'habitation are charged only on the first top-up of the month, so the result is the same per month.
  - The taxe d'habitation is a flat on-bill municipal charge, included here because it appears on every electricity bill.
  - Tariffs are frozen despite cost pressure, and an increase is possible.
  - Confidence: high.

## ML Mali

- Source: EDM-SA's own BT bill simulator, https://www.edmsa.ml/service/simulateur-conso-bt. The tariff parameters were read from its backend for Bamako.
- Grid, social tariff (2 fils 5 A):
  - Blocks: 0-50 kWh 59; 51-100 kWh 94; 101-200 kWh 109; >200 kWh 130 FCFA/kWh. TVA 18% on blocks 3-4 only.
  - Entretien/location compteur: 176 + 18% TVA.
  - Redevance éclairage public, Bamako: 320/month.
- Grid, normal tariff (10 A):
  - 0-200 kWh 109; >200 kWh 130, all with TVA 18%.
  - Entretien/location: 540 + TVA.
  - EP, Bamako: 592.
- The social block structure dates from the 2013 CREE adjustment (social 0-50 kWh at 59 unchanged, other blocks +3-5%): https://maliactu.net/nouvelle-grille-tarifaire-de-lelectricite-et-de-leau-pas-daugmentation-pour-les-petits-consommateurs/. BT tariffs have been unchanged since about 2014, per L'Essor of July 2024 (https://lessor.ml/posts/mali-crise-energetique-la-hausse-des-tarifs-est-elle-inevitable-668d7ef8ea83c), which says a rise is under discussion but none had been applied.
- Bill at 200 kWh, social tariff (5 A), Bamako:
  - Energy: 50 x 59 + 50 x 94 + 100 x 109 = 18,550
  - TVA: 18% x 10,900 = 1,962
  - Meter: 176 + 32 TVA
  - EP: 320
  - Total 21,040 FCFA, which gives **105.20 FCFA/kWh**.
- On the normal 10 A tariff at 200 kWh: 21,800 + 3,924 + 540 + 97 + 592 = 26,953, which gives 134.77 FCFA/kWh.
- Caveats:
  - EDM warns that the simulator "may not be up to date".
  - A March 2024 EDM statement announced an increase, but no new BT grid was found (https://www.newafrique.net/articles/38X01gAqYYepNM07ASsM).
  - The EP levy varies by town.
  - Prepaid (ISAGO) applies the same blocks plus a stamp duty per purchase (not included).
  - No social/normal customer split was found.
  - Confidence: medium.

## MR Mauritania

- Source: SOMELEC "Tarifs Basse Tension" table, https://somelec.mr/sites/default/files/Tarifs%20Basse%20Tension.xls, linked from https://somelec.mr/?q=node/1414 (posted 2021, file dated April 2021).
- Grid:
  - Tarif social: 2.459 MRU/kWh, prime fixe 27.991.
  - Domestique 6 kVA: 5.903 MRU/kWh, prime fixe 165.072 (9 kVA: 340.439; 12 kVA: 701.473).
- The social rate matches the 24.59 old ouguiya after the March 2020 20% cut (https://fr.saharamedias.net/la-somelec-dement-laugmentation-de-la-tarification-de-lelectricite/). The domestic rate is otherwise unchanged since the 2000s.
- A May 2025 prepaid receipt (50.12 kWh for 300 MRU, https://www.scribd.com/document/865716544/80248062988-1325052103464393328) shows 5.99 MRU/kWh, consistent with 5.903 still being in force (sanity check only).
- VAT: 16% (CGI 2023, https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf). Electricity up to 150 kWh per month per consumer is VAT-exempt (art. on exemptions, item 15).
- Bill at 300 kWh, domestic 6 kVA:
  - Energy: 300 x 5.903 = 1,770.90
  - Prime fixe: 165.07
  - TVA: 16% x (150 x 5.903 + 165.07) = 168.08
  - Total 2,104.06 MRU, which gives **7.01 MRU/kWh**.
- Caveats:
  - The eligibility ceiling of the social tariff (2.459) was not found. Small households on it pay about 2.6-3 MRU/kWh.
  - It is assumed that the prime is monthly and taxable.
  - The VAT exemption is read as applying to the first 150 kWh of every bill. If it instead applies only to bills of ≤150 kWh, the whole bill would be taxed, giving 7.49 MRU/kWh.
  - Prepaid (Mounsif) customers pay no prime.
  - The tariff file dates from 2021, and no 2022-2026 change was found.
  - Confidence: medium.

## GM Gambia

- Source: the PURA electricity and water tariff table, https://pura.gm/economic-regulations/tariff/electricity-tariff/, mirrored on NAWEC's tariff page https://nawec.gm/?page_id=203.
  - "2023 determined rates", domestic credit meters: 0-300 kWh 13.85; 301-600 kWh 14.06; 601-1000 kWh 14.43; >1000 kWh 15.46 GMD/kWh.
  - Prepaid domestic: flat 13.85 GMD/kWh.
- Effective 10 April 2023 (The Point, https://thepoint.gm/africa/gambia/headlines/water-electricity-tariffs-to-increase-from-april-10th).
- No increase since: in Nov 2024 the government paid NAWEC US$20M to avoid a tariff increase (https://thepoint.gm/africa/gambia/headlines/govt-invests-us20m-to-avoid-electricity-tariff-increment).
- VAT: the standard rate is 15%. The GRA VAT brochure lists "monthly domestic electricity consumption below 1,000 kWh" as exempt (https://www.gra.gm/download-file/8d0cfa28-d217-11ed-9b31-029254d29bb1).
- No fixed or service charge is published.
- Bill at 200 kWh, prepaid (or credit meter, first block): 200 x 13.85 = 2,770 GMD, which gives **13.85 GMD/kWh**.
- Caveats:
  - The GRA brochure is undated and does not explicitly cover prepaid purchases.
  - No lifeline tariff was found.
  - Confidence: medium.

## GN Guinea

- Source: EDG "Nouveaux Tarifs DCO EDG", tariff order of 3 Sept 2021, image on https://edg.com.gn/service/comprendre-ma-facture/ (https://edg.com.gn/wp-content/uploads/2023/02/Nouveaux_Tarifs_DCO_EDG_03092021-2-scaled.jpg).
  - Prepaid, domestic private BT monophasé: 1.1-3.3 kVA (5-15 A) 387 GNF/kWh; 4.4-9.9 kVA 453.
  - Postpaid, domestic: 1-40 kWh 107; 41-330 kWh 387; >330 kWh 453. Prime fixe 10,000 GNF monophasé, 20,000 triphasé.
- Per Guineematin (Apr 2023, https://guineematin.com/2023/04/20/edg-comment-minimiser-sa-consommation-et-payer-sa-facture/), the whole month is billed at the tier its consumption falls in (non-progressive).
- Still in force in 2026: on 2 Jul 2026 the energy minister said the kWh is billed "à environ 400 GNF" while the real cost is about 1,500 (https://mosaiqueguinee.com/2026/07/laye-sekou-camara-subvention-edg-ne-recoit-aucun-franc-cest-le-gap-entre-le-cout-reel-et-le-prix-de-vente-que-letat-prend-en-charge/).
- Bill at 300 kWh, prepaid monophasé ≤3.3 kVA: flat 387 x 300 = 116,100 GNF, which gives **387 GNF/kWh**.
- Postpaid at 300 kWh: 300 x 387 + 10,000 prime = 126,100, which gives 420.3 GNF/kWh. Progressive reading: 40 x 107 + 260 x 387 + 10,000 = 114,900, which gives 383.0.
- Caveats:
  - TVA and other on-bill taxes could not be verified and are not included. A TVA at 18% would make the price 456.7.
  - No prepaid/postpaid customer split was found.
  - Guineematin dates the grid to 29 June 2021; the EDG image is dated 3 Sept 2021.
  - Some press articles quote 800 or 1,100-1,200 GNF/kWh for prepaid. These could not be verified and conflict with the minister's ~400.
  - Confidence: medium (tariff verified at the utility, taxes unverified).

## GW Guinea-Bissau

- Sources:
  - Domestic blocks as given by the energy minister in Feb 2019 (La Tribune, https://www.latribune.fr/economie/strategies/2019-02-07/guinee-bissau-annonce-d-une-prochaine-baisse-de-50-du-cout-de-l-electricite-806607.html): 0-50 kWh 81; 51-200 kWh 161; >200 kWh 322 XOF/kWh. A 50% cut was announced then, but no evidence shows it was applied.
  - World Bank completion report P148797 (Feb 2025), which describes an "outdated tariff (electricity: CFAF 231 per kWh)", most likely an average across all customers: http://documents.worldbank.org/curated/en/099021425153021775/pdf/BOSIB178d1f59d03f1bac81be9db3fca262.pdf
- Bill at 200 kWh (progressive blocks assumed): 50 x 81 + 150 x 161 = 28,200 XOF, which gives **141.00 XOF/kWh**.
- Caveats:
  - No EAGB or regulator tariff document could be found (EAGB's site is empty).
  - Whether the blocks are progressive or all-units is unknown. All-units at 161 would give 161.
  - IVA was introduced in Jan 2025 (Lei 4/2022), but its application to household electricity is unknown, so it is not included.
  - Fixed charges are unknown.
  - The WB average of 231 XOF/kWh suggests households may pay more.
  - Confidence: low.

## Currency notes

- BJ, TG, NE, ML, GW are billed in West African CFA franc (XOF), at 1 EUR = 655.957 XOF.
- MR is billed in the new ouguiya (MRU), in place since the 2018 redenomination (1 MRU = 10 old MRO). SOMELEC's table is in MRU (2.459 social = 24.59 old ouguiya, matching the 2021 SOMELEC statement).
- GM is billed in dalasi (GMD) and GN in Guinean franc (GNF). None of these countries is dollarised or has dual rates.

## Zone candidates

- None. All eight countries have a single national tariff grid from a single dominant utility.
- Mali's public-lighting levy varies by town, but by far less than 2x.
- Off-grid and mini-grid tariffs (e.g. Mali AMADER/rural concessions, Niger/Guinea mini-grids) can be much higher, but they serve a small share of households.

## Gaps

- No country is unpriced.
- Low-confidence items:
  - GW: no official tariff document; the grid is from a 2019 press report and the IVA status is unknown.
  - GN: TVA and on-bill taxes unverified.
  - MR: social tariff eligibility unknown, and whether the prime fixe is monthly is unverified.
  - ML: the EDM simulator carries a "may not be up to date" disclaimer, and a 2024 increase was announced without a published BT grid.
