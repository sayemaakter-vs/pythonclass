products = {
    "rice": 75,
    "milk": 90,
    "bread": 55,
    "egg": 15,
    "apple": 180,
    "oil": 190,
    "sugar": 130,
    "salt": 45,
    "soap": 60,
    "tea": 220
}

order = {}

print("Available Products:")

for product, price in products.items():
    print(product, ":", price)

while True:
    name = input("Enter product name (or done to finish): ").lower()

    if name == "done":
        break

    if name not in products:
        print("Product not available")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Invalid quantity")
        continue

    order[name] = order.get(name, 0) + quantity

grand_total = 0

print("\nItemised Bill")
print("Product  Price  Quantity  Total")

for product, quantity in order.items():
    price = products[product]
    total = price * quantity

    print(product, price, quantity, total)

    grand_total += total

print("Grand Total:", grand_total)