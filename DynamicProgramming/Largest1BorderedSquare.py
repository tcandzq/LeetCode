# -*- coding: utf-8 -*-
# @File    : Largest1BorderedSquare.py
# @Date    : 2022-08-21
# @Author  : tc
"""
1139. 最大的以 1 为边界的正方形
给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1组成的最大正方形子网格，并返回该子网格中的元素数量。如果不存在，则返回 0。

示例 1：
输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
输出：9

示例 2：
输入：grid = [[1,1,0,0]]
输出：1

第一步先计算每个网格中横向和竖向连续1的个数。
第二步遍历二维网格，以每一个格子为正方形的右下角，分别找出上边和左边连续1的个数，取最小值作为正方形的边长，
然后判断正方形的左边和上边长度是否都大于等于正方形边长，如果都大于等于正方形边长就更新正方形的最大边长，
否则缩小正方形的边长，继续判断……。

思路参考:https://leetcode.cn/problems/largest-1-bordered-square/solution/shu-ju-jie-gou-he-suan-fa-zui-da-de-yi-1-8l94/

"""
from typing import List

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # dp[i][j][0]: (i, j) 横向连续1的个数
        # dp[i][j][1]: (i, j)竖向连续1的个数
        dp = [[[0] * 2 for i in range(n + 1)] for j in range(m + 1)]

        maxSide = 0 # 记录正方形的最大长度
        for i in range(1, m+1):
            for j in range(1, n+1):
                # 如果当前位置是0，就跳过
                if grid[i - 1][j - 1] == 0:
                    continue
                # 如果是1，我们就计算横向和竖向连续1的个数
                dp[i][j][0] = dp[i][j - 1][0] + 1
                dp[i][j][1] = dp[i - 1][j][1] + 1
                # 沿着当前坐标往上和往左找出最短的距离，暂时看做是正方形的边长(正方形的具体边长
                # 还要看上边和左边的长度，所以这里要判断一下)
                curSide = min(dp[i][j][0], dp[i][j][1])
                if curSide <= maxSide:
                    continue
                # curSide可以认为是正方形下边和右边的长度，我们还需要根据正方形上边和左边的长度
                # 来确认是否满足正方形的条件
                for side in range(curSide, maxSide, -1):
                    # 判断正方形的左边和上边的长度是否大于curSide，如果不大于，我们就缩小正方形
                    # 的长度curSide，然后继续判断
                    if dp[i][j - side + 1][1] >= side and dp[i - side + 1][j][0] >= side:
                        maxSide = side
                        # 更短的就没必要考虑了，这里直接中断
                        break
        # 返回正方形的边长
        return maxSide**2