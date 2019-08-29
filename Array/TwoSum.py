#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 17:34
# @Author  : tc
# @File    : TwoSum.py

"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

因为要返回的是两个数对应的位置 所以字典的value是每个数对应数组中的下标

"""
def twoSum(nums,target):
    nums_dict = {}
    res = []
    for i, num in enumerate(nums):
        if nums_dict.get(target - num) is not None:
            res = [nums_dict.get(target - num), i]
        nums_dict[num] = i
    return res

if __name__ == '__main__':
    nums = [3,3]
    target = 6
    print(twoSum(nums,target))

