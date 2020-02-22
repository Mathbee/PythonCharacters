# -*-coding:utf-8-*-

class Person:
    name = 'user'

class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name

if __name__=='__main__':
    user = Student('mukewang')

    #通过__dict__查询属性
    print(user.__dict__)
    print(Person.__dict__)
    #通过__dict__增加一个属性
    user.__dict__['school_addr'] = "dalian"
    print(user.school_addr)
    print(user.name)

    print(dir(user))
    a = [1,2]
    print(dir(a))
