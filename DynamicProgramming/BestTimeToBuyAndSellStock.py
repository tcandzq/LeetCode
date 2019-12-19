#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/24 0:03
# @Author  : tc
# @File    : BestTimeToBuyAndSellStock.py

"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票
Input1:[7,1,5,3,6,4]
Output1:5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

Input1:[7,6,4,3,1]
Output1:0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

提示:动态规划 前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}
优化后的代码真优雅

"""
#解法1
def maxProfit(prices):
    m = len(prices)
    if m in [0,1]:
        return 0
    dp = [0] * m
    min_buy = float('inf')
    for i in range(m-1):
        min_buy = min(min_buy, prices[i])
        if prices[i+1] >= prices[i]:
            dp[i+1] = max(dp[i], prices[i+1] - min_buy)
        else:
            dp[i+1] = dp[i]
    return dp[-1]

# 优化后
def maxProfit2(prices):
    min_p, max_p = 999999, 0
    for i in range(len(prices)):
        min_p = min(min_p, prices[i])
        max_p = max(max_p, prices[i] - min_p)
    return max_p

# 标准解法
def maxProfit3(prices):
    n = len(prices)
    if n < 2:
        return 0
    dp = [[0]*2 for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        dp[i][1] = max(dp[i-1][1], -prices[i])  # 注意这里是-prices[i]因此你只能买入一次股票，所以当你买入股票的时候，利润一定是0
    return dp[n-1][0]

if __name__ == '__main__':

    prices = [7,1,5,3,6,4]

    print(maxProfit3(prices))

