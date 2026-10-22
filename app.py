"""Lab 15 interface: all estimation and portfolio math lives in portfolio.py."""
import io
from pathlib import Path
import streamlit as st
import portfolio as p

st.set_page_config(page_title="Lowest-risk mandate mix", layout="wide")
st.title("Lowest-risk mandate mix")
st.caption("Built with AI help, a learning demonstration, not investment advice.")

mode = st.sidebar.selectbox("Mandate", ["Meridian training", "Project 2: VOO / QQQ / VB / emerging markets"])
personal = mode.startswith("Project 2")
objective = st.sidebar.number_input("Expected-return objective (%)", value=7.0 if personal else 6.5,
                                    step=0.1, key=f"objective-{personal}") / 100
minimum = st.sidebar.number_input("Reserve minimum (%)", min_value=0.0,
                                  max_value=100.0, value=0.0 if personal else 3.0,
                                  step=1.0, key=f"minimum-{personal}") / 100
upload = st.sidebar.file_uploader("Upload prices.csv (monthly Adj Close)", type=["csv"])
last_36 = st.sidebar.checkbox("Use only the last 36 monthly returns")

try:
    minimum_weights, maximum_weights = {}, {}
    if personal:
        st.info("Project 2 mandate: VOO at least 40%; VB at most 30%; emerging-markets "
                "fund at most 30%; expected return at least 7% by default. No reserve minimum stated.")
        if upload is None and not Path(__file__).with_name('prices.csv').exists():
            st.info("Upload your five-year prices.csv for VOO, QQQ, VB and the selected emerging-markets ETF.")
            st.stop()
    if upload is None and not personal:
        loaded, loaded_correlations = p.SLEEVES, p.CORRELATIONS
        current, correlations = loaded, loaded_correlations
        identity = "meridian"
        st.write("Meridian: course-authored training estimates.")
        if last_36:
            st.info("The 36-month switch applies to uploaded prices. Meridian has fixed inputs.")
    else:
        raw = upload.getvalue() if upload is not None else Path(__file__).with_name('prices.csv').read_bytes()
        import hashlib
        identity = hashlib.sha256(raw).hexdigest()
        loaded, loaded_correlations = p.estimate_from_csv(io.BytesIO(raw))
        current, correlations = p.estimate_from_csv(io.BytesIO(raw), last_36)
        if personal:
            if set(loaded) != {"VOO", "QQQ", "VB", "EEM"}:
                raise ValueError("Project 2 CSV must contain VOO, QQQ, VB and EEM.")
            minimum_weights = {"VOO": .40}
            maximum_weights = {"VB": .30, "EEM": .30}
        st.write("Historical arithmetic return estimates: monthly mean × 12; "
                 "sample volatility × √12. History is not a forecast.")
        st.caption("Upload five years of monthly adjusted closes. The engine checks at least "
                   "37 consecutive prices; verify five-year coverage and source dates in your notes.")

    st.subheader("Return estimates and reserve eligibility")
    edited = {}
    eligible = set()
    for name, (estimate, volatility) in current.items():
        left, right = st.columns([3, 1])
        # Window-specific keys reset edits to the estimates for the selected window.
        value = left.number_input(f"{name} expected return (%)", value=estimate * 100,
                                  step=0.1, key=f"return-{identity}-{last_36}-{name}")
        edited[name] = (value / 100, volatility)
        if right.checkbox(f"{name}: reserve-eligible", value=(not personal and upload is None and name in p.RESERVE_ELIGIBLE),
                          key=f"reserve-{identity}-{name}"):
            eligible.add(name)

    answer = p.search_mix(edited, correlations, objective, minimum, eligible,
                          minimum_weights, maximum_weights)
    baseline = p.search_mix(loaded, loaded_correlations, objective, minimum, eligible,
                            minimum_weights, maximum_weights)

    def display_result(title, result):
        st.subheader(title)
        if result is None:
            st.write("no mix meets the objective")
            return
        st.dataframe([{"Asset": name, "Weight (%)": f"{weight * 100:.2f}"}
                      for name, weight in zip(loaded, result["weights"])],
                     hide_index=True, width="stretch")
        st.write(f"Expected return: {result['return']:.2%}")
        st.write(f"Volatility: {result['volatility']:.2%}")
        st.write(f"Reserve-eligible weight: {result['reserve']:.2%}")

    left, right = st.columns(2)
    with left:
        display_result("Current inputs", answer)
    with right:
        display_result("As loaded (all months for CSV)", baseline)
    if answer is not None and baseline is not None:
        largest = max(abs(a - b) for a, b in zip(answer["weights"], baseline["weights"])) * 100
        st.metric("Largest weight change (percentage points)", f"{largest:.2f}")
    else:
        st.caption("Largest weight change unavailable: both runs must have a feasible mix.")
    st.caption("Fully invested, long-only search in 5 percentage point steps. Both columns use "
               "the current objective and reserve rule. Lowest risk refers to estimated volatility "
               "on this grid; other mandate constraints require separate checks.")
except (ValueError, TypeError, KeyError) as error:
    st.error(f"Cannot calculate: {error}")
