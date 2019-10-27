#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/22 21:20
# @Author  : tc
# @File    : JumpGameII.py
"""
题号: 45
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

vivo2020届校园招聘在线笔试第一题

既然要跳跃的步数最少,那就每次在可跳的范围往最远的的位置跳。

动态规划求解:这种方法和leetcode139单次拆分的解法很类似。求解dp[i]的值需要遍历并与dp的前j~i之间的值进行比较。

"""
# 动态规划求解(超时)
def jump(nums):
    if not nums:
        return 0
    dp = [float('inf')] * len(nums)  # 这里用float('inf')很巧妙
    dp[0] = 0
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] >= i - j:
                dp[i] = min(dp[i], dp[j]+1)
    return dp[-1]

# 贪心算法(这种写法不是很好理解)
def jump2(nums):
    steps = 0
    end = 0  # 当前能跳的边界
    max_position = 0
    for i in range(len(nums)-1):
        max_position = max(max_position, nums[i]+i)  # 可跳范围内能达到的最远位置
        print(max_position)
        if i == end:
            end = max_position
            steps += 1
    return steps

# 我自己写的这种写法问题很大
def jump3(nums):
    start = 0
    end = 0
    steps = 0
    if not nums or len(nums) <= 1:
        return 0
    while start <= len(nums) - 1:
        steps += 1
        for i in range(1,nums[start]+1):
            if start + i >= len(nums) - 1:
                return steps + 1
            if nums[start+i] >= end:
                end = start+i
                print(end)
        start = start + end

    return steps


if __name__ == '__main__':
    nums = [1,1,1,2,1]
    print(jump3(nums))
