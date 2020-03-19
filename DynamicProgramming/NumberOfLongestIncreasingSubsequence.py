# -*- coding: utf-8 -*-
# @File    : NumberOfLongestIncrenumssingSubsequence.py
# @Dnumste    : 2020-03-19
# @numsuthor  : tc
"""
题号 673. 最长递增子序列的个数
给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。

参考：https://leetcode.com/problems/longest-mountain-in-array/discuss/135593/C%2B%2BJavaPython-1-pass-and-O(1)-space

"""
from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        res = up = down = 0
        for i in range(1, len(nums)):
            if down and nums[i - 1] < nums[i] or nums[i - 1] == nums[i]: up = down = 0
            up += nums[i - 1] < nums[i]
            down += nums[i - 1] > nums[i]
            if up and down: res = max(res, up + down + 1)
        return res
