# coding=utf-8
def param(**kwargs):
    print(type(kwargs))
    for name, value in kwargs.items():
        print('{0} = {1}'.format(name, value))

param(apple = 'fruit', cabbage = 'vegetable')
