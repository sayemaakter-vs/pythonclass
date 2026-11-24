prices = {
    "rice": 80,
    "oil": 180,
    "sugar": 120,
    "milk": 90,
    "bread": 50,
    "eggs": 12,
    "flour": 60,
    "salt": 30,
    "tea": 150,
    "coffee": 250,
    "soap": 40,
    "shampoo": 200,
    "biscuits": 30,
    "juice": 100,
    "butter": 220
}

order = {}

n = int(input("Enter number of products: "))

for i in range(n):
    product = input("Enter product name: ").lower()
    quantity = int(input("Enter quantity: "))

    if product in prices and quantity > 0:
        order[product] = order.get(product, 0) + quantity
    else:
        print("Invalid product or quantity")

bill = {}
subtotal = 0

for product, quantity in order.items():
    total = prices[product] * quantity

    bill[product] = {
        "quantity": quantity,
        "unit_price": prices[product],
        "total": total
    }

    subtotal += total

discount = 0

if subtotal >= 1000:
    discount = subtotal * 0.05

vat = (subtotal - discount) * 0.02
final_amount = subtotal - discount + vat

print("\nGROCERY BILL")
print("Product\tQuantity\tPrice\tTotal")

for product, details in bill.items():
    print(product, "\t", details["quantity"], "\t\t", details["unit_price"], "\t", details["total"])

print("\nSubtotal:", subtotal)
print("Discount:", discount)
print("VAT:", vat)
print("Final Amount:", final_amount)