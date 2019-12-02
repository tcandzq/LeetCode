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

思路参考:https://leetcode-cn.com/problems/increasing-triplet-subsequence/solution/jie-jian-di-300ti-de-si-lu-onshi-jian-fu-za-du-o1k/

"""
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        first = float('inf')
        second = float('inf')
        for num in nums:
            if num <= first:
                first = num  # first 始终记录最小的元素
            elif num <= second:
                second = num  # 接下来不断更新first，同时保持second尽可能的小。
            else:
                return True  # 如果下一个元素比second大，说明找到了三元组。
        return False

if __name__ == '__main__':
    nums = [2,1,5,0,3]
    solution = Solution()
    print(solution.increasingTriplet(nums))