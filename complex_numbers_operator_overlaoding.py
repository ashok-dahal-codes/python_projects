class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def show(self):
        print(f"{self.real}i + {self.img}j")
    
    def __add__(self, other):
        new_real = self.real + other.real
        new_img = self.img + other.img
        return Complex(new_real,new_img)
    
    def __sub__(self, other):
        new_real = self.real - other.real
        new_img = self.img - other.img
        return Complex(new_real,new_img)



num1 = Complex(2,3)
num1.show()
num2 = Complex(5,4)
num2.show()
num3 = num1 + num2
num3.show()
num4 = num1 - num2
num4.show()