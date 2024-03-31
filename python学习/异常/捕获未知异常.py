#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/31 14:54
# @Author  : JiCheng
# @File    : 捕获未知异常.py
# @Software: PyCharm
'''
没有提前预判到的未知错误！需要捕获这部分异常并输出

'''
try:
    #提示用户输入一个整数
    num = int(input("输入一个整数："))

    #使用8除以用户输入的整数并输出
    result = 8 / num

    print(result)
except ValueError:
    print('请输入正确的整数！')
#未知错误的捕捉语法：
except Exception as  result:
    print("未知错误：%s"%result)