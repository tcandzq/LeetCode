#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 20:17
# @Author  : tc
# @File    : MinimumSizeSubarraySum.py

"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

Input1:s = 7, nums = [2,3,1,2,4,3]
Output1:2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

本题的方法有很多，这里均采用双指针
参考解答:https://leetcode-cn.com/problems/minimum-size-subarray-sum/solution/chang-du-zui-xiao-de-zi-shu-zu-by-leetcode/

解法1是自己的写法 解法是2参考官网的答案，思路都是一样的，用两个指针，一个指针指向初始位置，另外一个指针指向使得数组的和大于等于k的
第一个下标。然后不断移动第一个指针 该过程中要维护数组的和始终大于等于k

"""
#解法1
def minSubArrayLen(s, nums):
    m = len(nums)
    if not nums:
        return 0
    j = -1
    for k in range(0, m):
        if sum(nums[0:k + 1]) >= s:
            j = k
            break
    if j >= m or j == -1:
        return 0
    i = 0
    min_len = j + 1
    while (i <= j) and (i <= m - 1) and (j <= m - 1):
        if sum(nums[i:j + 1]) >= s:
            min_len = min(min_len, j - i + 1)
            i += 1
        else:
            j += 1
    return min_len

#优化后
def minSubArrayLen2(s,nums):
    n = len(nums)

    ans = float('inf')

    left = 0

    sums = 0

    for i in range(n):
        sums += nums[i]
        while sums >= s:
            ans = min(ans, i+1-left)

            sums -= nums[left]

            left += 1

    return ans if ans != float('inf') else 0

if __name__ == '__main__':
    nums = [2,3,1,2,4,3]

    s = 7

    print(minSubArrayLen2(s,nums))
