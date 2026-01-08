import  math
# circumference
'''
radius = float(input("What is your radius?: "))
circumference = 2 * math.pi * radius
print(f"The area of the circle with radius {radius} is {math.ceil(circumference)}")
print(f"The area of the circle with radius {radius} is {round(circumference, 2)}")
'''

# area
'''
radius = float(input("What is your radius?: "))
area = math.pi * pow(radius, 2)
print(f"The area of the circle with radius {radius} is {round(area, 2)} cm2")
'''

# hypotenuse
a = float(input("What is your side a?: "))
b = float(input("What is your side b?: "))
c = math.sqrt(a * a + b * b)
print(f"your side hypotenuse is {round(c, 2)} cm2")

