print("Welcome to Calculator Master!")
operator = input("Please enter an operator to begin (+ - * /): ")

if operator == "+" or operator == "-" or operator == "*" or operator == "/":
    # If the operator is valid then it asks for the numbers to work with
    num1 = float(input("Enter the first number/s: "))
    num2 = float(input("Now enter the second number/s: "))

    # algorithm to complete calculations
    if operator == "+":
        result = num1 + num2
        print(f"The result it {result:.2f}")
    elif operator == "-":
        result = num1 - num2
        print(f"The result it {result:.2f}")
    elif operator == "*":
        result = num1 * num2
        print(f"The result it {result:.2f}")
    elif operator == "/":
        result = num1 / num2
        print(f"The result it {result:.2f}")
else:
    print(f"{operator} is not a valid operator.")
