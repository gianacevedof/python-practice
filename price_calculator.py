print("Hello! \nTo calculate the total cost of your purchase,")

item = input("please enter below the item you would like to buy: ")
price = float(input("What's the price of your item:"))
quantity = int(input("How many items would you like?"))

total = price * quantity

print(f"You have bought {quantity} {item}/s. The total cost of your purchase"
      f" will be ${total:.2f}.")