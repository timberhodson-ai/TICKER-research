# Lab 17: Rates and historical vintages

Worked October 29, 2026. This continues the Lab 16 chat and its point-in-time lesson. The earlier fictional AAA/BBB/CCC exercise remains in `Lab 16 Point-in-Time.md` and `asof.py`.

## The question

**Was each number in your series knowable on the day you would have traded on it — and may Project 2 use it?**

An observation date alone does not establish availability. Use the vintage available before the decision, with a trading-time rule that excludes releases after execution. Project 2 may use an eligible historical observation; it may not silently substitute today's revised history.

## Files and running the app

`asof_app.py` supplies the four default series, an additional ID box, charts and an as-known comparison table. Each series makes one current CSV request and one historical-vintage request on a cache miss; the functions cache results for one hour. Chart start dates affect charts only; the table counts compare full histories. Missing observations remain missing.

```powershell
py -m streamlit run asof_app.py
```

Dependencies: `streamlit`, `pandas`, `requests`. If needed: `py -m pip install streamlit pandas requests`.

`verify_asof_app.py` reproduces the live numerical checks and saves `Lab 17 live verification.json`. `check_asof_ui.py` exercises the actual Streamlit page and starts a local server on port 8503. The numerical reference values appear only in verification code, never as app data.

## Live known-answer evidence

Downloaded October 29, 2026 using the app's real download functions, with the vintage set to October 5, 2026:

| Series | Last observation known then | Value | Result |
|---|---|---:|---|
| BAA | September 2026 | 6.47 | Pass |
| FEDFUNDS | September 2026 | 3.75 | Pass |
| DGS10 | October 2, 2026 | 5.28 | Pass |
| MORTGAGE30US | October 1, 2026 | 7.28 | Pass |

Monthly observations are represented by the first of the month in the CSV; September 1 means the September observation, not publication on September 1.

PAYEMS, vintage January 15, 2025: the last observation was December 2024 at **159,536 thousand persons**. Today's value for that same month is **158,316**, lower by 1,220 thousand. The full-history comparison found **381 revised common observations** and 21 later observations. This demonstrates that the vintage request is not simply another copy of today's history. Counts depend on the download date and comparison coverage.

## Data card: DGS10

| Field | Record |
|---|---|
| Source and link | Board of Governors of the Federal Reserve System, H.15; distributed by [FRED](https://fred.stlouisfed.org/series/DGS10) and [ALFRED](https://alfred.stlouisfed.org/series?seid=DGS10) |
| Measure | Market yield on U.S. Treasury securities at a constant 10-year maturity, quoted on an investment basis; a yield-curve measure, not an ETF return |
| Units and frequency | Percent per annum; daily; not seasonally adjusted. A value of 4.99 means 4.99%, not 499%. |
| Publication lag | The September 30 vintage ends September 29: a one-calendar-day lag at that cutoff. The Federal Reserve's H.15 page schedules weekday publication at 4:15 p.m., excluding holidays/closures. FRED distribution timing also matters. |
| Revisions | Zero differences on common nonmissing dates between the September 30 vintage and today's history. This tested interval does not establish that corrections can never occur. |
| Download date | October 29, 2026 |
| Missing data | Non-observation days remain missing; the app does not forward-fill rates. |
| Historical availability rule | Use the ALFRED vintage for the calendar day before each decision and its latest nonmissing observation. Never use a current-day vintage for an earlier intraday trade. |

Source details: [FRED DGS10](https://fred.stlouisfed.org/series/DGS10) and [Federal Reserve H.15](https://www.federalreserve.gov/releases/h15/). The lag and revision counts above come from the saved app downloads, not an assumed constant lag.

### Three values checked against the FRED page

| Observation | App CSV | FRED page | Match |
|---|---:|---:|---|
| October 26, 2026 | 5.00 | 5.00 | Yes |
| October 27, 2026 | 4.99 | 4.99 | Yes |
| October 28, 2026 | 5.05 | 5.05 | Yes |

These are **AI source checks**, not claimed as the student's independent hand checks. The student still needs to read these three entries on the linked FRED page personally.

### Last month versus today

At September 30, 2026, the last available DGS10 observation was September 29 at **5.26%**. The refreshed October 29 FRED download ends October 28 at **5.05%**, with **20 later nonmissing observations** and **zero revised common observations**. Moving back to September 30 removes those later observations because they were unavailable then.

Today's ALFRED vintage and the refreshed FRED CSV both end October 28 at **5.05%**. An earlier download on October 29 had FRED ending October 27 while ALFRED already included October 28; the fresh download resolved that endpoint timing difference. The saved current snapshot and JSON now reflect the refreshed download. Refresh before interpreting the newest observation; compare revisions only on shared dates. The app warns when the selected historical vintage extends beyond the current download.

## AI peer summary and fresh eyes

This is an AI peer substitute requested because no partner was available. It is a summary, not an invented conversation or a claim that a timed, no-screen exchange occurred.

The Project 2 universe is VOO, QQQ, VB and EEM. DGS10 is an economically motivated candidate because long-term rates affect discount rates and borrowing costs, which can affect equity valuations. That explanation motivates investigation; the lab does not establish predictive power or authorize a new allocation rule.

The connection to the earlier Lab 16 work is direct: AAA's March observation was published in April and could not enter a March 31 decision. Likewise, a rate dated on the decision day cannot automatically enter that day's trade. Observation period, availability and vintage are separate fields.

**AI peer attack: publication timing is the least trustworthy field.** A daily label is easy to mistake for immediate availability, and the current FRED/ALFRED endpoint difference makes that concern concrete.

**Two-sentence response:** The September 30 ALFRED vintage ends September 29 at 5.26%, and H.15 schedules weekday publication at 4:15 p.m., so an observation date is not proof of availability before a trade. I will use the prior calendar day's vintage for decisions and quarantine a record if its availability is unclear, including any unresolved discrepancy between the endpoints.

### Student's code summary

Student-provided response, with spelling and grammar cleaned up: "It gathers FRED data for the dataset, converts the data into a usable format by reading the files, makes charts from this data for the relevant information, compares current to past versions to check dates, and uses that cross-checking of dates to handle errors."

Technical clarification: the historical versions come from ALFRED. Comparing versions checks availability and revisions; failed downloads, invalid IDs, and parsing errors are handled separately through exceptions. The student's summary is recorded, but it does not by itself establish completion of the independent line-by-line explanation.

### Explaining the historical download function

In `download_as_known`:

1. `@st.cache_data(...)` caches by the function's arguments, including the series and vintage date, for one hour.
2. `requests.get(...)` requests the public **ALFRED** CSV endpoint, not the current FRED endpoint.
3. `params` supplies the series ID and the date converted to `YYYY-MM-DD` by `isoformat()`.
4. `timeout=45` limits waiting for an unresponsive request.
5. `raise_for_status()` makes an HTTP failure an exception; the page catches it per series so other charts still work.
6. `parse_csv(response.text)` reads the response, converts periods to missing values, parses dates/numbers, and normalizes the vintage-dependent value-column name.
7. The final filter excludes observation dates beyond the requested vintage date. The ALFRED request is what prevents revision leakage; this filter alone would not reconstruct historical knowledge from today's values.

**AI peer question:** Why not download today's CSV and discard rows dated after the decision? **Answer from the code:** The `vintage_date` parameter requests the earlier versions of observations; a date filter on current data would retain later revisions of older observations, as PAYEMS demonstrates.

The student still needs to explain this function independently. This written explanation does not stand in for the requested six-minute no-AI exercise.

## The call

**Admit DGS10 conditionally as a candidate input for Project 2, using only the latest nonmissing observation in the prior calendar day's ALFRED vintage.** The required numerical checks pass, and the September 30 comparison shows a short observed lag and no revisions on common dates. This admits the data under an availability rule; it does not establish that a rate signal improves the portfolio.

**Change the call to quarantine** if historical vintages cannot be retrieved, availability at the decision is uncertain, unexplained revisions or endpoint discrepancies affect a selected record, or the rule cannot be reproduced. Freeze the actual trading rule before evaluating its holdout.

## Learning and reflection

A data card records source, meaning, units, availability, revisions and retrieval date. The availability rule prevents future publications entering a historical decision; the vintage rule prevents later revisions entering earlier observations. Units prevent a different error: treating a percentage yield as a decimal return or an asset's realized return.

“Cleaned the data” does not identify the source, tell a reader what a value means, or explain whether the value existed before the trade. The data card makes those assumptions inspectable.

The September 30 cutoff shows a short observed publication lag: September 29 was available, while later dates were not. A backtest on today's series could overstate how current the strategy's information was; PAYEMS shows how it could also import revised information. Such leakage can bias measured performance, but this lab does not calculate the size or prove that every contaminated result rises.

## Submission status

Local deliverables: this Markdown file, `asof_app.py`, `verify_asof_app.py`, `Lab 17 live verification.json`, and the two DGS10 CSV snapshots. `check_asof_ui.py` and `Lab 17 UI verification.txt` document completed automated page checks: the four defaults, the October 5 values, typed PAYEMS at January 15, and unknown-ID isolation all passed. The local server was started at http://localhost:8503. Browser automation was unavailable, so a browser rendering inspection is not claimed.

Remaining student actions: personally read the three FRED values; independently explain the code; open Brightspace → Quizzes → Lab 17; upload the Markdown and Python files (plus evidence as useful) to GitHub and submit their links. No quiz attempt, human partner activity, independent hand check, or GitHub publication is claimed here.
