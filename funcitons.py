# Functions are pieces of reusable code that you can call later on if you need them.

def add(a,b):
    z = a+b
    return z

def subtract(a,b):
    z = a-b
    return z

def multiply(a,b):
    z = a*b
    return z

def divide(a,b):
    z = a/b
    return z

# Calculator
choice = input("Do you want to: + - * /? ")

if choice == "+":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"That equals to: {add(num1, num2)}")
elif choice == "-":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"That equals to: {subtract(num1, num2)}")
elif choice == "*":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"That equals to: {multiply(num1, num2)}")
elif choice == "/":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"That equals to: {divide(num1, num2)}")
else:
    print("Invalid input")