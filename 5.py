# coding:utf-8

#�����б�
list1 = [10, 20, 30, 40]
list2 = [20, 30, 40, 50]

#�б��Ƶ�ʽ
va = [num for num in list1 if num not in list2]
print(va)

#Ԫ���Ƶ�ʽ

vb = (num for num in list1 if num in list2)
print(vb)
#for a in vb:
#    print(a)

vc = (i for i in range(5))
print(vc)

#�ֵ��Ƶ�ʽ
dic1 = {'a':10,'b':34,'A':7,'Z':3,'B':20,'b':50}
vd = {key:value for (key,value) in dic1.items() }
print(vd)
