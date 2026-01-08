# function = a block of reusable code
#   place () after the function name to invoke it

"""
def happy_birthday(name, age):
    print(f"Happy Birthday! {name}")
    print(f"you are {age} years old!")
    print(f"happy birthday!")

happy_birthday("andres", 22)

def display_invoice(username, amount, due_date):
    print(f"Hello, {username}!")
    print(f"Your bill of ${amount: .2f} is due to {due_date}. ")

display_invoice("andres", 35.55, (2021/12/25))

def add(x, y):
    z = x + y
    return z
def subtract(x, y):
    z = x - y
    return z
def multiply(x, y):
    z = x * y
    return z
def divide(x, y):
    z = x / y
    return z

print(add(2, 3))
print(subtract(2, 3))
print(multiply(2, 3))
print(divide(2, 3))
"""
"""
def concession():
    print("Food/Drink Options: ")
    print("popcorn: $8-10")
    print("Candy: $3-5")

concession()
"""

selected_game = "practice"
players = 3

def find_teammates():
    if players >= 3:
        print("Match starting . . . .")
    else:
        print("you need more players . . . .")

def game_on ():
    if selected_game == "br":
        def battle_royal():
            find_teammates()
        battle_royal()
    else:
        def practice():
            map_game = input("Enter the map you want to play?: ")
            print(f"launching practice on {map_game}")
        practice()

game_on()