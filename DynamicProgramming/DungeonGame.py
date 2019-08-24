#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 0:58
# @Author  : tc
# @File    : DungeonGame.py

"""
题目比较复杂，详见：https://leetcode-cn.com/problems/dungeon-game/

一直在自顶向下走，发现一直解决不掉问题，看了答案，可以尝试自底向上走
答案参考:https://leetcode-cn.com/problems/dungeon-game/solution/dong-tai-gui-hua-by-powcai-8/
"""


def calculateMinimumHP(dungeon):
    row = len(dungeon)

    col = len(dungeon[0])

    dp = [[0] * col for _ in range(row)]

    # 初始化右下角
    dp[-1][-1] = max(1 - dungeon[-1][-1], 1)

    # 行
    for i in range(col - 2, -1, -1):
        dp[-1][i] = max(dp[-1][i + 1] - dungeon[-1][i], 1)

    #列
    for j in range(row - 2,-1,-1):
        dp[j][-1] = max(dp[j+1][-1] - dungeon[j][-1],1)

    for i in range(row - 2,-1,-1):
        for j in range(col - 2,-1,-1):
            dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)
    return dp[0][0]

if __name__ == '__main__':
    grid = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]

    print(calculateMinimumHP(grid))
