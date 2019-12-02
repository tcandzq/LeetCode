#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 20:01
# @Author  : tc
# @File    : IncreasingTripletSubsequence.py
"""
题号 334 递增的三元子序列

给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

数学表达式如下:

如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

示例 1:

输入: [1,2,3,4,5]
输出: true
示例 2:

输入: [5,4,3,2,1]
输出: false

"""
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = dp[j] + 1
                if dp[i] >= 3:
                    return True
        return False


if __name__ == '__main__':
    nums = [2,1,5,0,3]
    solution = Solution()
    print(solution.increasingTriplet(nums))