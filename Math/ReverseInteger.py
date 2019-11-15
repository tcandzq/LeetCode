#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 23:21
# @Author  : tc
# @File    : ReverseInteger.py
"""
题号 7 整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

参考:https://leetcode-cn.com/problems/reverse-integer/solution/reverse-integer-by-jin407891080/

"""

class Solution:
    # 暴力解
    def reverse(self, x: int) -> int:
        if x < 0:
            res = int('-' + str(x)[1:][::-1])
            return res if res >= -(2 ** 31) else 0

        return int(str(x)[::-1]) if int(str(x)[::-1]) <= 2 ** 31 - 1 else 0

    #  优雅解
    def reverse2(self, x: int) -> int:
        y, res = abs(x), 0
        of = (1 << 31) - 1 if x > 0 else 1 << 31  # 1 << 31 等价于 2^31
        while y != 0:
            res = res * 10 + y % 10
            if res > of: return 0  # 如果溢出，直接返回0
            y //= 10
        return res if x > 0 else -res


if __name__ == '__main__':
    x = -123
    solution = Solution()
    print(solution.reverse(x))