# -*- coding: utf-8 -*-
# @File    : DegreeOfAnArray.py
# @Date    : 2022-06-21
# @Author  : tc
"""
697. 数组的度
给定一个非空且只包含非负数的整数数组 nums，数组的 度 的定义是指数组里任一元素出现频数的最大值。
你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1：
输入：nums = [1,2,2,3,1]
输出：2
解释：
输入数组的度是 2 ，因为元素 1 和 2 的出现频数最大，均为 2 。
连续子数组里面拥有相同度的有如下所示：
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组 [2, 2] 的长度为 2 ，所以返回 2 。

示例 2：
输入：nums = [1,2,2,3,1,4,2]
输出：6
解释：
数组的度是 3 ，因为元素 2 重复出现 3 次。
所以 [2,2,3,1,4,2] 是最短子数组，因此返回 6 。

使用一个数组保存字符串中字符最后出现的位置，是一个经典做法。
https://leetcode.cn/problems/degree-of-an-array/solution/xiang-xi-fen-xi-ti-yi-yu-si-lu-jian-ji-d-nvdy/
"""
import collections
from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # 使用 left 和 right 分别保存了每个元素在数组中第一次出现的位置和最后一次出现的位置
        left, right = dict(), dict()
        counter = collections.Counter(nums)

        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
        max_freq = max(counter.values())
        res = len(nums)
        for key, value in counter.items():
            if value == max_freq:
                res = min(res, right[key] - left[key] + 1)
        return res