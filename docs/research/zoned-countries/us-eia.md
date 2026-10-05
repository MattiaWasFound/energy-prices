# EIA residential "average price" (electricity/retail-sales): what is in it

Researched 2026-10-04. Source PDFs and spreadsheets (eia.gov downloads, plus a 2015 Bloomberg BNA chart) are not kept here.

## TL;DR

| Component | In EIA avg price? | Confidence |
|---|---|---|
| Energy/demand charges, fuel adjustments, environmental surcharges, other riders | Yes | Explicit (EIA) |
| Fixed customer charges ("customer service charges") | Yes | Explicit (EIA) |
| Franchise fees | Yes | Explicit (EIA-861 instr.) |
| Taxes levied on the utility and recovered in rates (gross receipts taxes on the utility, utility income/property taxes) | Yes | Explicit ("taxes ... paid by the utility") |
| Delivery charges from a separate distribution utility when the household buys energy from a third-party supplier | Yes, at state level | Explicit in form design (energy-only revenue + delivery-only revenue are both collected) |
| Sales/use taxes and utility-users' taxes levied on the customer, which the utility only collects and remits | Most likely NO | Inferred. EIA never says so explicitly, and its FAQ says "taxes, and fees" are included |
| Prior-period adjustments and deferred credits | No | Explicit |

Bottom line: treat EIA's residential average price as the full bill before customer-levied sales and utility-users' taxes. To get an all-in household figure, multiply by (1 + combined sales/utility-users' tax rate) where the state or locality charges one.

## 1. EIA's own definitions (quotes)

**Electric Power Monthly, Technical Notes, Form EIA-861M (formerly EIA-826) section.** https://www.eia.gov/electricity/monthly/pdf/technotes.pdf
> "Average price of electricity to ultimate consumers represents the cost per unit of electricity sold and is calculated by dividing electric revenue from ultimate consumers by the corresponding sales of electricity."
> "The electric revenue used to calculate the average price of electricity to ultimate consumers is the operating revenue reported by the electric utility. Operating revenue includes energy charges, demand charges, consumer service charges, environmental surcharges, fuel adjustments, and other miscellaneous charges. Electric utility operating revenues also include State and Federal income taxes and taxes other than income taxes paid by the utility."
> "...does not reflect the per kWh rate charged by the electric utility to the individual consumers."

**Electric Power Annual 2024, Technical Notes** (same definition with clearer wording). https://www.eia.gov/electricity/annual/pdf/epa.pdf
> "Electric power industry participant operating revenues also include ratepayer reimbursements for state and federal income taxes and other taxes paid by the utility."

**Form EIA-861 instructions, Schedule 2 Part C, line 1** (OMB 1905-0129, exp. 07/31/2029). https://www.eia.gov/survey/form/eia_861/instructions.pdf
> "Revenue entered on line 1 is gross revenue and includes the revenue from state and local income taxes, energy or demand charges, customer service charges, environmental surcharges, franchise fees, fuel adjustments and other miscellaneous charges applied to end-use customers during normal billing operations. Revenue entered on line 1 should not include deferred charges, credits, or other adjustments, such as fuel or revenue from purchased power, from previous reporting periods..."

**EIA FAQ "Does EIA publish electricity sales and price data by state and by utility?"** https://www.eia.gov/tools/faqs/faq.php?id=507&t=3
> "The average retail electricity price we publish includes all costs for delivered electricity, including generation, transmission, distribution, taxes, and fees."

**EIA Glossary, "Revenue (electricity)".** https://www.eia.gov/tools/glossary/index.php?id=R
> "The total amount of money received by an entity from sales of its products and/or services; ..."

### Taxes: how to read this

EIA's technical definitions always describe the included taxes as taxes **"paid by the utility"**: income taxes, and "taxes other than income taxes", such as gross-receipts, franchise, property and kWh excise taxes levied on the utility. The utility recovers these through its rates. A sales tax or utility-users' tax is different. It is levied on the customer, appears as a separate line on the bill, and the utility collects it as an agent. Under the FERC Uniform System of Accounts, which IOUs report from, such collections go to a liability account, not to revenue: 18 CFR Part 101, Account 241 "Tax collections payable", "the amount of taxes collected by the utility ... pending transmittal of such taxes to the proper taxing authority" (https://www.ecfr.gov/current/title-18/chapter-I/subchapter-C/part-101). They are therefore not "operating revenue". The FAQ's "taxes, and fees" is the loose, consumer-facing summary.

**Caveat:** EIA publishes no explicit "sales tax excluded" statement, and utility reporting practice may vary, especially for small munis and co-ops. Taxes that a state passes through as a separate bill line but legally levies on the utility, such as some gross-receipts or kWh taxes, are probably included. Examples are the Illinois electricity excise tax, which is borderline because it is collected from customers, and Ohio's kWh tax, which is on the utility.

### Deregulated (retail-choice) states

Form EIA-861M collects four parts per state and sector: Part A bundled (energy + delivery), Part B energy-only (third-party supplier; "another electric company provided delivery services"), Part C "delivery-only service (and all other charges)" from the distribution utility, and Part D bundled marketer service ("Texas Retail Energy Providers (REPs) should include delivery revenues"). Instructions: https://www.eia.gov/survey/form/eia_861m/instructions.pdf. The 861M data page describes the state file as containing "revenue, sales ... of energy only and delivery service electricity to end-use customers by state and sector" (https://www.eia.gov/electricity/data/eia861m/). A shopping household's delivery charges therefore enter state revenue through Part C, while its kWh are counted once. The FAQ's "generation, transmission, distribution" confirms the intent. One thing I could not settle from the published files is whether third-party supplier revenue is fully captured monthly, since Part B is sampled or imputed by EIA. Annual 861 benchmarking corrects this at year end: the EPM technical notes say monthly values are ratio-adjusted to final EIA-861.

## 2. Licence / republishing

EIA "Copyrights and Reuse": https://www.eia.gov/about/copyrights_reuse.php
> "U.S. government publications are in the public domain and are not subject to copyright protection. You may use and/or distribute any of our data, files, databases, reports, graphs, charts, and other information products that are on our website ... However, if you use or reproduce any of our information products, you should use an acknowledgment, which includes the publication date, such as: "Source: U.S. Energy Information Administration (Oct 2008)."

The exceptions are photos and third-party contributed material only. Republishing the numbers is fine with a "Source: U.S. Energy Information Administration (<month year>)" credit. The API needs a free key, but the key does not restrict reuse.

## 3. Lag

- Electric Power Monthly, checked 2026-10-04: "July 2026 data released September 24, 2026" (https://www.eia.gov/electricity/monthly/). The latest month is about 2 months behind; release falls around the 24th of month M+2.
- The 861M file `sales_revenue.xlsx` downloaded today also ends at 2026-07, `Data Status = Preliminary`.
- Monthly values are preliminary, from a cutoff-model sample ("Values are preliminary estimates based on a cutoff model sample"). They are revised to final after annual EIA-861 data lands, roughly in the autumn of the following year. 2025 is still preliminary/early-final.
- Plan: show month M-2 or M-3 as "latest", and expect revisions.

## 4. Approximating the all-in household figure: sales tax on residential electricity

There is no open-licensed, maintained state-by-state dataset that I could find:

- **Bloomberg BNA "Sales and Use Tax Chart: Taxability of Utilities in the State Sales Tax"** (2015, compiled by Scott Drenkard / Tax Foundation for the Louisiana legislature): https://house.louisiana.gov/tsmc/Documents/2015/Sep/Taxability%20of%20Utilities%20in%20the%20State%20Sales%20Tax%20-%20Scott%20Drenkard.pdf. It has statute citations per state but is out of date, and it is Bloomberg BNA copyright, so not republishable. Use it as a checklist of statute cites only.
- **CallMePower "Taxes on Electricity in the US"** (May 2026): https://callmepower.com/energy-markets/tax-on-electricity. "© 2026 CallMePower — All rights reserved." It covers only 15 states and has visible errors; for example it lists Michigan as exempt, but Michigan taxes residential electricity at a reduced rate. Do not use it.
- **Recommended:** build our own 51-row table from each state Department of Revenue's statute or publication, one cited URL per state. Tax rates and exemptions are statutory facts and not copyrightable. Local add-ons (local sales tax, utility-users' taxes such as California cities' UUT or New York local sales tax on residential energy) vary by city. A state-level all-in figure can only use the state rate plus, at best, a population-weighted average local rate.

### Provisional classification (state sales tax on residential electricity), to verify per state DOR before use

Sources: the Bloomberg BNA 2015 chart above plus later law changes I know of. Items marked ? are the ones most in need of checking.

- **No state sales tax at all:** AK, DE, MT, NH, OR.
- **Residential exempt from state sales tax** (local tax or utility-specific taxes may still apply): AL (utility privilege tax instead), CA (local UUT common), CO (state exempt, some locals tax), CT, DC, FL (exempt from sales tax, but 2.5% gross receipts tax on the utility, in revenue), ID, IL (electricity excise tax instead), KY? (residential exempt; check recent bills), LA (state exempt, parish taxes may apply), MD, MA, MS, MO? (residential exempt from state, local may apply), NV, NY (state 4% exempt since 2000, local sales tax still applies in many counties incl. NYC?), OH (kWh tax on utility instead), OK (state exempt, local may apply), PA, RI, SC, TN, TX (state exempt, local up to 2% may apply), VT (fuel gross receipts tax instead), VA (exempt, utility consumer tax instead), WA (exempt, utility tax on the utility instead), WV, ME (first 750 kWh/month exempt), MN? (residential exempt only for primary-heating Nov–Apr; otherwise taxed).
- **Residential taxed by state sales/gross-receipts tax:** AZ (TPT), AR (reduced residential rate?), GA (4% + local), HI (GET/public service company tax, mostly embedded), IN (7%), IA (6%, residential exempt? check post-2022 law), KS (residential exempt from state since 2023? check), MI (reduced 4%), NE, NJ (6.625%), NM (GRT), NC (7%), ND (exempt? the chart says not generally taxed), SD, UT (reduced residential rate), WI (residential exempt Nov–Apr), WY.

Effect size: where a tax applies it is typically 4–8%, i.e. about +0.6 to +1.3 c/kWh on a 16 c/kWh average. That is small next to the 2–3x spread between states, so a per-state multiplier is enough. Flag the figure as "EIA average price + state sales tax (approx.)".

## Sources

- EPM technical notes: https://www.eia.gov/electricity/monthly/pdf/technotes.pdf
- EPA 2024 (technical notes): https://www.eia.gov/electricity/annual/pdf/epa.pdf
- EIA-861 instructions: https://www.eia.gov/survey/form/eia_861/instructions.pdf
- EIA-861M instructions: https://www.eia.gov/survey/form/eia_861m/instructions.pdf
- EIA-861M data page: https://www.eia.gov/electricity/data/eia861m/
- FAQ 507: https://www.eia.gov/tools/faqs/faq.php?id=507&t=3
- Glossary R: https://www.eia.gov/tools/glossary/index.php?id=R
- Copyright & reuse: https://www.eia.gov/about/copyrights_reuse.php
- EPM release status: https://www.eia.gov/electricity/monthly/
- 18 CFR 101 (FERC USofA), Account 241: https://www.ecfr.gov/current/title-18/chapter-I/subchapter-C/part-101
- Bloomberg BNA utility taxability chart (2015): https://house.louisiana.gov/tsmc/Documents/2015/Sep/Taxability%20of%20Utilities%20in%20the%20State%20Sales%20Tax%20-%20Scott%20Drenkard.pdf
