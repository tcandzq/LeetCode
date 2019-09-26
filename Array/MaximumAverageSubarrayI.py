#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 21:50
# @Author  : tc
# @File    : MaximumAverageSubarrayI.py
"""
题号:  643     子数组最大平均数 I
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例 1:

输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
 

注意:

1 <= k <= n <= 30,000。
所给数据范围 [-10,000，10,000]。

每次滑动窗口大小为k的数组会超时

优化的方法也很简单,就是每次都存下中间变量嘛,头疼,睡觉去了
"""
# 超时版本
from collections import deque
def findMaxAverage(nums,k):
    dq = deque(nums[:k])
    max_value = sum(dq)/k
    for num in nums[k:]:
        dq.popleft()
        dq.append(num)
        max_value = max(max_value,sum(dq)/k)
    return max_value

# 优化后的版本
def findMaxAverage2(nums,k):
    tmp = sum(nums[:k])
    max_mean = tmp / k
    for i in range(k, len(nums)):
        tmp = tmp + nums[i] - nums[i - k]
        max_mean = max(max_mean, tmp / k)
    return max_mean

if __name__ == '__main__':
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(findMaxAverage2(nums,k))

