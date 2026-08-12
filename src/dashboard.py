import pandas as pd
import os
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ==============================
# Load Dataset
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

sales = pd.read_csv(
    file_path,
    parse_dates=["Order_Date"]
)


# ==============================
# Dashboard Window
# ==============================

root = tk.Tk()

root.title("Sales Intelligence Dashboard")

root.geometry("1200x900")


# ==============================
# Region and Chart Variables
# ==============================

regions = ["All"] + sorted(
    sales["Region"].unique().tolist()
)

charts = [
    "All Charts",
    "Sales by Category",
    "Monthly Sales Trend",
    "Sales Distribution",
    "Sales Histogram",
    "Profit by Category",
    "Profit Margin by Category",
    "Sales by Region",
    "Profit by Region"
]

selected_region = tk.StringVar(root)
selected_region.set("All")

selected_chart = tk.StringVar(root)
selected_chart.set("All Charts")


# ==============================
# Title
# ==============================

title = tk.Label(
    root,
    text="Sales Intelligence & Business Analytics Dashboard",
    font=("Arial", 20, "bold")
)

title.pack(pady=15)


# ==============================
# Filter Frame
# ==============================

filter_frame = tk.Frame(root)

filter_frame.pack(pady=5)


region_label = tk.Label(
    filter_frame,
    text="Select Region:",
    font=("Arial", 12)
)

region_label.grid(
    row=0,
    column=0,
    padx=10
)

region_menu = tk.OptionMenu(
    filter_frame,
    selected_region,
    *regions
)

region_menu.grid(
    row=0,
    column=1
)


chart_label = tk.Label(
    filter_frame,
    text="Select Chart:",
    font=("Arial", 12)
)

chart_label.grid(
    row=0,
    column=2,
    padx=10
)

chart_menu = tk.OptionMenu(
    filter_frame,
    selected_chart,
    *charts
)

chart_menu.grid(
    row=0,
    column=3
)


# ==============================
# KPI Frame
# ==============================

kpi_frame = tk.Frame(root)

kpi_frame.pack(pady=10)


sales_card = tk.Label(
    kpi_frame,
    font=("Arial", 14, "bold"),
    relief="solid",
    padx=20,
    pady=15
)

sales_card.grid(
    row=0,
    column=0,
    padx=10
)


profit_card = tk.Label(
    kpi_frame,
    font=("Arial", 14, "bold"),
    relief="solid",
    padx=20,
    pady=15
)

profit_card.grid(
    row=0,
    column=1,
    padx=10
)


average_card = tk.Label(
    kpi_frame,
    font=("Arial", 14, "bold"),
    relief="solid",
    padx=20,
    pady=15
)

average_card.grid(
    row=0,
    column=2,
    padx=10
)


orders_card = tk.Label(
    kpi_frame,
    font=("Arial", 14, "bold"),
    relief="solid",
    padx=20,
    pady=15
)

orders_card.grid(
    row=0,
    column=3,
    padx=10
)


# ==============================
# Top 5 Products Frame
# ==============================

products_frame = tk.Frame(
    root,
    height=220
)

products_frame.pack(
    fill="x",
    padx=20,
    pady=5
)

products_frame.pack_propagate(False)


# ==============================
# Main Chart Frame
# ==============================

chart_frame = tk.Frame(
    root,
    height=300
)

chart_frame.pack(
    fill="x",
    padx=20,
    pady=5
)

chart_frame.pack_propagate(False)


# ==============================
# Get Filtered Data
# ==============================

def get_filtered_sales():

    region = selected_region.get()

    if region == "All":

        return sales

    return sales[
        sales["Region"] == region
    ]


# ==============================
# Top 5 Products Chart
# ==============================

def top_5_products_chart():

    filtered_sales = get_filtered_sales()

    top_5_products = (
        filtered_sales
        .groupby("Product")["Sales"]
        .sum()
        .sort_values(ascending=True)
        .tail(5)
    )

    fig, ax = plt.subplots(
        figsize=(10, 2.5)
    )

    top_5_products.plot(
        kind="barh",
        ax=ax
    )

    ax.set_title(
        "Top 5 Products by Sales"
    )

    ax.set_xlabel(
        "Total Sales"
    )

    ax.set_ylabel(
        "Product"
    )

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(
        fig,
        master=products_frame
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )


# ==============================
# Clear Products Chart
# ==============================

def clear_products_chart():

    for widget in products_frame.winfo_children():

        widget.destroy()

    plt.close("all")


# ==============================
# Clear Main Chart
# ==============================

def clear_chart():

    for widget in chart_frame.winfo_children():

        widget.destroy()

    plt.close("all")


# ==============================
# Update Dashboard
# ==============================

def filter_data(*args):

    filtered_sales = get_filtered_sales()

    # ==============================
    # KPIs
    # ==============================

    total_sales = filtered_sales["Sales"].sum()

    total_profit = filtered_sales["Profit"].sum()

    average_sales = filtered_sales["Sales"].mean()

    total_orders = filtered_sales.shape[0]

    # ==============================
    # Update KPI Cards
    # ==============================

    sales_card.config(
        text=f"Total Sales\n₹{total_sales:,.2f}"
    )

    profit_card.config(
        text=f"Total Profit\n₹{total_profit:,.2f}"
    )

    average_card.config(
        text=f"Average Sales\n₹{average_sales:,.2f}"
    )

    orders_card.config(
        text=f"Total Orders\n{total_orders:,}"
    )

    # ==============================
    # Update Top 5 Products
    # ==============================

    clear_products_chart()

    top_5_products_chart()

    # ==============================
    # Update Selected Chart
    # ==============================

    if selected_chart.get() != "All Charts":

        show_charts()


# ==============================
# Sales by Category
# ==============================

def sales_by_category():

    filtered_sales = get_filtered_sales()

    category_sales = (
        filtered_sales
        .groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(
        figsize=(9, 3.5)
    )

    category_sales.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(
        "Sales by Category"
    )

    ax.set_xlabel(
        "Category"
    )

    ax.set_ylabel(
        "Total Sales"
    )

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(
        fig,
        master=chart_frame
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )


# ==============================
# Monthly Sales Trend
# ==============================

def monthly_sales_trend():

    filtered_sales = get_filtered_sales()

    monthly_sales = (
        filtered_sales
        .groupby(
            filtered_sales["Order_Date"].dt.to_period("M")
        )["Sales"]
        .sum()
    )

    fig, ax = plt.subplots(
        figsize=(9, 3.5)
    )

    monthly_sales.plot(
        kind="line",
        marker="o",
        ax=ax
    )

    ax.set_title(
        "Monthly Sales Trend"
    )

    ax.set_xlabel(
        "Month"
    )

    ax.set_ylabel(
        "Sales"
    )

    ax.grid(True)

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(
        fig,
        master=chart_frame
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )


# ==============================
# Sales Distribution
# ==============================

def sales_distribution():

    filtered_sales = get_filtered_sales()

    category_sales = (
        filtered_sales
        .groupby("Category")["Sales"]
        .sum()
    )

    fig, ax = plt.subplots(
        figsize=(7, 3.5)
    )

    category_sales.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90,
        ax=ax
    )

    ax.set_title(
        "Sales Distribution by Category"
    )

    ax.set_ylabel("")

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(
        fig,
        master=chart_frame
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )


# ==============================
# Sales Histogram
# ==============================

def sales_histogram():

    filtered_sales = get_filtered_sales()

    fig, ax = plt.subplots(
        figsize=(9, 3.5)
    )

    ax.hist(
        filtered_sales["Sales"],
        bins=20
    )

    ax.set_title(
        "Sales Distribution"
    )

    ax.set_xlabel(
        "Sales"
    )

    ax.set_ylabel(
        "Number of Orders"
    )

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(
        fig,
        master=chart_frame
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )


# ==============================
# Profit by Category
# ==============================

def profit_by_category():

    filtered_sales = get_filtered_sales()

    category_profit = (
        filtered_sales
        .groupby("Category")["Profit"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(
        figsize=(9, 3.5)
    )

    category_profit.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(
        "Profit by Category"
    )

    ax.set_xlabel(
        "Category"
    )

    ax.set_ylabel(
        "Total Profit"
    )

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(
        fig,
        master=chart_frame
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )


# ==============================
# Profit Margin by Category
# ==============================

def profit_margin_by_category():

    filtered_sales = get_filtered_sales()

    category_data = (
        filtered_sales
        .groupby("Category")
        .agg({
            "Sales": "sum",
            "Profit": "sum"
        })
    )

    category_data["Profit_Margin"] = (
        category_data["Profit"]
        / category_data["Sales"]
        * 100
    )

    category_margin = (
        category_data["Profit_Margin"]
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(
        figsize=(9, 3.5)
    )

    category_margin.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(
        "Profit Margin by Category"
    )

    ax.set_xlabel(
        "Category"
    )

    ax.set_ylabel(
        "Profit Margin (%)"
    )

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(
        fig,
        master=chart_frame
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )


# ==============================
# Sales by Region
# ==============================

def sales_by_region():

    region_sales = (
        sales
        .groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(
        figsize=(9, 3.5)
    )

    region_sales.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(
        "Sales by Region"
    )

    ax.set_xlabel(
        "Region"
    )

    ax.set_ylabel(
        "Total Sales"
    )

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(
        fig,
        master=chart_frame
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )


# ==============================
# Profit by Region
# ==============================

def profit_by_region():

    region_profit = (
        sales
        .groupby("Region")["Profit"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(
        figsize=(9, 3.5)
    )

    region_profit.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(
        "Profit by Region"
    )

    ax.set_xlabel(
        "Region"
    )

    ax.set_ylabel(
        "Total Profit"
    )

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(
        fig,
        master=chart_frame
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )


# ==============================
# Show Selected Chart
# ==============================

def show_charts():

    clear_chart()

    selected = selected_chart.get()

    if selected == "Sales by Category":

        sales_by_category()

    elif selected == "Monthly Sales Trend":

        monthly_sales_trend()

    elif selected == "Sales Distribution":

        sales_distribution()

    elif selected == "Sales Histogram":

        sales_histogram()

    elif selected == "Profit by Category":

        profit_by_category()

    elif selected == "Profit Margin by Category":

        profit_margin_by_category()

    elif selected == "Sales by Region":

        sales_by_region()

    elif selected == "Profit by Region":

        profit_by_region()

    else:

        clear_chart()


# ==============================
# Chart Dropdown Auto Update
# ==============================

def chart_changed(*args):

    if selected_chart.get() != "All Charts":

        show_charts()

    else:

        clear_chart()


# ==============================
# Refresh Dashboard
# ==============================

def refresh_dashboard():

    selected_region.set("All")

    selected_chart.set("All Charts")

    clear_products_chart()

    clear_chart()

    top_5_products_chart()


# ==============================
# Connect Filters
# ==============================

selected_region.trace_add(
    "write",
    filter_data
)

selected_chart.trace_add(
    "write",
    chart_changed
)


# ==============================
# Buttons
# ==============================

button_frame = tk.Frame(root)

button_frame.pack(
    pady=10
)


show_button = tk.Button(
    button_frame,
    text="Show Chart",
    font=("Arial", 12),
    width=15,
    command=show_charts
)

show_button.grid(
    row=0,
    column=0,
    padx=10
)


refresh_button = tk.Button(
    button_frame,
    text="Refresh",
    font=("Arial", 12),
    width=15,
    command=refresh_dashboard
)

refresh_button.grid(
    row=0,
    column=1,
    padx=10
)


exit_button = tk.Button(
    button_frame,
    text="Exit",
    font=("Arial", 12),
    width=15,
    command=root.destroy
)

exit_button.grid(
    row=0,
    column=2,
    padx=10
)


# ==============================
# Initial Dashboard Display
# ==============================

filter_data()


# ==============================
# Run Dashboard
# ==============================

root.mainloop()