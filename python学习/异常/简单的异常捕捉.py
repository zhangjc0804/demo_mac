#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/31 14:38
# @Author  : JiCheng
# @File    : 简单的异常捕捉.py
# @Software: PyCharm
# noinspection PyBroadException

def use():
    num=input('请输入一个数字:')
    if len(num) ==1:
        return  int(num)+12
    ex=Exception("这不是一个一位数字")
    raise ex

try :
    print(use())
except Exception as result:
    print(result)
