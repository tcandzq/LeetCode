# -*- coding: utf-8 -*-
# @File    : SuperUglyNumber.py
# @Date    : 2021-06-19
# @Author  : tc
"""
313. 超级丑数
编写一段程序来查找第 n 个超级丑数。

超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。

示例:

输入: n = 12, primes = [2,7,13,19]
输出: 32
解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
"""
from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [0] * n
        idx = [0] * len(primes)

        ugly[0] = 1
        for i in range(1, n):
            ugly[i] = float('inf')
            for j in range(len(primes)):
                ugly[i] = min(ugly[i], primes[j] * ugly[idx[j]])

            for j in range(len(primes)):
                while primes[j] * ugly[idx[j]] <= ugly[i]:
                    idx[j] += 1
        return ugly[n - 1]