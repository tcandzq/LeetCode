#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/25 12:12
# @Author  : tc
# @File    : BestTimeToBuyAndSellStockWithTransactionFee.py

"""
题号 714 买卖股票的最佳时机含手续费
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每次交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。
Input1:prices = [1, 3, 2, 8, 4, 9], fee = 2
Output1:8
解释: 能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

想了半天还是做不出来,原来需要动态规划里的新技术叫状态机 其实就是多维的DP Table
参考:https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-l-2/
对所有股票买卖问题都做了总结，讲解得很详细

其实无非就是一步转移的时候多个状态发生了改变,所以就需要多个数组来维护不同的状态嘛
对于本题在每一步都涉及到两个状态:1.手里持有股票,2.手里没有股票
故需要维护两个 dp table
dp_hold:手里持有股票时的最大收益;dp_cash:手里没有股票时的最大收益

状态转移的步骤如下:
1.手里有股票 -> 抛出 -> 手里没有股票
2.手里没有股票 -> 观望 -> 手里没有股票
3.手里有股票 -> 观望 -> 手里有股票
4.手里没有股票 -> 买入 -> 手里有股票

记住:是状态！！！在任何一个时刻你肯定处于手里没有股票和持有股票两种状态之一。不是动作!!!,动作有三种:买入、抛出、观望。你要记录的是
状态,是结果,不是动作,动作影响结果。

"""
#边界处理方法1:加入无意义的头节点
def maxProfit(prices, fee):
    m = len(prices)

    if not m:
        return 0

    dp_hold = [0] * (m+1)  # 手里有股票的最大收益

    dp_hold[1] = -prices[0]

    dp_cash = [0] * (m+1)  # 手里没有股票的最大收益

    for i in range(1, m):
        dp_hold[i+1] = max(dp_hold[i], dp_cash[i] - prices[i])

        dp_cash[i+1] = max(dp_cash[i], dp_hold[i] + prices[i] - fee)
    return dp_cash[-1]


# 边界处理方式2:保持不变
def maxProfit2(prices, fee):
    n = len(prices)
    if n < 2:
        return 0
    dp1 = [0 for _ in range(n)]  # 第i天手上有股票时的最大收益
    dp2 = [0 for _ in range(n)]  # 第i天手上无股票时的最大收益
    dp1[0] = -prices[0]
    for i in range(1, n):
        dp1[i] = max(dp1[i - 1], dp2[i - 1] - prices[i])
        dp2[i] = max(dp2[i - 1], dp1[i - 1] + prices[i] - fee)
    return dp2[n - 1]


if __name__ == '__main__':
    prices = [1,4,6,2,8,3,10,14]
    fee = 3
    print(maxProfit(prices, fee))
