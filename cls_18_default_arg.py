# default arguments = a default value for certain parameters
#    default is used when that argument is omitted

"""
def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500, 0.1))

import time

def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count(0,10)
"""
"""
def convert_temps( temps, unit):
    if unit == "F":
        for i in range(len(temps)):
            temps[i] = (temps[i] - 32) * 5/9
        unit = "C"
    else:
        for i in range(len(temps)):
            temps[i] = (temps[i] * 9/5) + 32
        unit = "F"

wknds_temps = [49.0, 51.0, 44.0]
deg_sign = u"\N{DEGREE SIGN}"
metric = "C"

convert_temps (wknds_temps, metric)

for temp in wknds_temps:
    print(f"{temp:.2f}{deg_sign}{metric}", end=" ")
"""
"""
def print_area(b,h):
    return (b * h) / 2
print(print_area(3,4))

def calc(l, w):
    sqf = l * w
    return sqf
print(calc(3,4))
"""
"""
def days_alive(age):
    days = round((age * 365.24), 2)
    return days
print(f"You have lived {days_alive(21)} days")
"""

def avg_list(list_numb):
    sum_total = 0
    avg_total = (sum(list_numb))/len(list_numb)
    return avg_total

list_num = [ 2, 2.5, 7.4, 3.5, 5]
print(avg_list(list_num))

