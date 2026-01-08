# collections + single variable used to store multiple values
# list = [] ordered and changeable. duplicates ok
# set = {} unordered and immutable, but add/remove ok no duplicates
# tuple = () ordered and unchangeable duplicates ok faster

""""""
# list
num_list = [2, 3, 4, 5, 6, 7, 8, 9]
print(num_list)
print("length: ", len(num_list))
print("4th element: ", num_list[3])
num_list[3] = 7
print(num_list)

"""
fruits= ["apple", "banana", "cherry"]
print (fruits[:2])
print(len(fruits))
print("apple" in fruits)
fruits[0]="watermelon"
fruits.append("mango")
fruits.remove("mango")
fruits.insert(0,"apple")
fruits.sort()
print (fruits)
print (fruits.index("cherry"))
print (fruits.count("cherry"))
for fruit in fruits:
    print (fruit)
"""
# set
"""
fruits= {"apple", "banana", "cherry"}
fruits.add("mango")
fruits.remove("banana")
fruits.pop()
print(len(fruits))
print("apple" in fruits)
print (fruits)
"""
"""
# tuples
fruits= ("apple", "banana", "cherry")
print (fruits.index("cherry"))
print(len(fruits))
print("apple" in fruits)
print (fruits)
for fruit in fruits:
    print (fruit)
"""
