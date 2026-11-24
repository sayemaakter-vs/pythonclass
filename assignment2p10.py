sales = [
    {"product": "Pen", "quantity": 3, "price": 15},
    {"product": "Book", "quantity": 2, "price": 120},
    {"product": "Pen", "quantity": 5, "price": 15},
    {"product": "Bag", "quantity": 1, "price": 850},
    {"product": "Book", "quantity": -1, "price": 120},
    {"product": "Ruler", "quantity": 4, "price": 20}
]

product_revenue = {}
total_revenue = 0
high_revenue_transactions = []
invalid_records = 0

for sale in sales:
    product = sale["product"]
    quantity = sale["quantity"]
    price = sale["price"]

    if quantity <= 0 or price < 0:
        invalid_records += 1
        continue

    revenue = quantity * price

    if product in product_revenue:
        product_revenue[product] += revenue
    else:
        product_revenue[product] = revenue

    total_revenue += revenue

    if revenue >= 200:
        high_revenue_transactions.append(sale)

highest_product = max(product_revenue, key=product_revenue.get)
highest_revenue = product_revenue[highest_product]

print("Revenue by product:", product_revenue)
print(f"Total revenue: Tk {total_revenue:.2f}")
print("Highest revenue product:", highest_product)
print(f"Highest product revenue: Tk {highest_revenue:.2f}")
print("High-revenue transactions:", high_revenue_transactions)
print("Invalid records:", invalid_records)