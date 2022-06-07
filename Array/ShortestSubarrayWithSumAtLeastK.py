# -*- coding: utf-8 -*-
# @File    : ShortestSubarrayWithSumAtLeastK.py
# @Date    : 2022-06-08
# @Author  : tc
"""
862. 和至少为 K 的最短子数组
给你一个整数数组 nums 和一个整数 k ，找出 nums 中和至少为 k 的 最短非空子数组 ，并返回该子数组的长度。如果不存在这样的 子数组 ，返回 -1 。
子数组 是数组中 连续 的一部分。

示例 1：
输入：nums = [1], k = 1
输出：1

示例 2：
输入：nums = [1,2], k = 4
输出：-1

示例 3：
输入：nums = [2,-1,2], k = 3
输出：3

用贪心的思想:减数越小越有可能满足条件，已经满足条件的结果要pop出去。
"""
import collections
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        d = collections.deque([[0, 0]])
        res, cur = float(inf), 0
        for i, a in enumerate(nums):
            cur += a
            while d and cur - d[0][1] >= k:
                res = min(res, i + 1 - d.popleft()[0])
            # 保证双端队列单调递增
            while d and cur <= d[-1][1]:
                d.pop()
            d.append([i+1, cur])
        return res if res < float('inf') else -1