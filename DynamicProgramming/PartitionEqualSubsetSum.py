#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/25 0:25
# @Author  : tc
# @File    : PartitionEqualSubsetSum.py

"""
得两个子集的元素和相等。
注意:
每个数组中的元素不会超过 100
数组的大小不会超过 200

示例 1:
输入: [1, 5, 11, 5]
输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
 
示例 2:
输入: [1, 2, 3, 5]
输出: false

解释: 数组不能分割成两个元素和相等的子集.

这个题目很经典,是以01背包问题为基础的动态规划题
本题的关键是:dp[i][j]：表示从数组的 [0, i] 这个子区间内挑选一些正整数，每个数只能用一次，使得这些数的和等于 j。
详细请参考:https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/0-1-bei-bao-wen-ti-xiang-jie-zhen-dui-ben-ti-de-yo/
"""
#  基础版
def canPartition(nums):
    size = len(nums)
    s = sum(nums)
    if s & 1 == 1:
        return False
    target = s // 2
    dp = [[False for _ in range(target+1)] for _ in range(size)]
    for i in range(target+1):
        dp[0][i] = False if nums[0] != i else True
    for i in range(1, size):
        for j in range(target+1):
            if j >= nums[i]:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]

            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

# 优化版1



# 优化版2




if __name__ == '__main__':
    print(canPartition([1, 5, 11, 5]))

