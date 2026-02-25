import random

options = ["Rock", "Paper", "Scissors"]
wins = 0
loses = 0

print("Welcome to the Rock-Paper-Scissors game.")
rounds = int(input("How many rounds would you like to play?: "))
print()

for round in range(rounds):
    computer_choice = random.choice(options)
    choice = input("Make your selection (Rock, Paper, or Scissors): ").capitalize()

    if choice == computer_choice:
        print(f"Computer chose {computer_choice}: That's a draw!")

    elif choice == "Rock":
        if computer_choice == "Scissors":
            print(f"Computer chose {computer_choice}: You win!")
            wins += 1
        elif computer_choice == "Paper":
            print(f"Computer chose {computer_choice}: You lose!")
            loses += 1

    elif choice == "Paper":
        if computer_choice == "Rock":
            print(f"Computer chose {computer_choice}: You win!")
            wins += 1
        elif computer_choice == "Scissors":
            print(f"Computer chose {computer_choice}: You lose!")
            loses += 1

    elif choice == "Scissors":
        if computer_choice == "Paper":
            print(f"Computer chose {computer_choice}: You win!")
            wins += 1
        elif computer_choice == "Rock":
            print(f"Computer chose {computer_choice}: You lose!")
            loses += 1

    else:
        print("That's not a valid choice!")
    print()

if wins > loses:
    print(f"You won {wins} out of {rounds} rounds. Congratulations!")
elif wins == loses:
    print(f"You won ({wins} out of {rounds} rounds. It's a draw!")
else:
    print(f"You lost ({loses} out of {rounds} rounds. You lost")