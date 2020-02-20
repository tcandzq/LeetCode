#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/4 23:24
# @Author  : tc
# @File    : FindMinimumInRotatedSortedArray.py
"""
题号 153 寻找旋转排序数组中的最小值
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1
示例 2:

输入: [4,5,6,7,0,1,2]
输出: 0

参考LeetCode81题 搜索旋转排序数组II的模板代码,注意不存在重复元素

"""
from typing import List

class Solution:

    #  正确解法
    def findMin2(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    solution = Solution()
    print(solution.findMin2(nums))