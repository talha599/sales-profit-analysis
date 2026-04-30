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


