# coding=utf-8
import time
def modify(function):
    print("modify")
    function()

@modify
def fun():
    print("run a test fun()")

def foo():
    print("in foo()")

def timeit(func):
    def wrapper():
        start = time.clock()
        func()
        end = time.clock()
        print("used:", end - start)
    return wrapper

if __name__ == '__main__':
    #fun

    foo = timeit(foo)
    foo()
