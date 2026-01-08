# list comprehension = a concise way to create lists in python
#    compact and easier to read than traditional loops
#       [expression for value in iterable if condition]

doubles= [x*2 for x in range (1,11)]
triples= [y*3 for y in range (1,11)]

print(doubles)
print(triples)

fruits= ["apple","banana","orange"]
fruits= [fruit.upper() for fruit in fruits]
fruits_chars= [fruit[0] for fruit in fruits]
print(fruits)
print(fruits_chars)

numbers = [1, -2, 3 , -4, 5]
positive_nums = [ num for num in numbers if num > 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]
print(positive_nums)
print(even_nums)
print(odd_nums)