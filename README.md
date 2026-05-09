# Financial Risk & Commodity Pricing Models

This repository contains finance and machine learning projects focused on commodity pricing, storage contract valuation, credit risk analysis, and borrower risk categorization using Python.

The objective of these projects is to apply quantitative analysis, financial modeling, and machine learning techniques to solve real-world financial problems.

---

# Project Overview

This repository consists of four tasks:

1. **Natural Gas Price Analysis**  
2. **Commodity Storage Contract Pricing**  
3. **Credit Risk Analysis**  
4. **FICO Score Bucketing & Risk Categorization**

---

# Task 1: Natural Gas Price Analysis

## Objective
Analyze historical natural gas prices and build a pricing model to estimate prices for selected dates.

## Features Implemented
- Historical natural gas price analysis
- Price estimation using historical data
- Data preprocessing and exploration

## Files Used

```text
Task1_Task2/
│── Nat_Gas.csv
│── price_model.py
```

## Technologies Used
- Python
- Pandas

---

# Task 2: Commodity Storage Contract Pricing

## Objective
Develop a pricing model for a commodity storage contract by considering gas injection and withdrawal operations across multiple dates.

## Parameters Considered
- Injection dates
- Withdrawal dates
- Commodity purchase/selling price
- Storage cost per unit
- Injection cost
- Withdrawal cost
- Maximum storage capacity
- Multiple gas transactions

## Features Implemented
- Multi-date injection and withdrawal handling
- Storage capacity validation
- Profit calculation for contracts
- Cost-adjusted pricing model
- Generalized pricing function

## Files Used

```text
Task1_Task2/
│── contract_pricing.py
```

## Technologies Used
- Python

---

# Task 3: Credit Risk Analysis

## Objective
Build a machine learning model to predict the **Probability of Default (PD)** for borrowers and estimate the **Expected Loss** on a loan.

## Model Used
- Logistic Regression

## Workflow
- Data loading and preprocessing
- Feature selection
- Train-test split
- Feature scaling using `StandardScaler`
- Model training
- Prediction and evaluation

## Evaluation Metrics
- Accuracy Score
- Confusion Matrix
- Classification Report

## Expected Loss Formula

```text
Expected Loss = PD × Loan Amount × (1 − Recovery Rate)
```

**Recovery Rate Assumed:** `10%`

## Files Used

```text
Task3_Task4/
│── credit_risk_model.py
│── Task 3 and 4_Loan_Data.csv
```

## Technologies Used
- Python
- Pandas
- Scikit-learn

---

# Task 4: FICO Score Bucketing & Risk Categorization

## Objective
Create a rating system that maps borrower **FICO scores** into categorical risk buckets and estimate the **Probability of Default (PD)** for each rating group.

## Approach Used
Quantization using **quantile-based bucketing (`qcut`)** was implemented to:

- Automatically generate FICO score boundaries
- Categorize borrowers into rating groups
- Estimate Probability of Default for each category
- Generalize for future datasets

## Features Implemented
- FICO score bucketing
- Credit rating generation
- Probability of Default calculation
- Borrower risk categorization

## Files Used

```text
Task3_Task4/
│── fico_bucket_model.py
```

## Technologies Used
- Python
- Pandas

---

# Repository Structure

```text
NG/
│── Task1_Task2/
│   │── contract_pricing.py
│   │── Nat_Gas.csv
│   │── price_model.py
│
│── Task3_Task4/
│   │── credit_risk_model.py
│   │── fico_bucket_model.py
│   │── Task 3 and 4_Loan_Data.csv
│
│── .gitignore
│── README.md
```

---

# Skills Demonstrated

- Python Programming
- Data Analysis
- Financial Modeling
- Commodity Pricing
- Credit Risk Analysis
- Machine Learning
- Logistic Regression
- Feature Scaling
- Probability of Default (PD)
- Quantitative Analysis
- Data Preprocessing
- FICO Score Quantization
- Problem Solving

---

# Author

**SAANVI PATNAIK**
