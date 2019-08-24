#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 0:35
# @Author  : tc
# @File    : MinimumPathSum.py
"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
Input1:[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output1:7
解释: 因为路径 1→3→1→1→1 的总和最小。
动态规划，平平无奇
"""


def minPathSum(grid):

    m = len(grid)

    if not m:
        return 0

    n = len(grid[0])

    dp = [[0] * n for i in range(m)]

    first_column = [grid[i][0] for i in range(m)]

    for i in range(m):
        dp[i][0] = sum(first_column[0:i+1])

    for j in range(n):
        dp[0][j] = sum(grid[0][0:j+1])

    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]

    return dp[m-1][n-1]

if __name__ == '__main__':
    grid = [
          [1,3,1],
          [1,5,1],
          [4,2,1]
        ]

    print(minPathSum(grid))
