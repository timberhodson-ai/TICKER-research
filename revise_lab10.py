"""One-time report refresh and regression checks for the Lab 10 revision."""
from pathlib import Path
import contextlib
import importlib.util
import io
import math
import re

root = Path(__file__).resolve().parent
report = root / 'Lab 10.md'
# This one-time helper reconstructs the report from its earlier backup. Protect
# later partner edits from being silently overwritten by an accidental rerun.
if '**My two-sentence answer (edited from my response):**' in report.read_text(encoding='utf-8'):
    raise SystemExit('Report now contains confirmed partner edits. Do not regenerate from the old backup; update the report directly.')
backup = root / 'Lab 10.before-technical-revision.md'
old = (backup if backup.exists() else report).read_text(encoding='utf-8')
if not backup.exists():
    backup.write_text(old, encoding='utf-8')
spec = importlib.util.spec_from_file_location('lab10', root / 'Lab 10_proforma.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
income, balance, cashflow, checks = m.run_model()
m.assert_balanced(checks)
for i in range(5):
    assert math.isclose(cashflow['Closing corporate cash'][i], cashflow['Opening corporate cash'][i] + cashflow['Free cash flow to equity (FCFE)'][i] - m.SHAREHOLDER_DIST, abs_tol=1e-8)
    previous = m.FY2026_INTANGIBLES if i == 0 else balance['Intangible assets, net'][i-1]
    assert math.isclose(balance['Intangible assets, net'][i], previous + cashflow['Capitalized intangible additions'][i] - previous*m.AMORT_INTANG_RATIO, abs_tol=1e-8)
try:
    m.assert_balanced(m.run_model(override_2027_cash=m.FY2026_CASH)[3])
except AssertionError as error:
    broken_message = str(error)
else:
    raise AssertionError('Broken balance sheet was not rejected')
# Exercise a funded revolver draw and a capacity failure, not just the base case.
original_dist = m.SHAREHOLDER_DIST
try:
    m.SHAREHOLDER_DIST = 5800.0
    si, sb, sc, sk = m.run_model()
    m.assert_balanced(sk)
    assert any(v > 0 for v in sc['Revolver draw / (repayment)'])
    for i in range(5):
        assert math.isclose(sc['Free cash flow to equity (FCFE)'][i], sc['FCFE before revolver financing'][i] + sc['Revolver draw / (repayment)'][i], abs_tol=1e-8)
    m.SHAREHOLDER_DIST = 10000.0
    try:
        m.assert_balanced(m.run_model()[3])
    except AssertionError as error:
        assert 'Liquidity check failed' in str(error)
    else:
        raise AssertionError('Insufficient revolver capacity was not rejected')
finally:
    m.SHAREHOLDER_DIST = original_dist
def capture(fn, *args):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        result = fn(*args)
    return out.getvalue().strip(), result
valuation_text, valuation = capture(m.perform_valuation, cashflow['Free cash flow to equity (FCFE)'])
value = valuation[2]
history = old[old.index('| Line Item | FY2024'):old.index('#### Two Items Independently')]
history = history.replace('| Confirmed |', '| Prior report; source locator retained |')
history = history.replace('Revenue − operating expenses', 'Contribution subtotal: revenue − operating expenses')
history = history.replace('Consolidated Balance Sheets, p. 47', 'FY2026 10-K p. 47 (FY2025/26); FY2025 10-K for FY2024, page unresolved')
ratio_rows = []
for label, vals in [
    ('Contribution margin: revenue minus operating expenses', [(19202.6-9050.1)/19202.6*100,(20560.9-9622.7)/20560.9*100,(21947.4-10240.6)/21947.4*100]),
    ('Gross margin after total cost of revenues',[(19202.6-10476.7)/19202.6*100,(20560.9-11097.3)/20560.9*100,(21947.4-11760.2)/21947.4*100]),
    ('Reported SG&A / contribution subtotal',[3778.9/10152.5*100,4051.7/10938.2*100,4408.2/11706.8*100]),
    ('Reported SG&A / gross profit after total cost of revenues',[3778.9/(19202.6-10476.7)*100,4051.7/(20560.9-11097.3)*100,4408.2/(21947.4-11760.2)*100]),
    ('Effective tax rate',[1120.3/4872.3*100,1230.4/5310.1*100,1316.8/5730.3*100]),
]:
    ratio_rows.append('| '+label+' | '+' | '.join(f'{v:.2f}%' for v in vals)+' |')
sec='https://www.sec.gov/Archives/edgar/data/8670/000000867026000030/adp-20260630.htm'
guidance='https://www.sec.gov/Archives/edgar/data/8670/000000867026000025/q4fy26exhibit99.htm'
text = f''' > **Class assignment:** Prepared for FIN 439. Values are conditional model outputs, not investment recommendations.

# Lab 10: ADP — Five-Year Integrated Pro Forma Valuation

**Company:** Automatic Data Processing, Inc. (Nasdaq: ADP)  
**Forecast:** FY2027E–FY2031E; FY2026 opening balance sheet; USD millions unless stated  
**Model value per share:** **${value:.2f}**  
**Share denominator:** 403.3 million FY2026 diluted weighted-average shares, held constant as a classroom convention  
**Verified market reference:** $263.68, September 23, 2026 closing price; retrieved September 24, 2026  
**Engine:** [Lab 10_proforma.py](Lab%2010_proforma.py)

## 1. D — The question

What are five years of your company's statements worth, built from assumptions you can defend?

ADP's distinctive line is **client funds**, rather than dealership inventory and floor-plan financing. The opening client assets of $43,957.8 million and obligations of $44,415.5 million are now displayed separately in the model. Their $457.7 million difference is retained; the engine does not force these balances to equal each other or treat client principal as distributable corporate cash.

The base case holds both client balances constant. Total revenue already includes client-funds interest, so adding another float-income line would double count it. This is an aggregate revenue model, with no separate portfolio-yield forecast: it does **not** demonstrate that fee growth offsets rate cuts. A separate yield scenario would require average investable balances and the timing of portfolio repricing.

**Filing correction:** FY2026 average client balances were $40.4 billion and client-funds interest revenue was $1,354.8 million. A one-percentage-point fall in the effective yield on the entire average balance implies about $404 million less annual pretax income before offsets. That is an illustrative full-portfolio calculation, not an immediate forecast following a one-point Fed cut. [FY2026 Form 10-K, MD&A](https://www.sec.gov/Archives/edgar/data/8670/000000867026000030/adp-20260630.htm)

**Actual partner question and answer:** Pending your confirmation; the prior report's rate-cut exchange has not been treated as verified partner dialogue.

## 2. R — History, ratios, and assumptions

### Source and verification scope

The historical grid below is retained from the earlier report, which identifies the FY2026 filing and FY2025 comparative balance sheet as its sources. The technical revision checked relevant FY2026 lines online; it did not independently re-audit every historical entry. A retained locator is not a new verification of the entire row. The requirement to have all three 10-Ks open and personally check two figures remains a student step.

Primary sources: [FY2026 Form 10-K]({sec}) and [FY2027 earnings outlook]({guidance}). FY2024 balance-sheet entries need an exact locator in the FY2025 filing; the FY2024 filing and supporting FY2023 opening PP&E have not been documented here.

### Three-year history grid

{history}

**Two figures for your personal check:** FY2026 revenue $21,947.4 million and net earnings $4,413.5 million, Statements of Consolidated Earnings, printed page 45. These are source checks to perform yourself; this report does not claim you completed them.

### Three-year ratio table

The model's 53.33% driver is a **contribution margin before R&D and D&A**, not gross margin after all reported costs of revenues. Both definitions are shown to prevent an inconsistent SG&A denominator.

| Ratio | FY2024 | FY2025 | FY2026 |
|---|---:|---:|---:|
{chr(10).join(ratio_rows)}
| Inventory days | 0.0 | 0.0 | 0.0 |
| PP&E depreciation / opening net PP&E | Unresolved: FY2023 opening PP&E needed | {201.8/685.6*100:.2f}% | {201.1/655.4*100:.2f}% |
| PP&E depreciation / closing net PP&E (different denominator) | {190.3/685.6*100:.2f}% | {201.8/655.4*100:.2f}% | {201.1/641.3*100:.2f}% |
| Reported revenue growth | 7.1% (prior report; FY2023 base unresolved) | {((20560.9/19202.6)-1)*100:.2f}% | {((21947.4/20560.9)-1)*100:.2f}% |
| Organic constant-currency growth | 6% (prior report; source recheck pending) | 7% | 6% |

### Capital-spending comparison

| Field (positive outflow magnitudes) | FY2024 | FY2025 | FY2026 |
|---|---:|---:|---:|
| Filing cash-flow statement: PP&E capex | 208.4 | 168.7 | 196.6 |
| Filing MD&A capex | Unresolved | 176.8 | 195.7 |
| External data provider's capex field | Unresolved | Unresolved | Unresolved |
| Capitalized intangible additions | 355.0 | 378.3 | 468.5 |
| Cash-flow capex plus intangible additions | 563.4 | 547.0 | 665.1 |

The MD&A is not a data provider. The external-provider comparison and the difference between the two filing presentations remain unresolved. The PP&E forecast now uses $212.5 million, the midpoint of the filing's FY2027 $200–225 million outlook; subsequent years hold that amount flat by judgment.

### Labelled assumption set

| Assumption / value | Label | Reason |
|---|---|---|
| Total revenue growth: 5.5% annually | Guidance / judgment | FY2027 midpoint of 5–6% **reported** revenue guidance; extending it through FY2031 is my model judgment, not five-year guidance. |
| Contribution margin: 53.33% | History / judgment | Approximately the latest-year margin, held flat. It is not the three-year average, which is about 53.14%. |
| SG&A before separately modeled D&A: {m.SGA_RATIO*100:.4f}% of contribution subtotal | History / judgment | Remove the 95.1 difference between total D&A (585.9) and cost-of-revenues D&A (490.8) from historical SG&A, then divide by 11,706.8. This aggregate reclassification avoids deducting that D&A twice; detailed functional allocation is not forecast. |
| R&D: 4.69% of revenue | History / judgment | Approximate FY2026 intensity, held constant to preserve ongoing development spending. |
| PP&E depreciation: {m.DEPR_PPE_RATIO*100:.4f}% of opening net PP&E | History / judgment | 201.1 / 655.4; apply the same turnover rate prospectively. |
| Intangible amortization: {m.AMORT_INTANG_RATIO*100:.4f}% of opening net intangibles | History / judgment | 384.8 / 1,603.0; a blended proxy covering the existing asset base and future additions, not the filing's existing-assets-only amortization schedule. |
| PP&E capex: $212.5 annually | Guidance / judgment | FY2027 guidance midpoint; flat thereafter as a simple maintenance-spending assumption. |
| Capitalized intangible additions: {m.SOFTWARE_CAPEX_RATIO*100:.4f}% of revenue | History / judgment | Preserve FY2026 reinvestment intensity (468.5 / 21,947.4) as revenue expands. |
| Tax rate: 23.0% of positive pretax income | Guidance / judgment | Approximate FY2027 adjusted tax outlook; no cash tax benefit assumed for losses. |
| Inventory and floor-plan debt: zero | History | Not relevant to this service business. |
| Client assets / obligations: $43,957.8 / $44,415.5, fixed | History / judgment | Isolate client principal and preserve the opening difference; do not treat it as equity cash flow. |
| Incremental other working capital: 1.2% of revenue change | Judgment | Simplified net operating investment allowance; detailed receivables, deferred contract costs and payables are not forecast separately. |
| Minimum corporate cash: $500 | Judgment | Modeling buffer for corporate liquidity; not a disclosed required minimum. |
| Revolver capacity: $2,000; rate: 5.5% | Judgment | Assumed corporate capacity available to this model, not ADP's total disclosed committed facilities. Use beginning debt for interest to avoid a circular calculation. |
| Term debt repayments: up to $200 annually | Judgment | Illustrative deleveraging, capped at outstanding debt; not a claim about contractual maturities. |
| Shareholder distributions: $3,500 annually | Judgment | Fixed cash-allocation scenario, not a forecast of the actual dividend payout ratio. No separate buyback share-count reduction is modeled. |
| Term borrowing rate: 4.50% | Judgment | Simplified corporate rate; does not reproduce total historical interest, including client-strategy financing. |
| Other income: $0; impairment: $0 | Judgment | No separate corporate investment income, gains, or impairment forecast. This omission can affect value and is not a claim that historical other income was zero. |
| Cost of equity: **8.565%** | Judgment | Inherited CAPM inputs: 4.83% + 0.83 × 4.50%. Use the exact result, not WACC. Input dates have not been refreshed. |
| Terminal growth: 2.50% | Judgment | Mature nominal growth assumption below the cost of equity. |
| Terminal debt policy: refinance scheduled term repayments | Judgment | Add back final-year term repayment before terminal growth; retain interest and capital reinvestment. Assumes access to refinancing, not debt forgiveness. |
| Shares: 403.3 million, constant | History / judgment | Historical diluted weighted average used as a per-share proxy; not today's point-in-time diluted shares. |
| Opening corporate cash added to value: $0 | Judgment | No separate excess-cash distribution is modeled; this is an operating FCFE value, not a fully reconciled excess-asset valuation. |

### Partner attack and two-sentence answer — awaiting your actual exchange

The previous draft attributed an AI competition/research-cost challenge to your partner. Please confirm or replace it before it is recorded as the actual exchange. Your final two-sentence response will be placed here, directly under the assumption table. If the response uses the earlier 90% threshold, it must say **retention below 90%**, not churn below 90%.

### Organic growth — learn on your own

Organic growth measures expansion of the existing business excluding acquired or divested operations; constant-currency growth also removes exchange-rate translation effects. ADP presents organic constant-currency growth in MD&A and reconciles it to reported growth. The total-revenue forecast here is not labeled organic. [ADP growth reconciliation]({sec})

Using the classroom figures supplied in the assignment, ABG's 1.8% represents growth in the comparable existing-store base, whereas 4.7% is reported growth across the changing company perimeter. Carrying 1.8% forward avoids assuming that acquisition-related expansion repeats without modeling the acquisition spending. This explains the teaching distinction; the video and exact bridge were not independently supplied for verification.

## 3. I — Company through the engine

Run `py "Lab 10_proforma.py"`. The model deducts PP&E and intangible investment, rolls both asset balances forward, includes net revolver borrowing in FCFE, and checks balance and minimum cash before valuation. D&A is charged once in earnings and added back once in cash flow.

The remaining balance sheet is aggregated: deferred taxes, stock compensation/dilution, deferred contract costs, noncontrolling interests and other operating balances do not have individual schedules. This is a classroom pro forma, not a complete reconstruction of reported GAAP cash flow. The fixed client-funds balances and aggregate revenue path also preclude a direct rate-cut sensitivity.

'''
for title, rows in [('Projected income statement',income),('Projected balance sheet',balance),('Projected cash flow / FCFE',cashflow)]:
    table, _ = capture(m.print_table,title,rows)
    text += f'### {title}\n\n```text\n{table}\n```\n\n'
check_text,_=capture(m.print_checks,checks)
text += f'''## 4. V — Checks and price comparison

```text
{check_text}
```

All five balance-sheet gaps are below the engine's $0.001 million tolerance and round to zero. Corporate cash remains above $500 million, ending at ${balance['Corporate cash & equivalents'][-1]:,.1f} million. The base case never draws the revolver because opening cash plus forecast cash generation covers investment, debt repayments and shareholder distributions.

```text
{valuation_text}
```

**Terminal interpretation:** Final-year FCFE plus the final scheduled term repayment is grown by 2.5% and capitalized at 8.565% minus 2.5%. This is a steady-state extrapolation with refinancing, not a perpetual extension of $200 million annual debt paydowns. Terminal value represents {valuation[1]*100:.2f}% of estimated equity value, so the result is sensitive to the terminal assumptions. No negative FCFE occurs in the base case; the engine refuses automatic valuation of nonpositive FCFE until its financing and terminal assumptions are reviewed.

**Market quote:** The earlier $265.74 September 24 quote could not be substantiated. The verified reference is **$263.68 at the September 23, 2026 close**, retrieved September 24, from [MarketBeat historical prices](https://www.marketbeat.com/stocks/NASDAQ/ADP/chart/), corroborated by [FinanceCharts](https://www.financecharts.com/stocks/ADP/summary/price). A timestamped September 24 quote remains unresolved.

> The model says ${value:.2f} per share, while the verified market reference says $263.68 at the September 23, 2026 close, using 403.3 million shares to express both implied equity values on a common basis: what different growth, reinvestment or risk assumptions could explain the gap?

The common denominator is a comparison convention; the market quotation itself is not calculated from our historical diluted share count.

## 5. E — Reciprocal partner exchange

**Pending actual details:** partner company/ticker; the assumption and number you challenged; your question; and the partner's response. The previous ABG / comparable-peer placeholder and suggested SG&A challenge have not been presented as a completed exchange. Your partner's attack and your two-sentence answer belong immediately below the assumption table above.

## 6. Refusal and regression verification

The revised engine was executed. Independently checked cash roll-forwards and intangible roll-forwards agree. Replacing FY2027 closing cash with opening cash causes this refusal:

```text
{broken_message}
```

A higher-distribution scenario exercised a funded revolver draw and confirmed that net borrowing enters FCFE; a still-higher-distribution scenario exhausted available funding and correctly failed the minimum-cash check. These are test scenarios, not the base-case assumptions.

## 7. Submission checklist

- [x] Five projected years balance and meet the cash floor.
- [x] Assumptions carry labels and reasons; simplifications are stated.
- [x] One reproducible value per share: **${value:.2f}**.
- [x] Organic-growth explanation and reported/organic distinction included.
- [ ] Confirm actual partner attack and add your two-sentence response beneath the table.
- [ ] Record actual reciprocal partner question and answer.
- [ ] Personally verify two historical figures and have the three required filings available.
- [ ] Resolve external-provider capex comparison and FY2024 source/opening-PP&E gaps.
- [ ] Obtain a sourced September 24 quote if the instructor requires that day's price rather than the latest verified close.
- [ ] Restore/rerun the ABG prerequisite: the work log records a prior $291.75 result, but `proforma.py` and `Lab 9.md` are currently empty, so that prior run is not reproducible from those files.

## Technical revision record — September 24, 2026

Revised both engine and report; supersedes the prior $222.39 result. Added intangible investment and amortization, avoided duplicate D&A, corrected CAPM arithmetic and ratio definitions, updated PP&E capex, separated client-funds balances, corrected FCFE financing, capped debt repayments, and regenerated all tables from the engine. Preserved the prior report as [Lab 10.before-technical-revision.md](Lab%2010.before-technical-revision.md), including its unconfirmed partner wording.
'''
report.write_text(text.lstrip(), encoding='utf-8')
print(f'Report updated. Value/share: ${value:.2f}. Base, cash/intangible roll-forwards, revolver, and refusal checks passed.')
