# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        sum = 0
        for i in self.marks:
            sum += i
        print(f"the average marks of {self.name} is {sum/len(self.marks)}")
student1 = Student("ashok", [99,98,97])
student1.average()
