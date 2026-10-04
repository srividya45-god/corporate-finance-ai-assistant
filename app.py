import streamlit as st
import anthropic
st.set_page_config(
    page_title="Corporate Finance AI Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Corporate Finance AI Assistant")
st.write(
    "A GenAI-based application for financial analysis, "
    "WACC, capital budgeting and financial interpretation."
)

st.info(
    "⚠️ Privacy Notice: Please do not upload confidential company information. "
    "Use anonymized or sample financial data."
)

st.sidebar.header("📌 Navigation")

module = st.sidebar.radio(
    "Select a module:",
    [
        "Home",
        "Ratio Analysis",
        "WACC Calculator",
        "Capital Budgeting",
        "AI Assistant"
    ]
)


# ---------------- HOME ----------------

if module == "Home":

    st.header("Welcome!")

    st.write("""
    This Corporate Finance AI Assistant helps users analyse
    financial information and understand the results in simple language.
    """)

    st.subheader("Main Features")

    col1, col2 = st.columns(2)

    with col1:
        st.write("📊 **Ratio Analysis**")
        st.write("Calculate profitability, liquidity and leverage ratios.")

        st.write("💰 **WACC Calculator**")
        st.write("Calculate the Weighted Average Cost of Capital.")

    with col2:
        st.write("📈 **Capital Budgeting**")
        st.write("Calculate NPV, IRR and Payback Period.")

        st.write("🤖 **AI Assistant**")
        st.write("Get simple explanations of financial results.")


# ---------------- RATIO ANALYSIS ----------------

elif module == "Ratio Analysis":

    st.header("📊 Ratio Analysis")

    revenue = st.number_input(
        "Revenue",
        min_value=0.0,
        value=1000.0
    )

    net_profit = st.number_input(
        "Net Profit",
        min_value=0.0,
        value=100.0
    )

    current_assets = st.number_input(
        "Current Assets",
        min_value=0.0,
        value=500.0
    )

    current_liabilities = st.number_input(
        "Current Liabilities",
        min_value=0.0,
        value=300.0
    )

    debt = st.number_input(
        "Total Debt",
        min_value=0.0,
        value=400.0
    )

    equity = st.number_input(
        "Shareholders' Equity",
        min_value=0.0,
        value=500.0
    )

    if st.button("Calculate Ratios"):

        if revenue > 0:
            net_margin = (net_profit / revenue) * 100
        else:
            net_margin = 0

        if current_liabilities > 0:
            current_ratio = current_assets / current_liabilities
        else:
            current_ratio = 0

        if equity > 0:
            debt_equity = debt / equity
        else:
            debt_equity = 0

        st.subheader("Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Net Profit Margin",
                f"{net_margin:.2f}%"
            )

        with col2:
            st.metric(
                "Current Ratio",
                f"{current_ratio:.2f}"
            )

        with col3:
            st.metric(
                "Debt-Equity Ratio",
                f"{debt_equity:.2f}"
            )

        st.success("Ratio calculation completed successfully.")



# ---------------- WACC ----------------

elif module == "WACC Calculator":

    st.header("💰 WACC Calculator")

    st.write(
        "Enter the capital structure and cost of each source of finance."
    )

    equity_weight = st.number_input(
        "Equity Weight (%)",
        min_value=0.0,
        value=55.0
    )

    equity_cost = st.number_input(
        "Cost of Equity (%)",
        min_value=0.0,
        value=14.0
    )

    debt_weight = st.number_input(
        "Debt Weight (%)",
        min_value=0.0,
        value=35.0
    )

    debt_cost = st.number_input(
        "Pre-tax Cost of Debt (%)",
        min_value=0.0,
        value=9.0
    )

    preference_weight = st.number_input(
        "Preference Capital Weight (%)",
        min_value=0.0,
        value=10.0
    )

    preference_cost = st.number_input(
        "Cost of Preference Capital (%)",
        min_value=0.0,
        value=10.0
    )

    tax_rate = st.number_input(
        "Tax Rate (%)",
        min_value=0.0,
        value=25.0
    )

    if st.button("Calculate WACC"):

        total_weight = (
            equity_weight
            + debt_weight
            + preference_weight
        )

        if total_weight != 100:

            st.warning(
                f"Your weights currently total "
                f"{total_weight:.2f}%. "
                "For a standard WACC calculation, "
                "they should total 100%."
            )

        else:

            e = equity_weight / 100
            d = debt_weight / 100
            p = preference_weight / 100

            ke = equity_cost / 100
            kd = debt_cost / 100
            kp = preference_cost / 100

            tax = tax_rate / 100

            wacc = (
                e * ke
                + d * kd * (1 - tax)
                + p * kp
            ) * 100

            st.metric(
                "WACC",
                f"{wacc:.2f}%"
            )

            st.success("WACC calculated successfully.")


# ---------------- CAPITAL BUDGETING ----------------

elif module == "Capital Budgeting":

    st.header("📈 Capital Budgeting")

    initial_investment = st.number_input(
        "Initial Investment",
        min_value=0.0,
        value=500.0
    )

    discount_rate = st.number_input(
        "Discount Rate / WACC (%)",
        min_value=0.0,
        value=11.06
    )

    st.subheader("Annual Cash Flows")

    cf1 = st.number_input(
        "Year 1 Cash Flow",
        value=120.0
    )

    cf2 = st.number_input(
        "Year 2 Cash Flow",
        value=150.0
    )

    cf3 = st.number_input(
        "Year 3 Cash Flow",
        value=180.0
    )

    cf4 = st.number_input(
        "Year 4 Cash Flow",
        value=200.0
    )

    cf5 = st.number_input(
        "Year 5 Cash Flow",
        value=220.0
    )


    if st.button("Calculate Project"):

        rate = discount_rate / 100

        cash_flows = [
            cf1,
            cf2,
            cf3,
            cf4,
            cf5
        ]


        # ---------- NPV ----------

        npv = -initial_investment

        for year, cash_flow in enumerate(
            cash_flows,
            start=1
        ):

            npv += (
                cash_flow
                / ((1 + rate) ** year)
            )


        # ---------- PAYBACK ----------

        cumulative = 0
        payback = None

        for year, cash_flow in enumerate(
            cash_flows,
            start=1
        ):

            previous = cumulative

            cumulative += cash_flow

            if cumulative >= initial_investment:

                remaining = (
                    initial_investment
                    - previous
                )

                if cash_flow != 0:
                    fraction = (
                        remaining / cash_flow
                    )
                else:
                    fraction = 0

                payback = (
                    year - 1
                ) + fraction

                break


        # ---------- IRR ----------

        def calculate_irr(investment, flows):

            def calculate_npv(rate):

                value = -investment

                for year, cash_flow in enumerate(
                    flows,
                    start=1
                ):

                    value += (
                        cash_flow
                        / ((1 + rate) ** year)
                    )

                return value


            low = -0.9999
            high = 1.0

            low_npv = calculate_npv(low)
            high_npv = calculate_npv(high)


            # Expand the upper limit if necessary

            attempts = 0

            while (
                low_npv * high_npv > 0
                and attempts < 20
            ):

                high = high * 2

                high_npv = calculate_npv(high)

                attempts += 1


            # No IRR found

            if low_npv * high_npv > 0:
                return None


            # Bisection method

            for _ in range(100):

                middle = (
                    low + high
                ) / 2

                middle_npv = calculate_npv(
                    middle
                )

                if abs(middle_npv) < 0.000001:

                    return middle * 100


                if low_npv * middle_npv <= 0:

                    high = middle
                    high_npv = middle_npv

                else:

                    low = middle
                    low_npv = middle_npv


            return middle * 100


        irr = calculate_irr(
            initial_investment,
            cash_flows
        )


        # ---------- DISPLAY RESULTS ----------

        st.subheader("Results")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "NPV",
                f"₹ {npv:.2f}"
            )

        with col2:

            if irr is not None:

                st.metric(
                    "IRR",
                    f"{irr:.2f}%"
                )

            else:

                st.metric(
                    "IRR",
                    "Not found"
                )

        with col3:

            if payback is not None:

                st.metric(
                    "Payback Period",
                    f"{payback:.2f} years"
                )

            else:

                st.metric(
                    "Payback Period",
                    "Not recovered"
                )


        # ---------- NPV COMMENT ----------

        if npv > 0:

            st.success(
                "Based on NPV, the project has a positive NPV."
            )

        elif npv < 0:

            st.error(
                "Based on NPV, the project has a negative NPV."
            )

        else:

            st.info(
                "The project has an NPV of zero."
            )


# ---------------- AI ASSISTANT ----------------

elif module == "AI Assistant":

    st.header("🤖 Corporate Finance AI Assistant")

    st.write(
        "Ask questions about corporate finance concepts "
        "and financial analysis."
    )

question = st.text_area(
        "Enter your question:"
    )

    if st.button("Submit Question"):
        if question.strip():
            try:
                client = anthropic.Anthropic(
                    api_key=st.secrets["ANTHROPIC_API_KEY"]
                )

                response = client.messages.create(
                    model="claude-3-5-haiku-latest",
                    max_tokens=500,
                    messages=[
                        {
                            "role": "user",
                            "content": question
                        }
                    ]
                )

                st.subheader("AI Response")
                st.write(response.content[0].text)

            except Exception as e:
                st.error(f"AI connection error: {e}")

        else:
            st.warning(
                "Please enter a question first."
    )


# ---------------- SIDEBAR FOOTER ----------------

st.sidebar.markdown("---")

st.sidebar.caption(
    "Corporate Finance AI Assistant | MBA Finance Project"
)
