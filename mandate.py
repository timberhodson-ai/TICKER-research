"""Meridian mandate checker. All weights and limits use percentage points."""

import math

# Editable inputs: holding -> (issuer, business days to redeem, reserve eligible).
HOLDINGS = {
    "Cash": ("none", 0, True),
    "Treasury bills": ("U.S. Treasury", 1, True),
    "Treasury 10-year note": ("U.S. Treasury", 1, True),
    "Global equity index fund": ("diversified fund", 2, False),
    "Investment-grade bond fund": ("diversified fund", 3, False),
    "Private real estate fund": ("diversified fund", 90, False),
    "Acme Corp bonds": ("Acme Corp", 4, False),
    "Acme Corp stock": ("Acme Corp", 1, False),
}
# Weights follow the holdings order above; zero weights are included.
CANDIDATES = {
    "A": dict(zip(HOLDINGS, [2, 2, 10, 60, 26, 0, 0, 0])),
    "B": dict(zip(HOLDINGS, [1, 0, 0, 55, 20, 15, 5, 4])),
    "C": dict(zip(HOLDINGS, [1, 1, 0, 70, 20, 0, 0, 8])),
    "D": dict(zip(HOLDINGS, [100, 0, 0, 0, 0, 0, 0, 0])),
    "E": dict(zip(HOLDINGS, [0, 0, 0, 60, 40, 0, 0, 0])),
}
RESERVE_SIZE = 100  # USD millions
QUARTERLY_DISTRIBUTION = 0.75  # USD millions
QUARTERS_TO_COVER = 4
LIQUIDITY_WINDOW = 5  # business days
MINIMUM_LIQUID_SHARE = 90
ISSUER_LIMIT = 8
EXEMPT_ISSUERS = {"none", "U.S. Treasury", "diversified fund"}


def reserve_minimum():
    return QUARTERS_TO_COVER * QUARTERLY_DISTRIBUTION / RESERVE_SIZE * 100


def check_portfolio(weights):
    """Return (rule, measured value, passes) tuples; never test S9."""
    if set(weights) != set(HOLDINGS):
        raise ValueError("Each candidate must specify every permitted holding.")
    if not all(math.isfinite(weight) for weight in weights.values()):
        raise ValueError("Weights must be finite numbers.")

    total = sum(weights.values())
    lowest = min(weights.values())
    reserve = sum(weights[name] for name, (_, _, eligible) in HOLDINGS.items()
                  if eligible)
    liquid = sum(weights[name] for name, (_, days, _) in HOLDINGS.items()
                 if days <= LIQUIDITY_WINDOW)
    company_totals = {}
    for name, (issuer, _, _) in HOLDINGS.items():
        if issuer not in EXEMPT_ISSUERS:
            company_totals[issuer] = company_totals.get(issuer, 0) + weights[name]
    largest_company = max(company_totals.values(), default=0)

    return [
        ("Weights sum to 100", total,
         math.isclose(total, 100, rel_tol=0, abs_tol=1e-9)),
        ("Long-only (lowest weight)", lowest, lowest >= 0),
        (f"Reserve >= {reserve_minimum():.1f}%", reserve,
         reserve >= reserve_minimum()),
        (f"Redeemable in {LIQUIDITY_WINDOW} days >= {MINIMUM_LIQUID_SHARE:.1f}%",
         liquid, liquid >= MINIMUM_LIQUID_SHARE),
        (f"Largest single company <= {ISSUER_LIMIT:.1f}%", largest_company,
         largest_company <= ISSUER_LIMIT),
    ]


def print_candidate(name, weights):
    print(f"\nCandidate {name}")
    checks = check_portfolio(weights)
    for rule, value, passes in checks:
        print(f"{rule}: {value:.1f} {'pass' if passes else 'FAIL'}")
    print("Calendar-year loss: requires CIO clarification")
    failures = sum(not passes for _, _, passes in checks)
    print("passes every checkable rule" if failures == 0
          else f"fails {failures} rule(s)")


def main():
    print(f"Reserve minimum: {reserve_minimum():.1f}% of the portfolio")
    for name, weights in CANDIDATES.items():
        print_candidate(name, weights)


if __name__ == "__main__":
    main()
