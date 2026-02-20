import random

low = 0
high = 0
number = 0
guess = 0

print("Welcome to the random number game!")
low = int(input("Enter the lowest number you want: "))
high = int(input("Now, enter the highest number you want: "))
number = random.randint(low, high)
attempts = 1

print("Now you have to guess what number the computer has selected.")

while True:
    guess = int(input("\nGuess a number: "))
    if guess > number:
        print("Your guess is too high.")
        attempts += 1
    elif guess < number:
        print("Your guess is too low.")
        attempts += 1
    else:
        print("You guessed the number!")
        break

print(f"It took you {attempts} attempts to guess the number.")