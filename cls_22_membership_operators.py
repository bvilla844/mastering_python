# membership operator = use to test whether a value or variable is found in a sequence
#   1. in
#   2. not in

word = "apple"

letter = input("guess a letter in secret word: ")

if letter in word:
    print(f"thers {letter} in the secret word")
else:
    print(f"{letter} was not found")


students = {"andres", "sergio", "camilo"}

student = input("Enter a name of a student: ")

if student in students:
    print(f"{student} is in the students list")
else:
    print(f"{student} is not in the students list")