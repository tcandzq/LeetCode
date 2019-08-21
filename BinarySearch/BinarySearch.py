#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/18 16:41
# @Author  : tc
# @File    : BinarySearch.py

"""
Although the basic idea of binary search is comparatively straightforward, the details can be surprisingly tricky...
                                                                                                      ---------KMP作
二分查找的思想很简单，但实现的细节很复杂，这题的答案是二分查找的一个基本框架
下面四个注意是二分查找最容易出错的地方
详细解释见:https://leetcode-cn.com/problems/binary-search/solution/er-fen-cha-zhao-xiang-jie-by-labuladong/

"""
#解法1:
def search(nums,target):
    if not nums:
        return -1
    left = 0
    right = len(nums) -1   #注意
    while left <= right:        #注意
        mid = (left+right) >> 1   #注意
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1   #注意
        elif target < nums[mid]:
            right = mid-1      #注意
    return -1


#解法2(推荐+标准写法):
"""
搜索区间是左闭右开

"""
def search2(nums,target):
    if not nums:
        return -1

    left = 0

    right = len(nums)

    while left < right:
        mid = left + ((right - left) >> 1)

        if nums[mid] == target:
            right = mid

        elif nums[mid] < target:
            left = mid + 1

        elif nums[mid] > target:
            right = mid

    return left if nums[left] == target else -1


if __name__ == '__main__':
    nums = [5,7,7,8,8,8,10]

    target = 0

    print(search2(nums, target))