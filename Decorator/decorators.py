def wrapper(f):
    def func_1(x):
        print("Inside func_1")
        print("Executing func_2")
        f(x)
        print("Done")
    return func_1

@wrapper
def func_2(x):
    for i in range(10):
        print(i)
    print(x)

func_2(10)