#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 0:38
# @Author  : tc
# @File    : SearchInRotatedSortedArray.py
"""
题号33 搜索旋转排序数组
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

题目说了要O(logn),其实就是告诉你要用二分查找

"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        if target == nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums) - 1
        if target < nums[left] and target > nums[right]:
            return -1
        if target > nums[left] or target > nums[right]:
            for i in range(left,len(nums)):
                if target == nums[i]:
                    return i

        if target < nums[left] or target < nums[right]:
            for j in range(len(nums)-1,-1,-1):
                if target == nums[j]:
                    return j
        return -1


if __name__ == '__main__':
    solution = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    print(solution.search(nums,target))

