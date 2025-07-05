class Dog:
    def __init__(self, name):
        self.name = name
        
    def display_name(self):
        print(f"the name of the dog is {self.name}")

class GuideDog(Dog):
    def guide_dog(self):
        print("this is  guide dog")
#this is single inheritance because the class GuideDog inherits the method and data from the class Dog

class BigDog(GuideDog):
    def big_dog(self):
        print("this is a big dog")

class Friendly:
    def woof(self):
        print("I am a freindly dog!")
class MultipleDog(Dog,Friendly):
    def multi_dog(self):
        print("this is a multiple inheriting dog")


guide = GuideDog("labrador")
guide.display_name()#accessing the parent method through a child class

bigdog1 = BigDog("bulldog")
bigdog1.display_name() # inheriting the properties from a parent class which inherits from another parent class that is multilevel class

mulitpledog1 = MultipleDog("kukur")
mulitpledog1.display_name()
mulitpledog1.woof()

