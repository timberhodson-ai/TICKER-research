> **Class assignment disclaimer:** This report was prepared for educational purposes as part of a class assignment. It is not financial or investment advice, or a recommendation to buy, sell, or hold any security. Valuations and conclusions depend on the stated assumptions and estimates.

# ADP: five-year DCF, sensitivity analysis and reverse DCF

Prepared September 10, 2026. Dollars are in millions except per-share values. This is an estimated valuation, not management guidance.

**Conditional call: watch/defer.** My adjusted base case is **$228.10 per diluted share**, versus the verified reference price of **$265.22**. Matching that price requires adding **3.56 percentage points to every annual growth forecast**, with the other inputs fixed. The sensitivity grid spans **$174.99–$335.20**, so the conclusion depends substantially on the discount rate and terminal growth.

**Quote limitation:** $265.22 is the September 9, 2026, 4:00 PM EDT close, verified from [Stock Analysis, price history](https://stockanalysis.com/stocks/adp/history/). Sources checked September 10 still displayed that quote. Today's quote remains unresolved; this report uses the explicitly dated reference price. Update `TARGET_PRICE` before submitting a same-day valuation.

## R — Five input rows, with sources

| Input | Value and unit | As-of date / status | Exact locator |
|---|---|---|---|
| Starting FCFF | **$4,570.537 million**, adjusted estimate; reconciliation below | FY ended June 30, 2026; estimated September 10 | [10-K](https://www.sec.gov/Archives/edgar/data/8670/000000867026000030/adp-20260630.htm), cash-flow statement pp. 48–49; Item 7 adjusted EBIT reconciliation p. 34 |
| FCFF growth, Years 1–5 | **7.0%, 6.5%, 6.0%, 5.5%, 5.0% annually** | FY2027–FY2031; analyst forecast September 10 | [Earnings release](https://www.sec.gov/Archives/edgar/data/8670/000000867026000025/q4fy26exhibit99.htm), fiscal 2027 outlook p. 3; forecast rationale below |
| WACC | **8.4% annually**, rounded from 8.3585% | Estimate September 10; mixed dated inputs disclosed below | Cost-of-capital calculation below; 10-K Note 10 p. 67; dated market inputs |
| Terminal growth | **2.5% annually**, nominal, in perpetuity | Analyst assumption September 10; begins FY2032 | [Federal Reserve inflation objective](https://www.federalreserve.gov/faqs/economy_14400.htm), FAQ updated August 22, 2025; economic rationale below |
| Cash / debt / diluted shares | **$4,368.7 million / $4,944.1 million / 403.3 million shares** | Balance-sheet amounts June 30, 2026; FY2026 diluted average; debt bridge estimate | 10-K Note 5 p. 62; Notes 9–10 pp. 66–67; Note 1.N p. 54 |

### Starting cash flow and ADP-specific corrections

The filing inputs are: operating cash flow **5,441.2**, cash interest **439.6**, capex **196.6**, intangible additions **468.5**, stock compensation **242.6**; tax rate **23.0%**. Item 7 separately identifies non-client-strategy interest expense **141.0** and interest income **92.9**. [10-K: cash-flow statement pp. 48–49; Item 7 pp. 30, 34–35](https://www.sec.gov/Archives/edgar/data/8670/000000867026000030/adp-20260630.htm).

First, the assignment's cash-flow calculation, with intangible investment included in capex:

**5,441.2 + 439.6 × (1 − 23%) − 196.6 − 468.5 = $5,114.592 million.**

I then make three explicit valuation adjustments:

| Reconciliation | $ million | Reason |
|---|---:|---|
| Assignment-style FCFF, including intangible investment | 5,114.592 | Unadjusted starting calculation |
| Replace total interest add-back with estimated non-client financing interest | (229.922) | (439.6 − 141.0) × 77%; retain client-strategy financing costs in operating cash flow |
| Remove after-tax non-client interest income | (71.533) | 92.9 × 77%; corporate investments are added separately in the equity bridge |
| Deduct stock compensation | (242.600) | Simplified allowance for ongoing compensation-related dilution |
| **Starting adjusted FCFF** | **4,570.537** | **Analyst estimate used throughout** |

This is equivalent to **OCF + 141.0 × 77% − capex − intangible investment − stock compensation − 92.9 × 77%**.

The non-client cash-interest split is **unresolved**: the 141.0 figure is an expense measure used as an explicit cash-interest proxy. The 229.922 adjustment is therefore a reconciliation estimate, not a reported client-interest payment. This keeps the model usable without pretending that the filing provides a cash split it does not provide. The tax rate is also a proxy for the marginal tax shield.

The compensation adjustment approximates the ongoing cost of future awards; the diluted denominator addresses existing dilution. Neither perfectly models future share issuance. I assume no additional share-count reduction from buybacks. Acquisitions and unusual working-capital movements are not separately normalized, so the result is an adjusted FCFF proxy rather than an exact measure of sustainable owner earnings.

### Growth forecast

Management projects fiscal 2027 revenue growth of **5%–6%**, adjusted EBIT-margin expansion of **70–90 basis points**, and adjusted diluted EPS growth of **9%–11%**. [Earnings release, p. 3](https://www.sec.gov/Archives/edgar/data/8670/000000867026000025/q4fy26exhibit99.htm).

My initial **7% total FCFF growth** assumes that modest margin improvement allows cash flow to grow somewhat faster than revenue. I reduce growth by half a percentage point each year as that benefit moderates. This forecast is my judgment; management did not provide this cash-flow path. EPS guidance is a reasonableness reference, not a substitute for company-wide cash-flow growth, because repurchases can increase EPS without increasing total cash generation.

### WACC estimate

| Component | Input | Date, source and treatment |
|---|---:|---|
| Risk-free rate | 4.83% | September 9, 2026 ten-year Treasury yield, [Yahoo Finance market recap](https://finance.yahoo.com/markets/live/stock-market-today-wednesday-september-9-dow-sp-500-nasdaq-futures-080411279.html); reference-date rate |
| Beta | 0.83 | [Stock Analysis overview, Beta field](https://stockanalysis.com/stocks/adp/), accessed September 10; vendor estimate, estimation window not verified |
| Equity risk premium | 4.5% | Analyst assumption September 10; not a measured ADP input |
| Pretax cost of debt | 5.14% | Recent note's effective rate, 10-K Note 10 p. 67; proxy for marginal funding cost, not a current bond yield |
| Tax rate | 23% | FY2026 effective rate used as tax-shield proxy |
| Market equity value | $105,362.023 million | $265.22 × 397.262737 million basic shares; July 31 cover-page shares used only for capital weights |
| Debt value | $4,944.1 million | 4,803.0 note fair value + 1.8 other debt + 139.3 reverse repos; June 30 values used as September proxies |

**Cost of equity = 4.83% + 0.83 × 4.5% = 8.565%.**

**After-tax cost of debt = 5.14% × 77% = 3.9578%.**

Equity and debt weights are approximately **95.52% and 4.48%**. Thus **WACC = 8.3585%, rounded to 8.4%**. This is a labeled estimate, not the previous report's investor-required return. Debt market values and basic shares determine capital weights; the assignment-required diluted average determines value per share.

### Terminal growth and the equity bridge

The **2.5% nominal terminal assumption** combines the Fed's **2% inflation objective** with an analyst allowance of roughly **0.5% real growth**. It is a restrained mature-business scenario tied to the long-run economy, not a sourced forecast of ADP or GDP. [Federal Reserve FAQ](https://www.federalreserve.gov/faqs/economy_14400.htm).

**Equity value = enterprise value + 4,368.7 − 4,944.1.** Debt includes the current portion through other debt; it is not added twice. Client-funds assets and client remittance obligations are excluded from surplus cash and financing debt. Reverse repos remain in the bridge as outstanding borrowing claims.

This simple bridge assumes corporate cash and securities can be valued at their reported amounts. Required operating liquidity, pledged balances and the economics of the client-funds portfolio could reduce distributable value. Keeping client-strategy financing costs in cash flow while deducting outstanding repos is a conservative simplification rather than a full valuation of that portfolio. Operating leases remain operating costs; no separate lease-debt deduction is made.

## I — ADP through the model

Year-end cash flows are discounted at 8.4%. The terminal value starts after Year 5.

| Forecast year | FCFF growth | FCFF, $ million | Present value, $ million |
|---|---:|---:|---:|
| FY2027 | 7.0% | 4,890.475 | 4,511.508 |
| FY2028 | 6.5% | 5,208.355 | 4,432.432 |
| FY2029 | 6.0% | 5,520.857 | 4,334.297 |
| FY2030 | 5.5% | 5,824.504 | 4,218.342 |
| FY2031 | 5.0% | 6,115.729 | 4,086.033 |

| Valuation step | Result |
|---|---:|
| PV of five explicit cash flows | $21,582.611 million |
| Terminal value: Year 5 FCFF × 1.025 ÷ (0.084 − 0.025) | $106,247.836 million |
| PV of terminal value | $70,986.160 million |
| Enterprise value | $92,568.771 million |
| Equity value after cash/debt bridge | $91,993.371 million |
| Divide by 403.3 million diluted shares | **$228.10 per share** |

The model uses full-year periods without a September stub-period adjustment. Its displayed precision is for reproducibility, not a claim of forecasting accuracy.

## V — Reasonableness

**$228.10 / $265.22 = approximately 0.86×**, inside the assignment's 0.5×–2× reasonableness band. The estimate is approximately **14.0% below** the reference price. I have not changed an assumption merely to match the price.

**The input I distrust most is starting normalized FCFF.** ADP's financing and investment activities complicate the distinction between operating and financing cash flows, and my interest adjustment uses an expense proxy. A mechanically correct DCF cannot eliminate that uncertainty. About **76.7% of enterprise value** comes from the terminal value, which also makes WACC and terminal growth consequential.

## E — Sensitivity grid and reverse DCF

All values are dollars per diluted share. Only WACC and terminal growth change in this grid.

| WACC / terminal growth | 1.5% | 2.5% | 3.5% |
|---|---:|---:|---:|
| 7.4% | 236.14 | 275.56 | 335.20 |
| 8.4% | 201.12 | **228.10** | 266.09 |
| 9.4% | 174.99 | 194.41 | 220.42 |

The base case is in the center. Value falls down each column and rises across each row. The opposing corners give **$174.99–$335.20**, approximately **34.0% below to 26.4% above** the reference price. This is a scenario range, not a confidence interval. The script marks terminal growth at or above WACC invalid.

**Reverse DCF question:** What uniform percentage-point shift in my five growth forecasts makes estimated value equal $265.22?

**Solved shift: +3.5584 percentage points per year.**

| Forecast year | Base growth | Price-implied growth |
|---|---:|---:|
| FY2027 | 7.0% | 10.5584% |
| FY2028 | 6.5% | 10.0584% |
| FY2029 | 6.0% | 9.5584% |
| FY2030 | 5.5% | 9.0584% |
| FY2031 | 5.0% | 8.5584% |

Held fixed: **starting FCFF $4,570.537 million; WACC 8.4%; terminal growth 2.5%; cash $4,368.7 million; debt $4,944.1 million; diluted shares 403.3 million; five forecast years; year-end discounting; and spacing between the annual growth rates.** Terminal growth is not increased by the solved shift.

Bisection uses an editable **−5 to +10 percentage-point bracket**. It rejects growth at or below −100% and reports no solution if the target is outside the bracket's valuation range. Repricing the solved path returns **$265.220000**. This is one set of assumptions consistent with the reference price, not proof of mispricing.

## Conditional call

**Initiate if the price is approximately $182 or lower while the base forecast and balance-sheet assumptions remain intact; otherwise watch/defer.** That threshold is approximately 20% below my $228.10 base estimate. A price below $228.10 would put the required growth below my forecast, but would not by itself meet my chosen margin-of-safety threshold.

**Monitor next quarter's adjusted EBIT-margin change against management's fiscal-year expansion objective.** Lack of progress would prompt a review of the initial cash-flow growth assumption before relying on the purchase threshold. Conversely, raising the forecast requires sourced evidence of sustainable cash generation rather than a higher stock price.

## Reproducibility and submission status

The accompanying `dcf.py` prints twelve base-case lines, the grid, and the reverse DCF using one command: **`python dcf.py`**. It has no external package requirements. Estimates and calculation inputs are editable at the top.

Run **`python dcf.py --training`** to check the separately labeled classroom example. All nine grid cells match the handout, and the solved shift is **+1.7779 percentage points**, reproducing the expected approximately +1.78. Training inputs are isolated from ADP inputs; the normal command runs ADP. Both modes print twelve base-case lines followed by the sensitivity and reverse-DCF blocks.

The original course `dcf.py` and its twelve known answers were not supplied; the provided attachment contains the assignment instructions. This is a new implementation, so preservation of an earlier script's exact inputs block and twelve-line format remains unverified. The available grid and reverse-DCF benchmarks have been verified.

The arithmetic, grid directions, reverse-solver repricing, invalid terminal-growth handling, invalid brackets, and unreachable-target behavior were tested. Files are ready to upload, but GitHub publication has not been performed. The same-day quote and comparison with the original course script's twelve known answers are the remaining submission-specific checks.

## Works Cited

Automatic Data Processing, Inc. [*Form 10-K for the Fiscal Year Ended June 30, 2026.*](https://www.sec.gov/Archives/edgar/data/8670/000000867026000030/adp-20260630.htm) U.S. Securities and Exchange Commission, 2026. Accessed September 10, 2026. Used for cash-flow inputs, interest adjustments, tax rate, corporate investments, debt, and share counts; specific statement and note locators appear above.

Automatic Data Processing, Inc. [“ADP Reports Fourth Quarter and Fiscal 2026 Results; Provides Fiscal 2027 Outlook.”](https://www.sec.gov/Archives/edgar/data/8670/000000867026000025/q4fy26exhibit99.htm) July 29, 2026. Exhibit 99, U.S. Securities and Exchange Commission. Accessed September 10, 2026. Used for management's revenue, margin, and earnings outlook and the growth forecast's business context.

Board of Governors of the Federal Reserve System. [“Why Does the Federal Reserve Aim for Inflation of 2 Percent over the Longer Run?”](https://www.federalreserve.gov/faqs/economy_14400.htm) Updated August 22, 2025. Accessed September 10, 2026. Used for the inflation objective underlying the terminal-growth rationale; the additional real-growth allowance is an analyst assumption.

Stock Analysis. [“Automatic Data Processing (ADP) Stock Price & Overview.”](https://stockanalysis.com/stocks/adp/) Accessed September 10, 2026. Used for the vendor-reported beta estimate of 0.83.

Stock Analysis. [“Automatic Data Processing (ADP) Stock Price History.”](https://stockanalysis.com/stocks/adp/history/) Accessed September 10, 2026. Used for the September 9, 2026 closing share price and quote timestamp.

Yahoo Finance. [“Stock Market Today: Dow, S&P 500, Nasdaq Fall as Treasury Yields Climb, Oil Tops $100.”](https://finance.yahoo.com/markets/live/stock-market-today-wednesday-september-9-dow-sp-500-nasdaq-futures-080411279.html) September 9, 2026. Accessed September 10, 2026 through the indexed search excerpt; direct-page retrieval was unavailable. Used for the reported September 9 ten-year Treasury yield of 4.83%.

The class instructions supplied with this assignment informed the report's structure, not its numerical inputs. Forecast growth, the equity risk premium, valuation adjustments, sensitivity ranges, and the margin-of-safety threshold are analyst assumptions or calculations, not figures attributed to these sources.
