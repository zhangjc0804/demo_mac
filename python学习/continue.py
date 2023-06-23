#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/23 14:59
# @Author  : JiCheng
# @File    : continue.py
# @Software: PyCharm
# 输出1-50之间5的倍数
for item in range(1, 51):
    if item % 5 == 0:
        print(item)

print('----------使用continue()--------')
for item in range(1, 51):
    if item % 5 != 0:
        continue
    print(item)
# 输出乘法表
for i in range(0, 10):  # 行 数
    for j in range(1, i + 1):  # 列数
        print(i, '*', j, '=', i * j, end='\t')  # 不换行
    print()

for i in range(5):
    for j in range(1, 10):
        if j % 2 == 0:
            # break # 满足条件停止执行，退出循环结构
            continue  # 满足条件结束当前循环进行下一次循环
        print(j, end='\t')
    print()
