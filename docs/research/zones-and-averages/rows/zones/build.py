# Builds zones.csv and static_prices.csv for group `zones` (KZ, IQ, SO, KN). Rerun: python3 build.py
import csv
LIC = "utility/regulator tariff (public regulatory document; rates are facts)"

def norm(d):
    t = sum(d.values()); w = {k: round(v / t, 6) for k, v in d.items()}
    last = list(w)[-1]; w[last] = round(1 - sum(v for k, v in w.items() if k != last), 6)
    return w

zones, prices = [], []

# ---- KZ: BNS population 1 Dec 2024 (via ru.wikipedia table)
ZH = "https://zhkh24.kz/ru/articles/skolko-stoit-svet-v-raznyh-regionah-kazahstana-tarify-dlya-naseleniya-v-2026-godu"
DB = "https://digitalbusiness.kz/2026-10-01/chto-podorozhaet-v-kazahstane-s-1-oktyabrya-2026-goda/"
kz = [  # id, name, pop, price, as_of, conf, arithmetic, urls, extra
 ("KZ-71","Астана",1520756,33.74,"2026-07","high","Astana-REK tier 2 (70-140 kWh, no electric stove) 33.74 incl. 16% VAT, valid from 2026-07-01; blended at 200 kWh: 70x24.81+70x33.74+60x42.18 = 6629.30 / 200 = 33.15","https://astrec.kz/abonentam/tarify-dlia-fizicheskih-lits","Astana-REK applied to raise the household limit price ~19% (32.74 to 38.98 excl. VAT) from 2026-10-01; approval not found"),
 ("KZ-75","Алматы",2286328,45.51,"2026-09","high","AZhK Energosbyt tier 2 39.23 excl. VAT x 1.16 = 45.51, from 2026-09-12 (unified household rate 37.92)","https://www.esalmaty.kz/ru/home-tariffs | https://vlast.kz/novosti/70802-v-almaty-i-almatinskoj-oblasti-s-12-sentabra-povysatsa-tarify-na-elektroenergiu.html",""),
 ("KZ-79","Шымкент",1253280,29.88,"2026-08","medium","tier 2 incl. 16% VAT, no electric stove, as of 2026-08-17",ZH,""),
 ("KZ-10","область Абай",603345,24.29,"2026-08","medium","tier 2 incl. 16% VAT, no electric stove, as of 2026-08-17",ZH,""),
 ("KZ-11","Акмолинская область",787896,39.13,"2026-08","medium","tier 2 incl. 16% VAT, no electric stove, as of 2026-08-17",ZH,""),
 ("KZ-15","Актюбинская область",948991,27.76,"2026-08","medium","tier 2 incl. 16% VAT, no electric stove, as of 2026-08-17",ZH,""),
 ("KZ-19","Алматинская область",1557932,45.51,"2026-09","high","AZhK Energosbyt (serves Almaty city and oblast) tier 2 39.23 excl. VAT x 1.16 = 45.51, from 2026-09-12","https://www.esalmaty.kz/ru/home-tariffs",""),
 ("KZ-23","Атырауская область",710273,34.13,"2026-10","medium","Aug tier 2 31.03 incl. VAT x (new household base 24.52 / old 22.29 excl. VAT, from 2026-10-01) = 31.03 x 1.1000 = 34.13",ZH+" | "+DB+" | https://www.inform.kz/ru/noviy-tarif-na-elektroenergiyu-utverdili-v-atirauskoy-oblasti-35f83c09",""),
 ("KZ-63","Восточно-Казахстанская область",724110,24.29,"2026-08","medium","tier 2 incl. 16% VAT, no electric stove, as of 2026-08-17",ZH,""),
 ("KZ-31","Жамбылская область",1222411,32.10,"2026-08","medium","tier 2 incl. 16% VAT, no electric stove, as of 2026-08-17",ZH,""),
 ("KZ-33","область Жетісу",694940,37.31,"2026-08","medium","tier 2 incl. 16% VAT, no electric stove, as of 2026-08-17",ZH,""),
 ("KZ-27","Западно-Казахстанская область",695724,35.37,"2026-10","low","Aug tier 2 33.69 incl. VAT x (household rate 30.49 / 29.04 excl. VAT, from 2026-10-01) = 33.69 x 1.0499 = 35.37",ZH+" | https://bes.media/news/v-zko-s-1-oktyabrya-podnimut-tarif-na-elektroenergiyu-dlya-naseleniya/","the Oct household base (30.49) does not reconcile with the Aug tier 2 (33.69 incl. VAT = 29.04 excl.), so the scaling is approximate"),
 ("KZ-35","Карагандинская область",1134002,27.71,"2026-08","medium","tier 2 incl. 16% VAT, no electric stove, as of 2026-08-17",ZH,""),
 ("KZ-39","Костанайская область",825735,41.99,"2026-08","medium","tier 2 incl. 16% VAT, no electric stove, as of 2026-08-17",ZH,""),
 ("KZ-43","Кызылординская область",845994,35.45,"2026-08","medium","tier 2 incl. 16% VAT, no electric stove, as of 2026-08-17",ZH,""),
 ("KZ-47","Мангистауская область",803631,23.98,"2026-08","medium","tier 2 incl. 16% VAT, no electric stove, as of 2026-08-17",ZH,""),
 ("KZ-55","Павлодарская область",751656,31.61,"2026-10","medium","Aug tier 2 30.11 incl. VAT x (household base 22.71 / 21.63 excl. VAT, from 2026-10-01) = 30.11 x 1.0499 = 31.61",ZH+" | "+DB,""),
 ("KZ-59","Северо-Казахстанская область",522695,23.86,"2026-08","medium","SEVKAZENERGO tier 2 incl. 16% VAT, no electric stove, as of 2026-08-17",ZH,"a ~15% average rise was requested (qaz-media.kz); not found approved"),
 ("KZ-61","Туркестанская область",2154304,29.88,"2026-08","medium","tier 2 incl. 16% VAT, no electric stove, as of 2026-08-17",ZH,""),
 ("KZ-62","область Ұлытау",221317,26.22,"2026-08","medium","tier 2 incl. 16% VAT, no electric stove, as of 2026-08-17",ZH,""),
]
w = norm({r[0]: r[2] for r in kz})
for r in kz:
    zones.append(("KZ", r[0], r[1], "", w[r[0]], "Bureau of National Statistics population 1 Dec 2024 (ru.wikipedia, Административно-территориальное деление Казахстана)"))
    note = f"{r[5]} confidence; tier 2 rate as the price at typical use (~200 kWh/month, flat per kWh, no standing charge)" + (f"; {r[8]}" if r[8] else "")
    prices.append(("KZ", r[0], f"{r[3]:.2f}", "KZT", r[4], r[6] + " | " + r[7], LIC, note))

# ---- IQ: 2024 census final results
iq_w = norm({"IQ-KR": 6519129, "IQ-FED": 46118793 - 6519129})
zones += [("IQ","IQ-KR","إقليم كوردستان","",iq_w["IQ-KR"],"2024 census final results: Kurdistan Region 6,519,129 of 46,118,793 (peregraf.com/en/news/10297)"),
          ("IQ","IQ-FED","محافظات العراق الأخرى","",iq_w["IQ-FED"],"2024 census final results: 46,118,793 minus Kurdistan Region 6,519,129")]
prices += [("IQ","IQ-KR","82.74","IQD","2025-05",
  "Runaki household blocks 72 IQD (0-400 kWh), 108 (401-800); at 570 kWh/month: 400x72 + 170x108 = 28,800 + 18,360 = 47,160 IQD / 570 = 82.74; no fixed charge or VAT found | https://en.964media.com/35966/ | https://en.964media.com/45190/ | https://runaki.gov.krd/en/",
  LIC, "medium confidence; at 570 kWh/month (Feb 2026 median Runaki bill: <853 kWh over a ~45-day cycle = ~570/month, KRG MoE); 72 at 400 kWh or less; Runaki 24-hour supply covers >90% of the region; temporary e-payment discounts excluded"),
  ("IQ","IQ-FED","10.00","IQD","2025-07",
  "Ministry of Electricity residential block 1-1500 kWh at 10 IQD; no fixed charge or VAT found | https://web.archive.org/web/20250709013453/https://moelc.gov.iq/?calculation",
  LIC, "high confidence; at 300 kWh/month (any use to 1,500 gives 10); grid only: most households also pay neighbourhood generators (~20,000 IQD per amp per month), not included; unconfirmed 3,000 IQD/bill fee excluded")]

# ---- SO: OCHA subnational population estimates 2025, regions mapped to member states
o = dict(Awdal=655894,Bakool=560267,Banaadir=3262129,Bari=1270552,Bay=1286787,Galguduud=837916,Gedo=1005924,Hiran=520517,LowerJuba=1194276,LowerShabelle=1642667,MiddleJuba=443507,MiddleShabelle=1044872,Mudug=1516035,Nugal=651464,Sanaag=442034,Sool=566053,Togdheer=887450,MaroodiJeex=1492506)
h = lambda k: o[k] / 2
so_pop = {"SO-BN": o["Banaadir"],
  "SO-JUB": o["Gedo"]+o["LowerJuba"]+o["MiddleJuba"],
  "SO-SWS": o["Bay"]+o["Bakool"]+o["LowerShabelle"],
  "SO-HIR": o["Hiran"]+o["MiddleShabelle"],
  "SO-GAL": o["Galguduud"]+h("Mudug"),
  "SO-PUN": o["Bari"]+o["Nugal"]+h("Mudug")+h("Sool")+h("Sanaag"),
  "SO-SML": o["Awdal"]+o["MaroodiJeex"]+o["Togdheer"]+h("Sool")+h("Sanaag")}
sw = norm(so_pop)
BGS = "https://bgs.so/wp-content/uploads/2025/10/Navigating-Non-Technical-Barriers-to-Affordable-Electricity-in-Somalia.pdf"
so = [("SO-BN","Banaadir (Muqdisho)","0.41","2023-01","BECO household rate $0.41/kWh flat (2023; BGS Fig. 2: 'maximum for household $0.41', all-customer average $0.36)",BGS+" | https://wardheernews.com/somalia-powers-ahead-with-affordable-renewable-energy/","low confidence; flat per kWh, any use; BECO (main Mogadishu provider); no 2024-26 BECO tariff found"),
 ("SO-JUB","Jubaland","0.90","2023-01","2023 state average $0.90/kWh (BGS Fig. 1, from Shuraako and NTP 2025); main city Kismayo",BGS,"low confidence; flat per kWh, any use; survey average, not a provider schedule"),
 ("SO-SWS","Koonfur Galbeed","0.70","2023-01","2023 state average $0.70/kWh (BGS Fig. 1, from Shuraako and NTP 2025); main city Baidoa",BGS,"low confidence; flat per kWh, any use; survey average, not a provider schedule"),
 ("SO-HIR","Hirshabeelle","1.00","2023-01","2023 state average $1.00/kWh (BGS Fig. 1, from Shuraako and NTP 2025); main cities Jowhar, Beledweyne",BGS,"low confidence; flat per kWh, any use; survey average, not a provider schedule"),
 ("SO-GAL","Galmudug","1.00","2023-01","2023 state average $1.00/kWh (BGS Fig. 1, from Shuraako and NTP 2025); main cities Galkayo (south), Dhusamareb",BGS,"low confidence; flat per kWh, any use; survey average, not a provider schedule"),
 ("SO-PUN","Puntland","0.79","2025-08","Bosaso (largest city), PEPCO $0.79/kWh (Somali Public Agenda, Aug 2025); Garowe ~$0.59",
  "https://somalipublicagenda.org/wp-content/uploads/2025/08/SPA_Governance_Briefs_36_2025_ENGLISH1.pdf","low confidence; flat per kWh, any use; reported price, not a published schedule; BGS 2023 state average $1.00"),
 ("SO-SML","Somaliland","0.59","2025-12","Ministry of Energy and Minerals tariff $0.59/kWh for cities except Berbera (was $0.73), from 2025-12-01; main city Hargeisa",
  "https://www.geeska.com/en/somaliland-cuts-electricity-tariffs-ease-energy-costs | https://www.somalilandcurrent.com/somaliland-government-announces-significant-reduction-in-national-electricity-tariff/","medium confidence; flat per kWh, any use; government-set cap tied to subsidised fuel; Berbera has its own lower rate")]
names = {r[0]: r[1] for r in so}
for r in so:
    zones.append(("SO", r[0], r[1], "", sw[r[0]], "OCHA Somalia subnational population estimates 2025 (18 regions, via en.wikipedia Regions of Somalia), mapped to member states; Mudug, Sool, Sanaag split 50/50"))
    prices.append(("SO", r[0], r[2], "USD", r[3], r[4] + " | " + r[5],
      "Barkhadle Global Studies report, Oct 2025 (publicly posted PDF)" if r[5].startswith(BGS) else ("press report of a ministry tariff decision" if r[0]=="SO-SML" else "Somali Public Agenda governance brief (publicly posted PDF)"), r[6]))

# ---- KN: 2022 census
kw = norm({"KN-K": 38138, "KN-N": 13182})
zones += [("KN","KN-K","St Kitts","",kw["KN-K"],"2022 Population and Housing Census summary report: St Kitts 38,138 of 51,320"),
          ("KN","KN-N","Nevis","",kw["KN-N"],"2022 Population and Housing Census summary report: Nevis 13,182 of 51,320")]
prices += [("KN","KN-K","0.70","XCD","2026-06",
  "SKELEC domestic energy 50x0.59 + 100x0.65 + 150x0.68 = 29.50 + 65.00 + 102.00 = 196.50, + demand charge 13.00 (one 15 A unit) = 209.50 / 300 = 0.698; Fuel Variation Charge government-subsidised (credited on bill); no VAT on electricity | https://www.skelec.kn/wp-content/uploads/2024/09/ElectricityTariffStructure-Jan2011-scaled.jpg | https://www.skelec.kn/skelec-bills-will-now-show-the-value-of-the-fuel-variation-charge/ | https://www.winnmediaskn.com/nevis-premier-says-cap-on-fuel-surcharge-to-be-removed-due-to-continued-global-volatility/",
  LIC, "medium confidence; at 300 kWh/month; subsidy still in force per Energy Minister Maynard, June 2026 (residential tariff below fuel cost, government covering the difference); tariff dated Jan 2011; a 60 A service (4 demand units) gives 0.83"),
  ("KN","KN-N","1.57","XCD","2026-09",
  "NEVLEC energy 50x0.65 + 75x0.70 + 175x0.75 = 32.50 + 52.50 + 131.25 = 216.25, + standing charge 18.00 (above 250 kWh) + fuel surcharge 300x0.79 = 237.00 = 471.25 / 300 = 1.571; no VAT on electricity | https://www.nevlec.com/residential/your-bill/electricity-rates/ | https://www.nevlec.com/wp-content/uploads/2026/09/UnderstandingYourResidentialBill.png | https://www.nevlec.com/important-notice-to-customers-fuel-surcharge-adjustment-effective-june-2026/",
  LIC, "medium confidence; at 300 kWh/month; fuel surcharge reinstated June 2026 (0.69), 0.79 in NEVLEC's Sept 2026 bill guide; it moves monthly")]

with open("zones.csv","w",newline="") as f:
    c = csv.writer(f); c.writerow(["country","id","name","area","weight","weight_source"]); c.writerows(zones)
with open("static_prices.csv","w",newline="") as f:
    c = csv.writer(f); c.writerow(["country","zone","price","currency","as_of","source","licence","note"]); c.writerows(prices)

pm = {(p[0],p[1]): float(p[2]) for p in prices}
for cc in ["KZ","IQ","SO","KN"]:
    zs = [z for z in zones if z[0]==cc]
    mean = sum(z[4]*pm[(cc,z[1])] for z in zs); ps = [pm[(cc,z[1])] for z in zs]
    print(cc, "weights sum", round(sum(z[4] for z in zs),6), "weighted mean", round(mean,3), "min", min(ps), "max", max(ps), "ratio", round(max(ps)/min(ps),2))
    for z in zs: print("   ", z[1], z[2], z[4], pm[(cc,z[1])])
