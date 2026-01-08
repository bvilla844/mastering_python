# while loop = execute some code while some condition remains true
"""
name = input("enter your name: ")
while name == "":
    print("name can't be empty")
    name = input("enter your name: ")
print(f"hello {name}")
"""
"""
food = input("enter food you like (q to quit): ")
while not food == "q":
    print (f"you like {food}")
    food = input("enter food you like (q to quit): ")
print("bye")
"""
"""
f = 1
g = 1
print(f,end = "")
while g < 28:
    print(g, end="")
    temp = f
    f = g
    g = temp + g

counter = 1
while counter <= 10:
    if counter % 2 == 0:
        print(counter)
    counter += 1

"""
"""
response = input("Enter a word: ")
while True:
    if response != "begin":
        response = input("Enter a word: ")
    else:
        print("correct word is begin")
        break
"""

n1 = 12
x = 0
sum_even = 0
while x < n1:
    x += 1
    if x % 2 == 0:
        sum_even += x
print(f"Suma de numeros pares {sum_even}")