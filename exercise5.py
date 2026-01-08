#Python compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = int(input("enter principle amount: "))
    if principle <= 0:
        print("principle amount cannot be zero or less")
while rate <= 0:
    rate = int(input("enter rate amount: "))
    if rate <= 0:
        print("rate amount cannot be zero or less")
while time <= 0:
    time= int(input("enter the time in years: "))
    if time <= 0:
        print("time cannot be zero or less")

total = principle * pow((1 + rate/100), time)
print(f"balance after {time} year/s {total:.2f}")