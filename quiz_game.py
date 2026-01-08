# python quiz game

questions = (
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "Who wrote the play 'Romeo and Juliet'?",
    "What is the largest ocean on Earth?",
    "What programming language is known for its snake logo?"
)

options = (
    ("A. Paris", "B. London", "C. Rome", "D. Berlin"),
    ("A. Earth", "B. Mars", "C. Jupiter", "D. Venus"),
    ("A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"),
    ("A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"),
    ("A. Java", "B. C++", "C. Python", "D. JavaScript")
)

answers = ("A", "B", "B", "D", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A , B, C ,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("correct!")
    else:
        print("incorrect!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("-----------------------")
print("        Results        ")
print("-----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
print("score: ", end="")
print(score)
