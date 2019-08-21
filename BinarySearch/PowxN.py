#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 22:49
# @Author  : tc
# @File    : PowxN.py

"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。
Input1: 2.00000, 10
Output1: 1024.00000

Input2: 2.10000, 3
Output2: 9.26100

Input3: 2.00000, -2
Output3: 0.25000

"""

def myPow(x , n):

    if n == 0:
        return 1

    if n == 1:
        return x

    if n == -1:
        return 1 / x

    if n % 2 == 0:

        return pow(x, n // 2) * pow(x, n // 2)

    if n % 2 == 1:

        return pow(x, n // 2) * pow(x, n // 2) * x

if __name__ == '__main__':

    res = myPow(2, 0)

    print(res)