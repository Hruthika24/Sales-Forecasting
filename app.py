import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Sales Overview Dashboard")

# Load dataset
df = pd.read_csv("train.csv")

# Convert date column
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    dayfirst=True
)

# Monthly sales
monthly_sales = df.groupby(
    pd.Grouper(
        key="Order Date",
        freq="ME"
    )
)["Sales"].sum()

# Monthly sales chart
st.subheader("Monthly Sales Trend")

st.line_chart(monthly_sales)

# Sales by region
st.subheader("Sales by Region")

region_sales = df.groupby(
    "Region"
)["Sales"].sum()

st.bar_chart(region_sales)

# Sales by category
st.subheader("Sales by Category")

category_sales = df.groupby(
    "Category"
)["Sales"].sum()

st.bar_chart(category_sales)