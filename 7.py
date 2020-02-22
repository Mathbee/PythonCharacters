
class A(object):
    def __init__(self):
        pass
    def save(self):
        print("A")

class B(A):
    def __init__(self):
        pass
#    def save(self):
#        print("B")

class C(A):
    def __init__(self):
        pass
#    def save(self):
#        print("C")

class D(B, C):
    def __init__(self):
        pass

if __name__ == "__main__":
    d = D()
    d.save()
