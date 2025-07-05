class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + " %"
        
        
student1 = Student(90,91,92)
print(student1.percentage)

student1.phy = 22
print(student1.percentage)