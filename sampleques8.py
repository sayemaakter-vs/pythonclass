import numpy as np

sales = np.array([
    [120, 150, 135, 170],
    [80, 95, 110, 105],
    [200, 180, 220, 240]
])

product_total = np.sum(sales, axis=1)
print("Total sales of each product:", product_total)

month_total = np.sum(sales, axis=0)
print("Total sales of each month:", month_total)

highest_product = np.argmax(product_total) + 1
print("Product with highest total sales: Product", highest_product)

lowest_month = np.argmin(month_total) + 1
print("Month with lowest total sales: Month", lowest_month)

modified_sales = sales.copy()
modified_sales[modified_sales < 100] = 0

print("Original array:")
print(sales)

print("Modified array:")
print(modified_sales)