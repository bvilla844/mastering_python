# object = a bundle of related attributes (variables) and methods (functions)
#   ex. phone, book, cup
# you need a class to create many objects

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.for_sale = for_sale
        self.color = color

    def drive(self):
        print(f"Driving... the {self.color} {self.model}")

    def stop(self):
        print(f"Stopping... the {self.color} {self.model}")

    def describe(self):
        print(f"{self.color} {self.model} {self.year} is for sale: {self.for_sale}")

car1= Car("Mustang", 2024, "red", False)
car2 = Car ("Ford", 2000, "blue", True)

print(car1.model, car1.year, car1.color, car1.for_sale)
print(car2.model, car2.year, car2.color, car2.for_sale)
car1.drive()
car1.stop()
car1.describe()
car2.describe()