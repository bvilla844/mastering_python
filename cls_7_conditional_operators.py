# conditional expression = a one-line shortcut for the if-else statement (ternary operator)
# X if condition else Y

num = 8
a = 6
b = 7
age = 13
temperature = 17
user_role = "user"

print("Positive" if num > 0 else "Negative")
result = "Even" if num % 2 == 0 else "Odd"
max_num = a if a > b else b
min_num = a if a < b else b
status = "A" if age >= 18 else "Child"
weather = "hot" if temperature >= 20 else "cold"
access_level = "enter" if user_role == "admin" else "deny"


print(max_num, min_num)
print(status)
print(weather)
print(access_level)