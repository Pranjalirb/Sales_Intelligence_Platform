import pandas as pd
import os

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build file path
file_path = os.path.join(BASE_DIR, "data", "raw", "sales.csv")

# Load dataset
sales = pd.read_csv(file_path, parse_dates=["Order_Date"])

# First 5 rows
print("First 5 Rows:")
print(sales.head())

# Dataset info
print("\nDataset Info:")
sales.info()

# Summary statistics
print("\nSummary Statistics:")
print(sales.describe())

# Shape
print("\nShape:")
print(sales.shape)

# Missing values
print("\n========== Missing Values ==========")
print(sales.isnull().sum())

# Duplicate rows
print("\n========== Duplicate Rows ==========")
print(sales.duplicated().sum())

# Data types
print("\n========== Data Types ==========")
print(sales.dtypes)

# Unique values
print("\n========== Unique Values ==========")
print("Cities:", sales["City"].nunique())
print("States:", sales["State"].nunique())
print("Regions:", sales["Region"].nunique())
print("Products:", sales["Product"].nunique())
print("Categories:", sales["Category"].nunique())

# Save cleaned dataset
cleaned_path = os.path.join(BASE_DIR, "data", "cleaned", "sales_cleaned.csv")

sales.to_csv(cleaned_path, index=False)

print("\n✅ Cleaned dataset saved successfully!")



