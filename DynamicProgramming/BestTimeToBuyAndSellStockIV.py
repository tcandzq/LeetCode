# -*- coding: utf-8 -*-
# @File    : BestTimeToBuyAndSellStockIV.py
# @Date    : 2019-12-18
# @Author  : tc
"""
题号 188 买卖股票的最佳时机IV
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2:

输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

"""
from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * 2] * (k+1) for _ in range(n)]
        for i in range(n):
            for j in range(k, 0, -1):
                if i == 0:
                    print(i,j)
                    dp[i][j][0] = 0  # 第0天 手里没有股票，利润为-prices[i]
                    dp[i][j][1] = -prices[i]  # 第0天直接卖出股票 不存在
                    continue
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        print(dp)
        return dp[n - 1][k][0]


if __name__ == '__main__':
    prices = [3,3,5,0,0,3,1,4]
    k = 2
    solution = Solution()
    print(solution.maxProfit(k,prices))
