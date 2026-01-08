# Class methods = Allows operations related to the class itself
#   take (cls) as the first parameter, which represents the class itself

#instance methods = best for operations on instance of the class
#Static methods= best for utility functions that do not need access to class data
#Class methods = best for class-level data or require access to the class itself


class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #instace method
    def get_info(self):
        return f"{self.name}, {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"total number of student: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count}"

student = Student("Spongebob", 3.13)
student2 = Student("Patrick", 3.55)
student3 = Student("Squidward", 3.22)
print(Student.get_count())
print(Student.get_average_gpa())