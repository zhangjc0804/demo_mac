#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/23 15:30
# @Author  : JiCheng
# @File    : 列表.py
# @Software: PyCharm
# list 列表特点：有序 可通过索引值取值
lst = ['hello world', 'lisa', 12]
print(type(lst[0]))
print(len(lst))
print(lst.index(12))  # 如果列表中含有重复的元素 ，只会返回第一个元素的索引值
print(lst[-1])
print(lst[:2])
print(lst[1:2])
lst1 = [10, 20, 30, 40, 50, 60, 70, 80]
print(lst1[1:6:2])  # 开始（默认0）  结束（不含，默认全部）  步长（默认1）
print(lst1[::-1])  # -1 默认从最后一个开始
'''清除列表中的所有元素'''
# lst.clear()
lst[1] = 100
lst[1:3] = [100, 200, 300, 400]
print(lst)
# list sort() 排序
lst12 = [12, 3, 24, 2, 13]
lst12.sort(reverse=True)
print(lst12)
# sorted()函数返回一个新的list
new_list = sorted(lst12)
print(new_list)
lst2 = [i * 2 for i in range(1, 6)]  # 列表生成式
print(lst2)
# 字典 {key:value } 不可变序列
scores = {'张三': 100, '李四': 80}
print(scores)
student = dict(name='jack')
print(student)
print(student.get('name'))  # get()获取name值
print('name' in student)
student['age'] = 100  # 新增
print(student)
print(list(student.keys()))
print(student.values())  # list
print(student.items())  # 元组
for item in student:
    for i in student.values():
        print(i)

# 字典生成式 zip（）
items = ['Fruits', 'Books', 'Others']
prices = [12, 2, 21]
d = {item.upper(): prices for item, prices in zip(items, prices)}  # 字典生成式
print(d)

# 元组 （） 元组不可变序列：不可变序列无增删改操作
'''
可变序列： 字典、列表 、集合 可变序列无增、删、改操作 
不可变序列： 字符串、元组 不可变序列无增、删、改操作
'''
print(id(lst))
print(id(lst.append(1)))
''' 第一种 ，使用（）'''
t = (12, 23, 23, 24,)
print(t)
''' 第二种 ，使用tuple（）'''
t = tuple((12, 23, 23, 24,))
print(t)
t = (10, [20, 30], 40)
print(t[0], t[1])
t[1].append(100)  # 可以往list表中添加元素
print(t[1])
for i in t:  # 通过for循环遍历元组内数据
    print(i)
'''集合{value,value}
集合中的元素不允许重复 且是无序的
'''
s = {12, 23, 23}
s1 = set(range(5))  # 内置函数set（）
print(s1, type(s1))
s2 = set()  # 定义一个空集合
s2.add(12)  # add() update()一次至少添加一个元素
s2.update({123, 23})
s2.remove(123)  # 移除元素 discard（）不抛出异常
print(s2)
'''一个子集是否是一个子集的子集'''
s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30}
print(s2.issubset(s1))  # Ture
print(s1.intersection(s2))  # 交集
print(s1 & s2)  # 交集
print(s1.union(s2))  # 并集
print(s1 | s2)  # 并集
print(s1.difference(s2))  # 差集  s1 - s2
print(s1.symmetric_difference(s2))  # 对称差集 s1 ^ s2
'''集合生成式'''
lst2 = {i * 2 for i in range(1, 6)}  # 集合生成式
print(lst2)


