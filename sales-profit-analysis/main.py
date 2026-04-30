# =====================================================
# RETAIL SALES & PROFIT ANALYSIS PROJECT
# =====================================================

# =========================
# IMPORT LIBRARIES
# =========================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# =========================
# LOAD DATASET
# =========================

df = pd.read_csv('data/superstore.csv', encoding='latin1')


# =========================
# BASIC DATA INSPECTION
# =========================

print("\n========== DATASET INFO ==========\n")

print("First 5 Rows:\n")
print(df.head())

print("\nDataset Shape:\n")
print(df.shape)

print("\nColumn Names:\n")
print(df.columns)

print("\nDataset Information:\n")
print(df.info())

print("\nSummary Statistics:\n")
print(df.describe())

print("\nMissing Values:\n")
print(df.isnull().sum())


# =========================
# DATA CLEANING
# =========================

print("\n========== DATA CLEANING ==========\n")

# 1. Remove duplicates
df.drop_duplicates(inplace=True)

# 2. Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# 3. Fill missing values
df['Postal Code'] = df['Postal Code'].fillna(
    df['Postal Code'].median()
)

print("Data Cleaning Completed")



# =========================
# FEATURE ENGINEERING
# =========================
 
print("\n========== FEATURE ENGINEERING ==========\n")
 
# 1. Order Month
df['Order Month'] = df['Order Date'].dt.month_name()
 
# 2. Order Year
df['Order Year'] = df['Order Date'].dt.year
 
# 3. Profit Margin
df['Profit Margin'] = (
    df['Profit'] / df['Sales']
) * 100
 
# 4. Sales Category
df['Sales Category'] = np.where(
    df['Sales'] > 500,
    'High Sales',
    'Low Sales'
)
 
print(df[['Order Month',
          'Order Year',
          'Profit Margin',
          'Sales Category']].head())
 
 
# =====================================================
# ANALYSIS 1 : REGION-WISE SALES
# SUBGROUP COMPARISON
# =====================================================
 
print("\n========== ANALYSIS 1 : REGION SALES ==========\n")
 
region_sales = df.groupby('Region')['Sales'].sum() \
                 .sort_values(ascending=False)
 
print(region_sales)
 
 
# =====================================================
# ANALYSIS 2 : CATEGORY-WISE PROFIT
# SUBGROUP COMPARISON
# =====================================================
 
print("\n========== ANALYSIS 2 : CATEGORY PROFIT ==========\n")
 
category_profit = df.groupby('Category')['Profit'].sum() \
                    .sort_values(ascending=False)
 
print(category_profit)
 
 
# =====================================================
# ANALYSIS 3 : CUSTOMER SEGMENT SALES
# =====================================================
 
print("\n========== ANALYSIS 3 : SEGMENT SALES ==========\n")
 
segment_sales = df.groupby('Segment')['Sales'].sum()
 
print(segment_sales)


# =====================================================
# ANALYSIS 4 : MONTHLY SALES TREND
# =====================================================

print("\n========== ANALYSIS 4 : MONTHLY SALES ==========\n")

monthly_sales = df.groupby(
    df['Order Date'].dt.month
)['Sales'].sum()

print(monthly_sales)


# =====================================================
# ANALYSIS 5 : OUTLIER ANALYSIS USING NUMPY
# =====================================================

print("\n========== ANALYSIS 5 : OUTLIER ANALYSIS ==========\n")

sales_mean = np.mean(df['Sales'])
sales_std = np.std(df['Sales'])

z_scores = (
    df['Sales'] - sales_mean
) / sales_std

outliers = df[np.abs(z_scores) > 3]

print(outliers[['Sales', 'Profit']])


# =====================================================
# ANALYSIS 6 : RELATIONSHIP ANALYSIS
# =====================================================

print("\n========== ANALYSIS 6 : SALES & PROFIT RELATIONSHIP ==========\n")

correlation = df['Sales'].corr(df['Profit'])

print("Correlation Between Sales and Profit:")
print(correlation)

