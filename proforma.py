"""Five-year integrated financial model and FCFE equity valuation for Asbury Automotive (ABG).

Projects FY2026E to FY2030E income statement, balance sheet, cash flow / FCFE,
and performs balance sheet equilibrium checks and discounted FCFE equity valuation.
Standard library only; no external package dependencies.
"""

# ==============================================================================
# Model Assumptions and Opening Balance Sheet
# ==============================================================================

# Operational Judgments & History
ORGANIC_REV_GROWTH = 0.018  # 1.8% annually (judgment)
GROSS_MARGIN = 0.1705       # 17.05% of revenue (judgment)
SGA_RATIOS = [0.665, 0.655, 0.645, 0.645, 0.645]  # SG&A / Gross Profit 2026-2030 (judgment)
DEPR_RATIO = 82.4 / 3070.4  # FY2025 depr / year-end PP&E (history)
IMPAIRMENT = 120.0          # $120M annually, non-cash (judgment)
CAPEX = 250.0               # $250M annually (guidance)
TAX_RATE = 0.255            # 25.5% tax rate (judgment)

# Working Capital & Financing History
# Inventory days = FY2025 inventory / FY2025 cost of sales * 365
INV_DAYS = 2135.8 / (17999.0 - 3071.7) * 365.0
# Floor plan / inventory = FY2025 floor plan / FY2025 inventory
FLOOR_PLAN_RATIO = 2027.0 / 2135.8
OWC_REV_RATIO = 0.008       # Other working capital = 0.8% of change in revenue (judgment)

# Liquidity, Debt & Capital Allocation
MIN_CASH = 25.0             # Minimum cash buffer $25M (history)
REVOLVER_LIMIT = 850.0      # Revolver borrowing capacity $850M (judgment)
REVOLVER_RATE = 0.06        # 6.0% revolver interest rate (judgment)
DEBT_REPAYMENT = 150.0      # $150M term debt repayment annually (judgment)
BUYBACK = 150.0             # $150M annual share buybacks (judgment)

# Interest Rates
FLOOR_PLAN_RATE = 0.0467    # 4.67% interest rate (history)
TERM_DEBT_RATE = 0.0544     # 5.44% interest rate (history)

# Valuation Parameters
COST_OF_EQUITY = 0.10       # 10.0% discount rate (judgment)
TERMINAL_GROWTH = 0.025     # 2.5% nominal perpetual growth (judgment)
SHARES_OUTSTANDING = 17.951349  # 17.951349 million shares (fact: 10-Q June 30, 2026)

# Opening Balance Sheet, FY2025 (USD millions)
FY2025_REVENUE = 17999.0
FY2025_INVENTORY = 2135.8
FY2025_PPE = 3070.4
FY2025_OTHER_ASSETS = 6371.6
FY2025_CASH = 40.4
FY2025_FLOOR_PLAN = 2027.0
FY2025_TERM_DEBT = 3572.0
FY2025_REVOLVER = 0.0
FY2025_OTHER_LIABILITIES = 2127.5
FY2025_EQUITY = 3891.7

YEARS = [2026, 2027, 2028, 2029, 2030]


def run_model(override_2026_cash=None):
    """Projects five years of financial statements and returns results dictionary."""
    is_rows = {
        "Revenue": [],
        "Gross profit": [],
        "SG&A": [],
        "Depreciation": [],
        "Impairment": [],
        "Operating income": [],
        "Interest expense": [],
        "Pretax income": [],
        "Income tax": [],
        "Net income": [],
    }

    bs_rows = {
        "Cash": [],
        "Inventory": [],
        "PP&E": [],
        "Other assets": [],
        "Total assets": [],
        "Floor plan notes": [],
        "Term debt": [],
        "Revolver": [],
        "Other liabilities": [],
        "Total liabilities": [],
        "Common equity": [],
        "Total liabilities & equity": [],
    }

    cf_rows = {
        "Net income": [],
        "Depreciation": [],
        "Impairment": [],
        "Capex": [],
        "Change in inventory": [],
        "Change in other working capital": [],
        "Change in floor plan": [],
        "Debt repayment": [],
        "Free cash flow to equity (FCFE)": [],
        "Opening cash": [],
        "Share buyback": [],
        "Revolver draw / (repayment)": [],
        "Closing cash": [],
    }

    checks = {
        "Assets - liabilities - equity": [],
        "Cash at or above minimum (25.0)": [],
        "Balance sheet gap": [],
    }

    # Initialize tracking variables with FY2025 opening values
    prior_rev = FY2025_REVENUE
    prior_inv = FY2025_INVENTORY
    prior_ppe = FY2025_PPE
    prior_other_assets = FY2025_OTHER_ASSETS
    prior_cash = FY2025_CASH
    prior_fp = FY2025_FLOOR_PLAN
    prior_debt = FY2025_TERM_DEBT
    prior_revolver = FY2025_REVOLVER
    prior_other_liab = FY2025_OTHER_LIABILITIES
    prior_equity = FY2025_EQUITY

    for idx, year in enumerate(YEARS):
        # 1. Income Statement
        rev = prior_rev * (1.0 + ORGANIC_REV_GROWTH)
        change_in_rev = rev - prior_rev
        gp = rev * GROSS_MARGIN
        sga = gp * SGA_RATIOS[idx]
        depr = prior_ppe * DEPR_RATIO
        imp = IMPAIRMENT
        op_inc = gp - sga - depr - imp
        interest = (prior_fp * FLOOR_PLAN_RATE +
                    prior_debt * TERM_DEBT_RATE +
                    prior_revolver * REVOLVER_RATE)
        pretax = op_inc - interest
        tax = max(0.0, pretax) * TAX_RATE
        net_inc = pretax - tax

        is_rows["Revenue"].append(rev)
        is_rows["Gross profit"].append(gp)
        is_rows["SG&A"].append(sga)
        is_rows["Depreciation"].append(depr)
        is_rows["Impairment"].append(imp)
        is_rows["Operating income"].append(op_inc)
        is_rows["Interest expense"].append(interest)
        is_rows["Pretax income"].append(pretax)
        is_rows["Income tax"].append(tax)
        is_rows["Net income"].append(net_inc)

        # 2. Balance Sheet (except cash)
        inv = (rev - gp) * INV_DAYS / 365.0
        change_inv = inv - prior_inv

        fp = inv * FLOOR_PLAN_RATIO
        change_fp = fp - prior_fp

        ppe = prior_ppe + CAPEX - depr

        change_owc = OWC_REV_RATIO * change_in_rev
        other_assets = prior_other_assets + change_owc - imp

        debt = prior_debt - DEBT_REPAYMENT
        other_liab = prior_other_liab
        equity = prior_equity + net_inc - BUYBACK

        # 3. Free Cash Flow to Equity (FCFE)
        fcfe = (net_inc + depr + imp - CAPEX - change_inv -
                change_owc + change_fp - DEBT_REPAYMENT)

        # 4. Cash and Revolver
        tentative_cash = prior_cash + fcfe - BUYBACK
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

        # Intentional test hook for partner check / break test
        if year == 2026 and override_2026_cash is not None:
            cash = override_2026_cash

        # Record Balance Sheet
        total_assets = cash + inv + ppe + other_assets
        total_liab = fp + debt + revolver + other_liab
        total_liab_equity = total_liab + equity

        bs_rows["Cash"].append(cash)
        bs_rows["Inventory"].append(inv)
        bs_rows["PP&E"].append(ppe)
        bs_rows["Other assets"].append(other_assets)
        bs_rows["Total assets"].append(total_assets)
        bs_rows["Floor plan notes"].append(fp)
        bs_rows["Term debt"].append(debt)
        bs_rows["Revolver"].append(revolver)
        bs_rows["Other liabilities"].append(other_liab)
        bs_rows["Total liabilities"].append(total_liab)
        bs_rows["Common equity"].append(equity)
        bs_rows["Total liabilities & equity"].append(total_liab_equity)

        # Record Cash Flow Statement
        cf_rows["Net income"].append(net_inc)
        cf_rows["Depreciation"].append(depr)
        cf_rows["Impairment"].append(imp)
        cf_rows["Capex"].append(CAPEX)
        cf_rows["Change in inventory"].append(change_inv)
        cf_rows["Change in other working capital"].append(change_owc)
        cf_rows["Change in floor plan"].append(change_fp)
        cf_rows["Debt repayment"].append(DEBT_REPAYMENT)
        cf_rows["Free cash flow to equity (FCFE)"].append(fcfe)
        cf_rows["Opening cash"].append(prior_cash)
        cf_rows["Share buyback"].append(BUYBACK)
        cf_rows["Revolver draw / (repayment)"].append(revolver_activity)
        cf_rows["Closing cash"].append(cash)

        # 5. Balance Sheet & Liquidity Checks
        gap = total_assets - total_liab - equity
        checks["Assets - liabilities - equity"].append(gap)
        checks["Cash at or above minimum (25.0)"].append(cash >= (MIN_CASH - 1e-4))
        checks["Balance sheet gap"].append(gap)

        # Roll forward balances
        prior_rev = rev
        prior_inv = inv
        prior_ppe = ppe
        prior_other_assets = other_assets
        prior_cash = cash
        prior_fp = fp
        prior_debt = debt
        prior_revolver = revolver
        prior_other_liab = other_liab
        prior_equity = equity

    return is_rows, bs_rows, cf_rows, checks


def assert_balanced(checks):
    """Raises an error naming the year and the gap if any check fails."""
    for idx, year in enumerate(YEARS):
        gap = checks["Balance sheet gap"][idx]
        is_above_min = checks["Cash at or above minimum (25.0)"][idx]
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
    header = f"{'Line Item':<35}" + "".join(f"{f'FY{y}E':>12}" for y in years)
    print(header)
    print("-" * len(header))
    for label, values in rows.items():
        val_str = "".join(f"{v:>12.1f}" for v in values)
        print(f"{label:<35}{val_str}")


def print_checks(checks, years=YEARS):
    """Prints the check block for all projection years."""
    print("\n=== Balance Sheet and Liquidity Checks ===")
    header = f"{'Check':<35}" + "".join(f"{f'FY{y}E':>12}" for y in years)
    print(header)
    print("-" * len(header))
    gap_str = "".join(f"{g:>12.1f}" for g in checks["Assets - liabilities - equity"])
    print(f"{'Assets - liabilities - equity':<35}{gap_str}")
    min_str = "".join(f"{('Pass' if ok else 'FAIL'):>12}" for ok in checks["Cash at or above minimum (25.0)"])
    print(f"{'Cash >= Minimum ($25.0M)':<35}{min_str}")


def perform_valuation(fcfe_list):
    """Calculates discounted FCFE equity value, terminal value, and value per share."""
    discount_factors = [(1.0 + COST_OF_EQUITY) ** t for t in range(1, 6)]
    pv_fcfe_list = [f / df for f, df in zip(fcfe_list, discount_factors)]
    pv_explicit_fcfe = sum(pv_fcfe_list)

    # Terminal Value: (2030 FCFE + 2030 repayment) * (1 + g) / (r - g)
    terminal_cash_flow = (fcfe_list[-1] + DEBT_REPAYMENT) * (1.0 + TERMINAL_GROWTH)
    terminal_value = terminal_cash_flow / (COST_OF_EQUITY - TERMINAL_GROWTH)
    pv_terminal_value = terminal_value / ((1.0 + COST_OF_EQUITY) ** 5)

    total_equity_value = pv_explicit_fcfe + pv_terminal_value
    tv_share = pv_terminal_value / total_equity_value
    value_per_share = total_equity_value / SHARES_OUTSTANDING

    print("\n=== Equity Valuation (Discounted FCFE Model) ===")
    print(f"Cost of Equity:                       {COST_OF_EQUITY * 100:.1f}%")
    print(f"Terminal Growth Rate:                 {TERMINAL_GROWTH * 100:.1f}%")
    print(f"Shares Outstanding:                   {SHARES_OUTSTANDING:.6f} million")
    print("-" * 55)
    for yr, pv, f in zip(YEARS, pv_fcfe_list, fcfe_list):
        print(f"FY{yr}E FCFE: ${f:>7.1f}M  |  PV: ${pv:>7.2f}M")
    print(f"PV of 5-Year Explicit FCFE:           ${pv_explicit_fcfe:>10.2f}M")
    print(f"2030 FCFE + Debt Repayment:           ${fcfe_list[-1] + DEBT_REPAYMENT:>10.2f}M")
    print(f"Terminal Value (at FY2030E):          ${terminal_value:>10.2f}M")
    print(f"PV of Terminal Value:                 ${pv_terminal_value:>10.2f}M")
    print(f"Total Equity Value:                   ${total_equity_value:>10.2f}M")
    print(f"Share of Value after 2030:            {tv_share * 100:>10.2f}% (approx. {round(tv_share * 100):.0f}%)")
    print(f"Value Per Share:                      ${value_per_share:>10.2f}")

    return total_equity_value, tv_share, value_per_share


def main():
    print("Projecting 5 Years of Integrated Financial Statements for Asbury Automotive (ABG)...")
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
