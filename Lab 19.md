# Lab 19 — Three investors, the same SEC facts

Question: When three investors' skills read the same 10-K facts, where do they agree, where do they split — and would you trust the panel?

Run from FIN 439:

```powershell
py -m streamlit run Lab19/lab19_app.py --server.port 8519
```

The app retains the Lab 18 chart, annual table, source tags, checks, memo and numeric flag. It adds Liabilities and ResearchAndDevelopmentExpense, all seven panel checks, separate verdicts, three editable memos side by side and a flag that scans all three. The memos are independent model-written judgments based on the shared script output; the checks do not mechanically dictate a verdict.

## COST known answer

| Investor | Check | Calculated result |
|---|---|---|
| Buffett | ROE at least 15% every year | pass |
| Buffett | Owner earnings positive every year | pass |
| Buffett | Owner earnings grew first to last | pass |
| Cathie Wood | Annual revenue growth at least 15% | fail — 7.51% |
| Cathie Wood | Latest R&D / revenue at least 5% | not known |
| Burry | Operating cash flow at least net income every year | pass |
| Burry | Latest liabilities / equity at most 2 | pass — 1.49 |

Annual liabilities/equity ratios round to 2.11, 1.75, 1.96, 1.64 and 1.49. Required R&D is not found in every year; its check stays unknown. The outputs were calculated from the downloaded SEC facts, not loaded from the expected-answer table. The expected answers appear only in tests and this explanation.

## Threshold probe

The app reads `Growth threshold retained: **15%**` in `.agents/skills/cathie-wood-screen/SKILL.md`. Temporarily change that value to 5%, then rerun the app: COST's growth check passes and its R&D check stays unknown. `probe/COST_printed.txt` preserves the computed 5% run; 15% is restored in the skill.

Threshold retained: 15%, to preserve a demanding growth screen rather than tune the screen to pass a known company. The line also appears under Wood's memo. A threshold can change a verdict without changing the company or facts. During the temporary probe the app warns that the saved memo was written at the retained threshold.

## Project 2 company — NVDA, from QQQ

The saved Project 2 portfolio includes QQQ. NVDA is used as the largest holding in the dated Invesco holdings evidence returned for 2026-10-14, with an 8.15% weight. The live issuer holdings table could not be loaded through the research tool, and other current sources differ on the latest ranking. This is a dated selection, not a claim that NVDA must be the largest holding today. Confirm it against your prework date before submission; no fund substitution or non-10-K fallback was needed.

| Investor | Checks | Model verdict |
|---|---|---|
| Buffett | 3 of 3 pass | watch it |
| Cathie Wood | 2 of 2 pass | own the business |
| Burry | cash conversion fails; liabilities check passes | watch it |

Annual revenue growth is 68.30%; latest R&D intensity is 8.57%; latest liabilities/equity is 0.31. Latest operating cash flow of 102,718 USD millions is below net income of 120,067 USD millions. The full table, verdicts and all memos are in `output/NVDA_report.md` and the app. Source tags, dates and accessions are in `output/NVDA_facts.json`.

The panel agrees that NVDA has favorable balance-sheet leverage under Burry's rule and strong historical returns and growth under the other rules. It splits because the same accounts show both rapid growth and cash conversion below reported net income. A failed cash check invites investigation; it does not prove fraud.

The user-supplied Michael Burry guide supplements the skill's skeptical treatment of earnings and cash conversion. Its broader forensic topics are not presented as completed investigations: this screen has not established receivables quality, auditor concerns, hidden liabilities or insider activity. Example figures in that guide are not inputs to these memos. The lab's printed-numbers-only memo format takes precedence over the guide's full forecasting and price-target schema.

Suggested bull case: NVDA passes Buffett's profitability and owner-earnings checks and both Wood checks. Rapid growth, positive owner earnings and substantial research spending support further study of the business.

Suggested bear case: Burry's cash-conversion check fails despite low liabilities relative to equity. High reported profits do not settle how quickly those profits become operating cash, or whether historical returns persist.

Suggested decision: **Only with a condition** — use the panel to shortlist companies, then verify the filings, investigate gaps and failed checks, and assess competitive durability and valuation separately.

These are model suggestions. No partner discussion or personal answer is invented.

## Explain the code briefly

`cathie_checks(rows, growth_threshold)` first reads the earliest and latest revenue. If exactly five years and valid endpoint revenues exist, it calculates `(last / first) ** (1/4) - 1`; otherwise growth is missing. `compare` returns `not known` for missing values, `pass` if the unrounded value reaches the threshold, and `fail` otherwise. The R&D check uses the latest ratio, with no proxy if the required tag is absent.

All investors receive the same rows from `year_row`. They disagree because each applies a different rule and weights evidence differently in its memo. Three personas sharing facts and code are not three independent data sources; consensus cannot validate the shared extraction logic.

A skill is a named folder of instructions and resources. Its name/description support discovery; the detailed instructions and scripts are read when the task needs them. Code makes arithmetic and missing-value handling repeatable. The model supplies qualitative judgment, which can vary and needs review.

## Verification and checkout

Run `py verify_investor_labs.py`. Tests compare all supplied COST values, preserve JPM gaps, test the 5% probe, scan every saved memo and inject an unprinted number into each investor's app memo. `verification.txt` stores the result. The numeric flag is exact-token checking, not semantic fact checking.

Use `Lab19_submission.zip` for GitHub upload; it contains the app, shared UI, all three skills, source snapshots, memos, outputs and tests. No repository URL was provided, so no GitHub publication or links are claimed. Fresh personalized SEC downloading still requires your name/email. The fifth merit criterion was not supplied; no content for it is invented.

Sources: [Cathie Wood perspective](https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/cathie_wood.md) and the supplemental text provided in chat; [Burry perspective](https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/michael_burry.md); [Buffett perspective](https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/warren_buffett.md); [SEC API docs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces); [Streamlit columns](https://docs.streamlit.io/develop/api-reference/layout/st.columns); [Invesco holdings source](https://www.invesco.com/us/en/financial-products/etfs/invesco-qqq-trust-series-1.html).
