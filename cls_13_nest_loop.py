# nested loop = a loop within another loop (outer , inner)
"""
rows = int(input("enter number of rows: "))
columns = int(input("enter number of columns: "))
symbols = input("enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbols, end="")
    print()
"""
"""
meal = "fg"
option = 2
if meal == "lunch":
    if option == 1:
        print("Your oder: Caesar salad")
    elif option == 2:
        print("Your order: Spicy chicken wrap")
    else:
        print("Your oder: Butternut squash soup")
else :
    if option == 1:
        print("Your oder: Baked salmon")
    elif option == 2:
        print("Your oder: Turkey burger")
    else:
        print("Your order: Mushroom risotto")

print()
x = 2
response1 = "odd" if x%2 == 0 else "odd"
print(response1)
"""
"""
ping = 100

pingReport = "low to average" if ping  < 150 else "to high"
print(pingReport)

"""
"""
hour = 8
minute = 0
while hour <= 9:
    while minute <= 59:
        print(hour, ":", minute)
        minute += 30
    hour += 1
    minute = 0

"""
range_num = 10
for i in range(range_num):
    for x in range(range_num):
        print(x , " ", end="")
    range_num -= 1
    print()





