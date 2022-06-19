# -*- coding: utf-8 -*-
# @File    : KnightProbabilityInChessboard.py
# @Date    : 2022-06-19
# @Author  : tc
"""
688. 骑士在棋盘上的概率
在一个 n x n 的国际象棋棋盘上，一个骑士从单元格 (row, column) 开始，并尝试进行 k 次移动。行和列是 从 0 开始 的，所以左上单元格是 (0,0) ，
右下单元格是 (n - 1, n - 1) 。

象棋骑士有8种可能的走法，如下图所示。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格。
每次骑士要移动时，它都会随机从8种可能的移动中选择一种(即使棋子会离开棋盘)，然后移动到那里。

骑士继续移动，直到它走了 k 步或离开了棋盘。

返回 骑士在棋盘停止移动后仍留在棋盘上的概率 。
示例 1：

输入: n = 3, k = 2, row = 0, column = 0
输出: 0.0625
解释: 有两步(到(1,2)，(2,1))可以让骑士留在棋盘上。
在每一个位置上，也有两种移动可以让骑士留在棋盘上。
骑士留在棋盘上的总概率是0.0625。
示例 2：

输入: n = 1, k = 0, row = 0, column = 0
输出: 1.00000

经典DFS解法,由于骑士走其中一个方向的概率是1/8，每做出一个选择都要除以1/8
"""
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # memo = [[[0] * n for i in range(n)] for i in range(k+1)]
        memo = {}
        return self.dfs(n, k, row, column, memo)

    def dfs(self, n, k, row, col, memo):
        if row < 0 or col < 0 or row >= n or col >= n:
            return 0
        if k == 0:
            return 1
        print(row, col, k)
        if (row, col, k) in memo:
            # return memo[row][col][k]
            return memo[(row, col, k)]

        ans = 0
        paths = [[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1],[2,1],[1,2]]
        for path in paths:
            ans += self.dfs(n, k - 1, row+path[0], col + path[1], memo) / 8

        # memo[row][col][k] = ans
        memo[(row, col, k)] = ans
        return ans