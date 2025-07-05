class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("the car is starting......")
    @staticmethod
    def stop():
        print("the car is stopping")

class ToyotaCar(Car):
    def __init__(self, name,type):
        self.name = name 
        super().__init__(type)

car1 = ToyotaCar("prius", "electric")
print(car1.type)