# Object-Oriented Programming (OOP) groups data and behavior together.
# A class is the blueprint. An object is one real thing made from that blueprint.


class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def introduce(self):
        return f"My name is {self.name} and I am learning {self.course}."


student_one = Student("Dikesh", "Python")
student_two = Student("Asha", "Web Development")

print(student_one.introduce())
print(student_two.introduce())
