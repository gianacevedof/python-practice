print("Welcome to the Quiz Project!")
print("Choose the correct answer for each question.")
print()

questions = [
    ["1. Which word is a fruit?"],
    ["2. What is the opposite of 'Cold'?"],
    ["3. Choose the correct pronounce for: __ am a student."],
    ["4. What color do you get when you mix blue and yellow?"]
]
options = [
    ["A. Table", "B. Dog", "C. Blue", "D. Apple"],
    ["A. Big", "B. Small", "C. Fast", "D. Hot"],
    ["A. They", "B. She", "C. I", "D. He"],
    ["A. Black", "B. Green", "C. Purple", "D. Red"],
]
answers = ["D", "D", "C", "B"]
question_num = 0
guesses = []
score = 0

# loop to print the questions
for question in questions:
    for row in question:
        print(row)

        # loop to print the options for each question
        for option in options[question_num]:
            print(option)
        guess = input("Enter your guess: ").upper()

        # validating answer
        if guess == answers[question_num]:
            print("Correct!")
            guesses.append(guess)
            score += 1
            question_num += 1
            print()
        else:
            print("Wrong!")
            print(f"Correct answer was '{answers[question_num]}'")
            guesses.append(guess)
            question_num += 1
            print()

print("-------------------")
print("----  RESULTS  ----")
print("-------------------")
print()
print("Your answers were:", end=" ")
for guess in guesses:
    for x in guess:
        print(x, end=" ")

print()
print("Correct answers were:", end=" ")
for answer in answers:
    for x in answer:
        print(x, end=" ")

print()
score = int((score / len(questions)) * 100)
print(f"Your score is {score}%")