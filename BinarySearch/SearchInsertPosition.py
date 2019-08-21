#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 15:00
# @Author  : tc
# @File    : SearchInsertPosition.py

"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

Input1: [1,3,5,6], 5
Output1:2

Input2: [1,3,5,6], 2
Output2:1

Input3: [1,3,5,6], 7
Output3:4

Input4: [1,3,5,6], 0
Output4:0

其实这题主要就是返回大于等于target值的最小索引

"""
#解法1：
def searchInsert(nums,target):

    left = 0

    right = len(nums) - 1

    if target == nums[-1]:
        return right

    if target == nums[0]:
        return left

    while left <= right:
        mid = (left+right) // 2

        if target == nums[mid]:
            return mid

        elif target < nums[mid]:
            right = mid - 1

        elif target > nums[mid]:
            left = mid + 1
    return left


if __name__ == '__main__':
    nums = [1,3,5,6]

    target = 5

    print(searchInsert(nums,target))