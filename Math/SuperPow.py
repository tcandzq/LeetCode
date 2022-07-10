# -*- coding: utf-8 -*-
# @File    : SuperPow.py
# @Date    : 2022-07-11
# @Author  : tc
"""
372. 超级次方
你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。

示例 1：

输入：a = 2, b = [3]
输出：8
示例 2：

输入：a = 2, b = [1,0]
输出：1024
示例 3：

输入：a = 1, b = [4,3,3,8,5,2]
输出：1
示例 4：

输入：a = 2147483647, b = [2,0,0]
输出：1198


快速幂：https://leetcode.cn/problems/super-pow/solution/kuai-su-mi-qiu-mo-yun-suan-gui-lu-by-desgard_duan/
"""
from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        for i in b:
            res = self.qpow(res, 10, 1337) * self.qpow(a, i, 1337)
        return res % 1337
    # 快速幂标准解法
    def qpow(self, x, n, m):
        ans = 1
        while n > 0:
            if n & 1 == 1:
                ans = ans * x % m
            x = x * x % m
            n >>= 1
        return ans