import math
x = int(input("Введіть значення для X в градусах: "))
c = int(input("Ввeдіть число С: "))
y=x*(math.pi/180)
g = pow(math.sin(y + c), 1/3)/c*math.exp(y)
print("g="+str(g))
a = input("")
