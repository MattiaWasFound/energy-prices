# Group C: Eastern Caribbean and Virgin Islands (AG AI DM GD KN LC MS VC VG VI)

Household electricity price per kWh, all-in, at 300 kWh/month. No sourced typical household
consumption was found for any of these territories, so the method's default of 300 kWh is used.
Prices are in the currency households are billed in. Researched 2026-10-04. Several utility sites
block plain HTTP clients (LUCELEC, DOMLEC, Dominica News Online). Those pages were read in headless
Chromium and the URLs are the real pages.

## AG Antigua and Barbuda (APUA): 1.28 XCD/kWh, Oct 2026, medium

- Domestic Tariff B: 1-300 kWh at 0.40, above 300 kWh at 0.38. Minimum charge EC$25. No separate customer charge.
  Sources: https://www.apua.ag/customer-service/rates/ and the old tariff sheet
  http://admin.theiguides.org/Media/Documents/APUA%20Tariffs_1.pdf (same rates).
- Fuel Variation Rate: 0.88/kWh from 1 Oct 2026 (it was 0.80 for July-Sept). Source:
  https://antiguaobserver.com/apua-fuel-rate-increase-pushes-october-electricity-bills-higher/
  (the APUA page still shows 0.80, labelled June 2026).
- At 300 kWh: 300 x 0.40 = 120.00, plus 300 x 0.88 = 264.00, gives **EC$384.00**, or **1.280/kWh**.
- Caveat: APUA's tariff shows no ABST line. ABST on domestic electricity was not verified, so it is treated as none.
  The fuel component is about 69% of the bill. Barbuda is billed on the same APUA tariff.

## AI Anguilla (ANGLEC): 1.81 XCD/kWh, Sept 2026, low

- Rates page (Sept 2026): https://www.anglec.com/rates.php. It lists:
  - minimum charge EC$22.00 for 0-40 kWh, then 41-25,000 kWh at 0.63;
  - meter rental EC$5.00;
  - fuel surcharge 1.05/kWh;
  - GST 13%, with domestic accounts exempt on the first 0-130 kWh.
- At 300 kWh:
  - 22.00 + 260 x 0.63 (163.80) + 5.00 + 300 x 1.05 (315.00) = 505.80 before GST.
  - GST: 13% on units 131-300, i.e. 170 x (0.63 + 1.05) = 285.60, which gives 37.13.
  - Total **EC$542.93**, or **1.810/kWh**.
- Big caveat: the Government of Anguilla has run a temporary residential fuel-surcharge subsidy.
  - Households pay about 0.42/kWh of the surcharge and the government pays the rest.
  - It is credited after billing. April 2026 is confirmed paid (721news.com, May 2026).
  - The Anguillian (June 2026) calls it current:
    https://theanguillian.com/2026/06/anglec-addresses-electricity-bill-concerns-and-promises-a-solar-powered-future/
  - The Sept 2026 rates page does not mention it. If it still applies: 22 + 163.80 + 5 + 126.00 + GST 13% x 170 x (0.63 + 0.42) = 23.21, giving EC$340.01, or **~1.13/kWh**.
  - Hence low confidence. Whether GST is charged on the fuel surcharge was also not verified.

## DM Dominica (DOMLEC, regulator IRC): 1.07 XCD/kWh, Oct 2026, medium

- IRC says the new DOMLEC tariff from the rate review takes effect on 1 Oct 2026:
  https://www.ircdominica.org/news/new-electricity-tariff-takes-effect-october-1-what-customers-should-know/.
  The final schedule was not found. The consultation's "Proposed Rates" table is used
  (https://www.ircdominica.org/download/proposed-rates/, OCR of a scanned PDF):
  - Domestic up to 150 kWh: first 50 at 0.5280, above 50 at 0.5870.
  - Domestic above 150 kWh goes on TOU: peak 0.6954, off-peak 0.6354. Customer charge EC$5.
  - Fuel and IPP (geothermal) costs pass through 100% as a per-kWh charge.
- Fuel + geothermal charge: July 2026 = 0.33/kWh (June 0.43; April 0.4953), from Dominica Gazette and DNO.
  August and September values were not found.
- VAT 15%. In IRC's worked example (https://www.ircdominica.org/download/domestic-4-bill-imapct/),
  VAT falls only on energy for kWh above 150 plus the customer charge. Fuel and geothermal are VAT-free.
- At 300 kWh, using IRC's example peak share of 158/250 = 63%:
  - average energy rate 0.632 x 0.6954 + 0.368 x 0.6354 = 0.6733;
  - energy 300 x 0.6733 = 202.00;
  - fuel + geothermal 300 x 0.33 = 99.00;
  - customer charge 5.00;
  - VAT 0.15 x (150 x 0.6733 + 5) = 15.90.
  - Total **EC$321.90**, or **1.073/kWh**.
- Cross-check on the old tariff (50 at 0.578, rest at 0.67, the same surcharge, VAT on energy above 150): about 1.04/kWh.
  The result does not depend much on the tariff assumption.

## GD Grenada (GRENLEC, regulator PURC): 1.38 XCD/kWh, Sept 2026, high

- Rates effective 9 Sept 2026 (https://grenlec.com/customers/ratesandfees/):
  - non-fuel 0.4057/kWh;
  - fuel charge 0.7388/kWh;
  - Fuel Adjustment Clause 0.19490/kWh, applied to the previous period's usage (steady use assumed);
  - RE charge 0.003588/kWh;
  - environmental levy EC$10 flat above 150 kWh.
- VAT is normally 7.5% of the non-fuel charge, with domestic customers exempt on the first 99 kWh.
  It is zero-rated from 1 Aug to 31 Dec 2026 under government relief:
  https://grenlec.com/customer-service/media-release-grenlec-explains-government-relief-measures-for-electricity-customers/
  The same relief gives an EC$50 credit, but only for 1-200 kWh users.
- At 300 kWh: 121.71 + 221.64 + 58.47 + 1.08 + 10.00 = **EC$412.90**, or **1.376/kWh**.
  With normal VAT (7.5% x 201 x 0.4057 = 6.12) it would be 1.397.
- Fuel (charge + FAC) is about 68% of the bill.

## KN Saint Kitts and Nevis: 0.70 XCD/kWh (St Kitts), low

**St Kitts (SKELEC), headline row:**

- Tariff image "effective January 2011", still the one SKELEC posts:
  https://www.skelec.kn/wp-content/uploads/2024/09/ElectricityTariffStructure-Jan2011-scaled.jpg
  - domestic energy: first 50 kWh at 0.59, next 100 at 0.65, above 150 at 0.68;
  - demand charge EC$13.00 per 15 A of fuse rating (or part of 15 A);
  - Fuel Variation Charge (FVC) on top.
- In Nov 2022 SKELEC said the FVC "is currently being subsidized by the Government", shown on the bill and credited back:
  https://zizonline.com/skelec-bills-will-now-show-value-of-fuel-variation-charge/.
  No 2026 FVC value or end of the subsidy was found on SKELEC's site or SKNIS/ZIZ/WINN.
- No VAT on electricity: NEVLEC states this (https://www.nevlec.com/residential/your-bill/vat-impact/).
  The federal VAT applies on both islands.
- At 300 kWh with the FVC subsidised and one 15 A demand unit:
  - energy 29.50 + 65.00 + 102.00 = 196.50, plus demand 13.00, gives EC$209.50, or **0.698/kWh**.
  - With a 60 A service (4 x 13): 248.50, or 0.83/kWh.
- Low confidence for three reasons: the 2026 status of the subsidy is unconfirmed, the demand-charge reading is ambiguous, and the tariff dates from 2011.

**Nevis (NEVLEC):**

- Rates: https://www.nevlec.com/residential/your-bill/electricity-rates/
  - energy: first 50 at 0.65, next 75 at 0.70, above 125 at 0.75;
  - standing charge EC$18 above 250 kWh.
- The fuel surcharge for domestic customers came back in June 2026, after four years at zero paid by the Nevis Island Administration:
  https://www.nevlec.com/important-notice-to-customers-fuel-surcharge-adjustment-effective-june-2026/
  - It was applied at 0.69 in June.
  - NEVLEC's 28 Sept 2026 bill guide uses 0.79/kWh "for residential customers":
    https://www.nevlec.com/wp-content/uploads/2026/09/UnderstandingYourResidentialBill.png
- At 300 kWh: 32.50 + 52.50 + 131.25 = 216.25 energy, + 18.00 standing + 237.00 fuel = **EC$471.25**, or **1.571/kWh**. Medium confidence.

## LC Saint Lucia (LUCELEC, regulator NURC): 1.25 XCD/kWh, Oct 2026, high

- https://www.lucelec.com/content/rates-service-standards (needed a headless browser because of Cloudflare):
  - 2026 base tariff: domestic 1-180 kWh at 0.812, 181+ at 0.862;
  - fuel cost adjustment applied to October 2026 bills: 0.415/kWh (September was 0.356);
  - no rebate is listed;
  - domestic minimum monthly charge EC$5. It is a floor, not added on top.
- At 300 kWh: 180 x 0.812 = 146.16, + 120 x 0.862 = 103.44, + 300 x 0.415 = 124.50, giving **EC$374.10**, or **1.247/kWh**.
- VAT: LUCELEC's sample domestic bill shows "VAT on Electric (0%)" at 217 kWh. The domestic VAT threshold was not
  verified. If VAT applied at 300 kWh, the price would be higher.

## MS Montserrat (MUL): 1.25 XCD/kWh, low

- Customer guide: https://mul.ms/calculating-your-electricity-bill/ and https://mul.ms/understanding-your-electricity-bill/
  - domestic block 1 (0-75 kWh) at 0.48, block 2 at 0.55;
  - fuel surcharge on all units, monthly. The deemed base fuel price is $0.2601 (1974);
  - minimum charge EC$3.50 (Domestic A) or EC$15 (Domestic B), a floor only.
- The only surcharge value MUL publishes is in its worked example: 0.72/kWh on a Dec 2020 bill. MUL has no news or
  tariff notices online, and no 2026 value was found.
- At 300 kWh with 0.72: 75 x 0.48 = 36.00, + 225 x 0.55 = 123.75, + 300 x 0.72 = 216.00, giving **EC$375.75**, or **1.253/kWh**.
- Low confidence: the surcharge is from 2020/21 and 2026 fuel prices are much higher. No VAT was found on the example bill.
  Whether the Government of Montserrat subsidises the tariff was not checked.

## VC Saint Vincent and the Grenadines (VINLEC): 1.34 XCD/kWh, Sept 2026, medium

- Fuel surcharge on September 2026 bills: **79.67 c/kWh**:
  https://www.vinlec.com/public/uploads/files/8.%20FRT%20AUGUST%20%202026%20%28Applicable%20for%20September%202026%29.pdf
  (EC$11.86m excess fuel cost over 14.89m kWh of sales).
- Energy rate and VAT come from VINLEC's sample bill (June 2022):
  https://www.vinlec.com/public/uploads/files/Get%20to%20Know%20Your%20E-BILL-%20FINAL.pdf
  - energy charge 107.00 on 214 kWh, which works out to 0.50/kWh flat;
  - "VAT 16% Over 150 KWh" = 5.12 = 16% x 64 kWh x 0.50. So VAT applies only to the energy charge on kWh above 150; the fuel surcharge is VAT-free.
- At 300 kWh: 300 x 0.50 = 150.00, + VAT 0.16 x 150 x 0.50 = 12.00, + 300 x 0.7967 = 239.01, giving **EC$401.01**, or **1.337/kWh**.
- Caveat: the 0.50 base rate is from 2022 and was not re-confirmed for 2026. Fuel is about 60% of the bill.

## VG British Virgin Islands (BVIEC): 0.51 USD/kWh, Aug 2026 bills, high

- Rates: https://bvielectricity.com/about-us/rates-regulations/
  - 0-60 units at 24c, 61-25,000 at 22.5c, unchanged since 1978;
  - fixed charge $2.50 per month;
  - fuel surcharge added per unit.
- Fuel data for June and July 2026: https://bvielectricity.com/bviecs-monthly-fuel-data-june-july-2026/
  - July gross surcharge 0.34758; after BVIEC's mandatory subsidy the net is **0.27606/kWh** (billed in August);
  - a one-off government credit in September brought July's effective rate to 0.206437;
  - June net was 0.19740.
- At 300 kWh: 60 x 0.24 = 14.40, + 240 x 0.225 = 54.00, + 2.50 + 300 x 0.27606 = 82.82, giving **US$153.72**, or **0.512/kWh**.
  With the one-off credit it would be 0.443. The BVI has no VAT or GST.

## VI US Virgin Islands (WAPA, regulator PSC): 0.43 USD/kWh, Jul-Dec 2026, medium

- WAPA rate breakdown "as of March 1, 2022":
  https://www.viwapa.vi/docs/default-source/default-document-library/electric-rate-infographic.pdf?sfvrsn=a338535c_18
  - Residential, first 250 kWh: energy 0.181456 + LEAC fuel charge 0.222246 + PILOT 0.000686 + self-insurance 0.001925 + OPEB 0.002166 = 0.408479.
  - Residential, other kWh: energy 0.207654 + the same surcharges = 0.434677.
  - Customer charge $4.86.
- PSC kept the LEAC at 22.2226 c/kWh for 1 Jul-30 Sep 2026
  (https://psc.vi.gov/006-26-01-psc-regular-meeting-energy-matters-june-2026/). On 8 Sept 2026 it voted to keep the
  current LEAC through the end of 2026 (https://psc.vi.gov/009-26-02-psc-regular-meeting-telecommunication-energy-matters-september-2026/).
  The press-release value differs from the infographic's 0.222246 only in the 6th decimal.
- At 300 kWh: 250 x 0.408479 = 102.12, + 50 x 0.434677 = 21.73, + 4.86, giving **US$128.71**, or **0.429/kWh**.
- Caveat: no base-rate change after 2022 was found, but the PSC order list was not fully reviewed. WAPA's own
  "kilowatt per hour rate" page still shows Feb 2020 figures (40.03 / 42.65 c), so the site is not consistently updated.

## Currency

- **XCD (Eastern Caribbean dollar)** for AG, AI, DM, GD, KN, LC, MS and VC. All eight are members of the Eastern
  Caribbean Currency Union, and every utility tariff above is quoted and billed in EC$. For example, ANGLEC writes
  "EC$0.63 per k.w.h" and MUL's sample bill totals "XCD 217.36".
- **USD** for VG and VI.
  - The BVI uses the US dollar as legal tender. BVIEC quotes rates in US cents and fuel costs in US$ per gallon.
  - The USVI is a US territory. WAPA bills in USD.

## Zone candidates

- **Saint Kitts and Nevis: yes, about 2.2x.**
  - St Kitts (SKELEC, about 35k people) is roughly 0.70-0.83 XCD/kWh, if the government still subsidises SKELEC's fuel variation charge.
  - Nevis (NEVLEC, about 12k people) is 1.57 XCD/kWh, after the domestic fuel surcharge came back in June 2026 at 0.79/kWh in September.
  - Residents clearly recognise the two islands, with two utilities and two administrations.
  - Caveat: the St Kitts side rests on the 2022 subsidy notice. If SKELEC now bills its FVC, the gap closes.
- Antigua vs Barbuda: same APUA tariff. Not a zone.
- St Vincent vs the Grenadines: VINLEC bills one tariff and fuel surcharge on St Vincent, Bequia, Union Island and
  Canouan. Mustique and Palm Island have private supply, but they are tiny resort populations. Not a zone.
- Grenada vs Carriacou/Petite Martinique: same GRENLEC tariff. Not a zone.
- Anguilla: one territory-wide price. Its unknown is the subsidy, not geography.

## Gaps

- **MS Montserrat:** no current (2026) fuel surcharge was found. MUL publishes no notices online. The figure uses
  the surcharge from MUL's 2020/21 worked example: low confidence, probably an underestimate given 2026 fuel prices.
- **KN (St Kitts):** the current SKELEC fuel variation charge, and whether the government subsidy continues, were not
  found. The demand-charge reading (EC$13 per 15 A) is ambiguous.
- **AI:** unclear whether the government's residential fuel-surcharge subsidy was still in force for Sept/Oct 2026.
  The price is 1.81 without it and about 1.13 with it.
- **DM:** the final approved Oct 2026 tariff schedule was not found, so the proposed rates are used. The latest fuel +
  geothermal charge found is July 2026.
- **VC:** the base energy rate (0.50) comes from a 2022 sample bill.
- **LC:** the domestic VAT threshold was not verified.
- **AG:** ABST treatment was not verified.
