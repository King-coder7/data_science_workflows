import pandas as pd
import matplotlib.pyplot as plt

# --- STEP 1: LOAD THE DATA ---
# Ensure your Nike CSV file is in the same folder as this script
try:
    df = pd.read_csv('nike_sales.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'nike_sales.csv' not found. Please check the filename.")
    exit()

# --- STEP 2: DATA CLEANING (Wednesday Goal / Risk 1 Action Plan) ---
# [cite: 19, 24, 25]
# Clean column names by stripping hidden leading/trailing spaces
df.columns = df.columns.str.strip()

# Fix the Date formatting issue (Risk 1: Inconsistent formatting) [cite: 23]
# Using dayfirst=True because your data uses the DD-MM-YYYY format
df['Invoice Date'] = pd.to_datetime(df['Invoice Date'], dayfirst=True)

# Handle potential null values (Risk 1: Missing data) [cite: 22, 25]
df = df.dropna(subset=['Product', 'Total Sales'])

# --- STEP 3: AGGREGATION (Thursday Goal / Question 1) ---
# [cite: 13, 19]
# Which product category generates the highest total revenue?
revenue_by_product = df.groupby('Product')['Total Sales'].sum().sort_values(ascending=False)

print("\n--- Question 1: Total Revenue by Product Category ---")
print(revenue_by_product)
print(f"\nTop Performer: {revenue_by_product.index[0]} at ${revenue_by_product.iloc[0]:,.2f}")

# --- STEP 4: STATISTICAL ANALYSIS (Friday Goal / Question 2) ---
# [cite: 14, 19]
# Is there a correlation between the time of day and the volume of sales?
df['Hour'] = df['Invoice Date'].dt.hour
hourly_volume = df.groupby('Hour')['Units Sold'].sum()

print("\n--- Question 2: Sales Volume by Hour ---")
print(hourly_volume)

# Calculate statistical correlation
# Note: If timestamps are all identical (e.g., 00:00), correlation will be NaN
correlation = df['Hour'].corr(df['Total Sales'])
print(f"\nCorrelation between Hour of Day and Sales Revenue: {correlation:.4f}")

# --- STEP 5: VISUALIZATION (Stretch Challenge) ---
# 
# Generate a bar chart visualizing the revenue distribution
plt.figure(figsize=(12, 7))
revenue_by_product.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Nike Revenue Distribution by Product Category', fontsize=14)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xlabel('Product Category', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the plot for your demo video 
plt.tight_layout()
plt.savefig('nike_revenue_analysis.png')
print("\nStretch Challenge: Chart saved as 'nike_revenue_analysis.png'")

# Display the plot
plt.show()