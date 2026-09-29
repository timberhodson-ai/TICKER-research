# Lab 11 — Pro Forma Sensitivity

**Automatic Data Processing, Inc. (ADP)**  
FIN 439 | September 29, 2026  
Forecast period: FY2027–FY2031 | Based on the existing Lab 10 integrated pro forma

## Purpose and approach

This analysis measures how ADP's forecast operating profit, free cash flow to equity (FCFE), and modeled value per share change when revenue growth or operating margin changes. Each driver is tested separately at its previously specified lower, base, and higher values. It is a sensitivity analysis, not a probability-weighted forecast or a combined best/worst case.

Each run uses a fresh independent copy of the preserved base inputs. Only the selected driver changes; linked expenses, taxes, reinvestment, assets, cash, and equity recalculate through the full model. The base is restored and rerun after the analysis.

**Units:** Operating profit, FCFE, and statement amounts are USD millions. Value is USD per share. Operating profit means EBIT. FCFE is after interest, taxes, reinvestment, and net borrowing, but before dividends and share repurchases. A percentage-point change is an absolute change in a rate: 26.43% to 27.43% is one percentage point.

## 1. Drivers and reproducible ranges

| Driver | Lower | Base | Higher | Affected years |
|---|---|---|---|---|
| Total reported revenue growth | 4.0% annually | 5.5% annually | 7.0% annually | FY2027–FY2031 |
| Operating margin: EBIT / revenue | Base path minus 1.00 percentage point each year | Model-generated annual path below | Base path plus 1.00 percentage point each year | FY2027–FY2031 |

| Operating-margin path | FY2027 | FY2028 | FY2029 | FY2030 | FY2031 |
|---|---:|---:|---:|---:|---:|
| Lower | 25.43% | 25.45% | 25.47% | 25.50% | 25.53% |
| Base | 26.43% | 26.45% | 26.47% | 26.50% | 26.53% |
| Higher | 27.43% | 27.45% | 27.47% | 27.50% | 27.53% |

The margin shifts use the unrounded base path. They apply once to each affected year's margin and do not accumulate. The model implements the shift as a separate cash operating-cost adjustment, so the tax, cash-flow, and balance-sheet consequences remain linked. The existing 53.33% contribution margin is before SG&A, R&D, and D&A; it is not operating margin.

**Revenue-growth range — guidance and labeled judgment.** The 5.5% base is the midpoint of ADP's FY2027 reported-growth guidance of 5%–6%. Extending it through FY2031 is model judgment. FY2026 reported revenue grew approximately 6.74%, supporting 7.0% as a higher-growth sensitivity. The 4.0% lower case represents the previously selected judgment for weaker hiring, slower client additions, or weaker pricing. The endpoints are sensitivity assumptions, not management's five-year forecast. [ADP FY2026 results and FY2027 outlook](https://www.sec.gov/Archives/edgar/data/8670/000000867026000025/q4fy26exhibit99.htm)

**Operating-margin range — labeled judgment.** The existing ±1.00-percentage-point range allows for cost pressure or operating efficiencies around the model's base path. Higher research, service, cybersecurity, or selling costs could reduce margin; automation and scale could increase it. The base path and range are model operating margins, not ADP's adjusted EBIT margin guidance.

Revenue starts from the existing FY2026 base of **$21,947.4 million**. Each subsequent year's revenue equals prior-year revenue multiplied by one plus that year's growth rate. No new company data or ranges were introduced.

## 2. Sensitivity results

All outputs below are for FY2031, except value per share, which discounts the full forecast and terminal cash flows. Changes equal scenario output minus base output, calculated before rounding.

| Driver and run | EBIT ($m) | Change ($m) | FCFE ($m) | Change ($m) | Value/share ($) | Change ($/share) |
|---|---:|---:|---:|---:|---:|---:|
| Revenue growth: lower, 4.0% | 7,050.97 | −559.86 | 4,975.80 | −397.92 | 187.89 | −13.09 |
| Revenue growth: base, 5.5% | 7,610.83 | 0.00 | 5,373.72 | 0.00 | 200.99 | 0.00 |
| Revenue growth: higher, 7.0% | 8,203.83 | +593.00 | 5,794.57 | +420.85 | 214.79 | +13.81 |
| Operating margin: lower, −1.00 pp | 7,323.98 | −286.84 | 5,152.85 | −220.87 | 192.92 | −8.06 |
| Operating margin: base path | 7,610.83 | 0.00 | 5,373.72 | 0.00 | 200.99 | 0.00 |
| Operating margin: higher, +1.00 pp | 7,897.67 | +286.84 | 5,594.59 | +220.87 | 209.05 | +8.06 |

**All six runs pass the model's accounting and liquidity checks.** FY2031 FCFE is positive in every run. Raising either driver increases EBIT, FCFE, and modeled value; lowering either driver decreases them. These value changes are not realized investment returns or IRRs.

### Output spans over the tested ranges

A span is the maximum minus the minimum among valid lower/base/higher results.

| Driver | EBIT span ($m) | FCFE span ($m) | Value span ($/share) |
|---|---:|---:|---:|
| Revenue growth: 4.0%–7.0% | 1,152.86 | 818.77 | 26.90 |
| Operating margin: base ±1.00 pp | 573.69 | 441.74 | 16.12 |

**Over these ranges, revenue growth is the larger driver for operating profit, FCFE, and conditional value per share.** Growth compounds over five years. However, the growth range is three percentage points wide and the margin range is two percentage points wide, and the rates have different economic meanings. A larger span does not establish that revenue growth is inherently more important. The ranking could change with different ranges.

## 3. Trace one changed result through the statements

The selected case increases revenue growth from **5.5% to 7.0% annually**. An input comparison confirmed that only `REVENUE_GROWTH` changes. Opening balances, contribution margin, SG&A and R&D ratios, tax rate, investment ratios, distributions, financing assumptions, and valuation assumptions remain at base. The operating-margin adjustment remains zero. Dollar costs and the resulting margin are linked outputs and recalculate.

### Income statement

FY2031 revenue rises from **$28,684.37 million to $30,782.36 million**. Higher revenue increases the contribution subtotal, but also raises revenue-linked expenses and amortization associated with capitalized software investment.

| FY2031 bridge | Change from base ($m) |
|---|---:|
| Contribution before R&D and D&A | +1,118.86 |
| SG&A expense excluding D&A | +412.22 |
| R&D expense | +98.40 |
| D&A expense | +15.25 |
| **Operating profit / EBIT** | **+593.00** |
| Interest expense | 0.00 |
| Income tax expense | +136.39 |
| **Net earnings** | **+456.61** |

Expense increases are deducted from the contribution increase. Interest is unchanged; the 23% tax rate reduces the additional pretax earnings to $456.61 million of additional net earnings.

### Cash flow and balance sheet

| FY2031 FCFE bridge | Effect on FCFE ($m) |
|---|---:|
| Additional net earnings | +456.61 |
| Additional D&A add-back | +15.25 |
| Additional capitalized intangible investment | −44.78 |
| Additional working-capital investment | −6.22 |
| Changes in PP&E capex, debt repayments, and revolver financing | 0.00 |
| **Total FCFE change, before rounding** | **+420.85** |

The additional reinvestment explains why FCFE grows less than net earnings. Software investment increases intangible assets and future amortization; working-capital investment increases other corporate assets. Fixed shareholder distributions allow incremental FCFE to accumulate in cash. FY2031 corporate cash rises from **$10,608.39 million to $11,765.66 million**, a cumulative increase of **$1,157.27 million** across the forecast. Retained earnings increase equity, and the balance sheets continue to balance.

The higher forecast FCFE and terminal cash flow increase value from **$200.99 to $214.79 per share**. The discount rate and terminal-growth assumptions do not change.

For comparison, the higher-margin case adds 1% of base revenue to EBIT: $28,684.37 million × 0.01 = **$286.84 million**. After 23% tax, the increase is **$220.87 million** of FCFE. Revenue-linked reinvestment is unchanged in that margin-only run.

### Difference verification

Using outputs shown to six decimal places:

- EBIT: 8,203.826243 − 7,610.828027 = **+592.998216 million**.
- FCFE: 5,794.570810 − 5,373.721115 = **+420.849695 million**.
- Value: 214.794699 − 200.986146 = **+13.808553 per share**.

The audit uses the stored full-precision values. It verifies all 18 signed output changes and all six output spans.

## 4. Restored base and accounting audit

| Base output | Before analysis | After restoration | Difference | Status |
|---|---:|---:|---:|---|
| FY2031 EBIT ($m) | 7,610.83 | 7,610.83 | 0.00 | PASS: exact match |
| FY2031 FCFE ($m) | 5,373.72 | 5,373.72 | 0.00 | PASS: exact match |
| Value ($/share) | 200.99 | 200.99 | 0.00 | PASS: exact match |

| Audit check | Result |
|---|---|
| Fresh copies; only selected independent input changed | PASS |
| Balance-sheet equation across 30 scenario-years | PASS |
| EBIT, net earnings, and FCFE reconciliations | PASS |
| Cash and equity roll-forwards | PASS |
| Minimum corporate cash | PASS: lowest cash $4,759.17m versus $500.00m floor |
| Revolver limit | PASS: maximum outstanding $0.00m versus $2,000.00m limit |
| Signed differences and spans | PASS |
| Final restored base versus initial base | PASS: exact equality |

**ACCOUNTING FAILURES: None found in the actual runs.** The largest absolute reconciliation residual is approximately 0.00000000000728 USD million, below the 0.001-million accounting tolerance. The existing cash-floor tolerance is 0.0001 million.

**ROUNDING:** Output display tolerance is 0.005 million for EBIT/FCFE and $0.005/share for value, corresponding to half the two-decimal display unit. Because calculations precede rounding, subtracting displayed values can differ from the displayed change by 0.01. This is not an accounting failure.

Separate control tests deliberately introduce a broken cash balance, an invalid discount rate, and negative FCFE to verify failure handling. These are test fixtures, not company scenarios. Invalid accounting runs are flagged rather than ranked; signed cash flows are retained when valuation is withheld.

## 5. Valuation status and scope

**VALUATION LIMITATION:** The values are conditional outputs of the existing classroom FCFE model. They pass its accounting and mathematical valuation checks, but do not constitute a fully validated market valuation.

The model retains an **8.565% cost of equity**, **2.50% terminal growth**, and **403.3 million shares**. It assumes scheduled term-debt repayments are refinanced after FY2031 and adds back the final-year scheduled repayment in the terminal calculation. Approximately **77% of base value comes from the terminal period**. No separate excess-cash value is added.

The discount-rate inputs have not been refreshed, some historical source checks remain unresolved, and client-funds portfolio yields are not modeled separately. Thus the calculations are resolved, while the economic assumptions remain conditional. Positive FCFE and passing accounting checks alone do not validate those assumptions.

The analysis establishes how the existing model responds to the stated drivers. It does not by itself change the base valuation, establish scenario probabilities, or supply a new investment recommendation. No personal investment conclusion is attributed to the student here.

## 6. Supporting records and reproducibility

The numerical analysis is complete and the visible tables above can be reviewed without running code. The following files retain the implementation and full statement details:

- [Existing pro forma](Lab%2010_proforma.py) and [sensitivity runner](adp_sensitivity.py).
- [Full scenario statements and annual inputs](ADP_sensitivity_results.md).
- [Full-precision inputs and outputs](ADP_sensitivity_details.json).
- [Audit report](ADP_sensitivity_audit.md) and [audit script](audit_adp_sensitivity.py).
- [Input-isolation and invalid-run tests](test_adp_sensitivity.py).
- [Separate partner-exchange record](ADP_partner_exchange_record.md).

To reproduce the analysis:

```powershell
py "Lab 10_proforma.py" --sensitivity
py audit_adp_sensitivity.py
```

**Assignment documentation:** An actual partner exchange and an original locked prediction for this exercise were not supplied. They are not represented as completed or reconstructed retrospectively. Their placeholders remain in the separate partner record; they are not necessary for the numerical sensitivity calculations. The student's personal valuation conclusion or research-priority response likewise remains unrecorded.

Prepared with AI assistance from the existing FIN 439 model and recorded sensitivity outputs.
