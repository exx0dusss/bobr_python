'''
def my_func(x):
    return x

print(my_func(12))

f = (lambda x: print(x))(2)
print(f)



full_name = lambda first, second: f'Full name : {first.title()} {second.title()}'

print(full_name('ds', 'sd'))
'''

high_order_func = lambda x,func : x + func(x)
print(high_order_func(2, lambda x: x * x))

'''
import dis

add_func = lambda x, y : x + y
type(add_func)
dis.dis(add_func)
'''
'''
print((lambda x, y , z: x + y + z)(1, 2, 3))
print((lambda x, y , z=2: x + y + z)(1, 2))
print((lambda x, y , z=2: x + y + z)(x=1, y = 100))
print((lambda *args: sum(args))(1,2,3,4,5))
print((lambda **kwargs: sum(kwargs.values.values()))(x=1, y=1, z=100))
'''