# logical operators = evaluate multiple conditions (or, and, not)

# or logical
""""""
"""
temp = 236
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("the outdoor event is cancelled")
else:
    print("the outdoor event is ok")
"""
# and logical
"""
temp = 30
is_sunny = True

if temp >= 28 and is_sunny:
    print("is hot outside")
elif 28 > temp > 0 and is_sunny:
    print("is warm outside")
else:
    print("is cold outside")
"""

# or logical
"""
temp = 30
is_sunny = True

if temp >= 28 and not is_sunny:
    print("is hot outside")
elif 28 > temp > 0 and is_sunny:
    print("is warm outside")
else:
    print("is cold outside")
"""



number = 74
print(number,"squared", "is", number **2)
print(number, "cubed", "is", number ** 3)
print("One tenth of", number, "is", number/10)
print(number, "plus", "123 is", number + 123)
print(number, "minus", "456 is", number - 456 )