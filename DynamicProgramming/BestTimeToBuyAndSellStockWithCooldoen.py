# -*- coding: utf-8 -*-
# @File    : BestTimeToBuyAndSellStockWithCooldoen.py
# @Date    : 2019-12-17
# @Author  : tc
"""
题号 309 最佳买卖股票时机含冷冻期
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

股票系列的第三题

参考:https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-lab/

"""
from typing import List


class Solution:
    def max_Profix(self, prices:List[int]):
        n = len(prices)
        dp_i_0, dp_i_1 = 0, -float('inf')
        dp_pre_0 = 0
        for i in range(n):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0,dp_i_1+prices[i])
            dp_i_1 = max(dp_i_1,dp_pre_0-prices[i])
            dp_pre_0 = tmp
        return dp_i_0

if __name__ == '__main__':
    solution = Solution()
    prices = [1, 2, 3, 0, 2]
    print(solution.max_Profix(prices))