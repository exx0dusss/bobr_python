#1
this_tuple = tuple( )
print(type(this_tuple))
#2
my_tuple = (1, )
print(my_tuple)
#3
import random
my_tuple_1 = tuple( )

for i in range(5):
    my_tuple_1 = my_tuple_1 + ((random.randint(1, 100)),)
print(my_tuple_1)
#4
a, b, c, d, e = my_tuple_1
print(a)
print(b)
print(c)
print(d)
print(e)
#5
my_tuple_1 = my_tuple_1 * 2
print(my_tuple_1)
#6
my_tuple_2 = ("slava", "ukarine", "heroyam slava", )
print(type(my_tuple_2))
#7
print(my_tuple_2.count("heroyam slava"),my_tuple_2.count("da"))
#8
print(my_tuple_1[1:4])
#9
my_tuple_12 = my_tuple_1 + my_tuple_2
print(my_tuple_12)
#10
my_tuple_3 = (1, 2, 2, 3, 3, 3, 4, 5)
#11
print(my_tuple_3.index(5, 0,))
#12
print(my_tuple_3.index(3, 3))
try:
    print(my_tuple_3.index(10,2))
except ValueError:
    print("not in tuple")
#13
print(my_tuple_3.count(2),(3))
#14
odd_tuple = tuple()
for i in range(len(my_tuple_3)):
    if my_tuple_3[i]%2 != 0:
        odd_tuple = odd_tuple + (my_tuple_3[i], )

print(odd_tuple)
#15
print(max(odd_tuple))
#16
print(min(odd_tuple))
#17
same_ind_tuple = tuple()
for i in range((my_tuple_1)):
    print(i)
'''
А я щас покажу откуда на белорусь готовилось нападение,
и если бі за 6 часов не был нанесён превентивный удар по позициям
4 позиции шас покажу, я карту принём
'''
$18
