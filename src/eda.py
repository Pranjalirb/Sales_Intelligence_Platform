import pandas as pd
import os
import matplotlib.pyplot as plt


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_path = os.path.join(BASE_DIR, "data", "cleaned", "sales_cleaned.csv")

sales = pd.read_csv(file_path, parse_dates=["Order_Date"])



# BUSINESS KPIs
total_orders = sales.shape[0]
total_sales = sales["Sales"].sum()
total_profit = sales["Profit"].sum()
average_sales = sales["Sales"].mean()
average_profit = sales["Profit"].mean()

print("\n========== BUSINESS KPIs ==========")
print("Total Orders   :", total_orders)
print(f"Total Sales    : ₹{total_sales:,.2f}")
print(f"Total Profit   : ₹{total_profit:,.2f}")
print(f"Average Sales  : ₹{average_sales:,.2f}")
print(f"Average Profit : ₹{average_profit:,.2f}")

# SALES BY CATEGORY
category_sales = sales.groupby("Category")["Sales"].sum().sort_values(ascending=False)

print("\n========== SALES BY CATEGORY ==========")
print(category_sales)