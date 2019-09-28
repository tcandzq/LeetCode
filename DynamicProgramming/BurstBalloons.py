#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/28 16:42
# @Author  : tc
# @File    : BurstBalloons.py
"""
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

求所能获得硬币的最大数量。

说明:

你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
示例:

输入: [3,1,5,8]
输出: 167
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

这题是字节跳动2020届算法面试题

看了这道题,完全不知道怎么做
只能参考:https://github.com/grandyang/leetcode/issues/312

状态转移方程的定义是关键:其实是从暴力法的求解中不断优化而来,思考下:对于数组如果我想求得获得硬币最大数量的戳气球方法,那一定是要遍历
数组的每一个元素,即尝试每一种情况比较最大值即可。对于这种优化,可以考虑用动态规划,用动态规划维护一个数组dp[i][j]来存储中间的状态,其实就是
自底向上的方法。

dp[i][j]:表示打爆区间 [i,j] 中的所有气球能得到的最多金币

状态转移方程:dp[i][j] = max(dp[i][j],nums[i-1]*nums[k][j+1]+dp[i][k-1]+dp[k+1][j])  for k in [i,j]
"""
def maxCoins(nums):
    n = len(nums)
    nums.insert(0, 1)
    nums.append(1)
    print(nums)
    dp = [[0]*(n+2) for _ in range(n+2)]  # 注意这里的n是在数组nums开头和尾部插入1之前的长度
    for length in range(1,n+1):
        for i in range(1,n+1-length+1):  # 注意这里是用length,不是常规的for i in range(n) for j in (i)这种
            j = i+length-1
            for k in range(i,j+1):
                print(dp)
                dp[i][j] = max(dp[i][j],nums[i-1]*nums[k]*nums[j+1]+dp[i][k-1]+dp[k+1][j])
    return dp[1][n]

if __name__ == '__main__':
    nums = [3,1,5,8]
    print(maxCoins(nums))

