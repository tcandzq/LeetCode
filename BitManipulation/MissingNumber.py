#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 21:57
# @Author  : tc
# @File    : MissingNumber.py
"""
题号 268 缺失数字
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:

输入: [3,0,1]
输出: 2
示例 2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8
说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?

利用 a ^ b ^ b = a

"""
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i,num in enumerate(nums):
            res = res ^ i ^ num
        return res ^ len(nums)

if __name__ == '__main__':
     nums = [9,6,4,2,3,5,7,0,1]
     solution = Solution()
     print(solution.missingNumber(nums))