# 🏦  Banking & FinTech Analytics

## 📌 Project Overview

This project presents an end-to-end **Banking & FinTech Data Analytics solution** using Python, Jupyter Notebook, and Streamlit.

The project analyzes seven banking-related datasets covering:

- Customers
- Accounts
- Cards
- Loans
- Transactions
- Complaints
- Fraud Cases

The main objective is to transform raw banking data into meaningful analytical insights and an interactive business dashboard.

The complete workflow followed in this project is:

**Raw Data → Data Cleaning → Data Transformation → Exploratory Data Analysis (EDA) → Data Visualization → Business Insights → Recommendations → Streamlit Dashboard → GitHub**

---

# 🎯 Project Objectives

The key objectives of this project are:

1. Analyze customer demographic and financial characteristics.
2. Understand customer account ownership and balances.
3. Analyze card products, credit limits, and annual fees.
4. Evaluate loan portfolio performance and observed default rates.
5. Analyze transaction volume, value, type, and channels.
6. Examine fraud indicators and fraud case status.
7. Analyze customer complaints, resolution time, and satisfaction.
8. Perform descriptive statistical analysis.
9. Identify meaningful business patterns and insights.
10. Build an interactive Streamlit dashboard for business analysis.
11. Provide data-driven recommendations based on the observed findings.

---

# 📂 Dataset Description

The project contains seven main datasets.

| Dataset | Description |
|---|---|
| `customers.csv` | Customer demographic and financial information |
| `accounts.csv` | Customer account information, balances, branches, and account status |
| `cards.csv` | Card type, product, credit limit, and annual fee |
| `complaints.csv` | Customer complaints, priorities, resolution time, and satisfaction |
| `fraud_cases.csv` | Fraud flags, risk scores, detection methods, and case status |
| `loans.csv` | Loan type, amount, interest rate, tenure, and loan status |
| `transactions.csv` | Transaction dates, types, amounts, debit/credit status, merchant categories, and channels |

---

# 🛠️ Technologies Used

The project was developed using:

Python
Pandas
NumPy
Matplotlib
Seaborn
Jupyter Notebook
Streamlit
GitHub

# Installation & import
%pip install numpy pandas matplotlib seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 🧹 Data Cleaning

Before analysis, the raw datasets were cleaned and validated.

## Main cleaning activities

- Checked missing values in all datasets.
- Checked complete duplicate records.
- Standardized categorical text values.
- Removed unnecessary leading/trailing spaces.
- Standardized occupation values.
- Standardized loan type and loan status values.
- Standardized transaction type values.
- Standardized Debit/Credit values.
- Handled missing customer names.
- Filled missing customer ages using the median.
- Filled missing occupation values with an explicit category.
- Removed loan records where `Customer_ID` was unavailable.
- Filled missing loan amounts using the median.
- Removed incomplete transaction records where `Account_ID`, `Transaction_Date`, or `Type` was unavailable.
- Converted date columns into proper datetime format.
- Validated numerical ranges and categorical distributions.

## Duplicate Validation

Complete duplicate rows were checked across all seven datasets.

No complete duplicate records were found in the final datasets.

---

# 🔄 Data Transformation

Additional analytical columns were created to support EDA, visualization, and dashboard development.

## 👥 Customer Transformations

The following customer-level features were created:

- `Total_Accounts`
- `Total_Balance`

These were calculated from the related account data at customer level.

---

## 🏦 Account Transformations

The following date features were created from `Open_Date`:

- `Year`
- `Month_Number`
- `Month_Name`
- `Quarter`

---

## 📞 Complaint Transformations

The following date features were created from `Complaint_Date`:

- `Year`
- `Month_Number`
- `Month_Name`
- `Quarter`
- `Day`
- `Day_Name`

---

## 💳 Transaction Transformations

The following features were created from `Transaction_Date`:

- `Year`
- `Month_Number`
- `Month_Name`
- `Quarter`
- `Day`
- `Day_Name`

A new `Net_Amount` feature was also created.

For analysis:

- Credit transactions are treated as positive.
- Debit transactions are treated as negative.

Therefore:

**Net Amount = Credit Amount − Debit Amount**

> The calculated Net Amount is a transaction-flow metric for this dataset. It should not be interpreted as bank profit or loss.

---

## 💰 Loan Transformations

A new feature called:

`Estimated_Interest`

was created using a simple-interest calculation based on:

- Loan Amount
- Interest Rate
- Tenure

> Estimated Interest is used only for analytical purposes and does not represent the actual interest charged by the bank.

---

# 📊 Exploratory Data Analysis (EDA)

EDA was performed across all seven datasets.

## 👥 Customer Analysis

Customer analysis included:

- Total customers
- Age distribution
- Annual income
- Credit score
- Customer balance
- Total accounts
- Occupation distribution
- City distribution

### Key customer statistics

- Total Customers: **40,000**
- Average Age: **46.56 years**
- Average Annual Income: **₹76,958.89**
- Average Credit Score: **719.62**
- Average Customer Balance: **₹20,430.45**

---

# 🏦 Account Analysis

Account analysis included:

- Total account count
- Account type
- Account status
- Branch
- Account opening year
- Account balance

### Key account statistics

- Total Accounts: **50,000**
- Average Account Balance: **₹16,344.36**
- Total Account Balance: **₹817.22M**
- Active Accounts: **43,943**

---

# 💳 Card Analysis

Card analysis included:

- Card type
- Card product
- Credit limit
- Annual fee

### Key card statistics

- Visa: **18,554**
- RuPay: **18,237**
- Mastercard: **18,209**
- Average Credit Limit: **₹509,225.71**
- Average Annual Fee: **₹1,696.38**

---

# 📞 Complaint Analysis

Complaint analysis included:

- Complaint type
- Complaint priority
- Resolution days
- Satisfaction score
- Complaint year

### Key complaint statistics

- Total Complaints: **20,000**
- Average Resolution Time: **9.47 days**
- Average Satisfaction: **2.99 / 5**

---

# 🛡️ Fraud Analysis

Fraud analysis included:

- Fraud flag
- Risk score
- Detection method
- Case status

### Key fraud statistics

- Total Fraud Cases: **10,000**
- Fraud Flagged Cases: **755**
- Fraud Flag Rate: **7.55%**
- Average Risk Score: **0.504**

> `Fraud_Flag` and `Case_Status` are treated as separate indicators. A fraud flag does not automatically mean that the case is confirmed fraud.

---

# 💰 Loan Analysis

Loan analysis included:

- Loan type
- Loan status
- Loan amount
- Interest rate
- Tenure
- Estimated interest
- Observed default rate

### Key loan statistics

- Total Loans: **29,880**
- Total Loan Amount: **₹120.20B**
- Average Loan Amount: **₹4.02M**
- Average Interest Rate: **14.53%**
- Average Tenure: **89.48 months**
- Overall Observed Default Rate: **6.03%**

---

# 💳 Transaction Analysis

Transaction analysis included:

- Transaction count
- Transaction type
- Transaction amount
- Debit/Credit
- Merchant category
- Transaction channel
- Monthly activity
- Net amount

### Key transaction statistics

- Total Transactions: **395,213**
- Total Transaction Amount: **₹400.13M**
- Debit Transactions: **225,401**
- Credit Transactions: **169,812**
- Calculated Net Amount: **-₹57.18M**

---

# 📈 Data Visualizations

The project includes 12 major analytical visualizations.

## 7.1 Average Customer Balance by Occupation

**Chart Type:** Horizontal Bar Chart

Purpose:

Shows average customer balance across occupation groups and supports customer financial segmentation.

---

## 7.2 Loan Default Rate by Loan Type

**Chart Type:** Vertical Bar Chart

Purpose:

Compares the observed default rate across different loan types.

---

## 7.3 Monthly Transaction Volume Trend

**Chart Type:** Line Chart

Purpose:

Shows transaction-volume movement across months.

Month names are displayed on the x-axis for easier interpretation.

---

## 7.4 Annual Income vs Total Customer Balance by Occupation

**Chart Type:** Scatter Plot

Purpose:

Shows the distribution of annual income and customer balance across occupation groups.

Different colors are used to distinguish occupation groups.

> This chart describes an observed relationship and does not establish causation.

---

## 7.5 Complaint Type vs Priority — Average Satisfaction

**Chart Type:** Heatmap

Purpose:

Compares average customer satisfaction across complaint types and priority levels.

The dashboard uses a green color scale for this heatmap.

---

## 7.6 Fraud Case Composition by Case Status

**Chart Type:** Donut Chart

Purpose:

Shows the composition of fraud cases across:

- Open
- Closed
- Confirmed
- False Positive

---

## 7.7 Transaction Amount Distribution by Channel

**Chart Type:** Box Plot

Purpose:

Compares transaction-amount distributions across transaction channels.

---

## 7.8 Loan Amount Distribution by Loan Type

**Chart Type:** Box Plot

Purpose:

Shows loan amount distributions across loan types and highlights differences in spread and median values.

---

## 7.9 Average Account Balance by Account Type

**Chart Type:** Horizontal Bar Chart

Purpose:

Compares the average balance across account types.

---

## 7.10 Complaint Resolution Days vs Average Satisfaction

**Chart Type:** Filled Area Trend

Purpose:

Shows how average satisfaction varies across different complaint resolution times.

---

## 7.11 Transaction Type Distribution by Channel

**Chart Type:** Stacked Bar Chart

Purpose:

Compares transaction types across different channels.

The dashboard uses a combination of blue and green shades.

---

## 7.12 Customer Financial Profile by City

**Chart Type:** Heatmap

Purpose:

Compares city-level financial indicators:

- Average Customer Balance
- Average Loan Exposure
- Average Credit Score

The three measures are standardized before visualization so they can be compared despite having different units.

---

# 💡 Key Business Insights

## 1. Loan Risk

Education loans had the highest observed default rate among the defined loan types at approximately **6.32%**.

Home loans followed at approximately **6.17%**.

---

## 2. Customer Financial Profile

Average customer balances were relatively consistent across defined occupation groups, with values roughly between **₹20,280 and ₹20,612**.

---

## 3. Account Performance

Savings accounts recorded the highest average account balance at approximately **₹16,511**.

---

## 4. Customer Service

Average satisfaction remained relatively similar across complaint categories, approximately **2.97–3.01 out of 5**.

---

## 5. Transaction Activity

Online transactions recorded the highest total transaction value at approximately **₹67.07M**.

---

## 6. Fraud Risk

Fraud flags appeared across all case-status categories.

Therefore:

**Fraud Flag ≠ Confirmed Fraud**

and the two indicators should be analyzed separately.

---

## 7. Transaction Flow

The calculated transaction net amount was approximately:

**-₹57.18M**

This means debit transaction value exceeded credit transaction value in the dataset.

> This is a transaction-flow measure and should not be interpreted as bank profit or loss.

---

# 🎯 Business Recommendations

## Loan Portfolio Monitoring

Monitor loan performance by product type and repayment behavior, with particular attention to segments showing relatively higher observed default rates.

---

## Customer Segmentation

Use multiple customer variables such as:

- Credit Score
- Annual Income
- Customer Balance
- Account Ownership
- Transaction Behavior
- Occupation

instead of relying on occupation alone.

---

## Savings Product Strategy

Analyze savings-account customer behavior and deposit relationships to better understand customer engagement with savings products.

---

## Customer Service Improvement

Monitor:

- Resolution Time
- Complaint Priority
- Complaint Type
- Customer Satisfaction

together rather than relying on complaint category alone.

---

## Digital Transaction Monitoring

Monitor online and other digital transaction channels to understand customer transaction behavior and channel engagement.

---

## Fraud Risk Monitoring

Analyze:

- Fraud Flag
- Risk Score
- Detection Method
- Case Status

together for more complete fraud-risk monitoring.

---

## Transaction Flow Monitoring

Further investigate debit and credit transaction patterns to understand the drivers of the observed negative net transaction amount.

---

# 📈 Descriptive Statistics

The Streamlit dashboard includes an interactive descriptive-statistics module.

Users can select a dataset and view:

- Count
- Mean
- Standard Deviation
- Minimum
- Q1 (25%)
- Median
- Q3 (75%)
- Maximum

## Supported datasets

- Customers
- Accounts
- Loans
- Transactions
- Complaints
- Fraud Cases

The descriptive statistics update based on the selected dashboard filters.

---

# 📊 Streamlit Dashboard

The project includes an interactive Streamlit dashboard for business analysis.

## 🚀 Live Streamlit Dashboard

🔗 **[Open Banking & FinTech Analytics Dashboard](https://banking-fintech-analytics-miz5fptwu2irghrzgd5akb.streamlit.app/)**

The interactive dashboard is deployed using Streamlit Community Cloud.

The dashboard provides:

- Interactive KPI cards
- Combined dashboard filters
- Descriptive statistics
- Customer analytics
- Accounts and loan analysis
- Transaction analysis
- Fraud and risk analysis
- Customer service analysis
- Business insights and recommendations

## Dashboard Sections

### 📊 Overview / KPIs

The dashboard displays eight key performance indicators:

1. Total Customers
2. Total Accounts
3. Active Accounts
4. Total Loans
5. Total Loan Amount
6. Total Transactions
7. Loan Default Rate
8. Fraud Flag Rate

The KPI cards are designed with compact sizing and bordered styling.

All KPI values update according to the selected filters.

---

# 🔎 Interactive Dashboard Filters

The dashboard supports combined filtering using:

- Transaction Year
- City
- Occupation
- Account Type
- Loan Type
- Loan Status
- Transaction Type
- Transaction Channel
- Debit/Credit

The filters work together across related datasets.

For example:

**City → Customer → Account → Transaction**

and:

**City → Customer → Loan**

This allows multiple filters to be applied simultaneously.

---

# 👥 Customer Analytics

The Customer Analytics section contains:

- Average Customer Balance by Occupation
- Annual Income vs Total Customer Balance by Occupation
- Customer Financial Profile by City

---

# 💰 Accounts & Loans

The Accounts & Loans section contains:

- Loan Default Rate by Loan Type
- Average Account Balance Trend by Opening Year

The section combines loan-risk analysis with an account-opening-year trend.

---

# 💳 Transactions

The Transactions section contains:

- Monthly Transaction Volume Trend
- Transaction Type Distribution by Channel

---

# 🛡️ Fraud & Risk

The Fraud & Risk section contains:

- Fraud Case Composition by Case Status
- Fraud Risk Score Distribution

---

# 📞 Customer Service

The Customer Service section contains:

- Complaint Type vs Priority — Average Satisfaction
- Complaint Resolution Days vs Average Satisfaction

---

# 💡 Business Insights & Recommendations

The dashboard contains a dedicated management-summary section presenting:

- Key findings
- Supporting evidence
- Business implications
- Recommendations

This section summarizes the major findings from the complete analysis.

---

# 🗂️ Project Structure

```text
Banking_FinTech_Project/
│
├── data/
│   ├── accounts.csv
│   ├── cards.csv
│   ├── complaints.csv
│   ├── customers.csv
│   ├── fraud_cases.csv
│   ├── loans.csv
│   └── transactions.csv
│
├── notebooks/
│   └── banking_fintech_analysis.ipynb
│
├── dashboard/
│   └── app.py
│
├── outputs/
│   ├── charts/
│   └── cleaned_data/
│       ├── customers_clean.csv
│       ├── accounts_clean.csv
│       ├── cards_clean.csv
│       ├── complaints_clean.csv
│       ├── fraud_cases_clean.csv
│       ├── loans_clean.csv
│       └── transactions_clean.csv
│
├── README.md
│
└── requirements.txt