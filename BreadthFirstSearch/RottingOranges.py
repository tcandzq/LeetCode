#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 23:12
# @Author  : tc
# @File    : RottingOranges.py
"""
题号 994 腐烂的橘子

在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

示例 1：

输入：[[2,1,1],[1,1,0],[0,1,1]]
输出：4
示例 2：

输入：[[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
示例 3：

输入：[[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
 
"""
from typing import List

class Solution:
    #  垃圾版
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottings = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rottings.append((i,j))
        count = 0
        while rottings:
            new_rottings = []
            for i,j in rottings:
                for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    tmp_i = x + i
                    tmp_j = y + j
                    if 0 <= tmp_i <= len(grid) - 1 and 0 <= tmp_j <= len(grid[0]) - 1 and grid[tmp_i][tmp_j] == 1:
                        grid[tmp_i][tmp_j] = 2
                        new_rottings.append((tmp_i,tmp_j))
            if new_rottings:
                count += 1
            rottings = new_rottings
        for nums in grid:
            for num in nums:
                if num == 1:
                    return -1
        return count

    #  优雅版
    def orangesRotting2(self, grid):
        from collections import deque
        R, C = len(grid), len(grid[0])

        # queue - all starting cells with rotting oranges
        queue = deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))  # 统计grid中2的位置

        def neighbors(r, c):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d + 1))

        if any(1 in row for row in grid):
            return -1
        return d



if __name__ == '__main__':
    grid = [[0,2]]
    solution = Solution()
    print(solution.orangesRotting(grid))