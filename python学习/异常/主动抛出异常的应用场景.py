#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/31 15:19
# @Author  : JiCheng
# @File    : 主动抛出异常的应用场景.py
# @Software: PyCharm
# 根据特有的业务需求 主动抛出异常！
'''
1、创建一个Exception的对象
2、使用raise关键字抛出异常对象
需求：
1、定义input_password函数，提示输入用户名密码

'''
def input_password():
    # 1、提示用户输入密码：
    pwd = input("请输入密码：")
    #2、如果密码长度等于大于8位，返回密码
    if len(pwd)>=8:
        return  pwd

    #3、如果小于8 则主动抛出异常！
    print("主动抛出异常")
    #1、创建异常对象 - 可以使用错误字符串信息作为参数
    ex=Exception("密码长度不够")
    #2、主动抛出异常
    raise ex

try:
    print(input_password())
except Exception as result:
    print(result)