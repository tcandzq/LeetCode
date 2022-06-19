# -*- coding: utf-8 -*-
# @File    : MaxConsecutiveOnes.py
# @Date    : 2022-06-20
# @Author  : tc
"""
485. 最大连续 1 的个数
给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。

示例 1：

输入：nums = [1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
示例 2:

输入：nums = [1,0,1,1,0,1]
输出：2
"""
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # 代码中的 index保存的是遍历到的最后的一个0的位置，其默认值是 -1。
        index = -1
        res = 0
        for i, num in enumerate(nums):
            if num == 0:
                index = i
            else:
                res = max(res, i - index)
        return res
