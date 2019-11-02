#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/31 11:25
# @Author  : tc
# @File    : SurroundedRegions.py
"""
题号 130 被围绕的区域
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

Input:
X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：
X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

本题有3种解法：
1.DFS
2.BFS
3.并查集

思路：先解决边界上的'O'或与边界上的相连通的'O'情况，然后再统一处理。

参考：https://leetcode-cn.com/problems/surrounded-regions/solution/dfs-bfs-bing-cha-ji-by-powcai/

"""
from typing import List

class Solution:
    #  DFS解法
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        #  这个dfs的代码可以拿来做模板
        def dfs(i, j):
            board[i][j] = 'B'
            for x,y in [(-1,0),(0,-1),(1,0),(0,1)]:
                tmp_i = x + i
                tmp_j = y + j

            #  注意这里的边界是1和row，或者0和row - 1
                if 0 <= tmp_i <= row - 1 and 0 <= tmp_j <= col - 1 and board[tmp_i][tmp_j] == 'O':
                    dfs(tmp_i, tmp_j)

        # 下面开始对边界情况进行处理

        for j in range(col):  # 第一行
            if board[0][j] == 'O':
                dfs(0, j)
            if board[row - 1][j] == 'O':  # 最后一行
                dfs(row - 1, j)

        for i in range(row):
            if board[i][0] == 'O':  # 第一列
                dfs(i,0)
            if board[i][col - 1] == 'O':  # 最后一列
                dfs(i, col - 1)

        for i in range(0,row):
            for j in range(0,col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'B':
                    board[i][j] = 'O'

    #  BFS解法

    # 并查集解法



if __name__ == '__main__':
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]

    solution = Solution()
    print(solution.solve(board))
