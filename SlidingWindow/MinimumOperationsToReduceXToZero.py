# -*- coding: utf-8 -*-
# @File    : MinimumOperationsToReduceXToZero.py
# @Date    : 2022-06-21
# @Author  : tc
"""
1658. 将 x 减到 0 的最小操作数
给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改 数组以供接下来的操作使用。
如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。

示例 1：
输入：nums = [1,1,4,2,3], x = 5
输出：2
解释：最佳解决方案是移除后两个元素，将 x 减到 0 。

示例 2：
输入：nums = [5,6,7,8,9], x = 4
输出：-1

示例 3：
输入：nums = [3,2,20,1,1,3], x = 10
输出：5
解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。


问题等价于求解 最长连续子数组 nums[left, right]，使得其和为sum-x

https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/solution/hua-dong-chuang-kou-wen-ti-zhuan-hua-wei-vwwe/
"""
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sums = 0
        left, right = 0, 0
        n = len(nums)
        target = sum(nums) - x
        if target < 0:
            return -1
        res = -1
        while right < n:
            sums += nums[right]
            while sums > target:
                sums -= nums[left]
                left += 1
            if sums == target:
                res = max(res, right - left + 1)
            right += 1
        return res if res == -1 else n - res