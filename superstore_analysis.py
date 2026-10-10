import numpy as np
import pandas as pd

df = pd.read_csv("samplesuperstore.csv")

print(df)
print(df.shape)
print(df.isna().sum())

print("Columns names: ")
print(df.columns)

print("\nDataset Info: ")
print(df.info())

print("\nDuplicated rows: ", df.duplicated().sum())

print("\nUnique Customers: ", df["Customer ID"].nunique())
print("Unique Orders: ", df["Order ID"].nunique())
print("Unique Products: ", df["Product ID"].nunique())

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.month
df["Order Month Name"] = df["Order Date"].dt.strftime("%b")
df["Order Quarter"] = df["Order Date"].dt.to_period("Q").astype("str")

df.head(2)

# KPI Analysis


total_sales = df['Sales'].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

profit_margin = (total_profit / total_sales) * 100
average_order_value = total_sales / total_orders

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Quantity Sold: {total_quantity:,}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Customers: {total_customers:,}")
print(f"Profit Margin: {profit_margin:.2f}%")
print(f"Average Order Value: ${average_order_value:,.2f}")
