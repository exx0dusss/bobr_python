# nonlocal / global

if __name__ == "__main__":
    b = 10
    def func_one():
        print(b)
        a = 11
        print(a)
        def func_two():
            nonlocal a
            a += 1
            return a
        return func_two
    
    f = func_one()
    print(f())
