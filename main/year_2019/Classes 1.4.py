def trucks():
    all = n/20*100
    print("Машина сможет проехать", all,"км")
def racing():
    all = n/15*100
    print("Машина сможет проехать", all,"км")
def classic():
    all = n/5*100
    print("Машина сможет проехать", all,"км")
class Auto:
    def __init__(self,n):
        self.bak = n
        if n <= 50:
            print("Легковая машина, 5 лит. на 100км")
            print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            classic()
        elif n > 50 and n < 90:
            print("Гоночная машина,15 лит. на 100км")
            print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            racing()
        else:
            print("Грузовая машина,20 лит. на 100км")
            print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            trucks()
            
            
n = int(input("Введите вместимость автомобиля  "))
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
car1 = Auto(n)



