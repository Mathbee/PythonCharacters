# coding=utf-8
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    b = 1

if __name__== '__main__':
    a1 = MyClass()
    a1.b = 3
    b1 = MyClass()
    b1.b = 5
    print(a1.b)
    print(b1.b)

