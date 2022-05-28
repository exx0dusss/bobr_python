funcc = lambda x,func : x * func(x)
print(funcc(10, lambda x: x / x  ))