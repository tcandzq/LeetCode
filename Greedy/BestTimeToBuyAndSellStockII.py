#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 20:59
# @Author  : tc
# @File    : BestTimeToBuyAndSellStockII.py
"""
题号122 买卖股票的最佳时机II
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

在买卖股票最佳时机那道题的基础上，去掉了每次最多只能完成一笔交易的限制，可以尽可能多的完成交易,而且一支股票可以多次买卖。这样的话可能就和贪心有关了，所以我把
它移到了贪心栏目，而不是动态规划栏目。

"贪心算法的证明比实现更难，如果存在某个似乎可行的策略，自己又不能举出反例，那么就先写出来提交，干就完了"

思路:只要有股票在一直在涨，那就先买入然后一直观望，直到它跌的前一天卖出就行了，这样不仅单次买卖利益最大，还能尽可能多的完成交易。

不过我写的代码是真的丑，参考代码很优雅

参考:https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/best-time-to-buy-and-sell-stock-ii-zhuan-hua-fa-ji/

"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        stack = [prices[0]]
        res = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                stack.append(prices[i+1])  # 持续观望
                if i == len(prices) - 2:
                    res += stack[-1] - stack[0]
            else:
                if len(stack) >= 2:
                    res += stack[-1] - stack[0]  # 抛出股票
                stack = [prices[i+1]]  # 重新购入股票
        return res

    # 参考代码
    def maxProfit2(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0:
                profit += tmp  # 只要今天价格比昨天高，就卖出
        return profit


if __name__ == '__main__':
    prices = [1,2,3,4,5]
    solution = Solution()
    print(solution.maxProfit2(prices))