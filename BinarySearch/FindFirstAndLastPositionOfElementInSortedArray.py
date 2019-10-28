#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 18:03
# @Author  : tc
# @File    : FindFirstAndLastPositionOfElementInSortedArray.py
"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
Input1:nums = [5,7,7,8,8,10], target = 8
Output1:[3,4]

Input2:nums = [5,7,7,8,8,10], target = 6
Output2:[-1,-1]

详细接答:https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/er-fen-cha-zhao-suan-fa-xi-jie-xiang-jie-by-labula/

"""
def searchRange(nums,target):

    left = searchLeft(nums, target)

    if left == -1:
        return [-1, -1]

    right = searchRight(nums,target)

    return [left, right]


#二分寻找左边界
def searchLeft(nums,target):

    if not len(nums):
        return -1

    left = 0

    right = len(nums)

    while left < right:
        mid = left + ((right - left) >> 1)
        #找到 target 时不要立即返回，而是缩小「搜索区间」的上界 right，在区间 [left, mid)中继续搜索，即不断向左收缩，达到锁定左侧边界的目的。
        if nums[mid] == target:
            right = mid

        elif nums[mid] < target:
            left = mid + 1

        elif nums[mid] > target:
            right = mid

    return left if nums[left] == target else -1

#二分寻找右侧边界
def searchRight(nums,target):

    if not len(nums):
        return -1

    left = 0

    right = len(nums)

    while left < right:
        mid = left + ((right - left) >> 1)

        #当 nums[mid] == target 时，不要立即返回，而是增大「搜索区间」的下界 left，使得区间不断向右收缩，达到锁定右侧边界的目的。
        if nums[mid] == target:
            left = mid + 1

        elif nums[mid] < target:
            left = mid + 1

        elif nums[mid] > target:
            right = mid

    return left - 1 if nums[left-1] == target else -1


if __name__ == '__main__':
    nums = [5,7,7,8,8,10]

    target = 8

    print(searchRight(nums,target))