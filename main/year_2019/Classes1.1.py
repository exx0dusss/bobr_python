class Shopping:
    def __init__(self,w,c,n=0):
        self.what = w
        self.type = c
        self.numbers = n
        self.mwhere(n)

    def mwhere(self,n):
        if n <= 1:
            self.where = "Рынок"
        elif 2 < n < 10 :
            self.where = "Магазин"
        elif 10 < n < 20:
            self.where = "Супермаркет"
        else:
            self.where = "Гипермаркет"

    def plus(self,p):
        self.numbers = self.numbers + p
        self.mwhere(self.numbers)
    def minus(self,m):
        self.numbers = self.numbers - m
        self.mwhere(self.numbers)

m1 = Shopping("Макароны", "",11)
m2 = Shopping("Гречка","", 5)
m3 = Shopping("Вермишель","",1)
m4 = Shopping("Пицца","",2)

print (m1.what,m1.type,m1.where)
print (m2.what,m2.type,m2.where)
print (m3.what,m3.type,m3.where)
print (m4.what,m4.type,m4.where)
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
m1.plus(10)
print("В общем",m1.numbers,m1.where)
