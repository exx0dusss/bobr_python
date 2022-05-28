#Scopes -> Области видимости
#LEGB
#1. locals()
#2. enclosed()
#3. globals()
#4. built-ins()
'''
name = '...'

def say_hi():
    a = 55
    print(f'Locals: {locals()}')
    print(f'GLobals {globals()}')
    print(f'Hello {name}')

def say_bye():
    name = ",,,"
    print(f'Bye{name}')
say_hi()
say_bye()
say_hi()
'''
def my_func(a, b):
    x = 5
    print(f'X inside: {x}')
    print(x)
    
if __name__ == "__main__":
    x = 10
    my_func(3, 5)
    print(f'X outside: {x}')