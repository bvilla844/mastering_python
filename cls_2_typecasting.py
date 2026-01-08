# the process of converting a variable from one data type to another str(), int(), float (), bool()

"""
name = "brayan"
age= 26
gpa=3.2
is_student= True

gpa = int(gpa)
type(gpa)
print(type(gpa))

print(len(""))
concat = "1" + "2"
print(concat)

"""
"""
exam_1 = 93.0
exam_2 = 84.0
exam_3 = 85.5
average = (exam_1 + exam_2 + exam_3)/ 3
average_int = int((exam_1 + exam_2 + exam_3) / 3)
print(average, type(average))
print(average_int, type(average_int))
"""
"""
cups_daily_goal = 8
cups_drank = float(input("Enter the number of cups of water drank?: "))
cups_left = int( cups_daily_goal - cups_drank)
print("you have drank:", cups_drank, "today", end=",")
print("the remaining cups of water to drink is: ", cups_left)
test = "this" * 3
print(test)
"""
"""
num = 2
string_num = "345"
print(str(num) + "." + string_num)

string1 = "hello everybody"
string2 = "How you doing"
count = 3
print(((string1 + " " + string2) + "\n")* count)

print(f'{0.1:.30f}')
print(f'{0.2:.30f}')
print(f'{0.4:.30f}')

bill_amount = 22.70
tip_ratio = 0.15
tip_amount = bill_amount * tip_ratio
print("your tip amount is: $", tip_amount)

b = 7
h = 3.5
a = round(((b * h) / 2), 1)
a_nearest = int( (b * h) /2)
print("your rectangle area is: ", a)
print("your rectangle area is: ", a_nearest)
"""
"""
current_hour = int (input("Enter the current hour: "))
current_minute = int (input("Enter the current minute: "))
trip_time = float (input("Enter the trip time (in minutes): "))
arrival_hour = round((trip_time / 60) + current_hour)
arrival_minute = (current_minute + trip_time) % 60

print("Your arrival hour is: ", arrival_hour)
print("Your arrival minute is: ", arrival_minute)
"""
cash = float(input("Enter the cash: $"))
total = float(input("Enter the total amount: $"))

change = round(cash - total, 2)
print("Change Due $", change)
print()

# Convertir a centavos
cents = int(round(change * 100))

dollars = cents // 100
cents = cents % 100

quarters = cents // 25
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickels = cents // 5
cents = cents % 5

pennies = cents

print("Dollars:", dollars)
print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)
