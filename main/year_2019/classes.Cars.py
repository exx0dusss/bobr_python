class Auto:
    def check(self,f):
        s = int(input("Введите вместимость бака  "))
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        all = int(s/f*100)
        print("Машина проедет", all,"киллометра/ов ")
class Trucks(Auto):
    def __init__(self,f = 20):
        self.bak = f
class Racing(Auto):
    def __init__(self,f = 15):
        self.bak = f
class Classic(Auto):
    def __init__(self,f = 5):
        self.bak = f
         
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print("1 - Грузовик")
print("2 - Гоночный")
print("3 - Легковой")
print("0 - Обычная")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print("")
n = int(input("Введите тип автомобиля 0/1/2/3 "))

if n == 1:
    print("Легковая машина, 5 лит. на 100км")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    car = Trucks()
    car.check(5)
elif n == 2:
    print("Гоночная машина,15 лит. на 100км")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    car = Racing()
    car.check(15)
elif n == 3:
    print("Грузовая машина,20 лит. на 100км")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    car = Classic()
    car.check(20)
elif n == 0:
    print("Обычная машина,7 лит. на 100км")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    car = Auto()
    car.check(7)
else:
    print("Error")





