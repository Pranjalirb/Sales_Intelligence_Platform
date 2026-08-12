import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

# ==============================
# Load Dataset
# ==============================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

visual_path = os.path.join(BASE_DIR, "visuals")

os.makedirs(visual_path, exist_ok=True)

file_path = os.path.join(
    BASE_DIR,
    "data",
    "cleaned",
    "sales_cleaned.csv"
)

sales = pd.read_csv(
    file_path,
    parse_dates=["Order_Date"]
)

# ==============================
# Region Filter
# ==============================

if len(sys.argv) > 1:
    selected_region = sys.argv[1]
else:
    selected_region = "All"

if selected_region != "All":
    sales = sales[sales["Region"] == selected_region]

# ==============================
# Chart Selection
# ==============================

if len(sys.argv) > 2:
    selected_chart = sys.argv[2]
else:
    selected_chart = "All Charts"


# ==============================
# Sales by Category
# ==============================

def sales_by_category():

    category_sales = (
        sales.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 6))

    category_sales.plot(kind="bar")

    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            visual_path,
            "sales_by_category.png"
        )
    )

    plt.show()


# ==============================
# Monthly Sales Trend
# ==============================

def monthly_sales_trend():

    monthly_sales = (
        sales.groupby(
            sales["Order_Date"].dt.to_period("M")
        )["Sales"]
        .sum()
    )

    plt.figure(figsize=(10, 6))

    monthly_sales.plot(
        kind="line",
        marker="o"
    )

    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            visual_path,
            "monthly_sales_trend.png"
        )
    )

    plt.show()


# ==============================
# Sales Distribution by Category
# ==============================

def sales_distribution():

    category_sales = (
        sales.groupby("Category")["Sales"]
        .sum()
    )

    plt.figure(figsize=(8, 8))

    category_sales.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Sales Distribution by Category")

    plt.axis("equal")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            visual_path,
            "sales_distribution.png"
        )
    )

    plt.show()


# ==============================
# Sales Distribution Histogram
# ==============================

def sales_histogram():

    plt.figure(figsize=(10, 6))

    plt.hist(
        sales["Sales"],
        bins=20
    )

    plt.title("Sales Distribution")
    plt.xlabel("Sales")
    plt.ylabel("Number of Orders")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            visual_path,
            "sales_distribution_histogram.png"
        )
    )

    plt.show()


# ==============================
# Run Selected Chart
# ==============================

if selected_chart == "Sales by Category":

    sales_by_category()

elif selected_chart == "Monthly Sales Trend":

    monthly_sales_trend()

elif selected_chart == "Sales Distribution":

    sales_distribution()

elif selected_chart == "Sales Histogram":

    sales_histogram()

else:

    sales_by_category()
    monthly_sales_trend()
    sales_distribution()
    sales_histogram()