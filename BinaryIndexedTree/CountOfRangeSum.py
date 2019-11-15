#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 1:12
# @Author  : tc
# @File    : CountOfRangeSum.py
"""
题号 327 区间和的个数

给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。

说明:
最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。

示例:

输入: nums = [-2,5,-1], lower = -2, upper = 2,
输出: 3
解释: 3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。

多种解法,先写树状数组的解法

"""
from typing import List

class BinaryIndexedTree:
    def __init__(self,n):
        self.C = [0] * (n + 1)
        self.length = n

    def update(self, i):
        while i <= self.length:
            self.C[i] += 1
            i += (i & (-i))

    def get_num(self,i):
        _sum = 0
        while i > 1:
            _sum += self.C[i]
            i -= (i & -i)
        return _sum

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        pass




if __name__ == '__main__':
    nums = [2147483647,-2147483648,-1,0]
    lower = -1
    upper = 0
    solution = Solution()
    print(solution.countRangeSum(nums,lower,upper))