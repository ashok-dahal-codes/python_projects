class Car:
    color = "black"
    brand = "porsche"
    
    def __init__(self,name,model):
        self.name = name
        self.model = model

car1 = Car("gtr3", 911)
car2 = Car("gta", 912)

print("car1 information.....")
print(car1.name)
print(car1.color)
print(car1.brand)
print(car1.model)
print("car2 information.....")
print(car2.brand)
print(car2.name)
print(car2.model)
print(car2.color)

car1.name = "porsche phantom"
print(car1.name)

Car.color = "white"
print(car1.color)
print(car2.color)