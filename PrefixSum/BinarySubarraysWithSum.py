# -*- coding: utf-8 -*-
# @File    : BinarySubarraysWithSum.py
# @Date    : 2022-08-21
# @Author  : tc
"""
930. 和相同的二元子数组
给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。
子数组 是数组的一段连续部分。

 示例 1：
输入：nums = [1,0,1,0,1], goal = 2
输出：4
解释：
有 4 个满足题目要求的子数组：[1,0,1]、[1,0,1,0]、[0,1,0,1]、[1,0,1]

示例 2：
输入：nums = [0,0,0,0,0], goal = 0
输出：15

前缀和

具体地，我们用哈希表记录每一种前缀和出现的次数，假设我们当前枚举到元素nums[j]，
我们只需要查询哈希表中元素sum[j]−goal的数量即可，这些元素的数量即对应了以当前j值为右边界的满足条件的子数组的数量。
最后这些元素的总数量即为所有和为goal 的子数组数量。

思路来自：https://leetcode.cn/problems/binary-subarrays-with-sum/solution/he-xiang-tong-de-er-yuan-zi-shu-zu-by-le-5caf/
"""
from collections import defaultdict
from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = defaultdict(int, {0:1})
        ans = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            ans += d.get(total - goal, 0)
            d[total] = d.get(total, 0) + 1
        return ans