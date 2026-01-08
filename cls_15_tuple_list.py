
"""
fruits = ['apple','orange','banana','mango']
vegetable = ['carrots', 'celery', 'potatoes']
meats = ['chicken' , 'fish', 'turkey']

groceries = [fruits, vegetable, meats]
print(groceries[1][2])

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
"""
grades = [2, 3, 2.5, 5]
print("grades", grades, type(grades), sep="--")
grades = tuple(grades)
print("grades", grades, type(grades), sep="--")

first_choice = "x"
second_choice = "y"
third_choice = 15
fourth_choice = 20.2
my_tuple = (first_choice, second_choice, third_choice, fourth_choice)
print("my_tuple", my_tuple)


