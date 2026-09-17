import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Banking & FinTech Analytics",
    page_icon="🏦",
    layout="wide"
)

# ============================================================
# LOAD CLEANED AND TRANSFORMED DATA
# ============================================================

customers = pd.read_csv(
    "outputs/cleaned_data/customers_clean.csv"
)

accounts = pd.read_csv(
    "outputs/cleaned_data/accounts_clean.csv"
)

cards = pd.read_csv(
    "outputs/cleaned_data/cards_clean.csv"
)

complaints = pd.read_csv(
    "outputs/cleaned_data/complaints_clean.csv"
)

fraud_cases = pd.read_csv(
    "outputs/cleaned_data/fraud_cases_clean.csv"
)

loans = pd.read_csv(
    "outputs/cleaned_data/loans_clean.csv"
)

transactions = pd.read_csv(
    "outputs/cleaned_data/transactions_clean.csv"
)

# ============================================================
# TITLE
# ============================================================

#st.title("🏦 Banking & FinTech Analytics Dashboard")

#st.markdown(
 #   "Interactive analytics covering customers, accounts, loans, "
  #  "transactions, fraud, and customer service."
#)
# ============================================================
# TITLE & PROJECT SUMMARY
# ============================================================
# ============================================================
# TITLE & PROJECT SUMMARY
# ============================================================
# ============================================================
# TITLE & PROJECT SUMMARY
# ============================================================

st.markdown(
    "<h1 style='text-align:center; font-size:34px; font-weight:700; margin-bottom:10px;'>"
    "🏦 Banking & FinTech Analytics Dashboard"
    "</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; font-size:20px; max-width:850px; margin:auto; line-height:1.6;'>"
    "An interactive data analytics dashboard designed to explore "
    "customer profiles, accounts, loans, transactions, fraud risk, "
    "and customer service performance using banking and FinTech data."
    "</p>",
    unsafe_allow_html=True
)

st.markdown("<div style='height:18px;'></div>", unsafe_allow_html=True)
# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.header("🔎 Dashboard Filters")

# -------------------- Transaction Year --------------------

years = sorted(
    transactions["Year"].dropna().unique()
)

selected_year = st.sidebar.selectbox(
    "Transaction Year",
    ["All"] + [int(year) for year in years]
)

# -------------------- City --------------------

cities = sorted(
    customers["City"].dropna().unique()
)

selected_city = st.sidebar.selectbox(
    "City",
    ["All"] + list(cities)
)

# -------------------- Occupation --------------------

occupations = sorted(
    customers["Occupation"].dropna().unique()
)

selected_occupation = st.sidebar.selectbox(
    "Occupation",
    ["All"] + list(occupations)
)

# -------------------- Account Type --------------------

account_types = sorted(
    accounts["Account_Type"].dropna().unique()
)

selected_account_type = st.sidebar.selectbox(
    "Account Type",
    ["All"] + list(account_types)
)

# -------------------- Loan Type --------------------

loan_types = sorted(
    loans["Loan_Type"].dropna().unique()
)

selected_loan_type = st.sidebar.selectbox(
    "Loan Type",
    ["All"] + list(loan_types)
)

# -------------------- Loan Status --------------------

loan_statuses = sorted(
    loans["Status"].dropna().unique()
)

selected_loan_status = st.sidebar.selectbox(
    "Loan Status",
    ["All"] + list(loan_statuses)
)

# -------------------- Transaction Type --------------------

transaction_types = sorted(
    transactions["Type"].dropna().unique()
)

selected_transaction_type = st.sidebar.selectbox(
    "Transaction Type",
    ["All"] + list(transaction_types)
)

# -------------------- Transaction Channel --------------------

channels = sorted(
    transactions["Channel"].dropna().unique()
)

selected_channel = st.sidebar.selectbox(
    "Transaction Channel",
    ["All"] + list(channels)
)

# -------------------- Debit / Credit --------------------

debit_credit_values = sorted(
    transactions["Debit_Credit"].dropna().unique()
)

selected_debit_credit = st.sidebar.selectbox(
    "Debit / Credit",
    ["All"] + list(debit_credit_values)
)


# SIDEBAR INFORMATION


st.sidebar.markdown("---")

st.sidebar.info(
    "Select multiple filters together. "
    "All dashboard KPIs will update based on the combined selection."
)


# STEP 1 — FILTER CUSTOMERS


filtered_customers = customers.copy()

if selected_city != "All":
    filtered_customers = filtered_customers[
        filtered_customers["City"] == selected_city
    ]

if selected_occupation != "All":
    filtered_customers = filtered_customers[
        filtered_customers["Occupation"] == selected_occupation
    ]

# Customer IDs after City + Occupation filtering

customer_ids_from_customer_filters = set(
    filtered_customers["Customer_ID"]
)

# ============================================================
# STEP 2 — FILTER ACCOUNTS
# ============================================================

filtered_accounts = accounts[
    accounts["Customer_ID"].isin(
        customer_ids_from_customer_filters
    )
].copy()

if selected_account_type != "All":
    filtered_accounts = filtered_accounts[
        filtered_accounts["Account_Type"] == selected_account_type
    ]

# Account IDs after account filters

account_ids_from_account_filters = set(
    filtered_accounts["Account_ID"]
)

# Customer IDs connected to these accounts

customer_ids_from_accounts = set(
    filtered_accounts["Customer_ID"]
)

# ============================================================
# STEP 3 — FILTER TRANSACTIONS
# ============================================================

filtered_transactions = transactions[
    transactions["Account_ID"].isin(
        account_ids_from_account_filters
    )
].copy()

if selected_year != "All":
    filtered_transactions = filtered_transactions[
        filtered_transactions["Year"] == selected_year
    ]

if selected_transaction_type != "All":
    filtered_transactions = filtered_transactions[
        filtered_transactions["Type"] == selected_transaction_type
    ]

if selected_channel != "All":
    filtered_transactions = filtered_transactions[
        filtered_transactions["Channel"] == selected_channel
    ]

if selected_debit_credit != "All":
    filtered_transactions = filtered_transactions[
        filtered_transactions["Debit_Credit"] == selected_debit_credit
    ]

# Account IDs having transactions after ALL transaction filters

customer_ids_from_transactions = set(
    filtered_transactions["Account_ID"]
)

# Convert transaction Account IDs into Customer IDs

transaction_customer_ids = set(
    accounts.loc[
        accounts["Account_ID"].isin(
            customer_ids_from_transactions
        ),
        "Customer_ID"
    ]
)

# ============================================================
# STEP 4 — FILTER LOANS
# ============================================================

filtered_loans = loans[
    loans["Customer_ID"].isin(
        customer_ids_from_customer_filters
    )
].copy()

if selected_loan_type != "All":
    filtered_loans = filtered_loans[
        filtered_loans["Loan_Type"] == selected_loan_type
    ]

if selected_loan_status != "All":
    filtered_loans = filtered_loans[
        filtered_loans["Status"] == selected_loan_status
    ]

# Customer IDs having loans after ALL loan filters

loan_customer_ids = set(
    filtered_loans["Customer_ID"]
)

# ============================================================
# STEP 5 — CREATE ONE COMBINED CUSTOMER POPULATION
# ============================================================

combined_customer_ids = customer_ids_from_customer_filters.copy()

# Account filter affects customer population

if selected_account_type != "All":
    combined_customer_ids = (
        combined_customer_ids
        & customer_ids_from_accounts
    )

# Transaction filters affect customer population

if (
    selected_year != "All"
    or selected_transaction_type != "All"
    or selected_channel != "All"
    or selected_debit_credit != "All"
):
    combined_customer_ids = (
        combined_customer_ids
        & transaction_customer_ids
    )

# Loan filters affect customer population

if (
    selected_loan_type != "All"
    or selected_loan_status != "All"
):
    combined_customer_ids = (
        combined_customer_ids
        & loan_customer_ids
    )

# ============================================================
# STEP 6 — FINAL CUSTOMER DATA
# ============================================================

filtered_customers = customers[
    customers["Customer_ID"].isin(
        combined_customer_ids
    )
].copy()

# ============================================================
# STEP 7 — FINAL ACCOUNT DATA
# ============================================================

filtered_accounts = accounts[
    accounts["Customer_ID"].isin(
        combined_customer_ids
    )
].copy()

if selected_account_type != "All":
    filtered_accounts = filtered_accounts[
        filtered_accounts["Account_Type"] == selected_account_type
    ]

# If transaction filters are selected,
# keep only accounts having matching transactions.

if (
    selected_year != "All"
    or selected_transaction_type != "All"
    or selected_channel != "All"
    or selected_debit_credit != "All"
):
    filtered_accounts = filtered_accounts[
        filtered_accounts["Account_ID"].isin(
            filtered_transactions["Account_ID"]
        )
    ]

# ============================================================
# STEP 8 — FINAL LOAN DATA
# ============================================================

filtered_loans = loans[
    loans["Customer_ID"].isin(
        combined_customer_ids
    )
].copy()

if selected_loan_type != "All":
    filtered_loans = filtered_loans[
        filtered_loans["Loan_Type"] == selected_loan_type
    ]

if selected_loan_status != "All":
    filtered_loans = filtered_loans[
        filtered_loans["Status"] == selected_loan_status
    ]

# ============================================================
# STEP 9 — FINAL TRANSACTION DATA
# ============================================================

filtered_transactions = transactions[
    transactions["Account_ID"].isin(
        filtered_accounts["Account_ID"]
    )
].copy()

if selected_year != "All":
    filtered_transactions = filtered_transactions[
        filtered_transactions["Year"] == selected_year
    ]

if selected_transaction_type != "All":
    filtered_transactions = filtered_transactions[
        filtered_transactions["Type"] == selected_transaction_type
    ]

if selected_channel != "All":
    filtered_transactions = filtered_transactions[
        filtered_transactions["Channel"] == selected_channel
    ]

if selected_debit_credit != "All":
    filtered_transactions = filtered_transactions[
        filtered_transactions["Debit_Credit"] == selected_debit_credit
    ]

# ============================================================
# STEP 10 — FRAUD DATA CONNECTED TO FILTERED TRANSACTIONS
# ============================================================

filtered_transaction_ids = set(
    filtered_transactions["Transaction_ID"]
)

filtered_fraud_cases = fraud_cases[
    fraud_cases["Transaction_ID"].isin(
        filtered_transaction_ids
    )
].copy()

# ============================================================
# OVERVIEW / KPI CARDS
# ============================================================

st.header("📊 Overview / KPIs")

# ============================================================
# KPI CALCULATIONS
# ============================================================

# -------------------- Customers --------------------

total_customers = len(
    filtered_customers
)

# -------------------- Accounts --------------------

total_accounts = len(
    filtered_accounts
)

# -------------------- Active Accounts --------------------

active_accounts = (
    filtered_accounts["Status"] == "Active"
).sum()

# -------------------- Loans --------------------

total_loans = len(
    filtered_loans
)

# -------------------- Total Loan Amount --------------------

total_loan_amount = filtered_loans[
    "Loan_Amount"
].sum()

# -------------------- Transactions --------------------

total_transactions = len(
    filtered_transactions
)

# -------------------- Loan Default Rate --------------------

if len(filtered_loans) > 0:

    loan_default_rate = (
        (
            filtered_loans["Status"] == "Defaulted"
        ).mean()
        * 100
    )

else:

    loan_default_rate = 0

# -------------------- Fraud Flag Rate --------------------

if len(filtered_fraud_cases) > 0:

    fraud_flag_rate = (
        filtered_fraud_cases["Fraud_Flag"].mean()
        * 100
    )

else:

    fraud_flag_rate = 0

# ============================================================
# KPI CARD STYLING
# ============================================================

st.markdown(
    """
    <style>

    div[data-testid="stMetric"] {

        border: 1.5px solid #0B3D91;

        border-radius: 8px;

        padding: 9px 11px;

        background-color: white;

        box-shadow:
            0 1px 4px rgba(0, 0, 0, 0.08);

        min-height: 78px;

    }

    div[data-testid="stMetricLabel"] {

        font-size: 12px;

        font-weight: 600;

    }

    div[data-testid="stMetricValue"] {

        font-size: 21px;

        font-weight: 700;

    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# FIRST ROW — KPI CARDS
# ============================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        label="👥 Total Customers",
        value=f"{total_customers:,}"
    )

with col2:

    st.metric(
        label="🏦 Total Accounts",
        value=f"{total_accounts:,}"
    )

with col3:

    st.metric(
        label="✅ Active Accounts",
        value=f"{active_accounts:,}"
    )

with col4:

    st.metric(
        label="💰 Total Loans",
        value=f"{total_loans:,}"
    )

# Small spacing

st.markdown(
    "<div style='height:7px'></div>",
    unsafe_allow_html=True
)

# ============================================================
# SECOND ROW — KPI CARDS
# ============================================================

col5, col6, col7, col8 = st.columns(4)

with col5:

    st.metric(
        label="💵 Total Loan Amount",
        value=f"₹{total_loan_amount / 1e9:.2f}B"
    )

with col6:

    st.metric(
        label="💳 Total Transactions",
        value=f"{total_transactions:,}"
    )

with col7:

    st.metric(
        label="⚠️ Loan Default Rate",
        value=f"{loan_default_rate:.2f}%"
    )

with col8:

    st.metric(
        label="🛡️ Fraud Flag Rate",
        value=f"{fraud_flag_rate:.2f}%"
    )

st.markdown("---")
# ============================================================
# DESCRIPTIVE STATISTICS
# ============================================================

st.header("📈 Descriptive Statistics")

st.markdown(
    "Summary statistics for the selected data. "
    "The statistics update automatically according to the "
    "filters selected in the sidebar."
)

# ============================================================
# DATASET SELECTION
# ============================================================

stats_dataset = st.selectbox(
    "Select Dataset",
    [
        "Customers",
        "Accounts",
        "Loans",
        "Transactions",
        "Complaints",
        "Fraud Cases"
    ]
)

# ============================================================
# SELECT DATA BASED ON DATASET
# ============================================================

if stats_dataset == "Customers":

    stats_data = filtered_customers[
        [
            "Age",
            "Annual_Income",
            "Credit_Score",
            "Total_Balance",
            "Total_Accounts"
        ]
    ].copy()

    stats_data = stats_data.rename(
        columns={
            "Age": "Age",
            "Annual_Income": "Annual Income",
            "Credit_Score": "Credit Score",
            "Total_Balance": "Customer Balance",
            "Total_Accounts": "Total Accounts"
        }
    )


elif stats_dataset == "Accounts":

    stats_data = filtered_accounts[
        [
            "Balance"
        ]
    ].copy()

    stats_data = stats_data.rename(
        columns={
            "Balance": "Account Balance"
        }
    )


elif stats_dataset == "Loans":

    stats_data = filtered_loans[
        [
            "Loan_Amount",
            "Interest_Rate",
            "Tenure_Months",
            "Estimated_Interest"
        ]
    ].copy()

    stats_data = stats_data.rename(
        columns={
            "Loan_Amount": "Loan Amount",
            "Interest_Rate": "Interest Rate",
            "Tenure_Months": "Tenure (Months)",
            "Estimated_Interest": "Estimated Interest"
        }
    )


elif stats_dataset == "Transactions":

    stats_data = filtered_transactions[
        [
            "Amount",
            "Net_Amount"
        ]
    ].copy()

    stats_data = stats_data.rename(
        columns={
            "Amount": "Transaction Amount",
            "Net_Amount": "Net Amount"
        }
    )


elif stats_dataset == "Complaints":

    stats_data = complaints[
        [
            "Resolution_Days",
            "Satisfaction"
        ]
    ].copy()

    stats_data = stats_data.rename(
        columns={
            "Resolution_Days": "Resolution Days",
            "Satisfaction": "Satisfaction"
        }
    )


elif stats_dataset == "Fraud Cases":

    stats_data = filtered_fraud_cases[
        [
            "Risk_Score",
            "Fraud_Flag"
        ]
    ].copy()

    stats_data = stats_data.rename(
        columns={
            "Risk_Score": "Risk Score",
            "Fraud_Flag": "Fraud Flag"
        }
    )

# ============================================================
# CALCULATE DESCRIPTIVE STATISTICS
# ============================================================

if stats_data.empty:

    st.warning(
        "No data is available for the selected filters."
    )

else:

    descriptive_stats = (
        stats_data
        .describe()
        .T
        .reset_index()
    )

    descriptive_stats = descriptive_stats.rename(
        columns={
            "index": "Variable",
            "count": "Count",
            "mean": "Mean",
            "std": "Standard Deviation",
            "min": "Minimum",
            "25%": "Q1 (25%)",
            "50%": "Median",
            "75%": "Q3 (75%)",
            "max": "Maximum"
        }
    )

    # Round numerical values
    descriptive_stats[
        [
            "Count",
            "Mean",
            "Standard Deviation",
            "Minimum",
            "Q1 (25%)",
            "Median",
            "Q3 (75%)",
            "Maximum"
        ]
    ] = descriptive_stats[
        [
            "Count",
            "Mean",
            "Standard Deviation",
            "Minimum",
            "Q1 (25%)",
            "Median",
            "Q3 (75%)",
            "Maximum"
        ]
    ].round(2)

    # ========================================================
    # DISPLAY TABLE
    # ========================================================

    st.dataframe(
        descriptive_stats,
        use_container_width=True,
        hide_index=True
    )

# ============================================================
# STATISTICS EXPLANATION
# ============================================================

with st.expander("ℹ️ What do these statistics mean?"):

    st.markdown(
        """
        **Count** — Number of observations.

        **Mean** — Average value.

        **Median** — Middle value after sorting the data.

        **Standard Deviation** — Measures how spread out the
        values are around the mean.

        **Minimum** — Smallest observed value.

        **Q1 (25%)** — 25% of observations are below this value.

        **Q3 (75%)** — 75% of observations are below this value.

        **Maximum** — Largest observed value.
        """
    )

# ============================================================
# DASHBOARD SECTIONS
# ============================================================

# ============================================================
# CUSTOMER ANALYTICS
# CHART 7.1 — AVERAGE CUSTOMER BALANCE BY OCCUPATION
# ============================================================

st.header("👥 Customer Analytics")


# Create occupation summary from filtered customer data
occupation_balance = (
    filtered_customers
    .groupby("Occupation", as_index=False)["Total_Balance"]
    .mean()
    .sort_values("Total_Balance", ascending=True)
)

# Check whether data is available
if occupation_balance.empty:

    st.warning(
        "No customer data is available for the selected filters."
    )

else:

    # --------------------------------------------------------
    # CREATE BLUE SHADES
    # Lowest value = light blue
    # Highest value = dark blue
    # --------------------------------------------------------

    blue_shades = sns.color_palette(
        "Blues",
        n_colors=len(occupation_balance) + 2
    )[2:]

    # Reverse so lowest gets lightest and highest gets darkest
    blue_shades = blue_shades

    # --------------------------------------------------------
    # CREATE COMPACT CHART
    # --------------------------------------------------------

    fig, ax = plt.subplots(
        figsize=(5, 1.8)
    )

    bars = ax.barh(
        occupation_balance["Occupation"],
        occupation_balance["Total_Balance"],
        color=blue_shades,
        height=0.55
    )

    # --------------------------------------------------------
    # VALUE LABELS
    # --------------------------------------------------------

    for bar in bars:

        value = bar.get_width()

        ax.text(
            value + occupation_balance["Total_Balance"].max() * 0.01,
            bar.get_y() + bar.get_height() / 2,
            f"₹{value:,.0f}",
            va="center",
            ha="left",
            fontsize=4
        )

    # --------------------------------------------------------
    # TITLE
    # --------------------------------------------------------

    ax.set_title(
        "Average Customer Balance by Occupation",
        fontsize=7,
        fontweight="bold",
        pad=10
    )

    # --------------------------------------------------------
    # AXIS LABELS
    # --------------------------------------------------------

    ax.set_xlabel(
        "Average Customer Balance (₹)",
        fontsize=5
    )

    ax.set_ylabel(
        "",
        fontsize=5
    )

    # --------------------------------------------------------
    # TICK SIZE
    # --------------------------------------------------------

    ax.tick_params(
        axis="x",
        labelsize=5
    )

    ax.tick_params(
        axis="y",
        labelsize=5
    )

    # --------------------------------------------------------
    # GRID
    # --------------------------------------------------------

    ax.grid(
        axis="x",
        linestyle="--",
        alpha=0.20
    )

    # Keep grid behind bars
    ax.set_axisbelow(True)

    # --------------------------------------------------------
    # REMOVE EXTRA BORDERS
    # --------------------------------------------------------

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # --------------------------------------------------------
    # LAYOUT
    # --------------------------------------------------------

    plt.tight_layout()

    # Display chart
    st.pyplot(
        fig,
        use_container_width=False
    )

    plt.close(fig)

    # --------------------------------------------------------
# BUSINESS INSIGHT
# --------------------------------------------------------

highest_occupation = occupation_balance.iloc[-1]

st.markdown(
    f"""
    <div style="
        color: #003366;
        font-size: 18px;
        font-weight: 500;
        padding: 8px 0px;
    ">
        <b>Business insight:</b> {highest_occupation['Occupation']}
        customers have the highest average balance at
        ₹{highest_occupation['Total_Balance']:,.0f}
        within the selected filters.
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# CHART 7.4 — ANNUAL INCOME VS CUSTOMER BALANCE


# ------------------------------------------------------------
# Prepare filtered customer data
# ------------------------------------------------------------

income_balance_data = filtered_customers[
    [
        "Annual_Income",
        "Total_Balance",
        "Occupation"
    ]
].dropna().copy()

# ------------------------------------------------------------
# Check data availability
# ------------------------------------------------------------

if income_balance_data.empty:

    st.warning(
        "No customer data is available for the selected filters."
    )

else:

    # --------------------------------------------------------
    # Create compact scatter plot
    # --------------------------------------------------------

    fig, ax = plt.subplots(
        figsize=(8, 2.2)
    )

    # --------------------------------------------------------
    # Multicolor occupation groups
    # --------------------------------------------------------

    occupation_colors = {
        "Business": "royalblue",
        "Salaried": "seagreen",
        "Self Employed": "darkorange",
        "Student": "mediumpurple",
        "Retired": "crimson",
        "Undefined": "gray"
    }

    # --------------------------------------------------------
    # Plot each occupation
    # --------------------------------------------------------

    for occupation in income_balance_data["Occupation"].unique():

        occupation_data = income_balance_data[
            income_balance_data["Occupation"] == occupation
        ]

        ax.scatter(
            occupation_data["Annual_Income"],
            occupation_data["Total_Balance"],
            alpha=0.45,
            s=18,
            label=occupation,
            color=occupation_colors.get(
                occupation,
                "steelblue"
            )
        )

    # --------------------------------------------------------
    # Title
    # --------------------------------------------------------

    ax.set_title(
        "Annual Income vs Total Customer Balance",
        fontsize=8,
        fontweight="bold",
        pad=10
    )

    # --------------------------------------------------------
    # Axis labels
    # --------------------------------------------------------

    ax.set_xlabel(
        "Annual Income (₹)",
        fontsize=5
    )

    ax.set_ylabel(
        "Total Customer Balance (₹)",
        fontsize=5
    )

    # --------------------------------------------------------
    # Tick sizes
    # --------------------------------------------------------

    ax.tick_params(
        axis="both",
        labelsize=5
    )

    # --------------------------------------------------------
    # Grid
    # --------------------------------------------------------

    ax.grid(
        linestyle="--",
        alpha=0.20
    )

    ax.set_axisbelow(True)

    # --------------------------------------------------------
    # Legend
    # --------------------------------------------------------

    ax.legend(
        title="Occupation",
        fontsize=5,
        title_fontsize=6,
        loc="upper right"
    )

    # --------------------------------------------------------
    # Remove unnecessary borders
    # --------------------------------------------------------

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()

    # --------------------------------------------------------
    # Display chart
    # --------------------------------------------------------

    st.pyplot(
        fig,
        use_container_width=False
    )

    plt.close(fig)

# --------------------------------------------------------
# Business explanation
# --------------------------------------------------------

st.markdown(
    """
    <p style="color: #003366; font-size: 18px;">
    <b>Business insight:</b> This chart shows how annual income
    and customer balance are distributed across different
    occupational groups.<br> It describes the relationship in
    the filtered customer population and does not imply
    that income causes balance changes.
    </p>
    """,
    unsafe_allow_html=True
)

# ============================================================
# CHART 7.12 — CUSTOMER FINANCIAL PROFILE BY CITY
# ============================================================

#st.subheader("Customer Financial Profile by City")

# ------------------------------------------------------------
# CUSTOMER-LEVEL DATA
# ------------------------------------------------------------

customer_profile = filtered_customers[
    [
        "Customer_ID",
        "City",
        "Credit_Score"
    ]
].copy()

# ------------------------------------------------------------
# ACCOUNT BALANCE BY CUSTOMER
# Use filtered accounts so account filters are respected
# ------------------------------------------------------------

account_balance_summary = (
    filtered_accounts
    .groupby("Customer_ID", as_index=False)
    .agg(
        Customer_Balance=("Balance", "sum")
    )
)

# ------------------------------------------------------------
# LOAN EXPOSURE BY CUSTOMER
# Use filtered loans so loan filters are respected
# ------------------------------------------------------------

loan_exposure_summary = (
    filtered_loans
    .groupby("Customer_ID", as_index=False)
    .agg(
        Loan_Exposure=("Loan_Amount", "sum")
    )
)

# ------------------------------------------------------------
# MERGE CUSTOMER + ACCOUNT + LOAN INFORMATION
# ------------------------------------------------------------

customer_profile = customer_profile.merge(
    account_balance_summary,
    on="Customer_ID",
    how="left"
)

customer_profile = customer_profile.merge(
    loan_exposure_summary,
    on="Customer_ID",
    how="left"
)

# Customers without matching accounts/loans get zero exposure
customer_profile["Customer_Balance"] = (
    customer_profile["Customer_Balance"]
    .fillna(0)
)

customer_profile["Loan_Exposure"] = (
    customer_profile["Loan_Exposure"]
    .fillna(0)
)

# ------------------------------------------------------------
# CITY-LEVEL SUMMARY
# ------------------------------------------------------------

city_profile = (
    customer_profile
    .groupby("City", as_index=False)
    .agg(
        Avg_Customer_Balance=("Customer_Balance", "mean"),
        Avg_Loan_Exposure=("Loan_Exposure", "mean"),
        Avg_Credit_Score=("Credit_Score", "mean")
    )
)

# ------------------------------------------------------------
# CHECK DATA
# ------------------------------------------------------------

if city_profile.empty:

    st.warning(
        "No customer data is available for the selected filters."
    )

else:

    # --------------------------------------------------------
    # STANDARDIZE THE THREE MEASURES
    # This allows different units to be compared in one heatmap
    # --------------------------------------------------------

    city_heatmap = city_profile.set_index("City")[
        [
            "Avg_Customer_Balance",
            "Avg_Loan_Exposure",
            "Avg_Credit_Score"
        ]
    ].copy()

    city_heatmap.columns = [
        "Avg Customer Balance",
        "Avg Loan Exposure",
        "Avg Credit Score"
    ]

    # Standardization
    city_heatmap_standardized = (
        city_heatmap - city_heatmap.mean()
    ) / city_heatmap.std()

    # If only one city or zero variation exists
    city_heatmap_standardized = (
        city_heatmap_standardized
        .replace([np.inf, -np.inf], 0)
        .fillna(0)
    )

    # --------------------------------------------------------
    # CREATE COMPACT HEATMAP
    # --------------------------------------------------------

    fig, ax = plt.subplots(
        figsize=(7.5, 1.8)
    )

    sns.heatmap(
        city_heatmap_standardized,
        annot=True,
        fmt=".2f",
        cmap="Blues",
        linewidths=0.5,
        cbar_kws={
            "label": "Standardized Value"
        },
        annot_kws={
            "fontsize": 5
        },
        ax=ax
    )

    # --------------------------------------------------------
    # TITLE
    # --------------------------------------------------------

    ax.set_title(
        "Customer Financial Profile by City",
        fontsize=7,
        fontweight="bold",
        pad=10
    )

    # --------------------------------------------------------
    # LABELS
    # --------------------------------------------------------

    ax.set_xlabel(
        "",
        fontsize=5
    )

    ax.set_ylabel(
        "City",
        fontsize=5
    )

    ax.tick_params(
        axis="both",
        labelsize=5
    )

    plt.tight_layout()

    # --------------------------------------------------------
    # DISPLAY
    # --------------------------------------------------------

    st.pyplot(
        fig,
        use_container_width=False
    )

    plt.close(fig)

    # --------------------------------------------------------
    # EXPLANATION
    # --------------------------------------------------------

    st.markdown(
    """
    <p style="color: #003366; font-size: 18px;">
    <b>Business insight:</b> This heatmap compares city-level 
        customer balance, loan exposure, and credit score. <br>
        Values are standardized so the three measures can be 
        compared despite having different units.
    </p>
    """,
    unsafe_allow_html=True
)

# ============================================================
# ACCOUNTS & LOANS
# ============================================================

st.header("💰 Accounts & Loans")

# ============================================================
# CHART 7.2 — LOAN DEFAULT RATE BY LOAN TYPE
# ============================================================

loan_default_summary = (
    filtered_loans
    .groupby("Loan_Type")
    .agg(
        Total_Loans=("Loan_ID", "count"),
        Defaulted_Loans=(
            "Status",
            lambda x: (x == "Defaulted").sum()
        )
    )
    .reset_index()
)

if loan_default_summary.empty:

    st.warning(
        "No loan data is available for the selected filters."
    )

else:

    # Calculate default rate
    loan_default_summary["Default_Rate"] = (
        loan_default_summary["Defaulted_Loans"]
        / loan_default_summary["Total_Loans"]
        * 100
    )

    # Sort from lowest to highest
    loan_default_summary = (
        loan_default_summary
        .sort_values("Default_Rate", ascending=True)
    )

    # --------------------------------------------------------
    # GREEN SHADES
    # --------------------------------------------------------

    green_shades = sns.color_palette(
        "Greens",
        n_colors=len(loan_default_summary) + 2
    )[2:]

    # --------------------------------------------------------
    # COMPACT VERTICAL BAR CHART
    # --------------------------------------------------------

    fig, ax = plt.subplots(
        figsize=(7.5, 1.8)
    )

    bars = ax.bar(
        loan_default_summary["Loan_Type"],
        loan_default_summary["Default_Rate"],
        color=green_shades,
        width=0.60
    )

    # --------------------------------------------------------
    # VALUE LABELS ABOVE BARS
    # --------------------------------------------------------

    for bar in bars:

        value = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.08,
            f"{value:.2f}%",
            ha="center",
            va="bottom",
            fontsize=5
        )

    # --------------------------------------------------------
    # TITLE
    # --------------------------------------------------------

    ax.set_title(
        "Loan Default Rate by Loan Type",
        fontsize=7,
        fontweight="bold",
        pad=10
    )

    # --------------------------------------------------------
    # AXIS LABELS
    # --------------------------------------------------------

    ax.set_xlabel(
        "Loan Type",
        fontsize=6
    )

    ax.set_ylabel(
        "Default Rate (%)",
        fontsize=6
    )

    # --------------------------------------------------------
    # TICK SETTINGS
    # --------------------------------------------------------

    ax.tick_params(
        axis="x",
        labelsize=5
    )

    ax.tick_params(
        axis="y",
        labelsize=5
    )

    # --------------------------------------------------------
    # GRID
    # --------------------------------------------------------

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.20
    )

    ax.set_axisbelow(True)

    # --------------------------------------------------------
    # REMOVE EXTRA BORDERS
    # --------------------------------------------------------

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # --------------------------------------------------------
    # LAYOUT
    # --------------------------------------------------------

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=False
    )

    plt.close(fig)

# --------------------------------------------------------
# BUSINESS INSIGHT
# --------------------------------------------------------

highest_default = (
    loan_default_summary
    .iloc[-1]
)

st.markdown(
    f"""
    <div style="
        color: #003366;
        font-size: 18px;
        font-weight: 600;
        margin-top: 8px;
        margin-bottom: 8px;
    ">
        Business insight: {highest_default['Loan_Type']}
        has the highest observed default rate at
        {highest_default['Default_Rate']:.2f}%
        within the selected filters.
    </div>
    """,
    unsafe_allow_html=True
)
# ============================================================
# CHART — ACCOUNT BALANCE TREND BY OPENING YEAR
# ============================================================

#st.subheader("Average Account Balance Trend by Opening Year")

# ------------------------------------------------------------
# Prepare yearly account summary
# ------------------------------------------------------------

account_trend = (
    filtered_accounts
    .groupby("Year", as_index=False)
    .agg(
        Average_Balance=("Balance", "mean"),
        Total_Balance=("Balance", "sum"),
        Total_Accounts=("Account_ID", "count")
    )
    .sort_values("Year")
)

if account_trend.empty:

    st.warning(
        "No account data is available for the selected filters."
    )

else:

    # --------------------------------------------------------
    # COMPACT LINE CHART
    # --------------------------------------------------------

    fig, ax = plt.subplots(
        figsize=(7.5, 1.8)
    )

    ax.plot(
        account_trend["Year"],
        account_trend["Average_Balance"],
        marker="o",
        linewidth=2
    )

    # --------------------------------------------------------
    # VALUE LABELS
    # --------------------------------------------------------

    for x, y in zip(
        account_trend["Year"],
        account_trend["Average_Balance"]
    ):

        ax.annotate(
            f"₹{y:,.0f}",
            (x, y),
            textcoords="offset points",
            xytext=(0, 7),
            ha="center",
            fontsize=6
        )

    ax.set_title(
        "Average Account Balance Trend by Opening Year",
        fontsize=7,
        fontweight="bold",
        pad=10
    )

    ax.set_xlabel(
        "Account Opening Year",
        fontsize=5
    )

    ax.set_ylabel(
        "Average Account Balance (₹)",
        fontsize=5
    )

    ax.tick_params(
        axis="both",
        labelsize=5
    )

    ax.grid(
        linestyle="--",
        alpha=0.20
    )

    ax.set_axisbelow(True)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=False
    )

    plt.close(fig)

    st.markdown(
    """
    <p style="color: #003366; font-size: 18px;">
    <b>Business insight:</b> This trend shows how average account <br>
        balances differ across account opening years within 
        the selected customer and account filters.
    </p>
    """,
    unsafe_allow_html=True
)

# ============================================================
# TRANSACTIONS
# ============================================================

st.header("💳 Transactions")

# ============================================================
# CHART 7.3 — MONTHLY TRANSACTION VOLUME TREND
# ============================================================

#st.subheader("Monthly Transaction Volume Trend")

# ------------------------------------------------------------
# Prepare month information
# ------------------------------------------------------------

monthly_data = filtered_transactions.copy()

monthly_data["Transaction_Date"] = pd.to_datetime(
    monthly_data["Transaction_Date"],
    errors="coerce"
)

monthly_data["Month_Number"] = (
    monthly_data["Transaction_Date"].dt.month
)

monthly_data["Month_Name"] = (
    monthly_data["Transaction_Date"].dt.strftime("%b")
)

# ------------------------------------------------------------
# Create monthly transaction summary
# ------------------------------------------------------------

monthly_transactions = (
    monthly_data
    .groupby(
        ["Month_Number", "Month_Name"],
        as_index=False
    )
    .size()
    .rename(
        columns={
            "size": "Transaction_Count"
        }
    )
    .sort_values("Month_Number")
)

if monthly_transactions.empty:

    st.warning(
        "No transaction data is available for the selected filters."
    )

else:

    # --------------------------------------------------------
    # LINE CHART
    # --------------------------------------------------------

    fig, ax = plt.subplots(
        figsize=(7.5, 1.8)
    )

    ax.plot(
        monthly_transactions["Month_Name"],
        monthly_transactions["Transaction_Count"],
        marker="o",
        linewidth=2
    )

    # --------------------------------------------------------
    # VALUE LABELS
    # --------------------------------------------------------

    for x, y in zip(
        monthly_transactions["Month_Name"],
        monthly_transactions["Transaction_Count"]
    ):

        ax.annotate(
            f"{y:,}",
            (x, y),
            textcoords="offset points",
            xytext=(0, 6),
            ha="center",
            fontsize=6
        )

    # --------------------------------------------------------
    # TITLE
    # --------------------------------------------------------

    ax.set_title(
        "Monthly Transaction Volume Trend",
        fontsize=7,
        fontweight="bold",
        pad=10
    )

    # --------------------------------------------------------
    # AXIS LABELS
    # --------------------------------------------------------

    ax.set_xlabel(
        "Month",
        fontsize=6
    )

    ax.set_ylabel(
        "Number of Transactions",
        fontsize=6
    )

    # --------------------------------------------------------
    # TICK SETTINGS
    # --------------------------------------------------------

    ax.tick_params(
        axis="x",
        labelsize=6,
        rotation=0
    )

    ax.tick_params(
        axis="y",
        labelsize=6
    )

    # --------------------------------------------------------
    # GRID
    # --------------------------------------------------------

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.20
    )

    ax.set_axisbelow(True)

    # --------------------------------------------------------
    # REMOVE EXTRA BORDERS
    # --------------------------------------------------------

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()

    # --------------------------------------------------------
    # DISPLAY CHART
    # --------------------------------------------------------

    st.pyplot(
        fig,
        use_container_width=False
    )

    plt.close(fig)

    # --------------------------------------------------------
# BUSINESS INSIGHT
# --------------------------------------------------------

highest_month = monthly_transactions.loc[
    monthly_transactions["Transaction_Count"].idxmax()
]

st.markdown(
    f"""
    <div style="
        color: #003366;
        font-size: 18px;
        font-weight: 600;
        margin-top: 8px;
        margin-bottom: 8px;
    ">
        Business insight: {highest_month['Month_Name']}
        has the highest transaction volume with
        {highest_month['Transaction_Count']:,} transactions.
        <br>
              This insight is based on the selected filters.
    </div>
    """,
    unsafe_allow_html=True
)
# ============================================================
# CHART 7.11 — TRANSACTION TYPE DISTRIBUTION BY CHANNEL
# ============================================================


transaction_channel = (
    filtered_transactions
    .groupby(
        ["Channel", "Type"]
    )
    .size()
    .unstack(fill_value=0)
)

if transaction_channel.empty:

    st.warning(
        "No transaction data is available for the selected filters."
    )

else:

    # --------------------------------------------------------
    # CREATE BLUE + GREEN PALETTE
    # --------------------------------------------------------

    transaction_types_present = list(
        transaction_channel.columns
    )

    blue_palette = sns.color_palette(
        "Blues",
        n_colors=max(1, len(transaction_types_present) // 2 + 1)
    )

    green_palette = sns.color_palette(
        "Greens",
        n_colors=max(1, len(transaction_types_present))
    )

    combined_colors = []

    for i, transaction_type in enumerate(
        transaction_types_present
    ):

        if i % 2 == 0:

            combined_colors.append(
                blue_palette[
                    min(
                        i // 2,
                        len(blue_palette) - 1
                    )
                ]
            )

        else:

            combined_colors.append(
                green_palette[
                    min(
                        i // 2,
                        len(green_palette) - 1
                    )
                ]
            )

    # --------------------------------------------------------
    # STACKED BAR CHART
    # --------------------------------------------------------

    fig, ax = plt.subplots(
        figsize=(7.5, 2.0)
    )

    transaction_channel.plot(
        kind="bar",
        stacked=True,
        color=combined_colors,
        width=0.65,
        ax=ax
    )

    # --------------------------------------------------------
    # VALUE LABELS
    # --------------------------------------------------------

    for container in ax.containers:

        labels = []

        for rectangle in container:

            height = rectangle.get_height()

            if height >= 1000:
                labels.append(
                    f"{int(height):,}"
                )
            else:
                labels.append("")

        ax.bar_label(
            container,
            labels=labels,
            label_type="center",
            fontsize=6
        )

    ax.set_title(
        "Transaction Type Distribution by Channel",
        fontsize=7,
        fontweight="bold",
        pad=10
    )

    ax.set_xlabel(
        "Transaction Channel",
        fontsize=6
    )

    ax.set_ylabel(
        "Number of Transactions",
        fontsize=6
    )

    ax.tick_params(
        axis="x",
        labelsize=6,
        rotation=0
    )

    ax.tick_params(
        axis="y",
        labelsize=6
    )

    # --------------------------------------------------------
    # LEGEND
    # --------------------------------------------------------

    ax.legend(
        title="Transaction Type",
        fontsize=5,
        title_fontsize=8,
        bbox_to_anchor=(1.02, 1),
        loc="upper left"
    )

    # --------------------------------------------------------
    # GRID
    # --------------------------------------------------------

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.20
    )

    ax.set_axisbelow(True)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=False
    )

    plt.close(fig)

    st.markdown(
        """
        <p style="color: #003366; font-size: 18px;">
        <b>Business insight:</b> The stacked bars compare transaction 
        types across channels and show the composition of <br>
        transaction activity within the selected filters.
        </p>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# FRAUD & RISK
# ============================================================

st.header("🛡️ Fraud & Risk")


# ============================================================
# CHART 7.6 — FRAUD CASE COMPOSITION BY CASE STATUS
# ============================================================


fraud_status_summary = (
    filtered_fraud_cases
    .groupby("Case_Status")
    .size()
    .reset_index(name="Case_Count")
)

if fraud_status_summary.empty:

    st.warning(
        "No fraud case data is available for the selected filters."
    )

else:

    fig, ax = plt.subplots(
        figsize=(4.5, 2.8)
    )

    wedges, texts, autotexts = ax.pie(
        fraud_status_summary["Case_Count"],
        labels=fraud_status_summary["Case_Status"],
        autopct="%1.1f%%",
        startangle=90,
        wedgeprops={
            "width": 0.42,
            "edgecolor": "white"
        },
        textprops={
            "fontsize": 6
        }
    )

    for autotext in autotexts:
        autotext.set_fontsize(8)

    ax.set_title(
        "Fraud Case Composition by Case Status",
        fontsize=7,
        fontweight="bold",
        pad=10
    )

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=False
    )

    plt.close(fig)


    
    st.markdown(
        """
        <p style="color: #003366; font-size: 18px;">
        <b>Business insight:</b> The donut chart shows how filtered 
        fraud cases are distributed across Open, Closed, ,<br>
        Confirmed, and False Positive statuses.
        </p>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# CHART — RISK SCORE DISTRIBUTION
# ============================================================



if filtered_fraud_cases.empty:

    st.warning(
        "No fraud case data is available for the selected filters."
    )

else:

    risk_scores = (
        filtered_fraud_cases["Risk_Score"]
        .dropna()
        .sort_values()
    )

    fig, ax = plt.subplots(
        figsize=(7.5, 1.8)
    )

    # Create distribution using histogram
    ax.hist(
        risk_scores,
        bins=20,
        alpha=0.75
    )

    # Mean risk score
    mean_risk = risk_scores.mean()

    ax.axvline(
        mean_risk,
        linestyle="--",
        linewidth=2,
        label=f"Avg Risk Score: {mean_risk:.3f}"
    )

    ax.set_title(
        "Fraud Risk Score Distribution",
        fontsize=7,
        fontweight="bold",
        pad=10
    )

    ax.set_xlabel(
        "Risk Score",
        fontsize=6
    )

    ax.set_ylabel(
        "Number of Fraud Cases",
        fontsize=6
    )

    ax.tick_params(
        axis="both",
        labelsize=6
    )

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.20
    )

    ax.set_axisbelow(True)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.legend(
        fontsize=5
    )

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=False
    )

    plt.close(fig)

    st.markdown(
            """
            <p style="color: #003366; font-size: 18px;">
            <b>Business insight:</b>  The distribution shows how risk 
        scores are spread across filtered fraud cases. ,<br>
        The dashed line indicates the average risk score.
            </p>
            """,
            unsafe_allow_html=True
        )
# ============================================================
# CUSTOMER SERVICE
# ============================================================

st.header("📞 Customer Service")


# ============================================================
# FILTER COMPLAINTS THROUGH FINAL CUSTOMER POPULATION
# ============================================================

filtered_complaints = complaints[
    complaints["Customer_ID"].isin(
        filtered_customers["Customer_ID"]
    )
].copy()


# ============================================================
# CHART 7.5 — COMPLAINT TYPE VS PRIORITY
# AVERAGE SATISFACTION HEATMAP

complaint_satisfaction = (
    filtered_complaints
    .pivot_table(
        index="Type",
        columns="Priority",
        values="Satisfaction",
        aggfunc="mean"
    )
)

if complaint_satisfaction.empty:

    st.warning(
        "No complaint data is available for the selected filters."
    )

else:

    # --------------------------------------------------------
    # CREATE COMPACT GREEN HEATMAP
    # --------------------------------------------------------

    fig, ax = plt.subplots(
        figsize=(7.5, 2.3)
    )

    sns.heatmap(
        complaint_satisfaction,
        annot=True,
        fmt=".2f",
        cmap="Greens",
        linewidths=0.5,
        cbar_kws={
            "label": "Average Satisfaction"
        },
        annot_kws={
            "fontsize": 5
        },
        ax=ax
    )

    # --------------------------------------------------------
    # TITLE
    # --------------------------------------------------------

    ax.set_title(
        "Average Satisfaction by Complaint Type and Priority",
        fontsize=7,
        fontweight="bold",
        pad=10
    )

    # --------------------------------------------------------
    # AXIS LABELS
    # --------------------------------------------------------

    ax.set_xlabel(
        "Complaint Priority",
        fontsize=6
    )

    ax.set_ylabel(
        "Complaint Type",
        fontsize=6
    )

    # --------------------------------------------------------
    # TICK SETTINGS
    # --------------------------------------------------------

    ax.tick_params(
        axis="both",
        labelsize=5
    )

    # --------------------------------------------------------
    # LAYOUT
    # --------------------------------------------------------

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=False
    )

    plt.close(fig)

    st.markdown(
                """
                <p style="color: #003366; font-size: 18px;">
                <b>Business insight:</b> The heatmap compares average 
        customer satisfaction across complaint types and ,<br>
        priority levels within the selected filters.
                </p>
                """,
                unsafe_allow_html=True
            )
    # ============================================================
# CHART 7.10 — COMPLAINT RESOLUTION DAYS VS
# AVERAGE SATISFACTION
# ============================================================


resolution_satisfaction = (
    filtered_complaints
    .groupby("Resolution_Days", as_index=False)
    .agg(
        Average_Satisfaction=(
            "Satisfaction",
            "mean"
        ),
        Complaint_Count=(
            "Complaint_ID",
            "count"
        )
    )
    .sort_values("Resolution_Days")
)

if resolution_satisfaction.empty:

    st.warning(
        "No complaint data is available for the selected filters."
    )

else:

    # --------------------------------------------------------
    # CREATE FILLED AREA CHART
    # --------------------------------------------------------

    fig, ax = plt.subplots(
        figsize=(7.5, 2.0)
    )

    ax.fill_between(
        resolution_satisfaction["Resolution_Days"],
        resolution_satisfaction["Average_Satisfaction"],
        alpha=0.30
    )

    ax.plot(
        resolution_satisfaction["Resolution_Days"],
        resolution_satisfaction["Average_Satisfaction"],
        marker="o",
        linewidth=2
    )

    # --------------------------------------------------------
    # VALUE LABELS
    # --------------------------------------------------------

    for x, y in zip(
        resolution_satisfaction["Resolution_Days"],
        resolution_satisfaction["Average_Satisfaction"]
    ):

        ax.annotate(
            f"{y:.2f}",
            (x, y),
            textcoords="offset points",
            xytext=(0, 6),
            ha="center",
            fontsize=5
        )

    # --------------------------------------------------------
    # TITLE
    # --------------------------------------------------------

    ax.set_title(
        "Complaint Resolution Days vs Average Satisfaction",
        fontsize=7,
        fontweight="bold",
        pad=10
    )

    # --------------------------------------------------------
    # AXIS LABELS
    # --------------------------------------------------------

    ax.set_xlabel(
        "Resolution Days",
        fontsize=6
    )

    ax.set_ylabel(
        "Average Satisfaction",
        fontsize=6
    )

    # --------------------------------------------------------
    # Y-AXIS LIMIT
    # Satisfaction scale is 1–5
    # --------------------------------------------------------

    ax.set_ylim(
        1,
        5
    )

    # --------------------------------------------------------
    # TICK SETTINGS
    # --------------------------------------------------------

    ax.tick_params(
        axis="both",
        labelsize=6
    )

    # --------------------------------------------------------
    # GRID
    # --------------------------------------------------------

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.20
    )

    ax.set_axisbelow(True)

    # --------------------------------------------------------
    # REMOVE EXTRA BORDERS
    # --------------------------------------------------------

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()

    # --------------------------------------------------------
    # DISPLAY
    # --------------------------------------------------------

    st.pyplot(
        fig,
        use_container_width=False
    )

    plt.close(fig)

    # --------------------------------------------------------
    # BUSINESS INSIGHT
    # --------------------------------------------------------

    highest_satisfaction = (
        resolution_satisfaction.loc[
            resolution_satisfaction["Average_Satisfaction"].idxmax()
        ]
    )

    lowest_satisfaction = (
        resolution_satisfaction.loc[
            resolution_satisfaction["Average_Satisfaction"].idxmin()
        ]
    )

st.markdown(
    f"""
    <div style="
        color: #003366;
        font-size: 18px;
        font-weight: 600;
        margin-top: 8px;
        margin-bottom: 8px;
    ">
        Business insight: Average satisfaction is highest at
        {highest_satisfaction['Average_Satisfaction']:.2f}
        for complaints resolved in
        {int(highest_satisfaction['Resolution_Days'])} days.
        <br>
        The lowest observed average is
        {lowest_satisfaction['Average_Satisfaction']:.2f}
        at {int(lowest_satisfaction['Resolution_Days'])} days.
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# BUSINESS INSIGHTS
# ============================================================

st.markdown("---")

st.header("💡 Business Insights")

st.markdown(
    "Key findings derived from the banking and FinTech analysis."
)

# ------------------------------------------------------------
# BUSINESS INSIGHTS TABLE
# ------------------------------------------------------------

business_insights = pd.DataFrame(
    {
        "Business Area": [
            "Loan Risk",
            "Customer Finance",
            "Account Performance",
            "Customer Service",
            "Transactions",
            "Fraud Risk",
            "Transaction Flow"
        ],

        "Finding": [
            "Education loans had the highest observed default rate among defined loan types.",
            "Average customer balances were relatively consistent across defined occupations.",
            "Savings accounts had the highest average balance.",
            "Average satisfaction was nearly flat across complaint types.",
            "Online transactions had the highest total transaction value.",
            "Fraud flags appeared across every case status.",
            "Calculated transaction net amount was negative."
        ],

        "Evidence": [
            "Education loan default rate: 6.32%.",
            "Average balances across defined occupations were approximately ₹20,280–₹20,612.",
            "Average Savings account balance: approximately ₹16,511.",
            "Average satisfaction ranged from approximately 2.97 to 3.01 out of 5.",
            "Online transaction value: approximately ₹67.07M.",
            "Fraud flags were present in Open, Closed, Confirmed, and False Positive cases.",
            "Calculated transaction net amount: approximately -₹57.18M."
        ],

        "Business Implication": [
            "Loan portfolios should be monitored by product type and repayment behavior.",
            "Customer segmentation may benefit from additional variables beyond occupation.",
            "Savings products may represent an important deposit relationship.",
            "Service improvement efforts may need to consider factors beyond complaint category.",
            "Digital transaction channels represent significant transaction activity.",
            "Fraud Flag and Case Status should be monitored as separate indicators.",
            "The negative net amount indicates more debit value than credit value in this dataset; it should not be interpreted as bank profit or loss."
        ]
    }
)

st.dataframe(
    business_insights,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# RECOMMENDATIONS
# ============================================================

st.header("🎯 Recommendations")

st.markdown(
    "The following recommendations are based on the observed "
    "patterns in the dataset and should be validated with "
    "additional operational and business data."
)

recommendations = [
    (
        "Loan Portfolio Monitoring",
        "Monitor education and other higher-default loan segments "
        "regularly using product-level default-rate tracking."
    ),

    (
        "Customer Segmentation",
        "Combine occupation with credit score, income, balance, "
        "account ownership, and transaction behavior for richer "
        "customer segmentation."
    ),

    (
        "Savings Product Strategy",
        "Review savings-account customer behavior and explore "
        "opportunities to strengthen deposit relationships."
    ),

    (
        "Customer Service Improvement",
        "Track resolution time, priority, complaint type, and "
        "satisfaction together rather than relying on complaint "
        "category alone."
    ),

    (
        "Digital Transaction Monitoring",
        "Monitor online transaction activity and channel usage "
        "to understand digital customer engagement."
    ),

    (
        "Fraud Risk Monitoring",
        "Evaluate Fraud Flag, Risk Score, Detection Method, and "
        "Case Status together to improve fraud-monitoring analysis."
    ),

    (
        "Cash Flow Monitoring",
        "Investigate debit and credit transaction patterns further "
        "to understand the drivers of the observed negative net amount."
    )
]

recommendation_df = pd.DataFrame(
    recommendations,
    columns=[
        "Area",
        "Recommendation"
    ]
)

st.dataframe(
    recommendation_df,
    use_container_width=True,
    hide_index=True
)