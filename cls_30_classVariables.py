# class variables = shared among all instances of a class
#       defined outside the constructor
# allow you to share data among all objects created from that class

class Student:

    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("John", 25)
student2 = Student("Henry", 30)
student3 = Student("Jack", 40)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students: ")
print(student1.name, student1.age)
print(student1.class_year)
print(student2.name, student2.age)
print(Student.class_year)