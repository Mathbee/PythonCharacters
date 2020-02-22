#coding:utf-8
'''
#测试bool类型是否可变
def hello(x):
    x = True
a = False
print("a",a)
hello(a)
print("a",a)
'''
#测试元组中的数据类型
list1 = ['n1','n2','n3']
name = (list1,list1[0])
print(name)
list1[0] = 'm1'
print(name)
