stock = {"pen": 12, "book": 3, "bag": 2,
         "ruler": 9, "calculator": 1}

total_units = 0
low_stock = {}

for item, quantity in stock.items():
    total_units += quantity

    if quantity < 5:
        low_stock[item] = quantity

print("Total units:", total_units)
print("Low stock:", low_stock)