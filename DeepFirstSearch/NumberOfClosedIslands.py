# -*- coding: utf-8 -*-
# @File    : NumberOfClosedIslands.py
# @Date    : 2020-03-16
# @Author  : tc
"""
题号 1254. 统计封闭岛屿的数目
有一个二维矩阵 grid ，每个位置要么是陆地（记号为 0 ）要么是水域（记号为 1 ）。

我们从一块陆地出发，每次可以往上下左右 4 个方向相邻区域走，能走到的所有陆地区域，我们将其称为一座「岛屿」。

如果一座岛屿 完全 由水域包围，即陆地边缘上下左右所有相邻区域都是水域，那么我们将其称为 「封闭岛屿」。

请返回封闭岛屿的数目。

示例 1：

输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
输出：2
解释：
灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
示例 2：

输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
输出：1
示例 3：

输入：grid = [[1,1,1,1,1,1,1],
             [1,0,0,0,0,0,1],
             [1,0,1,1,1,0,1],
             [1,0,1,0,1,0,1],
             [1,0,1,1,1,0,1],
             [1,0,0,0,0,0,1],
             [1,1,1,1,1,1,1]]
输出：2

提示：

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1


参考：https://leetcode-cn.com/problems/number-of-closed-islands/solution/yi-ti-kan-tou-dfs-he-dfs-by-xiao-xiao-suan-fa/

使用DFS+标记位置，注意已经访问过的岛屿要标记，否则会无限堆栈，导致失败。

"""
from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    ret += self.dfs(grid,i,j)
        return ret


    def dfs(self,grid,r,c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return 0
        if grid[r][c] == 1:
            return 1
        grid[r][c] = 1
        vr = [0, -1, 0, 1]
        vc = [1, 0, -1, 0]
        ret = 1
        for i in range(4):
            ret = min(ret, self.dfs(grid, r + vr[i], c + vc[i]))
        return ret