"""Comparable P/E valuation. Standard library only; no data downloads.

Prices: September 9, 2026 closes. EPS: Latest public annual GAAP diluted EPS.
Inputs supplied by the user. Use matching periods, currency, and EPS basis.
Enter decimal inputs as strings to preserve their exact decimal values.
Missing values may be None. Duplicate tickers: first occurrence wins.
"""

# ==================== EDITABLE INPUTS ====================
TARGET = {"ticker": "ADP", "price": "265.22", "eps": "10.94"}
PEERS = [
    {"ticker": "PAYX", "price": "114.75", "eps": "4.89"},
    {"ticker": "PAYC", "price": "215.58", "eps": "8.08"},
]
# ========================================================

from fractions import Fraction
from statistics import median


def positive(value):
    """Return an exact positive rational, or None for unusable inputs."""
    try:
        result = Fraction(str(value))
    except (ValueError, TypeError, ZeroDivisionError, OverflowError):
        return None
    return result if result > 0 else None


def display(value, places=2, signed=False):
    """Exact rounding for display only; ties round away from zero."""
    scale = 10 ** places
    scaled = abs(value) * scale
    integer, remainder = divmod(scaled.numerator, scaled.denominator)
    if 2 * remainder >= scaled.denominator:
        integer += 1
    sign = "-" if value < 0 else ("+" if signed else "")
    return f"{sign}{integer // scale:,}.{integer % scale:0{places}d}"


def ticker(row):
    return str(row.get("ticker") or "").strip().upper()


def main(target=TARGET, peers=PEERS):
    target_name = ticker(target)
    target_eps = positive(target.get("eps"))
    target_price = positive(target.get("price"))
    print("P/E comparison | September 9, 2026 prices | Public annual GAAP diluted EPS")
    print("User-supplied inputs; no cash/debt adjustment. Currency: USD.\n")
    print(f"Target: {target_name or '(missing ticker)'}")
    if target_price is None:
        print("Target price: not meaningful (missing, invalid, or nonpositive).")
    else:
        print(f"Target observed price: ${display(target_price)}")
    if target_eps is None:
        print("Target EPS: not meaningful (missing, invalid, or nonpositive).")
    if target_price is None or target_eps is None:
        print("Target P/E: not meaningful.")
    else:
        print(f"Target P/E: {display(target_price / target_eps, 6)}x")

    valid = []
    seen = set()
    print("\nPeer P/E calculations:")
    for row in peers:
        name = ticker(row)
        if not name:
            print("Missing peer ticker: not meaningful; excluded.")
            continue
        if name == target_name:
            print(f"{name}: excluded (target).")
            continue
        if name in seen:
            print(f"{name}: excluded (duplicate; first occurrence retained).")
            continue
        seen.add(name)
        price, eps = positive(row.get("price")), positive(row.get("eps"))
        if price is None or eps is None:
            print(f"{name}: P/E not meaningful (missing, invalid, or nonpositive price/EPS).")
            continue
        multiple = price / eps
        valid.append((name, multiple))
        print(f"{name}: {display(multiple, 6)}x")

    if not valid:
        print("\nNo usable peers. Peer median and implied prices: not meaningful.")
        return

    multiples = [value for _, value in valid]
    full_median = median(multiples)
    print(f"\nValid peers: {len(valid)}")
    print(f"Peer median P/E: {display(full_median, 6)}x")
    full_estimate = full_median * target_eps if target_eps is not None else None
    if len(valid) == 1:
        print("One valid peer: reference estimate only; no range.")
        print("Reference implied price: " + (
            f"${display(full_estimate)}" if full_estimate is not None
            else "not meaningful (target EPS)."))
    else:
        for label, multiple in (("Minimum", min(multiples)),
                                ("Median", full_median),
                                ("Maximum", max(multiples))):
            price_text = (f"${display(multiple * target_eps)}" if target_eps is not None
                          else "not meaningful (target EPS)")
            print(f"{label}: {display(multiple, 6)}x | implied price: {price_text}")

    print("\nPeer removal sensitivity (change from full-peer median estimate):")
    for name in seen:
        # Invalid peers never enter the median; removing one leaves it unchanged.
        remaining = [value for peer_name, value in valid if peer_name != name]
        if not remaining:
            print(f"Remove {name}: no estimate (no usable peers remain).")
        elif full_estimate is None:
            print(f"Remove {name}: implied price and change not meaningful (target EPS).")
        else:
            estimate = median(remaining) * target_eps
            note = " | one-peer reference; no range" if len(remaining) == 1 else ""
            print(f"Remove {name}: ${display(estimate)} | "
                  f"change: {display(estimate - full_estimate, signed=True)} USD{note}")


if __name__ == "__main__":
    main()
