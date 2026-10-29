"""FRED/ALFRED learning app. Run: py -m streamlit run asof_app.py."""

from datetime import date
from io import StringIO
import re

import pandas as pd
import requests
import streamlit as st


SERIES = {
    "BAA": "Moody's Baa corporate bond yield",
    "FEDFUNDS": "federal funds rate",
    "DGS10": "10-year Treasury yield",
    "MORTGAGE30US": "30-year mortgage rate",
}


def parse_csv(text):
    """Keep missing days missing, and normalize vintage-dependent column names."""
    frame = pd.read_csv(StringIO(text), na_values=["."], dtype=str)
    if len(frame.columns) != 2:
        raise ValueError("Expected a date column and one series column in the CSV.")
    dates = pd.to_datetime(frame.iloc[:, 0], errors="raise")
    values = pd.to_numeric(frame.iloc[:, 1], errors="raise")
    result = pd.Series(values.to_numpy(), index=dates, name="Value").sort_index()
    result.index.name = "Observation date"
    if result.index.has_duplicates:
        raise ValueError("The download contains duplicate observation dates.")
    return result


@st.cache_data(ttl=3600, show_spinner=False)
def download_today(series_id, download_day):
    """One public FRED CSV request; the day also forms part of the cache key."""
    response = requests.get(
        "https://fred.stlouisfed.org/graph/fredgraph.csv",
        params={"id": series_id}, timeout=45,
    )
    response.raise_for_status()
    return parse_csv(response.text)


@st.cache_data(ttl=3600, show_spinner=False)
def download_as_known(series_id, as_known_on):
    """Download the historical vintage, rather than truncate today's history."""
    response = requests.get(
        "https://alfred.stlouisfed.org/graph/alfredgraph.csv",
        params={"id": series_id, "vintage_date": as_known_on.isoformat()},
        timeout=45,
    )
    response.raise_for_status()
    vintage = parse_csv(response.text)
    # Additional guard: an observation after the vintage date is ineligible.
    return vintage.loc[vintage.index <= pd.Timestamp(as_known_on)]


def compare(series_id, current, vintage):
    """Compare nonmissing observations across the full downloaded histories."""
    current_valid, vintage_valid = current.dropna(), vintage.dropna()
    old_date = vintage_valid.index[-1] if not vintage_valid.empty else None
    new_date = current_valid.index[-1] if not current_valid.empty else None
    common = pd.concat(
        [vintage_valid.rename("then"), current_valid.rename("now")], axis=1,
        join="inner",
    ).dropna()
    revised = int(((common["then"] - common["now"]).abs() > 1e-9).sum())
    return {
        "Series": f"https://fred.stlouisfed.org/series/{series_id}",
        "Last date known then": old_date,
        "Value known then": float(vintage_valid.iloc[-1]) if old_date is not None else None,
        "Last date today": new_date,
        "Value today": float(current_valid.iloc[-1]) if new_date is not None else None,
        "Later observations today": int((current_valid.index > old_date).sum()) if old_date is not None else None,
        "Revised common observations": revised,
    }


def main():
    st.set_page_config(page_title="Interest rates: as known then", layout="wide")
    today = date.today()
    st.title("Interest rates: as known then")
    st.caption(
        f"Data from FRED and ALFRED, Federal Reserve Bank of St. Louis, downloaded today "
        f"({today.isoformat()}); built with AI help, a learning demonstration, not investment advice."
    )
    selected = st.sidebar.multiselect(
        "Series", list(SERIES), default=list(SERIES),
        format_func=lambda item: f"{item} — {SERIES[item]}",
    )
    extra = st.sidebar.text_input("Add another FRED series ID", placeholder="DGS10 or PAYEMS").strip().upper()
    start = st.sidebar.date_input("Chart start date", date(2020, 1, 1))
    as_known = st.sidebar.date_input("As known on", today, max_value=today)
    if extra:
        if re.fullmatch(r"[A-Z0-9_]+", extra):
            selected = list(dict.fromkeys([*selected, extra]))
        else:
            st.sidebar.error("Enter one series ID using letters, numbers or underscores.")
    if st.sidebar.button("Refresh downloads"):
        st.cache_data.clear()
        st.rerun()
    st.write(f"Historical vintage: **{as_known.isoformat()}**")
    st.caption("Charts use today's history. Table counts use full histories, independent of the chart start date. Missing days are not filled. Cached downloads refresh within one hour.")
    rows = []
    for series_id in selected:
        st.subheader(f"{series_id} — {SERIES.get(series_id, 'Additional FRED series')}")
        try:
            current = download_today(series_id, today)
            vintage = download_as_known(series_id, as_known)
            if current.dropna().empty:
                raise ValueError("No nonmissing observations returned.")
            row = compare(series_id, current, vintage)
            if (row["Last date known then"] is not None
                    and row["Last date today"] is not None
                    and row["Last date known then"] > row["Last date today"]):
                st.warning("ALFRED's selected vintage extends beyond the current FRED download. The endpoints may update at different times; refresh before drawing a timing conclusion.")
            st.line_chart(current.loc[current.index >= pd.Timestamp(start)].to_frame(), y_label="Series native units")
            last = row["Last date known then"]
            st.caption(f"Last observation known on {as_known}: {last.date() if last is not None else 'none'}")
            rows.append(row)
        except (requests.RequestException, ValueError, pd.errors.ParserError) as exc:
            st.error(f"{series_id}: {exc}")
    st.subheader("As-known comparison")
    if rows:
        st.dataframe(
            pd.DataFrame(rows), hide_index=True, width="stretch",
            column_config={
                "Series": st.column_config.LinkColumn("Series", display_text=r"https://fred\.stlouisfed\.org/series/(.*)"),
                "Last date known then": st.column_config.DateColumn(format="YYYY-MM-DD"),
                "Last date today": st.column_config.DateColumn(format="YYYY-MM-DD"),
                "Value known then": st.column_config.NumberColumn(format="%.3f"),
                "Value today": st.column_config.NumberColumn(format="%.3f"),
            },
        )
    else:
        st.info("Select a valid series to populate the comparison.")
    st.caption("Later observations counts nonmissing values after the last observation available then. Revised counts compare nonmissing values on matching dates. An as-of date is not an intraday release timestamp.")


if __name__ == "__main__":
    main()
