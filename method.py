#coding:utf-8
class A(object):
    def foo(self,x):
        print("method",self,x)

    @classmethod
    def class_foo(cls,x):
        print("class method",cls,x)

    @staticmethod
    def static_foo(x):
        print("static method:",x)

a = A()
a.foo(1)
a.class_foo(2)
a.static_foo(3)
