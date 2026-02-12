import pandas as pd
import numpy as np

df = pd.read_csv("Assignment\\DAY22\\Question2\\sales.csv", sep="\t")
print("Orginal Data:")
print(df)

df["Total"] = df["Quantity"] * df["Price"]

print("\n Data with Total column:")
print(df)


total_sales = np.sum(df["Total"])

average_daily_sales = np.mean(df["Total"])

std_daily_sales = np.std(df["Total"])

print("\nSales Statistics:")
print("Total Sales:", total_sales)
print("Average Daily Sales:", average_daily_sales)
print("Standard Deviation of Daily Sales:", std_daily_sales)


product_quantity = df.groupby("Product")["Quantity"].sum()

best_selling_product = product_quantity.idxmax()
max_quantity = product_quantity.max()

print("\nBest-Selling Product:")
print("Product:", best_selling_product)
print("Total Quantity Sold:", max_quantity)