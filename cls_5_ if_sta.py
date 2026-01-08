# if + do some code only if some condition is true
#   else do something else
"""
age = int(input("enter your age:"))
if age >= 18:
    print("you are now signed up!")
elif age <= 0:
    print("you can't be below 1")
else:
    print("you are not yet signed up!")
"""
"""
x = 14
compare_result = x <= 13
print(compare_result)

day = "friday"
in_love = day == "friday"
print("Its friday, im in love", in_love, "is", day)

num = 5
even = num % 2 == 0
print(f"{num} is even:", even)
"""
"""
unit = "h"
temp = 90
if unit == "f":
    temp_celsius = (temp -32) * 5/9
    print(f"{temp}{unit} is {round(temp_celsius,2)} celsius")
else:
    temp_fahrenheit = (temp * 5/9) + 32
    print(f"{temp}{unit} is {temp_fahrenheit}fahrenheit")
"""

speed = 55
if not speed > 45 and speed < 70:
    print("you are out of speed limits")
else:
    print("good driving")

spectrum = 489

if spectrum >= 380 and spectrum <= 449:
    print(f"your color is violet")
elif spectrum >= 440 and spectrum <= 484:
    print(f"your color is blue")
elif spectrum >= 485 and spectrum <= 499:
    print(f"your color is cyan")
else:
    print("color out of range")