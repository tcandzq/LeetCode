# -*- coding: utf-8 -*-
# @File    : BestTimeToBuyAndSellStockIII.py
# @Date    : 2019-12-18
# @Author  : tc
"""
题号 123 买卖股票的最佳时机III
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。

k次交易从买入股票的角度或者卖出股票的角度，但只能择其一考虑。

dp[i][j][0]表示第i天交易了j次时不持有股票;
dp[i][j][1]表示第i天交易了j次时持有股票。

"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[[0] * 2 for _ in range(3)] for _ in range(n)]
        for k in range(3):
            dp[0][k][0] = 0
            dp[0][k][1] = -prices[0]
        for i in range(1, n):
            for j in range(3):
                if not j:
                    dp[i][j][0] = dp[i - 1][j][0]
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])  # 从买入股票的角度考虑
        return dp[n-1][2][0]

if __name__ == '__main__':
    prices = [3,3,5,0,0,3,1,4]
    solution = Solution()
    print(solution.maxProfit(prices))
