import pandas as pd
import re

sales_df = pd.read_csv('sales.csv')
products_df = pd.read_csv('products.csv')

print(sales_df)
print(products_df)

# Data Tranformation Task 1
print("TASK ONE")
sales_df['product_code'] = sales_df['description'].str.extract(r'\b([A-Z]{2}-\d{4}-[A-Z]{2})\b')
print(sales_df[['description', 'product_code']])  

# Pattern Matching Task 2

print("TASK TWO")
# Merge sales_df with products_df on product_code
merged_df = sales_df.merge(products_df, on='product_code', how='left')
print(merged_df[['product_code', 'product_name']])  


# Analysis Task 3
print("Task 3")

# Group by category and calculate total sales_amount
summary_table = merged_df.groupby('category')['amount'].sum().reset_index()
print(summary_table)  



