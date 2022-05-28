import random

year = 2019-50
more = 0
less = 0

age=[[1949,1960.1953,1995],[1957,1965,1990,1945],[1980,1998,1989,1986],[1988,1976,1967,2000]]
print (age)

for i in range (4):
    for j in range (4):
        if age[i] [j] > year:
            less += 1
        elif age[i] [j] <= year:
            more += 1
    

    
print("Баскетболистов старше 50 лет -" + str(more) + ",  младше - " + str(less) + ".")