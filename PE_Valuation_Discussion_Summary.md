# P/E Valuation Discussion Summary

Date: September 15, 2026

## What P/E means

The price-to-earnings (P/E) ratio measures how much investors pay for each dollar of a company's annual earnings.

**P/E = Stock price / Diluted earnings per share (EPS)**

We initially discussed this using ADP as context. A hypothetical $300 stock price and $10 EPS produce a 30x P/E. Those were illustrative numbers, not verified ADP data.

P/E helps compare companies of different sizes by expressing price relative to earnings. A lower stock price alone does not mean a stock is cheaper relative to its profits.

## When P/E helps and when it can mislead

- P/E is most useful for comparing profitable companies with similar businesses, growth prospects, and risks.
- A high P/E can reflect expected growth or an expensive valuation. A low P/E can indicate value or weak prospects.
- Negative earnings make P/E generally not meaningful for valuation; zero earnings make the ratio undefined.
- One-time gains can inflate earnings and make P/E appear unusually low. One-time expenses can reduce earnings and make P/E unusually high.
- Faster expected growth can justify a higher multiple, so different growth prospects complicate comparisons.
- Trailing P/E uses historical earnings; forward P/E uses forecasts. Comparisons should use consistent earnings definitions and periods.
- P/E should be considered alongside growth, earnings quality, debt, and cash flow. However, this P/E valuation does not add cash or subtract debt: multiplying P/E by EPS already produces an equity price per share.

## Asbury case: user-supplied inputs

The numerical exercise moved from ADP to Asbury Automotive. No data was fetched for the script. Inputs below were supplied by the user.

| Company | Ticker | Role | December 31, 2024 closing price | FY2024 total GAAP diluted EPS |
|---|---|---|---:|---:|
| Asbury Automotive | ABG | Target | $243.03 | $21.50 |
| AutoNation | AN | Candidate peer | $169.84 | $16.92 |
| Group 1 Automotive | GPI | Qualified candidate peer | $421.48 | $36.81 |

The script uses the supplied peer selection; the arithmetic does not independently establish business comparability.

## How the calculation works

1. Divide each valid peer's price by its diluted EPS.
2. Find the minimum, median, and maximum peer P/E.
3. Multiply each of those multiples by Asbury's EPS to estimate its price.
4. Remove each peer in turn and recalculate the median-implied price using the remaining usable peers.
5. Subtract the original full-peer median-implied price from the new estimate to measure the dollar change.

With two peers, the median equals the average of their two P/E multiples. Asbury's observed stock price is used to calculate its own P/E, but is not an input to the peer-implied prices.

## Python file and calculation rules

Script: [peer_pe.py](peer_pe.py)

- One Python file, using only the standard library; no package installation or data downloads.
- Editable target and peer inputs at the top.
- Peer tickers are normalized for capitalization and surrounding whitespace. The target is excluded, and duplicate peers retain their first occurrence.
- Missing, invalid, or nonpositive prices or EPS make affected calculations not meaningful. Invalid peers are excluded from the peer statistics.
- An invalid target price prevents its own P/E calculation, but valid target EPS can still support peer-implied prices. Invalid target EPS prevents implied-price calculations.
- One usable peer produces a reference estimate with no range; no usable peers produces no estimate.
- Removing an invalid peer leaves the usable-peer estimate unchanged. If removal leaves no usable peers, there is no estimate.
- Decimal-string inputs are converted to exact rational numbers with `Fraction`. Calculations retain full precision, including the leave-one-out dollar changes.
- Only displayed values are rounded: multiples to six decimal places and prices to cents.
- No cash/debt bridge is applied.

### Verified working run command

```powershell
python "C:\Users\timbe\OneDrive\Desktop\FIN 439\peer_pe.py"
```

The script ran successfully with `python`. The sandbox initially blocked the Windows Python launcher; execution outside the sandbox succeeded. Edge-case checks also passed for duplicate/target exclusion, invalid inputs, zero peers, one peer, and display rounding.

## Actual output compared with the case checks

| Check | Actual result | Status |
|---|---:|---|
| AutoNation P/E | 10.037825x | Pass |
| Group 1 P/E | 11.450149x | Pass |
| Peer median P/E | 10.743987x | Pass |
| Asbury minimum implied price | $215.81 | Pass |
| Asbury maximum implied price | $246.18 | Pass |
| Asbury at peer median | $231.00 | Pass |
| Remove GPI: remaining AN estimate | $215.81 | Pass |
| Remove GPI: change from full-peer estimate | -$15.18 | Pass |

Additional output: Asbury's own P/E was 11.303721x. Removing AN instead leaves a GPI-only reference estimate of $246.18, a +$15.18 change from the full-peer estimate.

## Leave-one-out prediction and explanation

Before explaining the result, we discussed how removing a peer changes the valuation benchmark while leaving Asbury's EPS unchanged.

In general, removing a higher-P/E peer may lower the median-based estimate; removing a lower-P/E peer may raise it. With more peers, a removal can leave the median unchanged. These are changes to the model's estimated value, not automatic changes in the actual market price.

**Your prediction:** Removing Group 1 would decrease the estimated price.

**Your reasoning:** Excluding the larger value that was pulling up the average would lower the estimated price.

That reasoning is correct here. With two peers, the median is their average. Group 1's P/E is higher than AutoNation's, so removing Group 1 leaves the lower multiple to apply to Asbury's unchanged $21.50 EPS.

The key comparison is the higher **P/E**, not the higher stock price or larger company size.

### Why the displayed change is -$15.18

The original estimate displays as $231.00, and the AN-only estimate displays as $215.81. Subtracting these already-rounded amounts gives -$15.19. The script instead subtracts the full-precision estimates and then rounds the difference, correctly displaying **-$15.18**.

### Why one peer gives a reference estimate, not a range

One remaining peer supplies only one comparison multiple. There are no distinct low and high peer multiples to form a range, so the result is labeled a **reference estimate**. It depends entirely on that one peer and does not express a spread across comparable companies.

## Sources used for the general P/E discussion

- [Investor.gov: Price-Earnings Ratio](https://www.investor.gov/introduction-investing/investing-basics/glossary/price-earnings-ratio)
- [Fidelity: P/E Ratio](https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/pe-ratio)
- [Fidelity: What is price-to-earnings ratio?](https://www.fidelity.com/learning-center/trading-investing/pe-ratio)
- [AccountingTools: Price earnings ratio definition](https://www.accountingtools.com/articles/price-earnings-ratio)

These sources supported the conceptual discussion. The Asbury case inputs came from the user, and the numerical results came from the local Python script.
