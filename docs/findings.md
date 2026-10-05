# What the research found

The findings behind `prices.json`, one per section. The sources for every
figure are in the `source` columns of the tables in `config/`. Every section
carries a marker line that `tools/browse.py` reads to place it on the browse
page:

    <!-- finding: countries=NO; figure=59% -->

`countries` lists the ISO codes the finding is about (empty for general ones),
and `figure` is an optional headline number. A new finding is a new section with its marker; the page
picks it up on the next `tools/browse.py`.

## Europe's day-ahead market moved to 15-minute slots
<!-- finding: countries=IE,CH; figure=15 min -->
Since delivery day 2025-10-01 every zone in the coupled European auction
publishes 96 quarter-hour prices a day. Ireland's market moved to 30 minutes
on the same date and Switzerland, outside the coupling, is still hourly. The
job reads the resolution from each response, and step_minutes is set per
entry.

## A delivery day is a Central European day, everywhere
<!-- finding: countries=; figure=92 · 96 · 100 -->
Every coupled zone trades 00:00 to 24:00 Central European time, Finland and
Portugal included, so a series starts at 22:00 or 23:00 UTC. Daylight saving
days have 92 or 100 quarter-hours.

## The ENTSO-E token is granted by email
<!-- finding: countries=; figure=1 day -->
Register on the Transparency Platform, then email transparency@entsoe.eu with
the subject "RESTful API access". ENTSO-E promises up to three working days;
ours came the next day. The token is then generated under My Account. Each token may make 400
requests a minute; the job makes about 40 a day.

## Day-ahead prices are not ENTSO-E's to license
<!-- finding: countries= -->
ENTSO-E's CC BY list does not include day-ahead prices: the power exchanges
own them, and the terms ask users not to harm their rights. The file publishes
derived household prices, not raw spot prices, and names the ENTSO-E
Transparency Platform as the source.

## Ireland's prices stopped on 2026-09-29
<!-- finding: countries=IE; figure=29 of 30 -->
On the first live run 29 of the 30 countries with a day-ahead market came back
live. ENTSO-E has published nothing for the Irish market since 2026-09-29, so
Ireland is priced from the country table until it returns, with no change
needed. ENTSO-E and Energi Data Service agree to the hundred-thousandth of a
euro where both cover an area.

## Two auctions for Germany and Austria
<!-- finding: countries=DE,LU,AT -->
DE-LU and AT publish two day-ahead auctions, both in 15-minute slots: the
coupled European auction (sequence 1) and EXAA (sequence 2). The only way to
tell them apart is the sequence number; the job keeps sequence 1.

## Britain left the platform after Brexit
<!-- finding: countries=GB; figure=0% VAT -->
Great Britain has published nothing on ENTSO-E since 2021-06-15, so it is
priced from the Ofgem price cap: 26.32 p/kWh plus 54.83 p/day for October to
December 2026, about 33.7 p/kWh at typical use. VAT on household electricity
is 0% from 2026-10-01 to 2027-03-31.

## A keyless Danish source covers six areas
<!-- finding: countries=DK,DE,NO,SE; figure=6 areas -->
Energinet's Energi Data Service publishes day-ahead prices for DK1, DK2,
DE-LU, NO2, SE3 and SE4 with no key. Its dataset was renamed when the market
moved to 15 minutes (Elspotprices became DayAheadPrices). The job uses it
as the backup for those areas.

## Denmark nearly abolished its electricity tax
<!-- finding: countries=DK; figure=0.8 øre -->
Elafgift fell from 72.0 to 0.8 øre/kWh, the EU minimum, for 2026 and 2027
only. Energinet's tariffs fell from 13.5 to 11.5 øre. Together they cut about
0.73 DKK/kWh before VAT, so Eurostat's 2025 figures overstate Danish prices
by roughly a third.

## Norgespris is 40 øre before VAT, everywhere
<!-- finding: countries=NO; figure=40 øre -->
Norway's fixed-price scheme is 40 øre/kWh excluding VAT in every price area.
The "50 øre" figure is the same price with 25% VAT; households in Nordland,
Troms and Finnmark pay no VAT and so pay 40. It replaces the energy price only;
grid tariffs and taxes still apply.

## Most Norwegian households chose Norgespris
<!-- finding: countries=NO; figure=59% -->
By 31 August 2026 about 59% of household meters were on Norgespris (Elhub):
77% in NO2, 65% in NO1 and NO5, 46% in NO3 and 0.2% in NO4, where spot prices
are far below 40 øre. Larger users chose it more often. The file offers it as
an option beside the spot price.

## Strømstøtte caps the spot price for everyone else
<!-- finding: countries=NO; figure=90% -->
Households on spot get 90% of the price above 77 øre/kWh (excluding VAT)
back, hour by hour, up to 5,000 kWh a month. The job applies it per slot, so
a Norwegian live price rises only a tenth as fast as spot above the threshold.

## Sweden cut its energy tax
<!-- finding: countries=SE; figure=36.0 öre -->
Energiskatt fell from 43.9 to 36.0 öre/kWh in 2026. The 46 northern
municipalities pay 9.6 öre less, which covers nearly all of SE1 and about half
of SE2, so those zones carry a lower add-on.

## Where Swedes and Norwegians live, by price zone
<!-- finding: countries=SE,NO; figure=68% -->
No statistics office publishes population per price zone. Household metering
points do: SCB counts 68% of Swedish homes in SE3 and 21% in SE4; Elhub counts
42% of Norwegian homes in NO1 and 24% in NO2. These weight the country
averages.

## Italians pay one national price
<!-- finding: countries=IT; figure=7 zones -->
Italy has seven day-ahead zones, but households pay the PUN Index, the
purchase-weighted mean of the zones, through an equalisation component. ARERA
has announced a gradual move to zonal prices with no date set. The file
weights the seven zones by ISTAT population, close to the PUN Index.

## Regulated prices sit below the market
<!-- finding: countries=HU,RS,ME,MK,BG,HR,FR,PL,SK,CH -->
In Hungary, Serbia, Montenegro and North Macedonia the regulated household
price is below the wholesale price, so the derived add-on is negative; in
Bulgaria and Croatia it is close to zero. The live curve there is one
households never see. table_instead_of_live can price these countries from
the table instead; they are kept live for now.

## How the add-on is derived
<!-- finding: countries= -->
For each live country: Eurostat's household price excluding VAT (2025-S2,
2,500 to 5,000 kWh a year) minus Ember's mean wholesale price over the same
months, plus the tax changes since. It includes standing charges spread per
kWh, so it is a household average, not a tariff.

## Norway's household is bigger than Eurostat's
<!-- finding: countries=NO; figure=1.31 NOK -->
Eurostat's band is 2,500 to 5,000 kWh a year; a typical Norwegian home uses
about 16,000. Spread over fewer kWh, the fixed grid charge makes the derived
add-on 1.31 NOK against roughly 0.6 bottom-up. It is kept for consistency with
every other country.

## Bulgaria bills in euros now
<!-- finding: countries=BG; figure=1.95583 -->
Bulgaria adopted the euro on 2026-01-01. Eurostat still reports 2025 in leva,
converted at the fixed rate of 1.95583.

## Portugal's effective VAT is not 23%
<!-- finding: countries=PT; figure=14.8% -->
The first band of a household's consumption is taxed at 6% and the rest at
23%, so a typical bill carries about 14.8% (Eurostat's ratio). The file uses
the effective rate.

## Estonia is the one country that got dearer
<!-- finding: countries=EE; figure=+1.29 c -->
A new security-of-supply charge, a balancing capacity fee and two excise steps
add about 1.29 c/kWh in 2026, after VAT rose to 24% in July 2025. Most of
Europe's household taxes fell.

## Temporary cuts to watch
<!-- finding: countries=AT,LU,ES,UA -->
Austria's electricity tax is 0.1 c instead of 1.5 c for 2026 only.
Luxembourg pays a 4 c subsidy from August to December 2026. Spain cut VAT to
10% from March to May 2026 and may do so again. Ukraine's fixed 4.32 UAH runs
to 2026-10-31 with nothing decided after.

## Eurostat misses Albania's tariff cut
<!-- finding: countries=AL,MD; figure=8.5 ALL -->
Albania's regulator cut the household tariff to 8.5 ALL/kWh before VAT in
February 2025, but Eurostat still shows 9.5; the file uses the regulator's
figure. Moldova charges no VAT on household electricity and its current
regulated price is below Eurostat's 2025 value.

## Exchange rates: two sources, chosen for their licences
<!-- finding: countries=; figure=153 -->
The ECB's reference rates (about 30 currencies, reuse with attribution) come
first; Frankfurter, a blend of about 100 central banks, covers the rest of the
153 billing currencies. Rejected: open.er-api forbids redistribution, and
fawazahmed0 has no stated provenance and showed the Syrian pound 100 times
too weak.

## EIA's price leaves out the household's taxes
<!-- finding: countries=US; figure=+3.7% -->
EIA's residential price is revenue divided by kWh sold. It includes energy,
delivery, fixed charges and the taxes the utility pays, but most likely not
sales tax or city utility taxes levied on the household. Adding those per
state moves the national figure from $0.1831 to $0.1898 for July 2026.

## US electricity taxes are a patchwork
<!-- finding: countries=US; figure=0–9% -->
Twenty-odd states exempt household electricity; others charge their full
sales tax (Indiana and North Carolina 7%). Utah adds a city energy tax of up
to 6% to a 2% state rate. New York City charges 4.5% though the state exempts
it. Wisconsin dropped its summer tax from 2025-10-01.

## Canada publishes no national price
<!-- finding: countries=CA; figure=0.168 CAD -->
Neither Statistics Canada, the energy regulator nor Natural Resources Canada
publishes a national household price, so the country average weights the 13
provinces and territories by population.

## Canada's open sources were not open enough
<!-- finding: countries=CA -->
The only survey covering every province allows non-commercial reuse only,
and Hydro-Québec's city comparison is all rights reserved. Every row was
rebuilt from the utility's own published tariff at 1,000 kWh a month, taxes
and rebates included, within 4% of the earlier figures.

## A fourfold gap across Canada
<!-- finding: countries=CA; figure=4× -->
Québec pays 9.7 ¢/kWh and the Northwest Territories 41 ¢, where most power
comes from diesel. Ontario's prices reset every 1 November, so its row is due
then.

## Russian tariffs rise in October, not July
<!-- finding: countries=RU; figure=+11.3% -->
Household tariffs rose 1.7% on 2026-01-01, passing through VAT going from 20%
to 22%, then 11.3% on average on 2026-10-01. The economy ministry forecasts
8.6% for 2027 and 9.1% for 2028, also from 1 October.

## A sixfold gap across Russia
<!-- finding: countries=RU; figure=6× -->
Irkutsk pays 2.10 RUB/kWh, cheap hydropower, and Chukotka 12.84. The file
uses the urban single-rate tariff for homes without electric stoves; the
population-weighted average is 7.10.

## Occupied territories are left out
<!-- finding: countries=RU,UA -->
The Russian regulator's tariff order lists Crimea, Sevastopol and the
occupied parts of Donetsk, Luhansk, Zaporizhzhia and Kherson. They are not in
the Russian zone list; only subjects with an ISO 3166-2:RU code are.

## 240 countries priced from data
<!-- finding: countries=; figure=240 / 250 -->
29 European countries are live. Every other country was priced from its
regulator's or main utility's published residential tariff, computed at a
stated monthly use with fixed charges and taxes, or from an official average.
No commercial price table was used as a source. Yemen and Pitcairn take their
region's average, seven uninhabited territories carry a labelled guess, and
North Korea has no price.

## Zone candidates beyond the first three
<!-- finding: countries=KZ,IQ,SO,KN; figure=5 -->
Kazakhstan (about 1.9x, north and west against Almaty), Iraq (Kurdistan about
7x the federal rate), Somalia (member states about 3x Mogadishu) and St Kitts
and Nevis (about 2.2x between the islands) also meet the rule for zones, with
Mexico. Argentina and China may; neither was confirmed.

## Mexico's tariff zones even out at real consumption
<!-- finding: countries=MX; figure=1.15x -->
CFE's climate tariffs (1, 1A to 1F) look 3x apart at the same consumption: 300
kWh in July costs 3.16 MXN/kWh on Tarifa 1 and 0.98 on 1F. But hot zones get
bigger subsidised blocks because they use more, and at each zone's own typical
use the yearly price is 1.17 to 1.35 MXN/kWh. That fails the 2x rule, so
Mexico has one national price, 1.327 MXN/kWh at 140 kWh a month, the
user-weighted mean of the seven tariffs. An earlier figure of 2.88 was
Tarifa 1 at 250 kWh, right under the DAC penalty threshold.

## Four more countries got zones
<!-- finding: countries=KZ,IQ,SO,KN; figure=31 zones -->
Kazakhstan (20 regions, 23.86 to 45.51 KZT), Iraq (Kurdistan Region 82.74 IQD
against 10 in federal Iraq), Somalia (Banaadir, the five member states and
Somaliland, 0.41 to 1.00 USD) and St Kitts and Nevis (0.70 against 1.57 XCD).
Each country's average is now the population-weighted mean of its zones.

## Svalbard and the Central African Republic left the averages
<!-- finding: countries=SJ,CF; figure=1.20 NOK -->
Longyearbyen households pay Svalbard Energi a flat 1.20 NOK/kWh with the fixed
charge folded in, against 3.14 from the Northern Europe mean. The Central
African Republic gets ENERCA's 83 XAF/kWh all-customer average from World Bank
project documents, low confidence. Vatican City takes Italy's price; Yemen and Pitcairn stay on averages.

## Yemen has two rials and no usable exchange rate
<!-- finding: countries=YE; figure=2 rials -->
A Sana'a household pays about 300 old rials per kWh on the public grid and an
Aden household 19 new rials, 40 to 50 times apart in real terms. Both rials
use the code YER, and the job's rate source quotes about 266 per euro, which
matches neither (about 600 and 1,800). Imported, Yemen's price would read
2.3 times too high in euros and lift the Western Asia mean, so Yemen stays on
the regional average.

## Seven guesses and one blank
<!-- finding: countries=KP,AQ,BV,GS,HM,IO,TF,UM; figure=7 + 1 -->
Seven territories have no households at all. Rather than a regional average
(Bouvet sat in "South America"), they get a labelled educated guess: South
Georgia the Falklands' price, the rest about 0.50 EUR/kWh, what inhabited
remote islands on diesel pay (Falklands, St Helena, Norfolk Island and the
Cook Islands: 0.41 to 0.55). North Korea is the one blank: a 2026 survey
found 650 won a month for 2 to 2.5 hours of power a day, not a per-kWh
price, and the official won rate is about 500 times the market's.

## Official exchange rates flatter some prices
<!-- finding: countries=CU,TM,MM,VE,IR,LB,SY -->
The job converts at official reference rates. Where the street rate is far
weaker, the euro price looks higher than a household feels it: Cuba's official
rate is 24 pesos to the dollar against a floating 695, Turkmenistan's about a
tenth of the street rate. Lebanon's utility bills in dollars, so its row is in
dollars.

## Subsidies set the floor
<!-- finding: countries=IR,LY,TM,IQ,BH,KW,VE,BN; figure=<1 cent -->
The cheapest household electricity in the file is heavily subsidised. Iran,
Libya, Turkmenistan, Iraq and Bahrain (citizens' tariff) come out below one
euro cent per kWh at official exchange rates; Kuwait, Venezuela and Brunei at
one to three cents. The sanity bound was lowered to 0.001 EUR/kWh so these
real figures pass.

## The Gulf prices households by nationality
<!-- finding: countries=AE,KW,QA,BH,OM,SA -->
Bahrain, Qatar, Kuwait and the UAE charge citizens and expatriates different
tariffs, up to nine times apart. The file uses the tariff most households pay:
expatriate rates where most households are foreign, the citizens' rate in
Bahrain. Oman and Saudi Arabia charge everyone the same.

## India's household price is mostly subsidy
<!-- finding: countries=IN; figure=3.06 INR -->
From the Central Electricity Authority's tariff book at the national average
household use of 109 kWh a month, weighted by household connections, after
state free-electricity schemes: 3.06 INR/kWh. Before those schemes it is 5.78.

## Island grids pay the most
<!-- finding: countries=VU,SB,BQ,NC,AI,SH,NF,FM,MH; figure=€0.45–0.96 -->
Small island grids that burn imported diesel charge households the most in the
file: Vanuatu about 0.96 EUR/kWh, Solomon Islands 0.76, Bonaire, New Caledonia
and Anguilla about 0.60, then Saint Helena, Norfolk Island, Micronesia and the
Marshall Islands around 0.5. Fuel surcharges reset monthly, and some prices
include temporary government fuel caps (Cayman Islands, Turks and Caicos) that
end around the turn of the year.
