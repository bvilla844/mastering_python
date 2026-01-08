# calculator

operator = input("What is your operator?: ")
num1 = float(input("What is your first number?: "))
num2 = float(input("What is your second number?: "))
result = 0
if operator == "+":
    result = num1 + num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == "-":
    result = num1 - num2
else:
    print("invalid operator")

print(round(result, 2))