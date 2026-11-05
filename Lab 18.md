# Lab 18 — Legend Investor as Skill

Question: Can an investor's philosophy become a skill your AI runs the same way every time — every number computed by code from the 10-K, the judgment the model's?

The runnable Lab 18 app is `Lab18/lab18_app.py`. This lab has its own folder, memo files and outputs. Earlier portfolio apps were left intact.

Run from the FIN 439 folder:

```powershell
py -m streamlit run Lab18/lab18_app.py --server.port 8518
```

The app opens on COST's saved SEC snapshot. Enter JPM to see the missing-capex probe. Edit the displayed memo to add `40.0%`; the red flag identifies the unprinted number. Editing the app textbox is temporary; use Download memo to save it.

The skill is `.agents/skills/buffett-screen/SKILL.md`. Its bundled script is `.agents/skills/buffett-screen/scripts/edgar.py`. Skills are instructions that the AI reads when needed; the script does the arithmetic, while Codex writes and saves the memo. The app displays saved model-written memos; it does not pretend a deterministic template is a fresh AI judgment. For a new ticker, run the skill in chat to produce its memo after obtaining the facts.

## Reproduce the data

No FAskills plugin was installed and no paid source was used. The original, unmodified SEC downloads are `cost_companyfacts.json` and `jpm_companyfacts.json` in the project root. Per-company source JSON in `Lab18/output` records the URL, date and SHA-256 hash. Facts JSON records each tag, fiscal period, filing date and accession. These saved snapshots make the graded run reproducible if later filings revise a value.

```powershell
py .agents/skills/buffett-screen/scripts/edgar.py COST --facts cost_companyfacts.json --out Lab18/output
py .agents/skills/buffett-screen/scripts/edgar.py JPM --facts jpm_companyfacts.json --out Lab18/output
py verify_investor_labs.py
```

For a fresh download, supply your real name and email:

```powershell
py .agents/skills/buffett-screen/scripts/edgar.py COST --user-agent "YOUR NAME YOUR EMAIL" --out Lab18/output
```

The initial research snapshots were downloaded before the student's email was provided. The fresh-download feature requires an identifying name/email; this personalization remains pending. The SEC ticker-mapping endpoint returned an error page in this environment. COST/JPM/NVDA can resolve CIK from their SEC snapshots; for another ticker the app attempts the required mapping URL and offers an explicit CIK fallback rather than guessing.

## Results and evidence

All supplied COST amounts and fiscal ends match the script. ROE rounds to 28.3%, 25.1%, 31.2%, 27.8%, 25.8%; all three checks pass. Owner earnings rise from 3,501 to 9,382 USD millions; net income rises from 5,844 to 9,226 USD millions. See `output/COST_printed.txt` for the actual script output and `output/COST_facts.json` for source provenance.

JPM capital spending and owner earnings remain `not found` in every selected year. Both owner-earnings checks remain `not known`. Its memo explicitly says owner earnings cannot be judged. No proxy capex or estimate was inserted.

The automated verification compares COST to the full supplied table, tests JPM gaps, latest-filing selection, annual-period filtering, nonpositive equity, missing inputs, and a `40.0%` injection. Streamlit AppTest opens both apps and confirms the flag responds in each displayed memo. `verification.txt` records the test run.

The fresh-chat comparison was not performed; no browser AI answer or partner exchange is fabricated.

## Explain the code briefly

`year_row` builds one fiscal year's row. The loop asks `select_fact` for each permitted tag and date. `select_fact` filters to 10-K, requires a one-year duration for flows, and selects the latest filing within the preferred available tag. If no fact qualifies, it returns `None`. `money` displays that as `not found`.

ROE is net income divided by year-end equity only when equity is positive and both inputs exist. Owner earnings subtract capital spending from operating cash flow only when both are present. The check functions return `not known` if any required input is absent. No missing number is silently changed to zero.

`printed` creates the numeric record used by the model. `unprinted_numbers` compares numeric tokens in the memo to that record. It catches unprinted digits and precision differences, but it cannot prove that an allowed number was used in the correct context or catch a number spelled out as a word.

Suggested decision, also under the memo: trust the reproducible screen conditional on checking the filings and competitive durability before acting. This is a model suggestion for review, not an invented personal reflection.

## Checkout

Use the files in `Lab18_submission.zip`, which preserves the folder paths needed to run the app. Upload them to your GitHub repository and submit links to this Markdown, `Lab18/lab18_app.py`, the skill, the bundled script and memo/output evidence. No repository URL was provided, so GitHub publication and genuine checkout URLs remain pending.

Sources: [Buffett perspective](https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/warren_buffett.md), [SEC API documentation](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [SEC ticker mapping](https://www.sec.gov/files/company_tickers.json), [Streamlit app testing](https://docs.streamlit.io/develop/api-reference/app-testing), [Codex skills](https://developers.openai.com/codex/skills/).
