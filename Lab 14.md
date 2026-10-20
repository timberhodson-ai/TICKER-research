# Lab 14 — Portfolio Baselines

## Decision

What does each simple portfolio earn and risk — and does any of them meet the Meridian mandate?

Course-authored training values are used, not market estimates. CPI is a labelled 2.5% estimate; CPI + 4% gives a 6.5% expected-return objective. Bills and the 10-year note are reserve-eligible.

## Files and commands

- `portfolio.py`: reusable risk engine; Python standard library only.
- `mandate.py`: Lab 13 checker with benchmark candidate E added.
- `portfolio_app.py`: Streamlit interface importing both engines.
- `verify_lab14.py`: known-answer and deliberate-break checks.
- `verify_portfolio_app.py`: Streamlit interaction checks.

```powershell
py mandate.py
py portfolio.py
py verify_lab14.py
py -m streamlit run portfolio_app.py
```

`python portfolio.py` also works if your Python installation exposes the `python` command.

## Verified results

| Portfolio | Bills / 10-year / IG / equity (%) | Return (%) | Volatility (%) | Reserve-eligible (%) | Meets 6.5%? |
|---|---|---:|---:|---:|---|
| Benchmark | 0.0 / 0.0 / 40.0 / 60.0 | 6.80 | 10.46 | 0.0 | yes |
| Equal weight | 25.0 / 25.0 / 25.0 / 25.0 | 5.20 | 5.21 | 50.0 | no |
| Inverse volatility | 84.3 / 6.0 / 7.0 / 2.6 | 3.77 | 1.05 | 90.3 | no |

Weights are calculated at full precision; displayed rounded weights may sum to 99.9%.

Executed the Lab 13 checker first: A and D pass every implemented rule; B fails three; C fails one. Added E as 40% IG bonds and 60% equity and reran: reserve weight is 0.0%, below the 3.0% minimum; E fails that rule only. The benchmark meets the expected-return objective but fails the reserve rule. The other two baselines miss the expected-return objective. None satisfies both requirements on these inputs. Expected volatility is not a guarantee about calendar-year losses; the unresolved Lab 13 CIO questions remain.

Automated verification matched every displayed known answer. Changing both IG–equity correlation cells to 0.50 produced 11.00% benchmark volatility. Setting both to 1.3 raised a clear refusal; an asymmetric table was also refused. Probes used copies, leaving the saved correlation at 0.25. These checks do not replace the required partner exchange.

Streamlit AppTest also passed: the displayed baseline volatility is 10.46%, candidate E shows a reserve failure, and moving the correlation slider to 0.50 changes volatility to 11.00%. The initial test hit the default three-second startup timeout; rerunning with a 30-second timeout passed.

## Diversification — AI study notes

Diversification combines assets whose returns do not move together perfectly. For positive weights, a correlation below +1 reduces the covariance contribution relative to perfect positive correlation; the size of the benefit depends on weights and volatilities. It does not always make a portfolio less volatile than every component.

For the benchmark, using decimal units:

```text
variance = (0.40 × 0.06)^2 + (0.60 × 0.16)^2
           + 2 × 0.40 × 0.60 × 0.25 × 0.06 × 0.16
         = 0.000576 + 0.009216 + 0.001152
         = 0.010944
volatility = sqrt(0.010944) = 0.10461357 = 10.46%
```

Omitting covariance gives sqrt(0.009792) = 9.90%, which is incorrect for the supplied correlation. At 0.50 correlation the cross term doubles, giving sqrt(0.012096) = 11.00%.

Inverse volatility assigns capital in proportion to 1/volatility. Bills' 0.5% volatility makes their inverse volatility 200, versus about 14.29, 16.67, and 6.25 for the other sleeves. Normalizing those numbers puts about 84.3% in bills. This rule does not optimize expected return or enforce the client's return target.

## Student and partner work — pending

### Completed AI comprehension quiz

- Student selected inverse-volatility normalization as the least-understood calculation.
- Question: For volatilities of 5% and 10%, inverse-volatility scores are 20 and 10. Using weight = score / sum of scores, what percentage goes into each asset, and why does A receive more?
- Student explanation before the AI explanation: "mathemeaticlaly it's because the lower the decimal means the higher the number returned will be if it's dividing something"
- Follow-up answer for the normalized weights: "66% and 33%"
- AI feedback: Correct approximately; the weights are 20/30 = 66.67% and 10/30 = 33.33%. Dividing every score by their common total preserves the 2:1 ratio and makes the weights sum to 100%. The code uses full precision, then rounds only for display. In `inverse_volatility_weights`, `inverse` contains the scores and `[value / sum(inverse) for value in inverse]` converts them into portfolio weights.

### Remaining student and partner activities

- Explain diversification to your partner without a screen.
- Explain `portfolio_volatility` line by line without AI; record your partner's question and your answer.
- Run and break the partner's file, then undo the change.
- In your own words: why does inverse volatility pile into bills? Which baseline would you show the CIO first, and why?

These activities have not been claimed as completed.

## Before Thursday — awaiting the student's Project 2 mandate

Lab 13 still lists the student's own client objective and constraints as pending. Supply that mandate or confirm the selected three to six funds before building the personal universe. The assignment's BIL / IEF / LQD / VT examples are practice examples, not an established personal selection.

`prices.csv` is pending fund selection and Yahoo Finance monthly adjusted-close verification. Record ticker, fund name, mandate role, source URL, and actual download date here when downloaded. Use five years of monthly Adj Close values, oldest first, with date first and one column per ticker. No synthetic price history has been substituted.

## GitHub checkout — pending

Repository destination/link is needed. Publish the Python and Markdown files and submit their GitHub file links individually. Local completion does not establish GitHub submission.
