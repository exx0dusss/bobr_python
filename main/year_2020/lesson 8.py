def my_func(*args, **kwargs):
    argslist = []
    kwargslist = []
    if args:
        for arg in args:
            argslist.append(arg)
    if kwargs:
        for key, value in kwargs.items():
            kwargslist.append(f'Key = {key},Value={value}')
    print(f'arguments = {argslist}')
    print(f'keyword arguments = {kwargslist}')
            
my_func("Smthing",1,2,3, name = "Smbdy", cat = "Motilda")

'''

dict = {"a": 123,
        "b": 12312,
        }
'''

'''
my_list_one = [1,2,3,4]
my_list_two = [77, 67, 23]
my_list_final = [*my_list_one, 77 ,67 ,23]
print(my_list_final)
'''