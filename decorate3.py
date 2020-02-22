# coding=utf-8

def my_decorate(func):
    print("this is ordinary function")
    def wrapper():
        print("this is the function returned by the decorate")
        func()
    return wrapper

def test_function():
    print("test")

@my_decorate
def test2_function():
    print("test2")

if __name__ == "__main__":
    #dec = my_decorate(test_function)
    #print("--------------------")
    #dec()
    test2_function()
