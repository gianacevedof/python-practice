# dictionaries are values that have inner values {key}: {value}
# E.g. Countries have capitals - we can make the following dictionary 'USA: Washington D.C.', 'Japan: Tokyo', etc...

# capitals = {
#     "USA": "Washington",
#     "Dominican Republic": "Santo Domingo",
#     "Russia": "Moscow",
#     "India": "New Delhi",
#     "China": "Beijing"
# }

# print(capitals)

# for key, values in capitals.items():
#     print(f"{key}: {values}")

# ====================================
#               PROJECT
# ====================================

# This is a program that displays a food menu, asks you to select your food, and gives you a final price.

menu = {
    "Pizza": 3.25,
    "Burger": 4.50,
    "Hotdog": 2.55,
    "Yogurt": 3,
    "Popcorn": 2.50,
    "Coke": 2,
    "Water": 1,
    "Lemonade": 3
}
cart = []
total = 0

print("Hello, this is Gian's Cafe!")
print("**When selecting from the menu, press 'q' to quit.")
# this displays the menu
print("-------- MENU --------")
for key, value in menu.items():
    print(f"{key:15} ${value:.2f}")
print("----------------------")

# loop to ask the user for input
while True:
    choice = input("What would like to have? ").capitalize()
    if choice == "Q":
        break

    # as long as the 'choice' is not 'none'
    # user's choice will be appended to the cart array to be stored
    if menu.get(choice) is not None:
        cart.append(choice)
    else:
        print("Sorry, we don't have that.")

# calculating final price for everything
for choice in cart:
    total += menu.get(choice)

# displaying the cart and total price
print("------ Your cart ------")
for item in cart:
    print(f"- {item}")
print(f"Your total is ${total:.2f}")
print("-----------------------")
