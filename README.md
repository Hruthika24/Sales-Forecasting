# Retail Sales Forecasting and Inventory Optimization

## Project Overview

This project analyzes historical retail sales data to forecast future demand, detect anomalies, and segment products based on demand patterns. The goal is to help retail companies optimize inventory planning and improve business decisions.

---

## Objectives

- Analyze historical sales trends.
- Forecast future sales using machine learning models.
- Detect unusual sales patterns.
- Segment products based on demand.
- Build an interactive dashboard using Streamlit.

---

## Dataset

Dataset used: Superstore sales dataset (`train.csv`)

Main columns:

- Order Date
- Sales
- Category
- Sub-Category
- Region

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Statsmodels
- Prophet
- XGBoost
- Streamlit

---

## Project Tasks

### Task 1: Data Preprocessing and EDA

- Data cleaning
- Date conversion
- Sales trend analysis
- Category and region analysis

### Task 2: Time Series Analysis

- Monthly sales aggregation
- Time series decomposition
- Stationarity testing

### Task 3: Sales Forecasting

Models used:

- SARIMA
- Prophet
- XGBoost

Evaluation metrics:

- MAE
- RMSE
- MAPE

### Task 4: Category and Region Forecasting

Forecasts generated for:

- Furniture
- Technology
- Office Supplies
- East Region
- West Region

### Task 5: Anomaly Detection

Methods used:

- Isolation Forest
- Z-score Analysis

### Task 6: Product Demand Segmentation

- K-Means Clustering
- PCA Visualization

### Task 7: Streamlit Dashboard

Dashboard pages:

1. Sales Overview Dashboard
2. Forecast Explorer
3. Anomaly Report
4. Product Demand Segments

### Task 8: Executive Business Report

- Business insights
- Sales forecasts
- Inventory recommendations

---

## Project Structure

```
SalesForecasting_Hruthika/

├── analysis.ipynb
├── train.csv
├── app.py
├── requirements.txt
├── README.md
├── summary.docx
└── charts/
```

---

## How to Run the Project

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit app

```bash
streamlit run app.py
```

---

## Author

Hruthika Reddy

B.Tech – Computer Science and Engineering (Data Science)

ACE Engineering College
