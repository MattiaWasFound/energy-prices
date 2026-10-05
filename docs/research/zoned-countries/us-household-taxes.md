# US household taxes on electricity (verified 2026-10-04)

**Question.** EIA's residential price excludes taxes levied on the household
(see `us-eia.md`). Which taxes does each state's household pay on top?

**How it was checked.** Four parallel passes, 12 to 13 states each, against
statutes and state revenue departments (official `.gov` pages; archive copies
where a site blocked automated access). Commercial tables (CallMePower,
Bloomberg BNA charts) were not used as sources. The per-state result, with
statute citations, is `config/household_taxes.csv`.

**Rule applied.** Added: taxes the household pays on its bill, which are
state sales tax, consumer excises (Illinois 0.33 c/kWh, DC $0.007/kWh,
Virginia $0.001595/kWh), itemised pass-throughs (Rhode Island's 4% gross
earnings tax, Vermont's 0.5%, Florida's 2.5%), and a typical local or city
utility tax. Left out: taxes on the utility that are already in its rates and
so already in EIA's revenue (Ohio's kWh excise, Pennsylvania's 5.9% gross
receipts tax, Hawaii's public service and franchise taxes, Washington's state
utility tax, West Virginia's B&O tax, Wisconsin's license fee).

**What the passes corrected.**

- Wisconsin exempts residential electricity all year from 2025-10-01 (2025
  Wis. Act 15); before, only November to April bills were exempt.
- Iowa exempts it from the 6% state tax; only the 1% local option applies.
- Delaware's 4.25% public utility tax applies to non-residential users only.
- Georgia has no residential exemption: 4% state plus local.
- Utah: 2% state, about 1% local sales tax, and a municipal energy tax of up
  to 6% that most large cities levy, so about 9% in a city.
- New York exempts it from state tax, but New York City charges 4.5%.
- Michigan taxes residential at 4%, not 6%.
- Maine exempts the first 750 kWh a month, which covers a typical household.
- Indiana's 7% stands: the 2026 repeal amendments failed. Nebraska's 5.5%
  stands: LB 117 was postponed indefinitely in April 2026. New Jersey's 6.625%
  stands: the S1932 suspension for 2026 was not enacted.
- South Dakota's 4.2% runs to 2027-06-30, then reverts to 4.5% by statute.

**Weak spots.** Every `local_rate` is an estimate of a typical place, not a
weighted average; the weakest are California's utility users' taxes,
Colorado's home-rule cities, Missouri's city utility license taxes and
Illinois' municipal taxes. Alabama's 4% utility gross receipts tax is added
because the statute requires it on the bill; if Alabama Power builds it into
rates instead, it is counted twice.

**National figure.** EIA's national price gets the states' taxes weighted by
each state's residential kWh sales that month (EIA's own `sales` series):
July 2026 $0.1831 becomes $0.1898.
