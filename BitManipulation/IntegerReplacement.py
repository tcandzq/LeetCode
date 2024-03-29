# -*- coding: utf-8 -*-
# @File    : IntegerReplacement.py
# @Date    : 2022-06-19
# @Author  : tc
"""
397. 整数替换
给定一个正整数 n ，你可以做如下操作：

如果 n 是偶数，则用 n / 2替换 n 。
如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。
返回 n 变为 1 所需的 最小替换次数 。

示例 1：

输入：n = 8
输出：3
解释：8 -> 4 -> 2 -> 1
示例 2：

输入：n = 7
输出：4
解释：7 -> 8 -> 4 -> 2 -> 1
或 7 -> 6 -> 3 -> 2 -> 1
示例 3：

输入：n = 4
输出：2

使用贪心方法+位运算,奇数与偶数的区别在于奇数的最低为1，偶数的最低为0。对于偶数而言直接除以2是最快的，
对于奇数而言如果次低为1，那就直接+1，作会把连续的 1 全部变成 0，直到不连续的那个 0 变成 1，而减 1 的话只能把最低位一个 1 变成 0，
显然，加 1 能更减少操作次数；
"""
class Solution:
    def integerReplacement(self, n: int) -> int:
        ans = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
            else:
                # 判断次低位是否为1
                if (n >> 1) & 1 == 1 and n != 3:
                    n += 1
                else:
                    n -= 1
            ans += 1
        return ans