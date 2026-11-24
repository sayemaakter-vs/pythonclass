delivery_1 = {"pen": 12, "book": 5, "bag": 2}
delivery_2 = {"book": 4, "ruler": 10, "pen": 3}

combined_delivery = {}

for item, quantity in delivery_1.items():
    combined_delivery[item] = quantity

for item, quantity in delivery_2.items():
    if item in combined_delivery:
        combined_delivery[item] += quantity
    else:
        combined_delivery[item] = quantity

grand_total = sum(combined_delivery.values())

print("Combined delivery:", combined_delivery)
print("Grand total:", grand_total)