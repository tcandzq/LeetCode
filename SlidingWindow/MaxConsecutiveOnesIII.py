# -*- coding: utf-8 -*-
# @File    : MaxConsecutiveOnesIII.py
# @Date    : 2022-06-20
# @Author  : tc
"""
1004. 最大连续1的个数 III
给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。

示例 1：

输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
示例 2：

输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。

经典滑动窗口解法,将题目看成求包含最多K个的最长子数组
"""
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        size = len(nums)
        left =right = 0
        zeros = 0
        res = 0
        while right < size:
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res