import time
import threading
a = ("a,b,c,d")
b = ("d,e,f,g")
def converter(a, b):
    print(f'"A" is a {type(a)} structure')
    print(f'"B" is a {type(b)} structure')
    for i in range(3):
        time.sleep(1)
        print('')
    a = set(a)
    b = set(b)
    c = a.intersection(b)
    print(f'First structure is converted to set: {a}')
    print(f'Second structure is converted to set: {b}')
    print(f'This is the common of two structures: {c}')
    
converter(a,b)