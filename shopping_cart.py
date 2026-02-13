items = []
prices = []
total = 0

print("Welcome to your Shopping Cart!")

while True:
    item = input("Enter your item (q to quit): ")

    if item.lower() == "q":
        break
    else:
        price = float(input("Enter its price: $"))
        items.append(item)
        prices.append(price)

print("\n===== YOUR SHOPPING CART =====")

for item in items:
    print(f"- {item}")

for price in prices:
    total += price

print(f"The total is ${total:.2f}")
print("Thanks you for using our shopping cart!")