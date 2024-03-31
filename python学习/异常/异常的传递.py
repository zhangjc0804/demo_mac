#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/31 15:09
# @Author  : JiCheng
# @File    : 异常的传递.py
# @Software: PyCharm
def demo1():
    return int(input("请输入一个整数:"))

def demo2():

    return  demo1()
# 利于异常的传递性，在主程序捕获异常
try :
    print(demo2())
except Exception as result:
    print("错误未知 %s"% result)