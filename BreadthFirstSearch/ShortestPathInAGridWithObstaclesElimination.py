# -*- coding: utf-8 -*-
# @File    : ShortestPathInAGridWithObstaclesElimination.py
# @Date    : 2022-06-21
# @Author  : tc
"""
1293. 网格中的最短路径
给你一个 m * n 的网格，其中每个单元格不是 0（空）就是 1（障碍物）。每一步，您都可以在空白单元格中上、下、左、右移动。
如果您 最多 可以消除 k 个障碍物，请找出从左上角 (0, 0) 到右下角 (m-1, n-1) 的最短路径，并返回通过该路径所需的步数。如果找不到这样的路径，则返回 -1 。

输入： grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
输出：6
解释：
不消除任何障碍的最短路径是 10。
消除位置 (3,2) 处的障碍后，最短路径是 6 。该路径是 (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

输入：grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
输出：-1
解释：我们至少需要消除两个障碍才能找到这样的路径。

经典BFS解法
"""

import collections
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        queue = collections.deque([(0, 0, k, 0)])
        visited = set()

        if k > (len(grid) - 1 + len(grid[0]) - 1):
            return len(grid) - 1 + len(grid[0]) - 1

        while queue:
            size = len(queue)
            for _ in range(size):
                row, col, eliminate, steps = queue.popleft()
                # if row == len(grid) - 1 and col == len(grid[0]) - 1:
                #     return steps
                # if (row, col, eliminate) in visited:
                #     continue

                # visited.add((row, col, eliminate))
                for new_row, new_col in [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]:
                    if new_row >= 0 and new_row <= len(grid) - 1 and new_col >= 0 and new_col <= len(grid[0]) - 1:
                        # 如果当前有障碍且可以消除,且此时肯定没有达到终点
                        if grid[new_row][new_col] == 1 and eliminate > 0 and (
                        new_row, new_col, eliminate - 1) not in visited:
                            queue.append((new_row, new_col, eliminate - 1, steps + 1))
                            visited.add((new_row, new_col, eliminate - 1))
                        elif grid[new_row][new_col] == 0 and (new_row, new_col, eliminate) not in visited:
                            if new_row == len(grid) - 1 and new_col == len(grid[0]) - 1:
                                return steps + 1
                            queue.append((new_row, new_col, eliminate, steps + 1))
                            visited.add((new_row, new_col, eliminate))
        return -1
