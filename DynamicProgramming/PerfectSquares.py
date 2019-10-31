#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 1:22
# @Author  : tc
# @File    : PerfectSquares.py
"""
题号 279 完全平方数
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

本题解法较多有动态规划、BFS等

参考:https://leetcode-cn.com/problems/perfect-squares/solution/bfs-dong-tai-gui-hua-shu-xue-by-powcai/

"""
class Solution:

    # 动态规划解法(超时)
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]


if __name__ == '__main__':
    n = 12
    solution = Solution()
    print(solution.numSquares(n))