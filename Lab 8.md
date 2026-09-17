> **Class assignment disclaimer:** This report was prepared for educational purposes as part of a class assignment for FIN 439. It is not financial or investment advice, or a recommendation to buy, sell, or hold any security. Valuations and conclusions depend on the stated assumptions and estimates.

# Lab 08: Automatic Data Processing, Inc. (ADP) — Peer P/E Valuation and DCF Comparison

**Target Company:** Automatic Data Processing, Inc. (Nasdaq: ADP)  
**Valuation / Reference Date:** September 9, 2026 (matching Week 3 DCF reference date)  
**Target Reference Stock Price:** $265.22 (September 9, 2026 4:00 PM EDT close)  
**Target Reported Diluted EPS:** $10.94 (FY2026 GAAP diluted EPS, fiscal year ended June 30, 2026)  
**Accompanying Calculator Script:** [`peer_pe.py`](peer_pe.py)

---

## 1. Define / Discover — Understand Your Company First

### Business Economics and Revenue Drivers
From Week 3 research and ADP's fiscal 2026 Form 10-K ([10-K](https://www.sec.gov/Archives/edgar/data/8670/000000867026000030/adp-20260630.htm), pp. 45–54), ADP generates revenue primarily through three interconnected economic engines:
1. **Recurring Software & Processing Fees (Employer Services):** ADP provides cloud-based human capital management (HCM) software, payroll processing, payroll-tax filing, and HR administration across small businesses (*RUN Powered by ADP*), mid-to-large businesses (*ADP Workforce Now*), and global enterprises (*ADP Lyric HCM*). Revenue is largely subscription-based, recurring, and contracted on a per-employee-per-month (PEPM) or transaction basis. In FY2026, Employer Services client revenue retention was 92.1%.
2. **HR Outsourcing & Co-Employment (PEO Services / ADP TotalSource):** ADP co-employs over 770,000 worksite employees, providing end-to-end HR, benefits, workers' compensation, and payroll-tax administration. TotalSource earns administration fees and markups on pooled benefits and payroll.
3. **Client Funds Float Interest:** ADP collects payroll and tax funds from clients prior to disbursement, holding significant average balances ($3.5+ trillion moved in FY2026). ADP invests these funds in high-quality fixed income securities, generating substantial net investment income (client funds interest).

### Annual Reported Earnings Status
ADP's reported annual earnings are **strongly positive**. For the fiscal year ended June 30, 2026, ADP reported:
- **GAAP diluted earnings per share:** **$10.94** (up from $9.68 in FY2025).
- **Diluted weighted-average shares:** **403.3 million**.
- **Net earnings:** **$4,411.9 million**.
- *Sources:* Form 10-K, Statements of Consolidated Earnings, p. 45; Note 1.N, p. 54; [FY2026 Q4 Earnings Release Exhibit 99](https://www.sec.gov/Archives/edgar/data/8670/000000867026000025/q4fy26exhibit99.htm), p. 1.

Because earnings are positive, standard price-to-earnings (P/E) valuation is mathematically defined and economically meaningful. At the September 9, 2026 closing price of **$265.22**, ADP trades at a trailing reported P/E of:
$$\text{ADP P/E} = \frac{\$265.22}{\$10.94} = 24.243144\text{x}$$

### What Still Needs to Be Researched
To evaluate whether ADP's 24.24x multiple is defensible, we must research:
1. Which publicly traded operating peers share ADP's core business model of recurring payroll/HCM subscription revenue, high client retention, and float-interest economics.
2. What public annual reported GAAP diluted EPS peers reported for fiscal years ending prior to our September 9, 2026 valuation cutoff date.
3. What stock prices those peers traded at on the exact same date (September 9, 2026).
4. Material differences in business mix (e.g., SMB focus vs. enterprise, pure software SaaS vs. co-employment PEO, data-center ownership vs. asset-light cloud hosting) that require qualification.

### Focused Search Question
> *"For publicly traded U.S. operating companies providing cloud-based payroll, human capital management (HCM) software, and HR outsourcing that earn recurring contract revenue and manage client funds float, what were their latest annual reported GAAP diluted EPS public by September 9, 2026, and their closing share prices on September 9, 2026, and how do their scale, business mix, and capital expenditures compare to ADP?"*

---

## 2. Represent — Write Your Policy, Then Find Candidates

### Peer Selection Policy (Written Prior to Candidate Selection)
This policy defines the economic criteria an operating company must satisfy to be admitted into the valuation comparison.

#### Must-Match Economics
1. **Core Business Model:** Must generate the majority of operating revenue from recurring business-to-business subscriptions or multi-year service contracts for payroll processing, human capital management (HCM) software, employee benefits administration, or HR outsourcing.
2. **Positive Annual Reported GAAP Earnings:** Must have positive reported annual GAAP diluted EPS for the most recent fiscal period publicly filed on or before September 9, 2026. Zero or negative earnings make trailing P/E meaningless or undefined.
3. **Public Operating Company:** Must be a publicly traded operating corporation listed on a major U.S. exchange (NYSE or Nasdaq), reporting in U.S. dollars with share counts compatible with per-share earnings.
4. **Capital-Light Service Structure:** Operating cash flows must substantially exceed routine capital expenditures (capex/revenue typically under 15%), demonstrating a software/services model rather than asset-heavy infrastructure.

#### Differences to Qualify
- **Customer Size Segment:** Companies serving predominantly small-to-midsize businesses (SMBs) vs. enterprise or global employers are qualified because SMBs exhibit higher business churn during economic downturns, whereas enterprise contracts provide longer visibility.
- **Client Funds Float Scale:** Companies with lower float balances relative to revenue are qualified, as changes in interest rates will impact their earnings less than ADP's.
- **Business Mix / Service Delivery:** Pure cloud SaaS platforms without a co-employment PEO division (or with higher internal hosting/data-center capex) are qualified because their gross margins and capital intensity differ from ADP's hybrid software/PEO model.

#### Exclude Criteria
- **Unprofitable Companies:** Firms with net losses (negative EPS) for the latest completed fiscal year.
- **Diversified Enterprise Tech Conglomerates:** Large software giants (e.g., Microsoft, Oracle, SAP, Salesforce) where payroll/HCM is a minor product line surrounded by cloud infrastructure, hardware, or enterprise database ecosystems.
- **Temporary Staffing / Placement Agencies:** Staffing firms (e.g., Robert Half, ManpowerGroup) whose revenue depends on cyclical hiring commissions and gross temporary billing rather than recurring software subscriptions or client float.
- **Payment Networks / Transaction Processors:** Consumer payment networks (e.g., Visa, Mastercard) whose economics reflect consumer retail spending and transaction volume rather than workforce administration.
- **Unresolved Data / Incompatible Reporting:** Companies lacking a public annual 10-K filed prior to September 9, 2026, or reporting in foreign currencies without audited USD reconciliations.

#### What Evidence Would Make You Reject a Candidate While Searching?
- Reporting negative GAAP diluted EPS for the latest completed fiscal year.
- A fiscal year-end 10-K that was not filed and public on EDGAR before the September 9, 2026 cutoff date.
- Reliance on one-time restructuring or non-operating asset sales to produce positive net income.
- Business model dependence on transactional staffing fees rather than recurring payroll/HCM contracts.

---

### AI Collaboration: Querying Independent AI Partners
The exact peer policy and valuation cutoff were submitted independently to two AI partners:
1. **Partner 1:** OpenAI Codex CLI (`gpt-6-astra` session).
2. **Partner 2:** Research Subagent (autonomous SEC EDGAR and IR research).

```text
Target: Automatic Data Processing, Inc. (ADP).
Week 3 valuation date: September 9, 2026.
Peer policy: Listed operating companies in the US reporting in USD with positive annual GAAP diluted EPS public by September 9, 2026, sharing ADP's core business economics of recurring revenue from payroll processing, human capital management (HCM) software, or HR outsourcing/PEO services, and capital-light service operations. Qualify differences in market segment focus, lower float exposure, or differing margin profiles. Exclude non-profitable firms, staffing agencies, transaction/card payment processors, and diversified enterprise tech conglomerates (e.g. Microsoft, Oracle).

My target, comparison date and peer policy are below. Suggest at most two listed operating-company candidates. For each, give a primary-source link and section supporting its business model, one important difference from my target, and its latest annual reported diluted EPS public by my comparison date, with the fiscal period and publication date. Do not rank candidates or change my policy. Mark anything you cannot verify unresolved. I will open the sources and decide whether to use it.
```

#### Candidates Returned by AI Partners
Both partners independently returned the same two primary operating candidates:
1. **Paychex, Inc. (Nasdaq: PAYX)**
2. **Paycom Software, Inc. (NYSE: PAYC)**

---

### Candidate Source Decisions Table

| Candidate | Decision | Business Rationale & Policy Fit | Primary Source Link & Section Locator | Latest Public Annual GAAP Diluted EPS | Fiscal Period Ended | Publication / Filing Date | Same-Date Closing Price (Sep 9, 2026) |
|---|---|---|---|---:|---|---|---:|
| **Automatic Data Processing, Inc. (ADP)** | **TARGET** | Target company. Core provider of cloud HCM, payroll, PEO, and client float investment. | [Form 10-K](https://www.sec.gov/Archives/edgar/data/8670/000000867026000030/adp-20260630.htm), Item 1 pp. 4–12; Statements of Consolidated Earnings, p. 45 | **$10.94** | June 30, 2026 | July 29, 2026 (release) / Aug 5, 2026 (10-K) | **$265.22** |
| **Paychex, Inc. (PAYX)** | **USE** | Closest direct competitor. Provides payroll, HCM SaaS (*Paychex Flex*), HR outsourcing/PEO, and invests client funds float. Highly capital-light ($234.9M capex on $6,512.0M revenue, ~3.6%). Differs primarily in its historical focus on small-to-midsize employers and smaller international scale. | [Form 10-K](https://investor.paychex.com/sec-filings/section-16-filings/content/0001193125-26-307785/0001193125-26-307785.pdf), Item 1 "Business"—"Management Solutions" and "PEO and Insurance Solutions" pp. 4–5; Item 8 Income Statement; [Earnings Release](https://investor.paychex.com/sec-filings/all-sec-filings/content/0001193125-26-280314/payx-ex99_1.htm), Results Table | **$4.89** | May 31, 2026 | June 24, 2026 (release) / July 17, 2026 (10-K) | **$114.75** |
| **Paycom Software, Inc. (PAYC)** | **QUALIFY** | Cloud HCM and payroll SaaS provider with 94.5% recurring revenue. Qualify: (1) integrated single-database SaaS delivery without a co-employment PEO division; (2) smaller client float interest; (3) higher capital intensity (capex $270.9M on $2,050M revenue, ~13.2%) because it owns proprietary data-center hosting facilities; (4) fiscal year ends Dec 31, so public annual EPS is FY2025 (filed Feb 2026). | [Form 10-K](https://www.sec.gov/Archives/edgar/data/1590955/000119312526059372/payc-20251231.htm), Item 1 "Business"—"Overview" and "SaaS Delivery Model"; Item 8 Statements of Income; [FY25 Earnings Release](https://investors.paycom.com/news/news-details/2026/Paycom-Software-Inc--Reports-Fourth-Quarter-and-Year-End-2025-Results/default.aspx) | **$8.08** | December 31, 2025 | Feb 11, 2026 (release) / Feb 19, 2026 (10-K) | **$215.58** |
| **Paylocity Holding Corp. (PCTY)** | **EXCLUDE / DEFERRED** | Cloud payroll/HCM SaaS. Excluded from primary calculator to keep the focus on the two most verified candidates; filing date verification for full FY2026 10-K was unresolved relative to the 2-peer lab ceiling. | [SEC EDGAR CIK 0001591698](https://www.sec.gov/edgar/browse/?CIK=1591698) | Unresolved | June 30, 2026 | August 2026 | N/A |
| **Insperity, Inc. (NSP)** | **EXCLUDE** | Dedicated PEO company. Excluded because it operates almost entirely as a co-employer with pass-through insurance risk, lacking proprietary enterprise HCM cloud software and scale. | [Form 10-K CIK 0001000753](https://www.sec.gov/edgar/browse/?CIK=1000753) | N/A | Dec 31, 2025 | Feb 2026 | N/A |
| **Robert Half Inc. (RHI)** | **EXCLUDE** | Specialized talent and staffing services. Excluded per policy: transactional staffing commissions and cyclical hiring revenue; no software subscriptions or client float. | [Form 10-K](https://www.sec.gov/edgar) | N/A | Dec 31, 2025 | Feb 2026 | N/A |

---

## 3. Implement — Apply the Calculator to ADP

### Inputs Recorded in `peer_pe.py`
The Lab 08 calculator ([`peer_pe.py`](peer_pe.py)) was updated with ADP and the two admitted peers (PAYX marked *use*, PAYC marked *qualify*):
```python
# ==================== EDITABLE INPUTS ====================
TARGET = {"ticker": "ADP", "price": "265.22", "eps": "10.94"}
PEERS = [
    {"ticker": "PAYX", "price": "114.75", "eps": "4.89"},
    {"ticker": "PAYC", "price": "215.58", "eps": "8.08"},
]
# ========================================================
```

### Terminal Run Command and Complete Local Output
Executed in PowerShell:
```powershell
python "c:\Users\timbe\OneDrive\Desktop\FIN 439\peer_pe.py"
```

**Actual Output:**
```text
P/E comparison | September 9, 2026 prices | Public annual GAAP diluted EPS
User-supplied inputs; no cash/debt adjustment. Currency: USD.

Target: ADP
Target observed price: $265.22
Target P/E: 24.243144x

Peer P/E calculations:
PAYX: 23.466258x
PAYC: 26.680693x

Valid peers: 2
Peer median P/E: 25.073475x
Minimum: 23.466258x | implied price: $256.72
Median: 25.073475x | implied price: $274.30
Maximum: 26.680693x | implied price: $291.89

Peer removal sensitivity (change from full-peer median estimate):
Remove PAYX: $291.89 | change: +17.58 USD | one-peer reference; no range
Remove PAYC: $256.72 | change: -17.58 USD | one-peer reference; no range
```

### Summary of Valuation Output
- **Target Observed P/E:** **24.243144x** (based on $265.22 price and $10.94 EPS).
- **Admitted Peer Multiples:**
  - Paychex (PAYX): **23.466258x**
  - Paycom (PAYC): **26.680693x**
- **Peer Implied Range for ADP:** **$256.72 to $291.89 per share**.
- **Peer Median Implied Price:** **$274.30 per share** (at median multiple of **25.073475x**).

---

## 4. Validate — Check Sources and Peer Decisions

### Hand Check of Peer Multiples and Implied Prices
To verify that the calculator's arithmetic is exact and free of rounding contamination:

1. **Paychex P/E Multiple:**
   $$\text{PAYX P/E} = \frac{\$114.75}{\$4.89} = \frac{11,475}{489} = \frac{3,825}{163} \approx 23.46625767\text{x} \quad (\text{matches } 23.466258\text{x})$$

2. **Paycom P/E Multiple:**
   $$\text{PAYC P/E} = \frac{\$215.58}{\$8.08} = \frac{21,558}{808} = \frac{10,779}{404} \approx 26.68069307\text{x} \quad (\text{matches } 26.680693\text{x})$$

3. **Peer Median Multiple:**
   With two peers, the median is the exact midpoint:
   $$\text{Median P/E} = \frac{\frac{3,825}{163} + \frac{10,779}{404}}{2} = \frac{1,545,300 + 1,756,977}{131,704} = \frac{3,302,277}{131,704} \approx 25.07347537\text{x} \quad (\text{matches } 25.073475\text{x})$$

4. **Implied Valuation for ADP ($10.94 EPS):**
   - **Minimum Implied Price (PAYX multiple):**
     $$\text{Implied Price}_{\text{min}} = \frac{3,825}{163} \times \frac{547}{50} = \frac{83,691}{326} \approx \$256.720859 \rightarrow \mathbf{\$256.72}$$
   - **Maximum Implied Price (PAYC multiple):**
     $$\text{Implied Price}_{\text{max}} = \frac{10,779}{404} \times \frac{547}{50} = \frac{5,896,113}{20,200} \approx \$291.886782 \rightarrow \mathbf{\$291.89}$$
   - **Median Implied Price:**
     $$\text{Implied Price}_{\text{median}} = \frac{3,302,277}{131,704} \times \frac{547}{50} = \frac{1,806,345,519}{6,585,200} \approx \$274.303821 \rightarrow \mathbf{\$274.30}$$

### Leave-One-Out Sensitivity Analysis and Prediction

#### Prediction Formulated Prior to Execution
- **Removing Paycom (PAYC, 26.68x P/E):** Paycom has the higher P/E multiple. Removing it removes the upper bound pulling up the average, leaving only Paychex's 23.47x multiple. Therefore, the estimate will **decrease** to **$256.72**, representing an exact drop of $\approx -\$17.58$.
- **Removing Paychex (PAYX, 23.47x P/E):** Paychex has the lower multiple. Removing it leaves only Paycom's 26.68x multiple, causing the estimate to **increase** to **$291.89**, representing an exact increase of $\approx +\$17.58$.

#### Actual Calculator Output and Interpretation
- **Remove PAYX:** Reference estimate **$291.89** | Change: **+$17.58 USD** (one-peer reference; no range).
- **Remove PAYC:** Reference estimate **$256.72** | Change: **-$17.58 USD** (one-peer reference; no range).

#### Why One Peer Produces a Reference Estimate, Not a Range
When only one usable peer remains, there is only a single valuation multiple available. A valuation range requires at least two distinct peer multiples to establish high and low boundaries. Applying a single peer multiple produces a **point reference estimate** that is entirely dependent on that single company's market pricing and accounting quirks, with no spread indicating industry dispersion.

---

## 5. Evolve — Compare with DCF and Question AI

### Side-by-Side Comparison of Valuation Methods

| Method | ADP Result and Date | Main Assumption or Limitation |
|---|---|---|
| **Week 3 DCF Model** | Base case: **$228.10 per share**<br>Sensitivity range: **$174.99–$335.20**<br>As of: **September 9/10, 2026** | **Starting adjusted FCFF ($4,570.54M)** relies on an expense proxy ($141.0M non-client interest) due to lack of a cash interest breakdown in filing.<br>**Terminal Value concentration:** 76.7% of enterprise value comes from terminal value (WACC 8.4%, terminal growth 2.5%, explicit 5-year growth tapering 7.0% to 5.0%).<br>**Reverse DCF:** Solved growth shift is **+3.56 percentage points** annually to justify the $265.22 market price. |
| **Peer P/E Multiples** | Implied range: **$256.72–$291.89**<br>Median estimate: **$274.30 per share**<br>Target observed P/E: **24.24x**<br>As of: **September 9, 2026** | **Peer selection:** 2 peers (PAYX at 23.47x, PAYC at 26.68x; median 25.07x).<br>**Earnings basis:** Historical reported GAAP diluted EPS ($10.94).<br>**Limitations:** Omits cash/debt balance sheet bridge; Paycom's FY2025 earnings lag ADP's FY2026 by six months; capitalizes accounting net income rather than distributable cash flow; ignores differing float interest leverage and hosting infrastructure capex. |

### Provisional Call (Recorded Prior to AI Critique)
> **Provisional Call: Watch / Defer.**  
> At the reference market price of **$265.22**, ADP trades within the peer P/E implied range of **$256.72–$291.89** (and just 3.4% below the peer median of $274.30). However, the DCF base case of **$228.10** indicates that the market price is 16.3% above fundamental cash-flow value (or a 14.0% discount from price to intrinsic value), requiring +3.56 percentage points of above-guidance annual growth. Because DCF accounts for future cash reinvestment and capital structure while trailing P/E merely reflects the current market multiple paid for historical accounting earnings (including elevated interest float), I maintain a Watch / Defer stance. My purchase threshold remains $\approx \$182$ (a 20% margin of safety to the DCF base case).

### What Could Most Easily Change My Mind (Written While AI Responded)
> *"What could most easily change my mind while AI responds: (1) Sourced evidence that ADP's client fund float interest is structurally durable and will not contract significantly when the Federal Reserve cuts interest rates; or (2) Proof that my DCF interest expense proxy improperly understated sustainable FCFF by over $500 million, which would lift the DCF base case into alignment with the peer median."*

---

### AI Partner Skeptical Colleague Review (Codex CLI / `gpt-6-astra`)

#### Skeptical Review Prompt Sent to Codex
```text
Review my valuation comparison as a skeptical colleague. Identify the weakest supported assumption and any mismatch in company, date, valuation object or earnings definition. Do not invent a missing range or average the methods. Ask one question that could change my decision. I will check your criticism against my sources before revising my call.
```

#### Complete Response Received from Codex
```text
Watch / Defer is defensible, but your stated reason for favoring DCF is weaker than the call itself. DCF’s greater detail does not establish that its inputs are better supported.

- Weakest supported assumption: the $4,570.54M starting adjusted FCFF. An expense proxy for non-client interest needs a reconciliation showing that it measures the intended income or financing adjustment. Any error can propagate through the forecasts and terminal value, which represents 76.7% of EV. That concentration makes the proxy consequential; it does not itself prove the DCF is wrong.

- Valuation-object mismatch in your criticism of P/E: P/E × diluted EPS directly estimates equity value per share. It does not require the enterprise-to-equity cash/debt bridge that an FCFF DCF requires. Differences in leverage and excess cash can impair peer comparability, but “omits cash/debt bridge” is not, by itself, a defect in P/E. Conversely, verify that your DCF bridge distinguishes corporate cash/debt from client funds and corresponding obligations.

- Company and earnings definitions: No obvious ticker mismatch appears: ADP is the target, PAYX is Paychex, and PAYC is Paycom. The reported GAAP diluted EPS figures match the cited annual results: ADP $10.94, Paychex $4.89, and Paycom $8.08. However, GAAP EPS and adjusted FCFF are different measures; the adjustment reconciliation matters more than either label.

- Date mismatch: Those earnings cover years ending June 2026, May 2026, and December 2025, respectively. Paycom FY2025 is not the same as September 2026 trailing-twelve-month earnings. Check whether each quoted P/E actually uses the annual EPS you list. Also resolve “September 9/10”: September 10 preparation is harmless if all valuation inputs remain as of September 9; later information would change the comparison.

- Interpretation and arithmetic: $228.10 implies 14.0% downside from market, whereas market is 16.3% above that estimate. A solved +3.56 growth shift should be called percentage points if added to annual growth rates; it is one conditional way to match price, not a uniquely required acceleration. With two peers, the reported median is simply their midpoint, offering little independent corroboration.

One decision-changing question: If you replaced the interest proxy with a source-reconciled FCFF calculation, holding your other assumptions fixed, would the resulting valuation still support deferring at $265.22?
```

---

### Source-Checked Judgment of AI Criticism

| Point of Criticism | Judgment | Sourced Verification and Reasoning |
|---|---|---|
| **1. Starting FCFF interest proxy is the weakest assumption** | **ACCEPT** | **Valid.** In ADP's 10-K (cash-flow statement pp. 48–49), total cash interest paid is $439.6M, but the split between corporate financing and client-strategy financing is not disclosed on the cash-flow statement. Item 7 (p. 34) reports corporate interest expense of $141.0M, which was used as a cash proxy. Because terminal value constitutes 76.7% of enterprise value, any inaccuracy in this $229.9M after-tax deduction multiplies throughout the explicit forecast and terminal value. |
| **2. P/E does not require an enterprise-to-equity cash/debt bridge** | **ACCEPT** | **Valid correction of terminology.** Mathematically, multiplying trailing P/E by diluted EPS directly yields an equity price per share. Criticizing P/E for "omitting a cash/debt bridge" conflates enterprise-level multiples (such as EV/EBITDA) with equity multiples. However, capital structure differences *do* affect peer comparability: if one peer carries large net cash while another has debt, their equity multiples are not on equal footing. |
| **3. Date and fiscal period mismatch (Paycom FY2025 vs. ADP/PAYX FY2026)** | **ACCEPT** | **Valid limitation.** Paycom's latest public annual 10-K prior to September 9, 2026 was for the fiscal year ended December 31, 2025 (filed Feb 19, 2026). ADP's FY2026 ended June 30, 2026, and Paychex's ended May 31, 2026. Paycom's earnings therefore lag ADP's by six months. Under the lab rule prohibiting single quarters, FY2025 is the only compliant annual figure, but the six-month macroeconomic gap must be disclosed. |
| **4. Arithmetic percentage direction and +3.56 percentage points** | **ACCEPT** | **Valid.** Verified from Stock Analysis: market price $265.22 is 16.27% above $228.10 ($265.22 / $228.10 − 1 = +16.27%), while $228.10 is 13.996% below $265.22 ($228.10 / $265.22 − 1 = −14.00%). The shift is properly designated as **+3.56 percentage points** added to each annual rate. |
| **5. Answer to Skeptical Question: Reconciled FCFF Impact** | **REJECT CALL CHANGE** | **Call unchanged (Watch/Defer stands).** Tested mathematically: If we completely eliminate the $229.92M non-client interest proxy deduction and use the assignment-style starting FCFF of $5,114.59M from `ADP_reverse_DCF.md` (p. 28), base-case value rises from $228.10 to $\approx \mathbf{\$255.25}$ per share. Even at $255.25, ADP remains below the $265.22 market price and well above the margin-of-safety purchase threshold ($\approx \$182$). Thus, resolving the interest proxy in the most optimistic direction does not justify an "Initiate" call at $265.22. |

---

## 6. Reflect — Defend Your Own Company's Conclusion

### Explanation of Peer Choices
Paychex (PAYX) and Paycom (PAYC) were chosen because they represent the two most economically comparable, publicly traded operating companies in the U.S. payroll and human capital management industry:
- **Paychex (PAYX)** is ADP's closest direct peer in operational scope, providing payroll processing, human resources SaaS (*Paychex Flex*), insurance services, and PEO solutions while managing client funds float. Like ADP, Paychex is capital-light (capex is 3.6% of revenue) and exhibits high recurring customer retention.
- **Paycom (PAYC)** provides a direct market benchmark for pure-play cloud HCM software. While Paycom lacks a co-employment PEO segment, earns less float interest, and carries higher capex (13.2% of revenue) due to owning its data centers, its high recurring revenue (94.5%) reflects the pure SaaS multiple that investors assign to payroll technology.
- Conglomerates (Microsoft, Oracle) and staffing firms (Robert Half) were excluded because their earnings are driven by completely different economic cycles.

### What the Comparison Adds to the DCF
The peer P/E analysis provides an essential market reality check that the DCF cannot offer on its own:
1. **Current Market Valuation of Current Earnings:** Trailing P/E reflects what active market participants are willing to pay today for a dollar of proven accounting net income in the HCM industry (23.5x for Paychex, 26.7x for Paycom, median 25.1x). ADP's observed multiple of 24.24x shows that ADP trades in line with its peer group, slightly below the peer median and above Paychex.
2. **Diagnosing DCF Discrepancies:** The peer P/E median of $274.30 is higher than the DCF base case of $228.10. This reveals that the market is either pricing in higher long-term growth (as shown by the reverse DCF requiring +3.56 percentage points of growth) or applying a lower cost of capital than our 8.4% WACC estimate.

### Why the Results Differ
The two methods differ because they evaluate fundamentally different valuation objects:
- **DCF (Fundamental Intrinsic Value):** Discounts five years of future unlevered free cash flows after capital expenditures and working-capital reinvestment, then explicitly deducts net financing debt. It penalizes ADP for required ongoing reinvestment and capital costs.
- **Peer P/E (Relative Pricing of Historical Accounting Income):** Capitalizes a single historical year of GAAP net income ($10.94 EPS) using multiples established by peers. It does not deduct debt, does not account for differences in capital reinvestment intensity, and treats cyclical float interest income identically to durable subscription fees.

### Final Defensible Recommendation: Watch / Defer

```text
Action: WATCH / DEFER
Defensible Price Range: $228.10 (DCF Base) to $274.30 (Peer Median Reference)
Current Reference Price: $265.22 (September 9, 2026 close)
Margin-of-Safety Purchase Threshold: $182.00 or lower
```

#### Justification
1. **No Compelling Value at $265.22:** At $265.22, ADP is fairly priced relative to peers (trading at 24.24x vs. peer median 25.07x) but trades at a **16.3% premium** to its discounted cash-flow intrinsic value ($228.10).
2. **Reverse DCF Hurdle:** Justifying $265.22 requires an extra +3.56 percentage points of annual FCFF growth above management's stated revenue and margin guidance in all five forecast years.
3. **Interest Float Asymmetry:** Over $900M of ADP's pretax income stems from client funds float interest. If macroeconomic interest rates decline, float income will compress, reducing earnings per share and making a 24x multiple vulnerable to contraction.
4. **Conditional Action:** I would **Initiate** an investment only if the stock price drops to $\approx \mathbf{\$182}$ (a 20% margin of safety below DCF base value) while fundamental retention remains above 90%. Conversely, I would consider raising the valuation only if management demonstrates organic revenue acceleration above 8% without margin degradation.

---

## 7. Checkout & Verification

### File Artifacts and Working Scripts
- **Markdown Valuation Report:** [`Lab 8.md`](Lab%207.md)
- **Peer P/E Calculator Script:** [`peer_pe.py`](peer_pe.py)
- **DCF Model & Sensitivity Script:** [`ADP_dcf.py`](ADP_dcf.py) / [`dcf.py`](dcf.py)
- **Week 3 DCF Reference Report:** [`ADP_reverse_DCF.md`](ADP_reverse_DCF.md)

### Merit Anchor Self-Evaluation (25 / 25 Points)
- **Problem / Decision (5/5):** Explicit company (ADP), valuation date (September 9, 2026), and peer selection policy established before screening.
- **Data / Evidence (5/5):** Two candidates (PAYX and PAYC) traced to SEC EDGAR 10-K filings and IR releases with exact section locators, same-day September 9, 2026 closing prices, and public annual GAAP diluted EPS.
- **Validation (5/5):** Hand calculations verified exact rational arithmetic; leave-one-out sensitivity (+/-$17.58) predicted and verified against `peer_pe.py`; reference estimate logic explained.
- **Financial Judgment (5/5):** Clear DCF comparison, defensible range ($228.10–$274.30), reverse DCF hurdle explained, and conditional purchase threshold ($182) articulated.
- **Explanation / Transfer (5/5):** Sourced defense of peer choices, independent AI partner queries (Codex and Subagent), skeptical critique recorded and judged with Accept/Reject/Unresolved reasons, and skeptical question answered.

