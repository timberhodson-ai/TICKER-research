"""Point-in-time training filter. Run: python asof.py"""

from datetime import date


# Editable inputs: row, ticker, month measured, published on, price.
TABLE = [
    (1, "AAA", "2026-01", "2026-02-10", 101.0),
    (2, "AAA", "2026-02", "2026-03-10", 104.0),
    (3, "AAA", "2026-03", "2026-04-10", 109.0),
    (4, "AAA", "2026-02", "2026-03-25", 103.0),
    (5, "BBB", "2026-01", "2026-02-10", 98.0),
    (6, "BBB", "2026-02", "2026-03-10", 97.0),
    (7, "BBB", "2026-02", "2026-03-10", 97.0),
    (8, "BBB", "2026-03", "2026-04-10", 92.0),
    (9, "CCC", "2026-01", "2026-02-10", 110.0),
    (10, "CCC", "2026-02", "2026-04-05", 112.0),
    (11, "", "2026-02", "2026-03-10", 99.0),
    (12, "CCC", "2026-02", "2026-03-10", 111.0),
]
DECISION_DATE = "2026-03-31"


def report(label, removed):
    numbers = ", ".join(str(row[0]) for row in removed) or "none"
    print(f"{label}: {len(removed)} rows; row numbers: {numbers}")


def latest_publications(rows):
    """Rule 4: keep the latest publication for each ticker/month pair."""
    latest = {}
    for row in rows:
        key = (row[1], row[2])
        if key not in latest or row[3] > latest[key][3]:
            latest[key] = row
    kept_numbers = {row[0] for row in latest.values()}
    kept = [row for row in rows if row[0] in kept_numbers]
    removed = [row for row in rows if row[0] not in kept_numbers]
    return kept, removed


def signals(panel, label):
    print(f"\n{label}")
    for ticker in sorted({row[1] for row in panel}):
        history = sorted(
            (row for row in panel if row[1] == ticker), key=lambda row: row[2]
        )
        if len(history) < 2:
            print(f"{ticker}: insufficient months")
            continue
        previous, latest = history[-2:]
        # Require the actual previous calendar month, not a gap in the series.
        year, month = map(int, latest[2].split("-"))
        previous_month = f"{year - 1}-12" if month == 1 else f"{year}-{month - 1:02d}"
        if previous[2] != previous_month:
            print(f"{ticker}: missing previous month for {latest[2]}")
            continue
        signal = (latest[4] / previous[4] - 1) * 100
        print(f"{ticker}: {signal:+.2f}% ({latest[2]})")


def main():
    decision = date.fromisoformat(DECISION_DATE)
    rows = list(TABLE)
    print(f"Decision date: {decision}\n\nRow funnel")

    removed = [row for row in rows if not row[1].strip()]
    rows = [row for row in rows if row[1].strip()]
    report("1. Quarantined: no ticker", removed)

    seen = set()
    unique, removed = [], []
    for row in rows:
        # The source row number is an identifier, not part of the observation.
        observation = row[1:]
        if observation in seen:
            removed.append(row)
        else:
            seen.add(observation)
            unique.append(row)
    rows = unique
    report("2. Exact duplicate removed", removed)

    # The naive comparison uses clean records but ignores the decision date.
    naive_panel, _ = latest_publications(rows)

    removed = [row for row in rows if date.fromisoformat(row[3]) > decision]
    rows = [row for row in rows if date.fromisoformat(row[3]) <= decision]
    report("3. Published after decision date", removed)

    rows, removed = latest_publications(rows)
    report("4. Older vintage replaced by revision", removed)

    print("\nAs-of panel")
    print("Row  Ticker  Month    Published   Price")
    for number, ticker, month, published, price in rows:
        print(f"{number:>3}  {ticker:<6}  {month}  {published}  {price:.1f}")
    signals(rows, "As-of signals")
    signals(naive_panel, "Naive signals (publication date ignored)")


if __name__ == "__main__":
    main()
