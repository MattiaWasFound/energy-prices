# mid-b: AO, CD, CG, CM, GA

Consumption basis: 300 kWh/month (lower-middle / upper-middle income default) for AO, CG, CM, GA; 200 kWh/month for CD (low-income default). No country-specific typical-use figure was sourced, except the Cameroon note below.

## AO Angola

- Source: IRSEA tariff table, https://irsea.gov.ao/electricidade/ (Despacho nº 3133/25 of 5 May 2025, in force June 2025, +11.5% average). Customer mix and IRSEA example bills: https://expansao.co.ao/angola/detalhe/familias-vao-pagar-mais-48-pela-luz-e-30-pela-agua-a-partir-de-junho-65434.html, https://www.opais.ao/economia/tarifas-da-electricidade-vao-subir-em-115e-as-da-agua-30-a-partir-de-junho/
- Structure: F = CF x kVA + T x kWh. Doméstica Social I (≤1.3 kVA, ≤120 kWh): 0 + 3.20 Kz/kWh. Social II (3.0 kVA, ≤200 kWh): 0 + 8.33. Doméstica Monofásica (3.0-9.9 kVA): 117.00 Kz/kVA + 14.16 Kz/kWh. Trifásica (>9.9 kVA): 130.00 Kz/kVA + 19.16 Kz/kWh.
- Monofásica is 84% of ENDE customers, so it is the representative tariff. 300 kWh is above the Social II ceiling.
- Bill at 300 kWh, 6.6 kVA (IRSEA's own example power): 117.00 x 6.6 = 772.20; 14.16 x 300 = 4248.00; total 5020.20 Kz, which gives **16.73 Kz/kWh**.
- Check: IRSEA's example of 13,516.16 Kz for 6.6 kVA is exactly 772.20 + 14.16 x 900 kWh, with nothing added, so the published household bills carry no IVA.
- Caveats: whether the 14% IVA applies to domestic electricity could not be confirmed. Lists of exemptions disagree, and distributors are named in the IVA cash-accounting regime. If 14% applied, the price would be 19.07 Kz/kWh. Possible municipal or waste levies on ENDE bills were not verified. The 2025-2028 tariff period may bring further steps ("initial adjustment"), but no 2026 step was found. Confidence: medium.

## CD DR Congo

- Source: SNEL tariff grid on https://www.snel.cd/ ("Grilles tarifaires Basse Tension"). The grid has four semi-annual adjustments. https://infos27.cd/2024/12/24/snel-face-a-lasphyxie-fiscale-fabrice-lusinde-sonne-lalarme-pour-des-reformes-urgentes/ (Dec 2024) says residential customers pay 0.039 USD/kWh, which is the reference average of the 4th adjustment. So the 4th adjustment is in force.
- Structure: "Résidentiel 1" (ordinary metered BT) is declining blocks in USD/kWh: 1-100 0.0388; 101-200 0.0394; 201-300 0.0390; 301-400 0.0386; 401-500 0.0382; 501+ 0.0378. "Résidentiel 2" averages 0.087. Unmetered "forfait" is 2.65 USD per 100 kWh (0.0265/kWh). No meter rental is listed for BT residential.
- Bill at 200 kWh: 100 x 0.0388 = 3.88; 100 x 0.0394 = 3.94; total 7.82 USD, which gives **0.0391 USD/kWh** (energy only).
- Caveats:
  - No separately published prepaid (Cash Power) tariff was found. A blog (not usable as a source) quotes 0.065 USD/kWh for 2026, so the true prepaid price may be higher than the grid.
  - TVA (16% standard) on domestic bills is unverified and not included. With 16% the price would be 0.0454.
  - The ARE and AfDB finished a cost-of-service study in Sept 2026 (https://notreafrik.com/electricite-rdc-tarif-snel/), but no new tariff has been published yet.
  - Confidence: low.

## CG Republic of the Congo

- Source: E2C low-voltage tariff table ("Source : Direction Technique de E²C") as republished on the government investment portal LIZIBA, https://liziba.cg/facteur-de-production-electricite/. It is the 1994-decree grid (39-49 FCFA/kWh, per https://lesechos-congobrazza.com/economie/9168-congo-hausse-du-prix-de-l-electricite).
- Structure: T = Ao (droit à la consommation, monthly fixed) + X x kWh, with prices "hors taxes, hors surtaxes":
  - T1 1.2 kW: 2268 + 49.08
  - T2 2 kW: 2394 + 49.08
  - T3 3 kW: 2550 + 49.08
  - T4 5 kW: 2868 + 44.64
  - T5 9 kW: 3498 + 44.64
  - T6 11.5 kW: 3972 + 43.56
- Bill at 300 kWh, T3: 2550 + 49.08 x 300 = 17,274 FCFA HT. Adding 18% TVA (the rate seen on an E2C bill, https://www.scribd.com/document/918664954/Facture: TVA 13,074 on 72,634 HT) gives 20,383 FCFA, which is **67.94 FCFA/kWh**. T4 (5 kW) would give 63.96.
- Caveats: a tariff increase was announced in Feb 2023 (IMF programme), but no new published grid was found. The sample bill's HT per kWh (about 52.8 at 1376 kWh) is above what the 1994 grid gives, so the grid may be outdated. The surtaxes are unknown, and so is whether TVA applies to domestic consumption. Confidence: low.

## CM Cameroon

- Sources:
  - Tariff: ARSEL, https://arsel-cm.org/tarifs-basse-tension/ (decision 0096/ARSEL/DG/DCEC/SDCT, in force 1 June 2012, still unchanged).
  - Prepaid harmonised to the same grid from 1 Nov 2024: https://www.investiraucameroun.com/gestion-publique/1811-21410-accuse-d-augmenter-les-prix-d-electricite-eneo-clarifie-l-harmonisation-des-tarifs-exigee-par-l-arsel
  - VAT rule: Eneo, https://www.eneocameroon.cm/index.php/fr/eneo-reponds-a-vos-questions-facturation/2972-la-loi-des-finances-2019-a-decide-de-l-exoneration-de-la-taxe-sur-la-valeur-ajoute-tva-sur-certaines-consommations-certains-clients-estiment-qu-eneo-n-applique-pas-convenablement-le-texte-ainsi-pour-une-facture-de-300-kwh-par-exemple-ils-estiment-qu-eneo-ne-doit-appliquer-la-tva-que-sur-80-kwh-epargnant-les-220-premiers-kwh
- Structure: progressive blocks with no fixed charge (meter and breaker fees abolished). The blocks are 0-110 kWh 50, 111-400 79, 401-800 94, and 801-2000 99 FCFA/kWh.
- VAT: Finance Law 2019 art. 128 exempts households at ≤220 kWh/month. Above that, the whole consumption is taxed at 19.25% (17.5% + 10% communal surcharge).
- Bill at 300 kWh: 110 x 50 = 5,500; 190 x 79 = 15,010; subtotal 20,510. TVA 19.25% brings it to 24,458 FCFA, which is **81.53 FCFA/kWh**.
- Caveats: about 80% of Eneo customers stay at or below 220 kWh. At 200 kWh the bill is 110 x 50 + 90 x 79 = 12,610 FCFA, or 63.05 FCFA/kWh with no VAT. The row keeps the 300 kWh default; 63.05 is the figure at sourced typical use. A 15% rise mooted in 2025 was for some professional customers only, not households. Confidence: medium.

## GA Gabon

- Sources:
  - Tariff: SEEG "Tarifs des fournitures d'électricité BT", valid from 01/01/2020, https://www.seeg-gabon.com/med/trf/Presentation_des_tarifs_1582277618493.pdf, plus the full barème https://www.seeg-gabon.com/med/trf/Baremes_revises_1582277696894.pdf.
  - Both are still the documents listed on https://www.seeg-gabon.com/relation_client/tarifs, which also states the reduced TVA of 5% for social tariffs and 3 kW.
- Structure: a flat price per kWh by subscribed power, with no fixed charge.

  | Tariff | HT price | CSE | Taxes | TTC price |
  |---|---|---|---|---|
  | S1 1 kW (≤120 kWh) | 52.40 | none | TVA 5% | 55.02 |
  | S2 2 kW (≤240 kWh) | 84.68 | none | TVA 5% | 88.91 |
  | 3 kW | 111.18 | 5.93 | TVA 5% | 122.96 |
  | 6 kW | 117.36 | 5.93 | TVA 10% + CSS 1% | 136.86 |
  | 9 kW | | | | 142.47 |
  | 12 kW | | | | 147.14 |

  Prepaid (EDAN) uses the same tariffs.
- Bill at 300 kWh on 3 kW: (111.18 + 5.93) x 1.05 = **122.96 FCFA/kWh**. The price is the same at any consumption.
- Caveats: SEEG's site still publishes the 2020 grid and no later per-kWh change was found. Households with 6 kW pay 136.86. From Jan 2026 SEEG collects the taxe forfaitaire d'habitation (a housing tax set by subscribed power, social meters exempt) on a separate invoice: https://www.gabonreview.com/le-patron-de-la-seeg-annonce-des-coupures-delectricite-en-cas-dimpaye-de-la-taxe-dhabitation/. It is not an electricity charge and its amounts are unpublished, so it is excluded. Confidence: medium.

## Currency notes

- CD: SNEL's tariffs are set and stated in USD (snel.cd grid), and households pay in CDF at the day's exchange rate. Prepaid units are bought in CDF, including through mobile money. The figure is given in USD, the tariff's currency. Convert at the BCC rate if CDF is needed.
- AO: AOA (kwanza).
- CG, CM, GA: XAF (CFA franc BEAC).

## Zone candidates

- CD: possibly. The SNEL grid is national, but much of the east (Goma, Bukavu, Butembo) is supplied by private concessionaires such as Virunga Energies and Nuru, whose prices are believed to be several times SNEL's. This could not be verified (no source opened), so there are no numbers. Re-check with ARE or the operators before considering zones.
- AO, CG, CM, GA: none. Each has a single national tariff (Gabon explicitly "applicables sur l'ensemble du Gabon").

## Gaps

- No country is unpriced. Weak points:
  - CG: the grid may predate a 2023 increase, and the surtaxes and TVA scope are unverified (low).
  - CD: no published prepaid tariff and TVA unverified (low).
  - AO: IVA status unverified (medium).
