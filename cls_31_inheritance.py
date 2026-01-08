# inheritance = allows a class to inherit attributes and methods from another class
# helps with code reusability and extensibility
# clas Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("wooof!")

class Cat(Animal):
    def speak(self):
        print("meow!")

class Mouse(Animal):
    def speak(self):
        print("squiit!")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(cat.name)
print(cat.is_alive)
dog.eat()
dog.sleep()
cat.speak()
dog.speak()