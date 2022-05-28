from random import randint
import asd

class Car:
    def __init__(self,one,two):
        self.color = one
        self.price = two
    def change_price():
        n = randint(500,1000)
        m = randint(500,1000)
        car1.price -= n
        car2.price -= m
        
        
car1 = Car('yellow',11000)
car2 = Car('red', 5000)

print(car1.color,car1.price)
print(car2.color,car2.price)
print('==========================')
class Sale:
    def sale(self):
        Car.change_price()
        print(car1.price)
        print(car2.price)

b1 = Sale()
b1.sale()