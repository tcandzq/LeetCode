#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/3 10:40
# @Author  : tc
# @File    : FirstMissingPositive.py
"""
题号 41 缺失的第一个正数
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
说明:

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。

"""
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 0
        _min = min(nums) if min(nums) > 0 else 1
        if _min > 1:
            return 1
        else:
            while _min in nums:
                _min += 1
            return _min

if __name__ == '__main__':
    nums = [7,8,9,11,12]
    solution = Solution()
    print(solution.firstMissingPositive(nums))