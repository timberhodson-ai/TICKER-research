# Lab 16: Point-in-time data

## Assignment and work boundary

This document covers only the assignment pasted and worked on October 27, 2026: the fictional AAA/BBB/CCC table, four provenance rules, as-of versus naive signals, yield sanity check, code quiz, and April 15 comparison. This assignment is Lab 16, including where the pasted instructions refer to a "Lab 15 chat."

The earlier Lab 15 portfolio-allocation work remains separate in `Lab 15.md`, `Lab 15 README.md`, `portfolio.py`, `app.py`, `prices.csv`, and `verify_lab15.py`. Its results and partner records are not included here. See [Lab 16 README.md](Lab%2016%20README.md) for this assignment's file guide.

## Question

On the day you would have traded, what did this data actually say—and how much of what you see now came later?

The month measured describes the period of an observation. The publication date tells us when it became available. A revision supplies a later version of the same month's observation. For a March 31, 2026 decision, only publications on or before March 31 are eligible.

## File and run command

The standard-library-only program is [asof.py](asof.py). Its table and decision date are editable inputs at the top. Run `py asof.py` on this computer, or `python asof.py` where that command is available.

## Verified row funnel

| Rule | Count | Source rows removed from the panel |
|---|---:|---|
| Quarantine missing ticker | 1 | 11 |
| Remove exact duplicate | 1 | 7 |
| Remove publication after March 31 | 3 | 3, 8, 10 |
| Replace older vintage | 1 | 2 |

The as-of panel contains rows **1, 4, 5, 6, 9, 12**. Row numbers remain attached to the observations. The duplicate check excludes the source row number from the comparison, so row 7 duplicates row 6.

## Verified signals

Return = (latest monthly price / previous monthly price - 1) × 100%.

| Fund | As-of March 31 | Naive |
|---|---|---|
| AAA | +1.98% (February) | +5.83% (March) |
| BBB | -1.02% (February) | -5.15% (March) |
| CCC | +0.91% (February) | +1.82% (February, revised) |

The naive panel retains the latest publication for each ticker/month without enforcing the decision date. It still excludes missing tickers and exact duplicates. The return formula is unchanged; the available records change.

AAA uses 103/101 - 1 as of March 31, but the naive signal uses 109/103 - 1. These returns also describe different months. March's 109 was published April 10, so the naive March return could not have informed the March 31 decision. Keeping February's first publication, 104, instead of its eligible revision, 103, would incorrectly produce +2.97% for the as-of signal.

## Sanity check: worked calculations

Yield = (100 / price - 1) × 100%.

| Row | Fund | Month | Price | Yield | Flag under the training assumptions |
|---|---|---|---:|---:|---|
| 1 | AAA | January | 101 | -0.99% | Negative yield |
| 4 | AAA | February | 103 | -2.91% | Negative yield |
| 5 | BBB | January | 98 | +2.04% | None |
| 6 | BBB | February | 97 | +3.09% | None |
| 9 | CCC | January | 110 | -9.09% | Negative yield; priced above AAA and BBB |
| 12 | CCC | February | 111 | -9.91% | Negative yield; priced above AAA and BBB |

For this fictional same-maturity training exercise, the expected price order is AAA > BBB > CCC. Both months violate it because CCC has the highest price. The provenance rules cannot detect this: they check identity, duplication, availability and vintage, not economic plausibility.

A fifth rule could quarantine any price above 100 for review under the exercise's nonnegative-yield assumption. That flags rows 1, 4, 9 and 12. An additional same-month credit-order check would flag CCC's position above AAA and BBB. Flagged data should be investigated rather than silently corrected.

## Later-date check

An AI-run check temporarily set the imported module's decision date to April 15, 2026. No saved input was changed. All three as-of signals then matched the naive signals: AAA +5.83%, BBB -5.15%, CCC +1.82%. The publication-date rule removed zero rows; the vintage rule removed rows 2 and 12. The saved decision date remains March 31.

## Code explanation

Rule 4 is implemented in `latest_publications`. Each `(ticker, month)` tuple is a dictionary key. If the key is new, the function stores the row. If the key already exists and the current row has a later publication date, it replaces the stored row. ISO dates in YYYY-MM-DD format sort chronologically as strings. For the as-of panel, rule 3 has already excluded future publications before rule 4 runs.

The function `signals(naive_panel, "Naive signals (publication date ignored)")` receives the naive rows as its first argument and an output heading as its second argument. The heading does not control the calculation. `signals` groups by ticker, sorts months, and calculates the latest month-over-month return.

## Look-ahead bias and reflection notes

Look-ahead bias occurs when a historical decision or backtest uses information unavailable at the time. Event time (the month measured) is distinct from publication time; a later revision introduces another publication time for the same event period.

Rule 3 matters most for excluding entire future publications, including AAA's March price. Rule 4 also matters: it chooses February's eligible revision. Which rule matters most depends on the error being considered.

A backtest using the naive column would treat later information as if it had been available on March 31. For AAA it could claim a +5.83% March signal available at that date. That signal uses an April publication. BBB also illustrates that look-ahead contamination need not make an individual return more positive; its naive value is more negative.

## Completion record

- Program run: all March 31 funnel rows and signals match the supplied answer.
- Later-date comparison: verified by AI execution, not a partner file swap.
- Code quiz: user correctly identified that the heading prints a label and that unpublished data cannot support the earlier decision; AI clarified that the first argument supplies data rows.
- Yield table and reflection notes: AI-worked explanations, not claimed as independent hand calculations or personal reflections.
- Partner activities: skipped at the user's request.
- GitHub checkout: links still need to be established before submission.

Thursday's own-series ALFRED exercise is a future task; no real series has been selected or downloaded here.
