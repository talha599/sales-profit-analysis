# Retail Sales & Profit Analysis Project

## Project Overview

This project analyzes a retail sales dataset using:

* Pandas
* NumPy
* Matplotlib

The main goal of the project is to identify business insights related to:

* Sales performance
* Profit trends
* Customer segments
* Product categories
* Regional performance

The project follows the requirements of a complete data analysis project using Python.

---

# Dataset Information

## Dataset Name

Sample Superstore Dataset

## Dataset Source

Kaggle Superstore Dataset

Dataset Link:

[https://www.kaggle.com/datasets/vivek468/superstore-dataset-final](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)

---

# Dataset Features

* 9994+ Rows
* 21+ Columns
* Numerical Data
* Categorical Data
* Date Columns

Main columns include:

* Order Date
* Region
* Category
* Segment
* Sales
* Profit
* Quantity
* Discount

---

# Technologies Used

| Technology       | Purpose               |
| ---------------- | --------------------- |
| Python           | Programming Language  |
| Pandas           | Data Analysis         |
| NumPy            | Numerical Computation |
| Matplotlib       | Data Visualization    |
| Jupyter Notebook | Interactive Analysis  |

---

# Project Structure

```text
sales-profit-analysis/
│
├── data/
│   └── superstore.csv
│
├── figures/
│   ├── sales_by_region.png
│   ├── monthly_sales_trend.png
│   ├── profit_distribution.png
│   └── sales_vs_profit.png
│
├── notebook.ipynb
├── main.py
├── report.docx
└── README.md
```

---

# Features of This Project

## Data Cleaning

* Removed duplicate records
* Converted date columns
* Handled missing values

---

## Feature Engineering

Created new features:

* Order Month
* Order Year
* Profit Margin
* Sales Category

---

## Analysis Performed

1. Region-wise sales analysis
2. Category-wise profit analysis
3. Customer segment analysis
4. Monthly sales trend analysis
5. Outlier detection using NumPy
6. Sales and profit relationship analysis

---

# Visualizations

The project includes 4 Matplotlib visualizations:

| Chart               | Type         |
| ------------------- | ------------ |
| Sales by Region     | Bar Chart    |
| Monthly Sales Trend | Line Chart   |
| Profit Distribution | Histogram    |
| Sales vs Profit     | Scatter Plot |

Generated charts are saved inside the `figures/` folder.

---

# Installation Guide

## Step 1: Install Python

Download Python:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

---

## Step 2: Install Required Libraries

Run this command in terminal:

```bash
pip install pandas numpy matplotlib
```

---

# How to Run the Project

## Run Python File

```bash
python main.py
```

---

# Output

After running the project:

* Analysis results will appear in terminal
* Charts will be generated automatically
* PNG files will be saved in the `figures/` folder

---

# Research Questions

1. Which region generates the highest sales?
2. Which category is most profitable?
3. Is there a relationship between sales and profit?
4. Which customer segment contributes the most sales?
5. Are there any unusual sales outliers?

---

# Key Findings

1. West region generated the highest sales.
2. Technology category produced the highest profit.
3. Consumer segment contributed the most sales.
4. Some high sales produced low profit.
5. Positive relationship exists between sales and profit.
6. Several unusual sales outliers were detected.

---

# NumPy Usage

NumPy was used for:

* Mean calculation
* Standard deviation
* Z-score outlier analysis
* Conditional classification using `np.where()`

Outlier Formula:

genui{"math_block_widget_always_prefetch_v2":{"content":"z=\frac{x-\mu}{\sigma}"}}

---

# Files Description

| File             | Purpose                  |
| ---------------- | ------------------------ |
| `main.py`        | Main Python project file |
| `notebook.ipynb` | Interactive notebook     |
| `report.docx`    | Final project report     |
| `superstore.csv` | Dataset file             |
| `figures/`       | Generated charts         |

---

# Author Information

## Student Name

MHAMMAD TALHA ISLAM

## Student ID

22-49599-3

## Student Name

WAFA

## Student ID

22-49542-3

## Course

PROGRAMMING IN PYTHON

---

# Conclusion

This project successfully demonstrates data analysis using Pandas, NumPy, and Matplotlib. The analysis provides meaningful business insights related to sales, profit, customer behavior, and product performance.

The project also demonstrates:

* Data cleaning
* Feature engineering
* Numerical analysis
* Data visualization
* Business interpretation
