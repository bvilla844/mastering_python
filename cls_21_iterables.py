# Iterables = an object/collection that can return its elements one at a time,
# allowing it ti be iterable over in a loop

numbers = [1,2,3,4,5]
numbers2 = (1,2,3,4,5)
fruits = {"apple", "orange", "strawberry", "banana"}
my_dictionary = {"A": 2, "B": 3, "C": 4, "D": 5}

for number in numbers:
    print(number)

for number in numbers2:
    print(number)

for fruit in fruits:
    print(fruit)

for key in my_dictionary:
    print(key)

for value in my_dictionary.values():
    print(value)