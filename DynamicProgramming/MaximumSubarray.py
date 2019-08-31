#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 15:10
# @Author  : tc
# @File    : MaximumSubarray.py
"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
Input1:[-2,1,-3,4,-1,2,1,-5,4],
Output1：6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""
def maxSubArray(nums):
    m = len(nums)
    if not m:
        return 0
    dp = [0] * (m+1)
    for i in range(m):
        dp[i+1] = max(dp[i]+nums[i], nums[i])
    return max(dp[1:])


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]

    print(maxSubArray(nums))