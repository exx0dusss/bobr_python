print(" \n#1\n")#1
this_tuple = tuple( )
print(f'Empty tuple: {(this_tuple)}')

print("\n#2\n")#2
my_tuple = (1, )
print(f'Tuple with one element: {my_tuple}')

print("\n#3\n")#3
import random
my_tuple_1 = tuple( )

for i in range(5):
    my_tuple_1 = my_tuple_1 + ((random.randint(1, 100)),)
print(f'Tuple_1 with five elements: {my_tuple_1}')

print("\n#4\n")#4
a, b, c, d, e = my_tuple_1
print(f'a={a}')
print(f'b={b}')
print(f'c={c}')
print(f'd={d}')
print(f'e={e}')

print("\n#5\n")#5
my_tuple_1x2 = my_tuple_1 * 2
print(f'Tuple multiplied by two: {my_tuple_1x2}')

print("\n#6\n")#6
my_tuple_2 = ("slava", "ukarine", "heroyam slava", )
print(f'Tuple_2 with three elements: {my_tuple_2}')

print("\n#7\n")#7
print(f'Tuple 2 check for availability: {my_tuple_2.count("heroyam slava"),my_tuple_2.count("da")}')

print("\n#8\n")#8
print(f'Tree elements starting from second: {my_tuple_1[1:4]}') #???????

print("\n#9\n")#9
my_tuple_12 = my_tuple_1 + my_tuple_2
print(f'First and second tuple: {my_tuple_12}')

print("\n#10\n")#10
my_tuple_3 = (1, 2, 2, 3, 3, 3, 4, 5)
print(f'Tuple_3 with repeated elements: {my_tuple_3}')

print("\n#11\n")#11
print(f'Checking for repeated elements: {my_tuple_3.index(5)}')

print("\n#12\n")#12
print(f'Element in tuple_3: {my_tuple_3.index(3, 4)}')
try:
    print(f'Element out of tuple_3: {my_tuple_3.index(10,4)}')
except ValueError:
    print("Element out of tuple_3")

print("\n#13\n")#13
print(f'Count of repeated elements: {my_tuple_3.count(2),(3)}')#ho ho ho

print("\n#14\n")#14
odd_tuple = tuple()
for i in range(len(my_tuple_3)):
    if my_tuple_3[i]%2 != 0:
        odd_tuple = odd_tuple + (my_tuple_3[i], )

print(f'Tuple_3 with odd indexes: {odd_tuple}')

print("\n#15\n")#15
print(f'Min element in tuple: {min(odd_tuple)}')

print("\n#16\n")#16
print(f'Max element in tuple: {max(odd_tuple)}')

print("\n#17\n")#17
same_ind_tuple = tuple()
for i in range(len(my_tuple_1)):
    #print(my_tuple_1[i], my_tuple_1.index(my_tuple_1[i]))
    #print(my_tuple_3[i], my_tuple_3.index(my_tuple_3[i]))
    same_ind_tuple = same_ind_tuple + ((my_tuple_1[i], my_tuple_3[i]),)
print(f'Couples with same indexes: {(same_ind_tuple)}')

print("\n#18\n")#18
my_tuple_1_elx3 = tuple()
for i in range(len(my_tuple_1)):
    my_tuple_1_elx3 = my_tuple_1_elx3 + (my_tuple_1[i] * 3,)
print(f'Tuple_1 with elements multiplied by three: {my_tuple_1_elx3}')

print("\n#19\n")#19
my_tuple_4 = my_tuple_3[-5:]
print(f'My tuple 3 slice(-5:): {my_tuple_4}')

print("\n#20\n")#20
my_tuple_1xtuple_4 = tuple()
for i in range(len(my_tuple_1)):
    my_tuple_1xtuple_4 = my_tuple_1xtuple_4 + (my_tuple_1[i] * my_tuple_4[i],)
print(f'Tuple_1 * tuple_4: {my_tuple_1xtuple_4}')

print("\n#21\n")#21
sum_my_tuple_1xtuple_4 = sum(my_tuple_1xtuple_4)
print(f'Sum of elements of tuple_1 * tuple_4: {sum_my_tuple_1xtuple_4}')

print("\n#22\n")#22
random_tuple = tuple()
for i in range(random.randint(4,9)):
    random_tuple = random_tuple + (random.randint(1, 20),)
random_tuple_sorted = sorted(random_tuple, reverse=True)
print(f'Random tuple sorted: {random_tuple_sorted}')

input()
