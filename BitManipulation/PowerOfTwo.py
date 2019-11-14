#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 23:04
# @Author  : tc
# @File    : PowerOfTwo.py
"""
题号 231  2的幂
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 20 = 1
示例 2:

输入: 16
输出: true
解释: 24 = 16
示例 3:

输入: 218
输出: false

"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return True if n & (n - 1) == 0 else False




if __name__ == '__main__':
    n = -16
    solution = Solution()
    print(solution.isPowerOfTwo(n))