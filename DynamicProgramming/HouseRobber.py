#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/24 18:01
# @Author  : tc
# @File    : HouseRobber.py
"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

Input1:[1,2,3,1]
Output1:4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

Input2:[2,7,9,3,1]
Output2:12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

动态规划的状态转移方程先从特殊情况开始考虑，比如当len(nums) == 1、2、3时 依次递推写出来。然后通过测试案例不断修正，得到最后完整的代码

官方解答:https://leetcode-cn.com/problems/house-robber/solution/da-jia-jie-she-by-leetcode/
"一个自然而然的想法是首先从最简单的情况开始" 与我刚刚阐述的解决步骤一致

"""
def rob(nums):

    m = len(nums)

    if not m:
        return 0

    dp = [0] * (m + 1)

    dp[1] = nums[0]

    for i in range(1,m):

        dp[i+1] = max(dp[i], dp[i-1]+nums[i])

    print(dp)
    return dp[-1]

if __name__ == '__main__':
    nums = [1,2,3,6]

    print(rob(nums))




