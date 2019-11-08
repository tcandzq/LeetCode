#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/8 9:30
# @Author  : tc
# @File    : UniquePathsIII.py
"""
题号 980 不同路径 III
在二维网格 grid 上，有 4 种类型的方格：

1 表示起始方格。且只有一个起始方格。
2 表示结束方格，且只有一个结束方格。
0 表示我们可以走过的空方格。
-1 表示我们无法跨越的障碍。
返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目，每一个无障碍方格都要通过一次。

 

示例 1：

输入：[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
输出：2
解释：我们有以下两条路径：
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
示例 2：

输入：[[1,0,0,0],[0,0,0,0],[0,0,0,2]]
输出：4
解释：我们有以下四条路径：
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
示例 3：

输入：[[0,1],[2,0]]
输出：0
解释：
没有一条路能完全穿过每一个空的方格一次。
请注意，起始和结束方格可以位于网格中的任意位置。


"""
from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def neighbor(r, c):  # 四个方向遍历
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:  # -1点是障碍物,不走
                    yield nr, nc

        todo = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val != -1:
                    todo += 1
                if val == 1:
                    sr, sc = r, c
                if val == 2:
                    tr, tc = r, c

        self.ans = 0

        def dfs(r, c, todo):
            todo -= 1
            if todo < 0:
                return
            if r == tr and c == tc:
                if todo == 0:
                    self.ans += 1
                return

            grid[r][c] = -1  # 尝试遍历每一个 0 方格，并在走过的方格里留下一个障碍
            for nr, nc in neighbor(r, c):
                dfs(nr, nc, todo)
            grid[r][c] = 0  # 状态回溯

        dfs(sr, sc, todo)
        return self.ans


if __name__ == '__main__':
    # grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    # solution = Solution()
    # print(solution.uniquePathsIII(grid))

    print((-1) % 2)
