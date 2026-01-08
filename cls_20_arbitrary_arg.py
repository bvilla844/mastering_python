# *args  = allows you to pass multiple non key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#   * unpacking operator

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1,2,3,5))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr","spongebob", "square pants", "Harold", )
print()
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 fake street" , apt= 102 , city= "Detroit" , state= "Mi", zip= "12344")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print ()
    for value in kwargs.values():
        print(value, end=" ")
    print(f"{kwargs.get('city') }")

shipping_label("Dr", "SpongeBob", "SquarePants", "Harold",
               street = "123 fake street",
               apt = 102,
               city= "Detroit",
               state= "Mi",
               zip= "12344" )