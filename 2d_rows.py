# meats = ["Pork", "Beef", "Chicken"]
# fruits = ["Banana", "Apple", "Strawberry"]
# drinks = ["Water", "Soda", "Juice"]
# groceries = [meats, fruits, drinks]
# print(groceries)

# groceries = [
#     ["Pork", "Beef", "Chicken"],
#     ["Banana", "Apple", "Strawberry"],
#     ["Water", "Soda", "Juice"]
# ]
# for list in groceries:
#     for item in list:
#         print(item, end=" ")
#     print()

key_pad = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["*", "0", "#"]
]

for row in key_pad:
    for key in row:
        print(key, end=" ")
    print()