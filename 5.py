# coding:utf-8

#两个列表
list1 = [10, 20, 30, 40]
list2 = [20, 30, 40, 50]

#列表推导式
va = [num for num in list1 if num not in list2]
print(va)

#元组推导式

vb = (num for num in list1 if num in list2)
print(vb)
#for a in vb:
#    print(a)

vc = (i for i in range(5))
print(vc)

#字典推导式
dic1 = {'a':10,'b':34,'A':7,'Z':3,'B':20,'b':50}
vd = {key:value for (key,value) in dic1.items() }
print(vd)
