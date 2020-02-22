# coding=utf-8

def my_decorate(decorate_function):
    def wrapper_function():
        print("wrapper before function runs")
        decorate_function()
        print("wrapper after function runs")

    return wrapper_function

@my_decorate
def test_function():
    print("this is test funciton")

if __name__ == "__main__":
    #使用AOP切面编程的方式
    test_function()
    #没有使用AOP切面编程的时候调用方式
    #a = my_decorate(test_function)
    #a()
