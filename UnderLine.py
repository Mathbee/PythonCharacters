# coding=utf-8

class A():
    def __init__(self):
        self.__superprivate = "Hello"
        self._semiprivate = ", World!"

    def printSelf(self):
        print(self.__superprivate, self._semiprivate)
if __name__ == "__main__":   
    a = A()
    a.printSelf()
    print(a.__superprivate)
    print(a._semiprivate)
