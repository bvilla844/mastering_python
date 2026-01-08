# format specifiers = {value : flags} format a value based on what flags are inserted

price1 = 343564.21432
price2 = -543654423000.54
price3 = 1200.54

"""
print(f"price 1 is {price1:.3f}")
print(f"price 2 is {price2:.3f}")
print(f"price 3 is {price3:.3f}")
"""
"""
print(f"price 1 is {price1:010}")
print(f"price 2 is {price2:010}")
print(f"price 3 is {price3:010}")
"""
"""
print(f"price 1 is {price1:>10}")
print(f"price 2 is {price2:>10}")
print(f"price 3 is {price3:>10}")
"""
"""
print(f"price 1 is {price1: ,}")
print(f"price 2 is {price2: ,}")
print(f"price 3 is {price3: ,}")
"""
print(f"price 1 is {price1:,.2f}")
print(f"price 2 is {price2:,.2f}")
print(f"price 3 is {price3:,.2f}")

