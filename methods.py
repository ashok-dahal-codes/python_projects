class Student:
    college = "amrit"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_age(self):
        print(f"{self.name} age is {self.age}")


student1 = Student("ashok", 21)
student1.student_age()
