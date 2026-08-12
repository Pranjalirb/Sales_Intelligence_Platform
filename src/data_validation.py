import pandas as pd
import os
import sys


# ==============================
# Project Paths
# ==============================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

file_path = os.path.join(
    BASE_DIR,
    "data",
    "cleaned",
    "sales_cleaned.csv"
)


# ==============================
# Check File Exists
# ==============================

if not os.path.exists(file_path):

    print("❌ ERROR: Cleaned dataset not found.")

    print(
        f"Expected file:\n{file_path}"
    )

    sys.exit(1)


# ==============================
# Load Dataset
# ==============================

try:

    sales = pd.read_csv(
        file_path,
        parse_dates=["Order_Date"]
    )

except Exception as e:

    print("❌ ERROR: Unable to read the dataset.")

    print(
        f"Reason: {e}"
    )

    sys.exit(1)


# ==============================
# Check Empty Dataset
# ==============================

if sales.empty:

    print("❌ ERROR: Dataset is empty.")

    sys.exit(1)


# ==============================
# Validation Report
# ==============================

print("=" * 50)
print("DATA VALIDATION REPORT")
print("=" * 50)


# ==============================
# Required Columns
# ==============================

required_columns = [
    "Order_ID",
    "Order_Date",
    "Customer_ID",
    "Customer_Name",
    "City",
    "State",
    "Region",
    "Product",
    "Category",
    "Quantity",
    "Unit_Price",
    "Discount",
    "Sales",
    "Profit"
]


print("\n1. REQUIRED COLUMN VALIDATION")

missing_columns = [
    column
    for column in required_columns
    if column not in sales.columns
]

if missing_columns:

    print("❌ Missing required columns:")

    for column in missing_columns:

        print(
            f"   - {column}"
        )

    sys.exit(1)

else:

    print(
        "✅ All required columns are present."
    )


# ==============================
# Dataset Size
# ==============================

print("\n2. DATASET SIZE")

print(
    f"Rows    : {sales.shape[0]}"
)

print(
    f"Columns : {sales.shape[1]}"
)


# ==============================
# Missing Values
# ==============================

print("\n3. MISSING VALUES")

missing_values = sales.isnull().sum()

missing_values = missing_values[
    missing_values > 0
]

if missing_values.empty:

    print(
        "✅ No missing values found."
    )

else:

    print(
        "⚠️ Missing values found:"
    )

    print(
        missing_values
    )


# ==============================
# Duplicate Orders
# ==============================

print("\n4. DUPLICATE ORDERS")

duplicate_orders = (
    sales["Order_ID"].duplicated().sum()
)

if duplicate_orders == 0:

    print(
        "✅ No duplicate Order_ID values found."
    )

else:

    print(
        f"⚠️ Duplicate Order_ID values: "
        f"{duplicate_orders}"
    )


# ==============================
# Sales Validation
# ==============================

print("\n5. SALES VALIDATION")

invalid_sales = (
    sales["Sales"] <= 0
).sum()

if invalid_sales == 0:

    print(
        "✅ All Sales values are valid."
    )

else:

    print(
        f"⚠️ Invalid Sales values: "
        f"{invalid_sales}"
    )


# ==============================
# Quantity Validation
# ==============================

print("\n6. QUANTITY VALIDATION")

invalid_quantity = (
    sales["Quantity"] <= 0
).sum()

if invalid_quantity == 0:

    print(
        "✅ All Quantity values are valid."
    )

else:

    print(
        f"⚠️ Invalid Quantity values: "
        f"{invalid_quantity}"
    )


# ==============================
# Date Validation
# ==============================

print("\n7. DATE VALIDATION")

invalid_dates = (
    sales["Order_Date"].isnull().sum()
)

if invalid_dates == 0:

    print(
        "✅ All Order_Date values are valid."
    )

else:

    print(
        f"⚠️ Invalid dates: "
        f"{invalid_dates}"
    )


# ==============================
# Profit Validation
# ==============================

print("\n8. PROFIT VALIDATION")

invalid_profit = (
    sales["Profit"].isnull().sum()
)

if invalid_profit == 0:

    print(
        "✅ Profit values are available."
    )

else:

    print(
        f"⚠️ Missing Profit values: "
        f"{invalid_profit}"
    )


# ==============================
# Data Types
# ==============================

print("\n9. DATA TYPES")

print(
    sales.dtypes
)


# ==============================
# Final Report
# ==============================

print("\n" + "=" * 50)

print(
    "✅ DATA VALIDATION COMPLETED SUCCESSFULLY"
)

print("=" * 50)