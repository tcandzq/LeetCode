# -*- coding: utf-8 -*-
# @File    : CountNumbersWithUniqueDigits.py
# @Date    : 2020-09-18
# @Author  : tc
"""
题号357. 计算各个位数不同的数字个数
给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n 。

示例:

输入: 2
输出: 91
解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。

参考：https://leetcode.com/problems/count-numbers-with-unique-digits/discuss/83040/Simple-Python-solution-90

"""

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, product = 1, 1

        for i in range(n if n <= 10 else 10):
            product *= choices[i]
            ans += product

        return ans


if __name__ == '__main__':
    pass