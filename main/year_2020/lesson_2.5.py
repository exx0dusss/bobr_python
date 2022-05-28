
def my_func(datatype):
    immutable_list = []
    mutable_list = []
    for el in datatype:
        try:
            hash(datatype)
        except TypeError as e:
            print(f'You have an Exception {e}')
            mutable_list.append(datatype)
            
        else:
            immutable_list.append(datatype)
    print(mutable_list)
    print(immutable_list)
this_list = {'score': 25}
my_func(this_list)