'''
def multiply_by(x): #multiply by x
    def multiplier(n): #nested function
        return x * n # n - local var: x - outer scope
    return multiplier

multiply_by5 = multiply_by(5)
print(type(multiply_by5))
print(multiply_by5(6))


def multiply_by(multiplier):
    x = multiplier
    def multiplier(n):
        return x * n
    return multiplier

multiply_by6 = multiply_by(6)
print(id(multiply_by))
del(multiply_by)

print(multiply_by6.__closure__[0].cell_contents)
 
def outer():
    x = 10
    print(f'Outer LOCALS: {locals()}')
    
    def inner():
    
        x = 100
        print(locals())
        print(f' X from INNER {x}')
    inner()
    print(f' X from OUTER {x}')
outer()

'''
#time_it
from datetime import  datetime
def time_it(func):
    print('*** INJECT ***')
    def wrapper(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)
        print(f'{datetime.now() - start}')
        return res
    return wrapper
@time_it
def one(n):
    l = []
    for x in range(n):
        if x%2 == 0:
            l.append(x)
        return l
@time_it
def two(n):
    #List comprehensions
    return [x for x in range(n) if x%2 == 0]

