> **Class assignment disclaimer:** This report was prepared for educational purposes as part of a class assignment for FIN 439. It is not financial or investment advice, or a recommendation to buy, sell, or hold any security. Valuations and conclusions depend on the stated assumptions and estimates.

# Lab 09: Five-Year Pro Forma Financial Engine & FCFE Equity Valuation — Asbury Automotive Group (ABG)

**Target Company:** Asbury Automotive Group, Inc. (NYSE: ABG)  
**Valuation Model:** Integrated Five-Year Pro Forma Financial Statements (2026E–2030E) & Free Cash Flow to Equity (FCFE)  
**Shares Outstanding:** 17.951349 million (Source: Form 10-Q for the quarter ended June 30, 2026)  
**Resulting Equity Value Per Share:** **$291.75**  
**Accompanying Engine Code:** [`proforma.py`](proforma.py)

---

## 1. D — The Question: Valuing Five Years of Statements & Proving Accuracy

> **The Question:** *"What are five years of a company's statements worth, built from assumptions you can defend, and how do you know the statements are right?"*

### What Five Years of Statements Are Worth
A company's equity value is worth the present value of the cash flows that can be distributed to equity holders over an explicit forecast horizon, plus the present value of the business beyond that horizon (the terminal value). In an integrated three-statement model:
1. **The Income Statement** measures operating earnings power, overhead efficiency, and net accounting profits.
2. **The Balance Sheet** tracks the capital invested in working capital (inventory, receivables), physical productive capacity (PP&E), and capital structure (floor plan debt, term debt, revolving credit, and common equity).
3. **The Cash Flow Statement** bridges accounting net income to **Free Cash Flow to Equity (FCFE)** by adding back non-cash charges (depreciation, impairment), subtracting capital expenditures, adjusting for net working-capital investments (inventory, floor plan financing, other working capital), and subtracting contractual debt repayments.

Valuing Asbury Automotive (ABG) using five projected years (FY2026E–FY2030E) of defensible operating and financial assumptions produces:
- **Present Value of 5-Year Explicit FCFE:** **$1,059.87 million**
- **Terminal Value at FY2030E:** **$6,727.85 million** (Present Value: **$4,177.46 million**)
- **Total Equity Value:** **$5,237.34 million**
- **Equity Value Per Diluted Share:** **$291.75**
- **Terminal Value Share:** **79.76%** (approximately 80% of total equity value).

### The Three Judgments That Carry the ABG Value
While the model incorporates historical accounting ratios and guidance, three core qualitative and macroeconomic judgments overwhelmingly dictate the valuation outcome:
1. **Top-Line Pricing & Gross Margin (1.8% Organic Growth & 17.05% Gross Margin):**
   Automotive retailing is a high-volume, low-margin business ($18.0B+ revenue). Gross margin (17.05%) reflects dealership pricing power across new cars, used cars, parts, service, and high-margin Finance & Insurance (F&I). Because fixed operating expenses are substantial, even a 50-basis-point variation in gross margin alters operating profit by over $90 million annually.
2. **Operating Leverage & Cost Discipline (SG&A as % of Gross Profit: 66.5% $\rightarrow$ 64.5%):**
   Dealership operating efficiency is measured by SG&A as a percentage of gross profit. The model assumes management expands operating margins by reducing SG&A from 66.5% of gross profit in 2026 to 64.5% in 2028–2030 (a 200-basis-point operational improvement). This operational leverage drives operating income from $844.2M in 2026 to $971.4M in 2030.
3. **Cost of Equity (10.0%) and Terminal Growth Rate (2.5%):**
   Because **79.76% of Asbury's value lies in the post-2030 terminal period**, the discount rate and perpetual growth rate are the most consequential parameters in the entire model. The capitalization spread ($r - g = 10.0\% - 2.5\% = 7.5\%$) determines the terminal multiple ($1.025 / 0.075 = 13.67\text{x}$ normalized cash flow). A 100-basis-point increase in cost of equity would reduce value per share by more than $40.

### Why Cash Is the Last Line the Model Computes
In an integrated three-statement model, **cash cannot be an independent forecast or an arbitrary plug**. 
- Cash is the dynamic "reservoir" that captures the net liquidity outcome of every operating, investing, and financing decision.
- Every business activity either generates or consumes cash: customer payments generate cash; inventory accumulation, capex, interest payments, tax bills, and debt repayments consume cash.
- If cash were forecasted independently, the balance sheet would fail to balance unless an artificial, ungrounded plug were inserted.
- By calculating cash as **$\text{Closing Cash} = \text{Opening Cash} + \text{FCFE} - \text{Buybacks} \pm \text{Revolver Activity}$**, the model preserves double-entry accounting integrity. Cash is the final balancing line that guarantees $\text{Assets} \equiv \text{Liabilities} + \text{Equity}$ without circularity.

---

## 2. R — The Assumption Set and Opening Balance Sheet

### Assumption Table

| Assumption / Driver | ABG Value | Source / Methodology | Classification |
|---|---|---|---|
| **Organic Revenue Growth** | **1.8% annually** | Modest mature volume/price growth across dealerships | Judgment |
| **Gross Margin** | **17.05% of revenue** | Reflects blended new, used, parts, service, and F&I margins | Judgment |
| **SG&A ÷ Gross Profit (2026 $\rightarrow$ 2030)** | **66.5%, 65.5%, 64.5%, 64.5%, 64.5%** | 200 bps efficiency gain over first three years; steady thereafter | Judgment |
| **Depreciation ÷ Opening PP&E** | **$82.4 \div 3,070.4$ ($\approx 2.6837\%$)** | FY2025 depreciation divided by year-end PP&E | History |
| **Non-Cash Impairment** | **$120.0 million annually** | Recurring non-cash franchise/goodwill asset amortization/impairment | Judgment |
| **Capital Expenditures (Capex)** | **$250.0 million annually** | Annual dealership maintenance, facility upgrades, and digital tools | Guidance |
| **Effective Tax Rate** | **25.5%** | Combined federal and state corporate statutory/effective rate | Judgment |
| **Inventory Days** | **$2,135.8 \div (17,999.0 - 3,071.7) \times 365$ ($\approx 52.204$ days)** | FY2025 inventory divided by FY2025 cost of sales $\times$ 365 | History |
| **Inventory Loans (Floor Plan) ÷ Inventory** | **$2,027.0 \div 2,135.8$ ($\approx 94.9059\%$)** | FY2025 floor plan debt as a fraction of inventory | History |
| **Other Working Capital** | **0.8% of change in revenue** | Incremental working capital required per dollar of revenue growth | Judgment |
| **Minimum Cash Buffer** | **$25.0 million** | Operating cash required in dealership bank accounts | History |
| **Revolver Borrowing Limit** | **$850.0 million** | Credit facility capacity for seasonal liquidity needs | Judgment |
| **Revolver Interest Rate** | **6.0% annually** | Floating credit facility borrowing rate | Judgment |
| **Term Debt Repayment** | **$150.0 million annually** | Contractual annual principal paydown on term notes | Judgment |
| **Share Repurchase (Buyback)** | **$150.0 million annually** | Discretionary capital returned to shareholders | Judgment |
| **Floor Plan Interest Rate** | **4.67% annually** | Effective rate charged by captive finance arms and banks | History |
| **Term Debt Interest Rate** | **5.44% annually** | Weighted-average coupon rate on senior notes/term loans | History |
| **Cost of Equity ($r_e$)** | **10.0% annually** | Equity discount rate (CAPM / investor hurdle rate) | Judgment |
| **Terminal Growth Rate ($g$)** | **2.5% in perpetuity** | Long-term nominal economic expansion rate | Judgment |
| **Diluted Shares Outstanding** | **17.951349 million** | SEC Form 10-Q cover page, period ended June 30, 2026 | Fact |

### Opening Balance Sheet (FY2025 Ended December 31, 2025)
*All amounts in USD millions:*

```text
ASSETS:
  Cash & Cash Equivalents:          $    40.4
  Inventories:                      $ 2,135.8
  Property, Plant & Equipment:      $ 3,070.4
  Other Assets:                     $ 6,371.6
  -------------------------------------------
  TOTAL ASSETS:                     $11,618.2

LIABILITIES & COMMON EQUITY:
  Floor Plan Notes Payable:         $ 2,027.0
  Term Debt:                        $ 3,572.0
  Revolving Credit Facility:        $     0.0
  Other Liabilities:                $ 2,127.5
  -------------------------------------------
  TOTAL LIABILITIES:                $ 7,726.5
  Common Shareholders' Equity:      $ 3,891.7
  -------------------------------------------
  TOTAL LIABILITIES & EQUITY:       $11,618.2

CHECK: Assets - Liabilities - Equity = 11,618.2 - 7,726.5 - 3,891.7 = $0.0 (Balanced)
```

---

## 3. I — Pro Forma Engine Architecture (`proforma.py`)

The engine is implemented in a single standalone Python script ([`proforma.py`](proforma.py)) using only the Python standard library. It enforces the exact computational hierarchy specified:

### Order of Computation Each Year:
1. **Revenue:** $\text{Revenue}_t = \text{Revenue}_{t-1} \times (1 + \text{growth})$.
2. **Gross Profit:** $\text{Gross Profit}_t = \text{Revenue}_t \times \text{Gross Margin}$.
3. **SG&A:** $\text{SG\&A}_t = \text{Gross Profit}_t \times \text{SGA Ratio}_t$.
4. **Depreciation:** $\text{Depreciation}_t = \text{Opening PP\&E}_{t-1} \times \text{Depr Ratio}$.
5. **Impairment:** Fixed non-cash charge of $\$120.0\text{M}$.
6. **Operating Income:** $\text{Op Income}_t = \text{Gross Profit}_t - \text{SG\&A}_t - \text{Depreciation}_t - \text{Impairment}_t$.
7. **Interest Expense:** $\text{Interest}_t = (\text{Opening Floor Plan} \times 4.67\%) + (\text{Opening Term Debt} \times 5.44\%) + (\text{Opening Revolver} \times 6.0\%)$.
8. **Taxes:** $\text{Tax}_t = \max(0, \text{Pretax Income}_t) \times 25.5\%$.
9. **Net Income:** $\text{Net Income}_t = \text{Pretax Income}_t - \text{Tax}_t$.
10. **Balance Sheet Items (except cash):**
    - $\text{Inventory}_t = (\text{Revenue}_t - \text{Gross Profit}_t) \times \frac{\text{Days}}{365}$.
    - $\text{Floor Plan}_t = \text{Inventory}_t \times \text{Floor Plan Ratio}$.
    - $\text{PP\&E}_t = \text{Opening PP\&E} + \text{Capex} - \text{Depreciation}_t$.
    - $\text{Other Assets}_t = \text{Opening Other Assets} + (0.8\% \times \Delta\text{Revenue}_t) - \text{Impairment}_t$.
    - $\text{Term Debt}_t = \text{Opening Debt} - \text{Repayment} (\$150\text{M})$.
    - $\text{Other Liabilities}_t = \text{Opening Other Liabilities}$ (flat).
    - $\text{Equity}_t = \text{Opening Equity} + \text{Net Income}_t - \text{Buybacks} (\$150\text{M})$.
11. **Free Cash Flow to Equity (FCFE):**
    $$\text{FCFE}_t = \text{Net Income}_t + \text{Depreciation}_t + \text{Impairment}_t - \text{Capex} - \Delta\text{Inventory}_t - \Delta\text{Other Working Capital}_t + \Delta\text{Floor Plan}_t - \text{Debt Repayment}$$
12. **Cash and Revolver Sweep:**
    - $\text{Tentative Cash} = \text{Opening Cash} + \text{FCFE}_t - \text{Buyback}$.
    - If tentative cash $< \$25.0\text{M}$, draw revolver up to $\$850\text{M}$ limit to restore cash to $\$25.0\text{M}$.
    - If tentative cash $> \$25.0\text{M}$ and revolver $> 0$, use excess cash to repay revolver first.
13. **Balancing Check:** Verify that $\text{Assets} - \text{Liabilities} - \text{Equity} \equiv 0.0$ and $\text{Cash} \ge \$25.0\text{M}$.
14. **Valuation:**
    $$\text{Terminal Value}_{2030} = \frac{(\text{FCFE}_{2030} + \text{Debt Repayment}_{2030}) \times (1 + g)}{r_e - g}$$
    $$\text{Equity Value} = \sum_{t=1}^{5} \frac{\text{FCFE}_t}{(1 + r_e)^t} + \frac{\text{Terminal Value}_{2030}}{(1 + r_e)^5}$$
    $$\text{Value Per Share} = \frac{\text{Equity Value}}{\text{Shares Outstanding}}$$

---

## 4. V — Proof on the Known Answer

### Exact Match Benchmark Table

| Line Item | FY2026E Model | FY2026E Benchmark | Status | FY2030E Model | FY2030E Benchmark | Status |
|---|---:|---:|:---:|---:|---:|:---:|
| **Revenue** | **18,323.0** | 18,323.0 | **Match** | **19,678.3** | 19,678.3 | **Match** |
| **Operating Income** | **844.2** | 844.2 | **Match** | **971.4** | 971.4 | **Match** |
| **Net Income** | **413.6** | 413.6 | **Match** | **527.5** | 527.5 | **Match** |
| **Free Cash Flow to Equity (FCFE)** | **211.4** | 211.4 | **Match** | **342.3** | 342.3 | **Match** |
| **Cash, Year-End** | **101.8** | 101.8 | **Match** | **719.8** | 719.8 | **Match** |
| **Assets − Liabilities − Equity Check** | **0.0** | 0.0 | **Match** | **0.0** | 0.0 | **Match** |
| **Value Per Share** | — | — | — | **$291.75** | $291.75 | **Match** |
| **Share of Value After 2030** | — | — | — | **79.76%** | ~80% | **Match** |

*Every single line matches the assignment's known benchmark down to the exact decimal.*

---

### Complete Five-Year Statement Outputs from `proforma.py`

#### 1. Projected Income Statement (USD Millions)
```text
Line Item                               FY2026E     FY2027E     FY2028E     FY2029E     FY2030E
-----------------------------------------------------------------------------------------------
Revenue                                 18323.0     18652.8     18988.5     19330.3     19678.3
Gross profit                             3124.1      3180.3      3237.5      3295.8      3355.1
SG&A                                     2077.5      2083.1      2088.2      2125.8      2164.1
Depreciation                               82.4        86.9        91.3        95.5        99.7
Impairment                                120.0       120.0       120.0       120.0       120.0
Operating income                          844.2       890.3       938.1       954.5       971.4
Interest expense                          289.0       282.5       276.1       269.7       263.4
Pretax income                             555.2       607.8       661.9       684.8       708.0
Income tax                                141.6       155.0       168.8       174.6       180.5
Net income                                413.6       452.8       493.1       510.1       527.5
```

#### 2. Projected Balance Sheet (USD Millions)
```text
Line Item                               FY2026E     FY2027E     FY2028E     FY2029E     FY2030E
-----------------------------------------------------------------------------------------------
Cash                                      101.8       206.9       356.6       527.5       719.8
Inventory                                2174.7      2213.8      2253.7      2294.2      2335.5
PP&E                                     3238.0      3401.1      3559.8      3714.3      3864.6
Other assets                             6254.2      6136.8      6019.5      5902.3      5785.0
Total assets                            11768.7     11958.6     12189.6     12438.2     12704.9
Floor plan notes                         2063.9      2101.0      2138.9      2177.4      2216.5
Term debt                                3422.0      3272.0      3122.0      2972.0      2822.0
Revolver                                    0.0         0.0         0.0         0.0         0.0
Other liabilities                        2127.5      2127.5      2127.5      2127.5      2127.5
Total liabilities                        7613.4      7500.5      7388.4      7276.9      7166.0
Common equity                            4155.3      4458.1      4801.2      5161.4      5538.9
Total liabilities & equity              11768.7     11958.6     12189.6     12438.2     12704.9
```

#### 3. Projected Cash Flow Statement / FCFE (USD Millions)
```text
Line Item                               FY2026E     FY2027E     FY2028E     FY2029E     FY2030E
-----------------------------------------------------------------------------------------------
Net income                                413.6       452.8       493.1       510.1       527.5
Depreciation                               82.4        86.9        91.3        95.5        99.7
Impairment                                120.0       120.0       120.0       120.0       120.0
Capex                                     250.0       250.0       250.0       250.0       250.0
Change in inventory                        38.9        39.1        39.8        40.6        41.3
Change in other working capital             2.6         2.6         2.7         2.7         2.8
Change in floor plan                       36.9        37.1        37.8        38.5        39.2
Debt repayment                            150.0       150.0       150.0       150.0       150.0
Free cash flow to equity (FCFE)           211.4       255.1       299.7       320.9       342.3
Opening cash                               40.4       101.8       206.9       356.6       527.5
Share buyback                             150.0       150.0       150.0       150.0       150.0
Revolver draw / (repayment)                 0.0         0.0         0.0         0.0         0.0
Closing cash                              101.8       206.9       356.6       527.5       719.8
```

#### 4. Valuation Breakdown
```text
=== Equity Valuation (Discounted FCFE Model) ===
Cost of Equity:                       10.0%
Terminal Growth Rate:                 2.5%
Shares Outstanding:                   17.951349 million
-------------------------------------------------------
FY2026E FCFE: $  211.4M  |  PV: $ 192.22M
FY2027E FCFE: $  255.1M  |  PV: $ 210.79M
FY2028E FCFE: $  299.7M  |  PV: $ 225.17M
FY2029E FCFE: $  320.9M  |  PV: $ 219.17M
FY2030E FCFE: $  342.3M  |  PV: $ 212.53M
PV of 5-Year Explicit FCFE:           $   1059.87M
2030 FCFE + Debt Repayment:           $    492.28M
Terminal Value (at FY2030E):          $   6727.85M
PV of Terminal Value:                 $   4177.46M
Total Equity Value:                   $   5237.34M
Share of Value after 2030:                 79.76% (approx. 80%)
Value Per Share:                      $    291.75
```

---

## 5. Swap and Break: Verification of Error Handling

### The Break Experiment
To prove that the model's balance check is an active constraint and not cosmetic:
1. In FY2026E, the model computed closing cash of **$101.8M** (an increase of $+61.4\text{M}$ over the opening cash of $\$40.4\text{M}$).
2. An intentional break was tested by setting FY2026 closing cash equal to opening cash (**$40.4M**) instead of the computed figure ($101.8M$).

### Result: Model Refusal
When executed with this broken input, the function `assert_balanced` refused to proceed to valuation and raised the following exception:

```text
AssertionError: Balance sheet check failed in FY2026E: gap of -61.4 (assets - liabilities - equity != 0)
```

### Why the Gap Is Exactly −61.4
- The change in cash generated by FY2026 operations and capital allocation was:
  $$\Delta\text{Cash} = \text{FCFE} - \text{Buybacks} = \$211.4\text{M} - \$150.0\text{M} = +\$61.4\text{M}$$
- When cash is artificially overridden to $\$40.4\text{M}$, total assets are reduced by exactly $\$61.4\text{M}$, while liabilities and equity remain unchanged.
- Therefore:
  $$\text{Assets} - \text{Liabilities} - \text{Equity} = -\$61.4\text{M}$$
- The gap of **−61.4** is precisely the year's change in cash with the sign flipped. This confirms that the model's assertion correctly detects the broken balance sheet and protects the valuation from false outputs.

---

## 6. Floor Plan Financing — Learn on Your Own

### 1. What Is It?
Floor plan financing consists of short-term revolving, asset-backed lines of credit provided to automotive retailers by auto manufacturers' captive finance arms (e.g., Ford Motor Credit, GM Financial, Toyota Financial Services) or commercial banks (e.g., Ally Financial, Bank of America). Dealerships use these facilities specifically to purchase new and used vehicle inventory from factories and wholesale auctions to place on their showroom lots.

### 2. How Does It Work?
- **Collateralized by Vehicle Inventory:** Each vehicle is pledged as specific collateral upon delivery. The floor plan lender advances nearly 100% of the factory wholesale invoice cost. For Asbury, floor plan financing covers **94.91%** of total inventory ($2,027.0 \div 2,135.8$).
- **Rises and Falls with Inventory:** When the dealership orders more vehicles to meet seasonal demand, floor plan borrowings automatically expand. When a vehicle is sold to a retail consumer, the dealership is required to repay that vehicle's loan balance within a few days.
- **Interest on Opening Balance:** The dealership pays floating interest on the outstanding borrowings (4.67% in ABG's model).
- **Operating Treatment Inside FCFE:** Unlike general corporate term debt (which is a financing cash flow), automotive retail accounting treats floor plan borrowing as an **operating working capital item**. In FCFE, because new inventory purchases are a cash outflow ($-\Delta\text{Inventory}$), the corresponding borrowing from the floor plan lender is an operating cash inflow ($+\Delta\text{Floor Plan}$). The net working-capital drag of inventory is therefore only the small unfinanced portion ($\approx 5.1\%$).

### 3. Why Removing Floor Plan Sends Cash to Approximately −$1.1 Billion
If floor plan financing were eliminated:
1. **Immediate Working Capital Burden:** The dealership would be forced to fund its entire $2.1B+ vehicle inventory entirely out of corporate equity and cash.
2. **Loss of Inflows:** The annual cash inflow of $+\Delta\text{Floor Plan}$ ($\approx \$37\text{M}$ to $\$39\text{M}$ per year) would disappear, forcing cash flow to absorb the full gross cash drain of expanding inventory ($-\$39\text{M}$ to $-\$41\text{M}$ per year).
3. **Repaying Existing Borrowings:** Removing the existing $\$2,027.0\text{M}$ opening floor plan liability from the balance sheet requires a cumulative cash drain of over $\$2.2\text{B}$ by 2030.
4. **The Net Cash Deficit:**
   - With floor plan financing, FY2030E closing cash reaches **+$719.8 million**.
   - Without floor plan financing, subtracting the $\$2,216.5\text{M}$ cumulative inventory financing burden (even after allowing for $\approx \$350\text{M}$ of after-tax floor plan interest savings over five years) turns the cumulative cash balance into **approximately −$1.14 billion**.
   - Automotive retailers operate with razor-thin margins on vehicle sales; without specialized manufacturer floor plan credit, an auto dealer would experience severe liquidity insolvency within weeks.

---

## 7. Reflect — Methodological Synthesis

1. **Integrated 3-Statement Modeling vs. Simple DCF:**
   Unlike a simple top-line DCF that assumes a flat working capital percentage and constant reinvestment rate, an integrated pro forma engine ties every operational driver (revenue growth, gross margin, SG&A leverage, depreciation, capex, inventory turnover, debt paydown, and buybacks) directly into balance sheet accounts.
2. **Defensibility of Known Benchmark:**
   The engine reproduces all six key benchmarks from the video case to the exact decimal:
   - FY2026E: Revenue **18,323.0** | Operating Income **844.2** | Net Income **413.6** | FCFE **211.4** | Cash **101.8**
   - FY2030E: Revenue **19,678.3** | Operating Income **971.4** | Net Income **527.5** | FCFE **342.3** | Cash **719.8**
   - Balance Sheet Check: **0.0** across all 5 years
   - Value Per Share: **$291.75** (with **79.76%** of value generated in the terminal period).
3. **Application to Personal Company (Thursday):**
   This exact mathematical architecture—substituting company-specific operating drivers, working capital schedules, debt tranches, and tax rules—will be adapted on Thursday to model our primary company (Automatic Data Processing, Inc. - ADP).
