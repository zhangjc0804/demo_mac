#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/23 13:50
# @Author  : JiCheng
# @File    : 转义符.py
# @Software: PyCharm

"""
变量 -数据的载体
1、字母（Unicode字符）、数字、下划线，不能使用特殊字符，数字不能开头
2、变量名是区分大小写的（大小写敏感，x和X是不同的变量名）
3、不能使用python中的关键字（python代码中有特殊含义的单词）和保留字
4、见名知意（看到变量的名字，就能知道它什么意思）
5、变量的命名使用全小写，多个单词使用下划线进行连接（Snake case）
"""
print('hello\nword')  # \n换行
print('hello\tword')  # t占3个位置
print('hello\rword')  # \r覆盖 >word
print('hello\bword')  # \b退一个格子
print('老师说：\'大家好\'')  # 输出 老师说：'大家好'
# 原字符，不希望字符串中的转义符起作用。在字符串前面添加R或者r
print(r'老师说： \b你好吗？')  # 老师说： \你好吗？
name = '玛丽亚'
print(name)
'''
常用的数据类型：
整数类型  int 可以表示正数 负数 和 0
浮点数类型 float
布尔类型 bool
字符串类型 str
'''
n1 = 12
n2 = -12
n3 = 0
print(n1, n2, n3)
from decimal import Decimal

print(1.12 + 2.203)
print(Decimal('1.12') + Decimal('2.203'))
str1 = '人生苦短，我用python！'
str2 = "人生苦短，我用python！"
str3 = """人生苦短，
我用python！"""
print(str1+str(n1))  # str()将其他类型转为字符串类型

