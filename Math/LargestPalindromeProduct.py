# -*- coding: utf-8 -*-
# @File    : LargestPalindromeProduct.py
# @Date    : 2022-06-08
# @Author  : tc
"""
479. 最大回文数乘积
给定一个整数 n ，返回 可表示为两个 n 位整数乘积的 最大回文整数 。因为答案可能非常大，所以返回它对 1337 取余 。

示例 1:

输入：n = 2
输出：987
解释：99 x 91 = 9009, 9009 % 1337 = 987
示例 2:

输入： n = 1
输出： 9

对于数位为 n的两个数而言，其乘积的位数要么是 2∗n，要么是2∗n−1。
"""
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        upper = 10 ** n - 1
        for left in range(upper, upper // 10, -1):  # 枚举回文数的左半部分
            p, x = left, left
            while x:
                p = p * 10 + x % 10  # 翻转左半部分到其自身末尾，构造回文数p，比如当x = 97时，此时回文数p为9779
                x //= 10
                print(p, x)
            x = upper
            while x * x >= p: # 因子x >= p^(1/2)
                if p % x == 0:  # x 是 p 的因子
                    return p % 1337
                x -= 1