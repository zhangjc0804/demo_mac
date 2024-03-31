#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/31 14:46
# @Author  : JiCheng
# @File    : 根据错误类型捕获异常.py
# @Software: PyCharm
'''
需要根据不同类型的异常，作出不同的响应，
这个时候就需要捕获错误类型啦
'''
try:
    #提示用户输入一个整数
    num = int(input("输入一个整数："))

    #使用8除以用户输入的整数并输出
    result = 8 / num

    print(result)
except ZeroDivisionError:
    print('除0错误') #抛出异常时，最后一行错误信息的第一个单词就是错误类型。
except ValueError:
    print('请输入正确的整数！')