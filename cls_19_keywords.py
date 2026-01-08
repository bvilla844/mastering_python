# keyword arguments = an argument preceded by an identifier
#       helps with readability
#       order of arguments
#       1. positional 2. default 3. keywords 4. arbitrary

"""
def hello(greeting, tittle, firstname, lastname):
    print(f"{greeting} {tittle} {firstname} {lastname}")

print(hello(greeting="Hello", tittle= "Mr", lastname="SpongeBob", firstname="Square pants"))

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"
phone_number= get_phone(country=1, area=123, first=456, last=9907)
print(phone_number)
"""
def donate(amount=5, name="Anonymous", msg=""):
    return f"{name} donated {amount} credits: {msg}"

print(donate(10,msg="gg"))

