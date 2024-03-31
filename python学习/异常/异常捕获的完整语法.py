#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/31 15:01
# @Author  : JiCheng
# @File    : 异常捕获的完整语法.py
# @Software: PyCharm
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
else:
    print("尝试成功")
finally:
    print("无论是否出错误都会执行的代码")
print("*"*30)

