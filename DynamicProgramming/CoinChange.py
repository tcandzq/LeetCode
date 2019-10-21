#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 10:53
# @Author  : tc
# @File    : CoinChange.py
"""
题号 322 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。

典型的完全背包问题,但也可用回溯算法解法

"""
from typing import List

class Solution:
    #  动态规划解法
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):

            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        # print(dp)
        return dp[-1] if dp[-1] != float("inf") else -1

    #  回溯算法解法
    def coinChange2(self, coins: List[int], amount: int) -> int:
        pass
if __name__ == '__main__':
    coins = [186,419,83,408]
    amount = 6249
    solution = Solution()
    print(solution.coinChange(coins, amount))