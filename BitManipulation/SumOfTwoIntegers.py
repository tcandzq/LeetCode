#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/29 23:40
# @Author  : tc
# @File    : SumOfTwoIntegers.py
"""
题号 371 两整数之和
不使用运算符 + 和 - ，计算两整数​a 、b之和。

示例 1:

输入: a = 1, b = 2
输出: 3
示例 2:

输入: a = -2, b = 3
输出: 1

参考:https://leetcode-cn.com/problems/sum-of-two-integers/solution/wei-yun-suan-xiang-jie-yi-ji-zai-python-zhong-xu-y/

"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0x100000000
        # 整型最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b != 0:
            # 计算进位
            carry = (a & b) << 1 # a与b的与运算后,再向左移动一位
            # 取余范围限制在 [0, 2^32-1] 范围内
            a = (a ^ b) % MASK
            b = carry % MASK  # 进位加法
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)


if __name__ == '__main__':
    a = 3
    b = -2
    solution = Solution()
    print(solution.getSum(a,b))