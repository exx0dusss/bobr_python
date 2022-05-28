import time

user_input = input("Enter any number ")

def iterr():
    my_list = (list(str(user_input)))
    time.sleep(1)
    print(type(my_list))
    my_iter = iter(my_list)
    time.sleep(1)
    print(type(my_iter))
    try:
        while True:
            time.sleep(1)
            print(next(my_iter))
    except StopIteration as e:
        print("You`ve reached end of iter_object")
iterr()
    