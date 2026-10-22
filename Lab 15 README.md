# Lab 15 — README

## Deliverables

| File | Purpose |
|---|---|
| [Lab 15.md](Lab%2015.md) | Lab write-up: mandate, sources, Meridian checks, personal results, partner discussion, EEM verification, reflection and allocation decision. |
| [portfolio.py](portfolio.py) | Shared portfolio engine, constrained 5-point grid search and monthly-price estimator. Original Lab 14 printed results preserved. |
| [app.py](app.py) | Required Streamlit interface importing the shared engine. |
| [prices.csv](prices.csv) | Five years of monthly adjusted-close prices for VOO, QQQ, VB and EEM. |

The partner's concerns and the response belong in **Lab 15.md**, alongside the rest of the lab. No separate partner-response document is required. The preferred organization for future labs is a lab document, a README describing the work and how to run it, and the Python deliverable file or files required by the assignment.

## Run

From this folder, with Streamlit, pandas and numpy installed:

```powershell
py portfolio.py
py -m streamlit run app.py
```

Use `python` instead of `py` if that is the available command. The first command prints the unchanged Lab 14 baseline results. The second starts the web app; open the local URL printed in the terminal.

Meridian training is the default. Select **Project 2: VOO / QQQ / VB / emerging markets** to load the saved prices.csv automatically. An uploaded CSV replaces the saved data. The confirmed emerging-markets ticker is EEM.

## Mandate and results

The personal objective is expected annual return at least 7%, with VOO at least 40%, VB at most 30%, and EEM at most 30%. No reserve minimum was stated. The engine searches fully invested, long-only portfolios in 5 percentage point steps and enforces all three weight limits in both result columns.

| Window | VOO / QQQ / VB / EEM (%) | Estimated return | Estimated volatility |
|---|---|---:|---:|
| All 60 monthly returns | 70 / 0 / 0 / 30 | 12.78% | 14.99% |
| Last 36 monthly returns | 80 / 0 / 0 / 20 | 21.70% | 12.17% |

The largest window change is 10 percentage points. Reducing any single fund's return estimate by one percentage point leaves the weights unchanged in both windows. Historical arithmetic estimates are not forecasts. See the lab document for the complete reasoning, sources and partner response.

## Data and reproduction

prices.csv has 61 month-end prices from September 2021 through September 2026, downloaded October 22, 2026. Each price is the final trading day's Yahoo Finance adjusted close for its month. October 2026 is excluded as incomplete. The lab records a source link and download date for each ticker.

Supporting files are retained for reproduction:

- `VOO_yahoo_daily.json`, `QQQ_yahoo_daily.json`, `VB_yahoo_daily.json`, `EEM_yahoo_daily.json`: raw provider responses.
- `prepare_project2.py`: extracts monthly prices from the saved responses and runs the shared engine.
- `project2_results.json`: estimates, correlations, allocations, stresses and source hashes.
- `audit_eem.py` and `EEM_data_audit.json`: independent checks of EEM extraction and return calculations; the discussion of these checks is included in the lab.

To run the recorded checks:

```powershell
py verify_lab14.py
py verify_lab15.py
py audit_eem.py
```

Checks passed for Meridian's two known answers, its 25-point stress change, correlation propagation from the engine, personal allocation constraints, both personal windows, a personal return edit and all 61 EEM source-price matches.

`prepare_project2.py` currently selects the five-year window relative to the run date. Its saved raw responses cover the recorded download; reproducing a later window requires fresh source data. The saved CSV and JSON results preserve the analysis reported in the lab.

## Remaining student actions

The partner concern and student's decision to retain the allocation are recorded in the lab. Still pending: an actual numeric app change by the partner if required, the remaining no-screen/paper/code activities, the student's condition for reconsidering the allocation, and the GitHub destination and submission. No unreported activity has been marked complete.

For checkout, include the lab document, this README, portfolio.py, app.py and prices.csv. Keep the supporting data and scripts accessible if reproducibility is required. Streamlit logs and Python cache files are not submission deliverables.
