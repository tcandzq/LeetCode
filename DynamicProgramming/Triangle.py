#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 17:27
# @Author  : tc
# @File    : Triangle.py
"""
题号 120 三角形最小路径和
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

可以从二维dp优化成一维dp,注意看:
二维dp的状态转移方程:dp[i][j] = min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
其中dp[i-1][j-1]和dp[i-1][j]都在同一行,所以可以只用一个一维的dp来存储,但需要自底向上

参考1:https://leetcode-cn.com/problems/triangle/solution/di-gui-ji-yi-hua-sou-suo-zai-dao-dp-by-crsm/
参考2:https://leetcode-cn.com/problems/triangle/solution/dong-tai-gui-hua-onkong-jian-by-powcai/
"""
from typing import List

class Solution:
    # 二维DP数组
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0] * len(triangle) for _ in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        for i in range(1,len(triangle)):
            for j in range(0,i+1):
                if j == 0:
                    dp[i][j] = dp[i - 1][0] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i - 1][i-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
        print(dp)
        return min(dp[-1])

    # 可以用triangle自身来存储dp数组
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        for i in range(1,len(triangle)):
            for j in range(0,i+1):
                if j == 0:
                    triangle[i][j] = triangle[i - 1][0] + triangle[i][j]
                elif j == i:
                    triangle[i][j] = triangle[i - 1][i-1] + triangle[i][j]
                else:
                    triangle[i][j] = min(triangle[i-1][j-1],triangle[i-1][j])+triangle[i][j]
        return min(triangle[-1])

    # 一维DP数组(优化)
    def minimumTotal3(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        min_len = [0] * (row+1)
        for level in range(row-1,-1,-1):
            for i in range(level+1):
                min_len[i] = min(min_len[i], min_len[i+1]) + triangle[level][i]
                print(min_len)
        return min_len[0]

if __name__ == '__main__':
    triangle = [
                 [2],
                [3,4],
               [6,5,7],
              [4,1,8,3]
            ]
    solution = Solution()
    print(solution.minimumTotal3(triangle))