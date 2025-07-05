class Student:
    def __init__(self, name):
        self.fname = name

s1 = Student("ashok")
print(s1)
print(s1.fname)
del s1.fname
print(s1.fname)
del s1
print(s1)

