"""Five-year integrated financial model and FCFE equity valuation for Automatic Data Processing, Inc. (ADP).

FIN 439 - Lab 10
Educational coursework only. Not financial or investment advice, and not a
recommendation to buy, sell, or hold any security. Outputs depend on simplified
assumptions and unresolved data limitations described in the accompanying report.
Projects FY2027E to FY2031E income statement, balance sheet, cash flow / FCFE,
performs balance sheet equilibrium checks, and computes discounted FCFE equity valuation.
Standard library only; no external package dependencies.
"""

# ==============================================================================
# Model Assumptions and Opening Balance Sheet (FY2026 ended June 30, 2026)
# ==============================================================================

# Operational Judgments & History
REVENUE_GROWTH = 0.055      # Total reported revenue; FY27 guidance midpoint, later years judgment
GROSS_MARGIN = 0.5333        # Contribution margin BEFORE R&D and D&A (history/judgment)
SGA_RATIO = (4408.2 - (585.9 - 490.8)) / 11706.8  # Exclude D&A outside cost of revenues
RD_RATIO = 0.0469            # 4.69% R&D as % of Revenue (history: $1,028.8M on $21,947.4M)
DEPR_PPE_RATIO = 201.1 / 655.4  # PP&E depr / opening PP&E (~30.68%, history)
IMPAIRMENT = 0.0             # $0.0M non-cash impairment (history/judgment)
CAPEX_PPE = 212.5            # FY27 $200-225M guidance midpoint; held flat by judgment
SOFTWARE_CAPEX_RATIO = 468.5 / 21947.4  # Capitalized intangibles scale with revenue
AMORT_INTANG_RATIO = 384.8 / 1603.0    # Amortization / opening net intangible assets
TAX_RATE = 0.230             # 23.0% effective tax rate (history/guidance: 3-yr average 23.0%)

# Working Capital & Operating History
INV_DAYS = 0.0               # ADP carries no physical product inventory (history: None)
FLOOR_PLAN_RATIO = 0.0       # ADP has no dealership floor plan debt (history: None)
OWC_REV_RATIO = 0.012        # Other working capital = 1.2% of change in revenue (judgment)

# Liquidity, Debt & Capital Allocation
MIN_CASH = 500.0             # Operating cash floor $500.0M (history/judgment)
REVOLVER_LIMIT = 2000.0      # Credit facility capacity $2,000.0M (judgment)
REVOLVER_RATE = 0.055        # 5.5% credit facility borrowing rate (judgment)
DEBT_REPAYMENT = 200.0       # $200.0M term debt repayment / retirement annually (judgment)
SHAREHOLDER_DIST = 3500.0    # $3,500.0M annual dividends + net share repurchases (judgment)

# Interest & Capital Rates
DEBT_INTEREST_RATE = 0.045   # Judgment: simplified corporate borrowing rate, not historical total expense
COST_OF_EQUITY = 0.0483 + 0.83 * 0.045  # CAPM = 8.565%; inherited inputs, not refreshed market estimates
TERMINAL_GROWTH = 0.025      # 2.50% nominal terminal growth rate (judgment)
SHARES_OUTSTANDING = 403.3   # 403.3 million diluted shares (fact: FY2026 10-K, p. 45)

# Opening Balance Sheet, FY2026 Ended June 30, 2026 (USD millions, 10-K p. 47)
FY2026_REVENUE = 21947.4
FY2026_CASH = 4230.1          # Corporate cash and cash equivalents
FY2026_INVENTORY = 0.0        # None
FY2026_PPE = 641.3            # Property, plant and equipment, net
FY2026_OTHER_ASSETS = 58321.9 # Receivables, client funds asset ($43,957.8M), intangibles, goodwill, other
FY2026_INTANGIBLES = 1653.3
FY2026_CLIENT_ASSETS = 43957.8
FY2026_CLIENT_OBLIGATIONS = 44415.5
FY2026_FLOOR_PLAN = 0.0       # None
FY2026_TERM_DEBT = 5104.4     # Long-term debt $4,964.1M + current $1.0M + reverse repos $139.3M
FY2026_REVOLVER = 0.0         # Commercial paper / credit facility drawn: $0.0M
FY2026_OTHER_LIABILITIES = 52057.7 # Client funds obligations ($44,415.5M), payables, accrued, other
FY2026_EQUITY = 6031.2        # Total stockholders' equity

YEARS = [2027, 2028, 2029, 2030, 2031]


def run_model(override_2027_cash=None):
    """Return income statement, balance sheet, cash flow and check dictionaries."""
    is_rows = {
        "Total revenues": [],
        "Operating expenses (direct cost)": [],
        "Contribution before R&D and D&A": [],
        "SG&A excluding D&A": [],
        "Research & development": [],
        "Depreciation & amortization": [],
        "Operating income (EBIT)": [],
        "Interest expense": [],
        "Pretax income": [],
        "Provision for income taxes": [],
        "Net earnings": [],
    }

    bs_rows = {
        "Corporate cash & equivalents": [],
        "Inventories": [],
        "Property, plant & equipment, net": [],
        "Intangible assets, net": [],
        "Funds held for clients": [],
        "Other corporate assets": [],
        "Total assets": [],
        "Floor plan notes": [],
        "Term borrowings & debt": [],
        "Credit facility / revolver": [],
        "Client funds obligations": [],
        "Other corporate liabilities": [],
        "Total liabilities": [],
        "Stockholders' equity": [],
        "Total liabilities & equity": [],
    }

    cf_rows = {
        "Net earnings": [],
        "Depreciation & amortization": [],
        "PP&E capital expenditures": [],
        "Capitalized intangible additions": [],
        "Change in other working capital": [],
        "Debt repayment": [],
        "FCFE before revolver financing": [],
        "Opening corporate cash": [],
        "Shareholder distributions (divs/buybacks)": [],
        "Revolver draw / (repayment)": [],
        "Free cash flow to equity (FCFE)": [],
        "Closing corporate cash": [],
    }

    checks = {
        "Assets - liabilities - equity": [],
        "Cash at or above minimum (500.0)": [],
        "Balance sheet gap": [],
    }

    # Initialize tracking variables with FY2026 opening balances
    prior_rev = FY2026_REVENUE
    prior_cash = FY2026_CASH
    prior_ppe = FY2026_PPE
    prior_intangibles = FY2026_INTANGIBLES
    prior_other_assets = FY2026_OTHER_ASSETS - FY2026_INTANGIBLES - FY2026_CLIENT_ASSETS
    prior_debt = FY2026_TERM_DEBT
    prior_revolver = FY2026_REVOLVER
    prior_other_liab = FY2026_OTHER_LIABILITIES - FY2026_CLIENT_OBLIGATIONS
    prior_equity = FY2026_EQUITY

    for idx, year in enumerate(YEARS):
        # 1. Income Statement
        rev = prior_rev * (1.0 + REVENUE_GROWTH)
        change_in_rev = rev - prior_rev
        direct_opex = rev * (1.0 - GROSS_MARGIN)
        gp = rev * GROSS_MARGIN
        sga = gp * SGA_RATIO
        rd = rev * RD_RATIO
        depr = prior_ppe * DEPR_PPE_RATIO
        amort = prior_intangibles * AMORT_INTANG_RATIO
        total_da = depr + amort
        software_capex = rev * SOFTWARE_CAPEX_RATIO
        op_inc = gp - sga - rd - total_da - IMPAIRMENT

        interest = prior_debt * DEBT_INTEREST_RATE + prior_revolver * REVOLVER_RATE
        pretax = op_inc - interest
        tax = max(0.0, pretax) * TAX_RATE
        net_inc = pretax - tax

        is_rows["Total revenues"].append(rev)
        is_rows["Operating expenses (direct cost)"].append(direct_opex)
        is_rows["Contribution before R&D and D&A"].append(gp)
        is_rows["SG&A excluding D&A"].append(sga)
        is_rows["Research & development"].append(rd)
        is_rows["Depreciation & amortization"].append(total_da)
        is_rows["Operating income (EBIT)"].append(op_inc)
        is_rows["Interest expense"].append(interest)
        is_rows["Pretax income"].append(pretax)
        is_rows["Provision for income taxes"].append(tax)
        is_rows["Net earnings"].append(net_inc)

        # 2. Balance Sheet (except cash)
        ppe = prior_ppe + CAPEX_PPE - depr
        intangibles = prior_intangibles + software_capex - amort
        change_owc = OWC_REV_RATIO * change_in_rev
        other_assets = prior_other_assets + change_owc - IMPAIRMENT
        debt_repayment = min(DEBT_REPAYMENT, prior_debt)
        debt = prior_debt - debt_repayment
        other_liab = prior_other_liab
        equity = prior_equity + net_inc - SHAREHOLDER_DIST

        # 3. Free Cash Flow to Equity (FCFE)
        fcfe = net_inc + total_da + IMPAIRMENT - CAPEX_PPE - software_capex - change_owc - debt_repayment

        # 4. Cash and Revolver Mechanics
        tentative_cash = prior_cash + fcfe - SHAREHOLDER_DIST
        revolver = prior_revolver
        revolver_activity = 0.0

        if tentative_cash < MIN_CASH:
            shortfall = MIN_CASH - tentative_cash
            draw = min(shortfall, REVOLVER_LIMIT - prior_revolver)
            revolver = prior_revolver + draw
            cash = tentative_cash + draw
            revolver_activity = draw
        elif tentative_cash > MIN_CASH and prior_revolver > 0.0:
            surplus = tentative_cash - MIN_CASH
            repay = min(surplus, prior_revolver)
            revolver = prior_revolver - repay
            cash = tentative_cash - repay
            revolver_activity = -repay
        else:
            cash = tentative_cash

        # Intentional test hook for broken balance sheet check
        if year == 2027 and override_2027_cash is not None:
            cash = override_2027_cash

        # Record Balance Sheet lines
        total_assets = cash + ppe + intangibles + FY2026_CLIENT_ASSETS + other_assets
        total_liab = debt + revolver + FY2026_CLIENT_OBLIGATIONS + other_liab
        total_liab_equity = total_liab + equity

        bs_rows["Corporate cash & equivalents"].append(cash)
        bs_rows["Inventories"].append(0.0)
        bs_rows["Property, plant & equipment, net"].append(ppe)
        bs_rows["Intangible assets, net"].append(intangibles)
        bs_rows["Funds held for clients"].append(FY2026_CLIENT_ASSETS)
        bs_rows["Other corporate assets"].append(other_assets)
        bs_rows["Total assets"].append(total_assets)
        bs_rows["Floor plan notes"].append(0.0)
        bs_rows["Term borrowings & debt"].append(debt)
        bs_rows["Credit facility / revolver"].append(revolver)
        bs_rows["Client funds obligations"].append(FY2026_CLIENT_OBLIGATIONS)
        bs_rows["Other corporate liabilities"].append(other_liab)
        bs_rows["Total liabilities"].append(total_liab)
        bs_rows["Stockholders' equity"].append(equity)
        bs_rows["Total liabilities & equity"].append(total_liab_equity)

        # Record Cash Flow Statement lines
        cf_rows["Net earnings"].append(net_inc)
        cf_rows["Depreciation & amortization"].append(total_da)
        cf_rows["PP&E capital expenditures"].append(CAPEX_PPE)
        cf_rows["Capitalized intangible additions"].append(software_capex)
        cf_rows["Change in other working capital"].append(change_owc)
        cf_rows["Debt repayment"].append(debt_repayment)
        cf_rows["FCFE before revolver financing"].append(fcfe)
        cf_rows["Opening corporate cash"].append(prior_cash)
        cf_rows["Shareholder distributions (divs/buybacks)"].append(SHAREHOLDER_DIST)
        cf_rows["Revolver draw / (repayment)"].append(revolver_activity)
        cf_rows["Free cash flow to equity (FCFE)"].append(fcfe + revolver_activity)
        cf_rows["Closing corporate cash"].append(cash)

        # 5. Balance Sheet & Liquidity Checks
        gap = total_assets - total_liab - equity
        checks["Assets - liabilities - equity"].append(gap)
        checks["Cash at or above minimum (500.0)"].append(cash >= (MIN_CASH - 1e-4))
        checks["Balance sheet gap"].append(gap)

        # Roll forward balances
        prior_rev = rev
        prior_cash = cash
        prior_ppe = ppe
        prior_intangibles = intangibles
        prior_other_assets = other_assets
        prior_debt = debt
        prior_revolver = revolver
        prior_other_liab = other_liab
        prior_equity = equity

    return is_rows, bs_rows, cf_rows, checks


def assert_balanced(checks):
    """Raises an error naming the year and the gap if any check fails."""
    for idx, year in enumerate(YEARS):
        gap = checks["Balance sheet gap"][idx]
        is_above_min = checks["Cash at or above minimum (500.0)"][idx]
        if abs(gap) > 1e-3:
            raise AssertionError(
                f"Balance sheet check failed in FY{year}E: gap of {gap:+.1f} (assets - liabilities - equity != 0)"
            )
        if not is_above_min:
            raise AssertionError(
                f"Liquidity check failed in FY{year}E: cash below minimum of ${MIN_CASH:.1f}M"
            )


def print_table(title, rows, years=YEARS):
    """Prints a financial statement table with years across, formatted to one decimal."""
    print(f"\n=== {title} (USD Millions) ===")
    header = f"{'Line Item':<40}" + "".join(f"{f'FY{y}E':>12}" for y in years)
    print(header)
    print("-" * len(header))
    for label, values in rows.items():
        val_str = "".join(f"{v:>12.1f}" for v in values)
        print(f"{label:<40}{val_str}")


def print_checks(checks, years=YEARS):
    """Prints the check block for all projection years."""
    print("\n=== Balance Sheet and Liquidity Checks ===")
    header = f"{'Check':<40}" + "".join(f"{f'FY{y}E':>12}" for y in years)
    print(header)
    print("-" * len(header))
    gap_str = "".join(f"{g:>12.1f}" for g in checks["Assets - liabilities - equity"])
    print(f"{'Assets - liabilities - equity':<40}{gap_str}")
    min_str = "".join(f"{('Pass' if ok else 'FAIL'):>12}" for ok in checks["Cash at or above minimum (500.0)"])
    print(f"{'Cash >= Minimum ($500.0M)':<40}{min_str}")


def perform_valuation(fcfe_list):
    """Calculates discounted FCFE equity value, terminal value, and value per share."""
    if len(fcfe_list) != len(YEARS):
        raise ValueError("Provide one FCFE for each forecast year.")
    if not COST_OF_EQUITY > TERMINAL_GROWTH:
        raise ValueError("Cost of equity must exceed terminal growth.")
    if any(f <= 0 for f in fcfe_list):
        raise ValueError("Nonpositive FCFE: review funding and terminal assumptions before valuation.")
    discount_factors = [(1.0 + COST_OF_EQUITY) ** t for t in range(1, 6)]
    pv_fcfe_list = [f / df for f, df in zip(fcfe_list, discount_factors)]
    pv_explicit_fcfe = sum(pv_fcfe_list)

    # Terminal judgment: scheduled term repayments are refinanced after FY2031.
    # This removes net term repayments, not interest expense or reinvestment.
    terminal_cash_flow = (fcfe_list[-1] + DEBT_REPAYMENT) * (1.0 + TERMINAL_GROWTH)
    terminal_value = terminal_cash_flow / (COST_OF_EQUITY - TERMINAL_GROWTH)
    pv_terminal_value = terminal_value / ((1.0 + COST_OF_EQUITY) ** 5)

    total_equity_value = pv_explicit_fcfe + pv_terminal_value
    tv_share = pv_terminal_value / total_equity_value
    value_per_share = total_equity_value / SHARES_OUTSTANDING

    print("\n=== Equity Valuation (Discounted FCFE Model) ===")
    print(f"Cost of Equity (r_e):                 {COST_OF_EQUITY * 100:.3f}%")
    print(f"Terminal Growth Rate (g):             {TERMINAL_GROWTH * 100:.2f}%")
    print(f"Diluted Shares Outstanding:           {SHARES_OUTSTANDING:.1f} million")
    print("-" * 60)
    for yr, pv, f in zip(YEARS, pv_fcfe_list, fcfe_list):
        print(f"FY{yr}E FCFE: ${f:>7.1f}M  |  PV: ${pv:>7.2f}M")
    print(f"PV of 5-Year Explicit FCFE:           ${pv_explicit_fcfe:>10.2f}M")
    print(f"Normalized FY2031 Cash Flow (FCFE+Repay): ${fcfe_list[-1] + DEBT_REPAYMENT:>8.2f}M")
    print(f"Terminal Value (at FY2031E):          ${terminal_value:>10.2f}M")
    print(f"PV of Terminal Value:                 ${pv_terminal_value:>10.2f}M")
    print(f"Total Equity Value:                   ${total_equity_value:>10.2f}M")
    print(f"Share of Value after FY2031:          {tv_share * 100:>10.2f}%")
    print(f"Model Implied Value Per Share:        ${value_per_share:>10.2f}")

    return total_equity_value, tv_share, value_per_share


def main():
    print("Projecting 5 Years of Integrated Financial Statements for Automatic Data Processing (ADP)...")
    is_rows, bs_rows, cf_rows, checks = run_model()

    # Print the three statements
    print_table("Income Statement", is_rows)
    print_table("Balance Sheet", bs_rows)
    print_table("Cash Flow Statement (FCFE)", cf_rows)

    # Print check block
    print_checks(checks)

    # Verify model balance before performing valuation
    assert_balanced(checks)
    print("\n[Pass] All balance sheet and liquidity checks verified: assert_balanced passed.")

    # Perform Valuation
    perform_valuation(cf_rows["Free cash flow to equity (FCFE)"])


if __name__ == "__main__":
    main()
