# Lab 13 — Meridian Foundation Reserve

**Case:** Meridian Foundation Reserve (fictional)  
**Reserve:** $100 million  
**Submission files:** `Lab 13.md` and `mandate.py`  
**Status:** In progress; student responses and verification pending.

## D — Define the decision

Which candidate portfolios does Meridian's mandate permit, and what must the CIO answer before anyone optimizes?

## R — Review the mandate and inputs

### Statement classification — complete independently before building

Choose objective, hard constraint, preference, unverifiable promise, or missing. Supply a one-line reason for each classification.

| Statement | CIO statement | Type — student response | Reason — student response |
|---|---|---|---|
| S1 | Horizon seven years; annual rebalancing. | Preference | Performance check: the horizon and annual review help keep the investment position aligned with its goals. |
| S2 | CPI + 4% annually, net of costs, over rolling five-year periods. | Unverifiable promise | Inflation protection: the intended return protects purchasing power and adds growth after costs. |
| S3 | Pays $0.75 million quarterly; twelve months of payouts held in cash or daily-liquid government securities. | Hard constraint | Payout protection: eligible reserves must cover a full year of the foundation's distributions. |
| S4 | Benchmark: 60% global equities, 40% U.S. investment-grade bonds. | Missing | Benchmark: this provides a simple reference portfolio for comparing investment performance. |
| S5 | Long-only; no borrowing, short sales, or derivatives. | Objective | Investment prohibitions: these restrictions limit the investment methods available to the portfolio. |
| S6 | No single issuer above 8%. | Hard constraint | Diversification: the issuer limit prevents excessive concentration in one company. |
| S7 | Annual turnover at most 25% without committee approval. | Objective | Trading limits: the turnover ceiling supports a disciplined strategy and requires approval for higher turnover. |
| S8 | At least 90% redeemable within five business days. | Objective | Liquidity requirements: most assets must be accessible within the stated redemption window. |
| S9 | The reserve cannot have a calendar-year loss greater than 10%; no measure or breach rule supplied. | Unverifiable promise | Loss protection: the absolute promise cannot be verified as written without a defined measure and breach rule. |
| S10 | No sector, ESG, tax, or home-bias preference; the pilot's optimization criterion is unspecified. | Missing | Pilot optimization: the CIO has not specified what the pilot should optimize. |

**Classification review pending:** Types above preserve the student's selections, including the accepted revision to S9. S1, S2, S4, S5, S7, and S8 need reconsideration: a target differs from a guarantee; a supplied benchmark is not absent information; and mandatory timing, prohibitions, and numerical limits differ from preferences or objectives. These selections have not been silently corrected.

### Permitted holdings

| Holding | Issuer | Business days to redeem | Reserve-eligible |
|---|---|---:|---|
| Cash | none | 0 | yes |
| Treasury bills | U.S. Treasury | 1 | yes |
| Treasury 10-year note | U.S. Treasury | 1 | yes |
| Global equity index fund | diversified fund | 2 | no |
| Investment-grade bond fund | diversified fund | 3 | no |
| Private real estate fund | diversified fund | 90 | no |
| Acme Corp bonds | Acme Corp | 4 | no |
| Acme Corp stock | Acme Corp | 1 | no |

Cash, U.S. Treasury securities, and diversified funds are exempt from the issuer limit. Securities of the same company must be combined.

| Holding | A (%) | B (%) | C (%) |
|---|---:|---:|---:|
| Cash | 2 | 1 | 1 |
| Treasury bills | 2 | 0 | 1 |
| Treasury 10-year note | 10 | 0 | 0 |
| Global equity index fund | 60 | 55 | 70 |
| Investment-grade bond fund | 26 | 20 | 20 |
| Private real estate fund | 0 | 15 | 0 |
| Acme Corp bonds | 0 | 5 | 0 |
| Acme Corp stock | 0 | 4 | 8 |

## I — Implement the checker

Implemented in `mandate.py`, using only Python's standard library. All holdings, candidate weights, exemptions, and policy parameters are editable at the top.

Run from this folder:

```powershell
python mandate.py
```

The program computes the reserve minimum, aggregates Acme stock and bonds under one issuer, and prints five measured checks per candidate. It never tests S9. These checks do not establish full mandate compliance: the static holdings alone do not verify rebalancing, turnover, or achievement of the return objective.

### Code comprehension quiz

- Line selected by student: pending.
- AI quiz question: pending.
- Student answer before explanation: pending.
- Explanation after answer: pending.

## V — Verify the results

Executed `python mandate.py` successfully. The computed reserve minimum is **3.0%**: 4 quarters × $0.75 million ÷ $100 million × 100. Every A–C value matches the assignment's known answer.

| Rule | A | B | C | D |
|---|---|---|---|---|
| Weights sum to 100 | 100.0 pass | 100.0 pass | 100.0 pass | 100.0 pass |
| Lowest weight | 0.0 pass | 0.0 pass | 0.0 pass | 0.0 pass |
| Reserve ≥ 3.0% | 14.0 pass | 1.0 FAIL | 2.0 FAIL | 100.0 pass |
| Redeemable in 5 days ≥ 90% | 100.0 pass | 85.0 FAIL | 100.0 pass | 100.0 pass |
| Largest company ≤ 8% | 0.0 pass | 9.0 FAIL | 8.0 pass | 0.0 pass |
| Calendar-year loss | requires CIO clarification | requires CIO clarification | requires CIO clarification | requires CIO clarification |
| Verdict | passes every checkable rule | fails 3 rule(s) | fails 1 rule(s) | passes every checkable rule |

Acme's two positions in B combine to 9.0%. A passes the implemented checks; that verdict does not establish compliance with every CIO statement.

Negative-weight probe executed on an in-memory copy of A with cash at −2% and the global equity fund at 64%. The checker returned total weight 100.0 pass; lowest weight −2.0 FAIL; eligible reserve 10.0 pass; five-day liquidity 100.0 pass; largest company 0.0 pass. Verdict: **fails 1 rule(s)**. Assertions confirmed that only long-only failed and the reserve measured 10.0%. The saved A inputs remain at cash 2% and global equities 60%.

## E — Examine a counterexample

**AI-proposed candidate D:** 100% cash; 0% in every other holding. This is a counterexample, not an optimized portfolio.

**AI's proposed objection — S2:** The CIO could reasonably reject an all-cash allocation because passing the reserve, liquidity, issuer, and long-only checks does not demonstrate that it can achieve CPI + 4% net of costs over rolling five-year periods. No cash-return assumptions have been supplied, so this is a suitability concern rather than a proven return shortfall. S10 also leaves the pilot's optimization criterion unresolved.

Candidate D was run successfully with the other portfolios; it **passes every checkable rule**, as shown in the verification table. This does not resolve the S2 objection.

### Independent judgment — AI closed

Student's two-sentence judgment on whether the objection holds and which statement decides it: pending.

### Partner exchange

Partner's candidate D: awaiting partner input.

Statement cited against the partner's portfolio and explanation: pending exchange.

### One question for the CIO — AI closed

Student's question that blocks optimization: pending.

Answer that would change the portfolio and its consequence: pending.

## R — Reflect and carry the mandate forward

### Investment policy statement — independent learning

1. What is an investment policy statement? Student response pending.
2. How do its objectives and constraints work? Student response pending.
3. Map S1–S10 onto it: student response pending; refer to the classification table above.

### Reflection following partner discussion

1. Why can a portfolio pass every checkable rule and still be wrong for this client? Student response pending.
2. Which S1–S10 classification was least certain, and why? Student response pending.

### Project 2 — own client's mandate

Client identity and relationship to the ADP project: awaiting student input. ADP is the company studied; it does not establish the reserve client's objectives or constraints.

- Objective: pending client details.
- Hard constraints: pending client details.
- One question for the client: pending client details.

### GitHub checkout

- Markdown file link: pending publication.
- Python file link: pending implementation and publication.

Submit both file links in the Lab 13 quiz after completing the student responses and verification.
