class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def sell(self):
        print(f"{self.brand} is the best selling car out there.....")


car1 = Car("porsche", 911)
car1.sell()