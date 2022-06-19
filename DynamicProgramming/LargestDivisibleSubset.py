# -*- coding: utf-8 -*-
# @File    : LargestDivisibleSubset.py
# @Date    : 2022-06-19
# @Author  : tc
"""
368. 最大整除子集
给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
answer[i] % answer[j] == 0 ，或
answer[j] % answer[i] == 0
如果存在多个有效解子集，返回其中任何一个均可。

示例 1：

输入：nums = [1,2,3]
输出：[1,2]
解释：[1,3] 也会被视为正确答案。
示例 2：

输入：nums = [1,2,4,8]
输出：[1,2,4,8]

序列DP
定义 f[i]为考虑前 i 个数字，且以第 i 个数为结尾的最长「整除子集」长度。
定义 g[i]为记录 f[i]是由哪个下标的状态转移而来，如果 f[i] = f[j] + 1, 则有g[i]=j。

"""
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        f, g = [0] * n, [0] * n
        for i in range(n):
            # 至少包含自身一个数，因此起始长度为 1，由自身转移而来
            length, prev = 1, i
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    # 如果能接在更长的序列后面，则更新「最大长度」&「从何转移而来」
                    if f[j] + 1 > length:
                        length = f[j] + 1
                        prev = j
            # 记录「最终长度」&「从何转移而来」
            f[i] = length
            g[i] = prev

        # 遍历所有的 f[i]，取得「最大长度」和「对应下标」
        max_len = idx = -1
        for i in range(n):
            if f[i] > max_len:
                idx = i
                max_len = f[i]

        # 使用 g[] 数组回溯出具体方案
        ans = []
        while len(ans) < max_len:
            ans.append(nums[idx])
            idx = g[idx]
        ans.reverse()
        return ans