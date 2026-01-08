# duck typing another way to achieve polymorphism besides inheritance
#   object must have the minimum necessary attributes
# if it looks like a duck and quacks like a duck it must be a duck

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("woof!")

class Cat(Animal):
    def speak(self):
        print("meow!")

class Car:
    alive = False
    def speak(self):
        print("Honk")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)