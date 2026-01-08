# validate user input
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

name = input("Enter your name: ")
if len(name) > 12 or name.find(" ") != -1 or name.isdigit():
    print("invalid name")
else:
    print("valid name")
