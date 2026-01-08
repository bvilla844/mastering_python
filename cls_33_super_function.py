# supper () = function used in a child class to call methods from a parent class (superclass)
# allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"it is  {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self):
        print(f"it is a circle with an area of {3.14 * self.radius * self.radius}")
        super().describe()

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"it is a square with an area of {self.width * self.width}")

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

circle = Circle("red", True, radius=5)
square = Square("blue", True, width=10)


print(circle.color)
print(circle.radius)
print(circle.is_filled)

print(square.color)
print(square.width)

circle.describe()
square.describe()