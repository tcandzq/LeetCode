#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/7 19:41
# @Author  : tc
# @File    : UglyNumberII.py
"""
编写一个程序，找出第 n 个丑数。
丑数就是只包含质因数 2, 3, 5 的正整数。
示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:
    1.1是丑数。
    2.n不超过1690。

这题不会做具体请参考:https://github.com/grandyang/leetcode/issues/264
"""
def nthUglyNumber(n):
    dp = [0] * n
    dp[0] = 1
    l_2 = 0
    l_3 = 0
    l_5 = 0
    for i in range(1, n):
        dp[i] = min(2 * dp[l_2], 3*dp[l_3], 5*dp[l_5])
        if dp[i] >= 2 * dp[l_2]:
            l_2 += 1
        if dp[i] >= 3 * dp[l_3]:
            l_3 += 1
        if dp[i] >= 5 * dp[l_5]:
            l_5 += 1
    return dp[-1]

if __name__ == '__main__':
    print(nthUglyNumber(20))



