# concession stand program

menu = {"pizza": 3.00,
        "nachos": 2.44,
        "popcorn's": 6.00,
        "fries": 2.90,
        "soda":5.00
}

cart = []
total = 0

print("---------MENU----------")
for key, values in menu.items():
    print(f"{key:10}: ${values: .2f}")
print("-----------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---------YOUR ORDER----------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total: .2f}")
