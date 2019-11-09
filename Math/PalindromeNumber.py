#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/9 18:34
# @Author  : tc
# @File    : PalindromeNumber.py
"""
题号 9 回文数

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？

"""
class Solution:
    # 转为字符串
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if not x:
            return True
        i = 0
        j = len(x) - 1
        while i < j:
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
        return True

    # 无需转为字符串(注意使用底板除)
    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False
        div = 1
        while x / div >= 10:
            div *= 10
        while x > 0:  # x为个位数时
            left = x // div  # 得到数字的第一位
            right = x % 10  # 得到数字的最后一位
            if left != right:
                return False
            x = (x % div) // 10
            div /= 100

        return True


if __name__ == '__main__':
    x = 121
    solution = Solution()
    print(solution.isPalindrome2(x))