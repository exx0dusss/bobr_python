
file = 'C:\\Games\\my_csv.csv'
def not_generator(file):
    row = 0
    with open(file,'r') as csv:
        print('Reading lines')
        lines = csv.readlines()
        print('Reading lines')
        return lines
not_generator(file)


def my_generator(file):
    with open(file, 'r') as csv:
        print('Reading Lines')
        for line in csv.readlines():
            yield print(line)
            yield print("Just Dumb Yield")
not_gen = not_generator(file)       
gen = my_generator(file)
print(type(not_gen))
print(type(gen))

for i in range(10):
    next(gen)

'''
def infinite_func():
    num = 0
    while True:
        yield num
        num += 1
gen = infinite_func()
type(gen)
print(next(gen))

gen_one = (num*2 for num in range(30))
gen_two = [num*2 for num in range(30)]

print(type(gen_one))
print(type(gen_two))
'''
'''
import inspect

def my_func():
    while True:
        x = yield
        yield x*3
gen = my_func()
print(type(gen))
a = gen.send(100)
print(a)
'''
'''
# Iterators
my_list = range(100)
my_list = list(my_list)
my_iter = iter(my_list)
print(type(my_list))
print(type(my_iter))
try:
    while True:
        print(next(my_iter))
except StopIteration as e:
    print("StopIteration")

'''