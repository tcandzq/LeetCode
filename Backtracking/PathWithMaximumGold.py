# -*- coding: utf-8 -*-
# @File    : PathWithMaximumGold.py
# @Date    : 2021-06-27
# @Author  : tc
"""
题号 1219. 黄金矿工
你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 0。

为了使收益最大化，矿工需要按以下规则来开采黄金：

每当矿工进入一个单元，就会收集该单元格中的所有黄金。
矿工每次可以从当前位置向上下左右四个方向走。
每个单元格只能被开采（进入）一次。
不得开采（进入）黄金数目为 0 的单元格。
矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。

示例 1：

输入：grid = [[0,6,0],[5,8,7],[0,9,0]]
输出：24
解释：
[[0,6,0],
 [5,8,7],
 [0,9,0]]
一种收集最多黄金的路线是：9 -> 8 -> 7。
示例 2：

输入：grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
输出：28
解释：
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
一种收集最多黄金的路线是：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7。

使用回溯算法尝试所有的路径，返回具有最多金矿的路径

不错的讲解1:https://leetcode-cn.com/problems/path-with-maximum-gold/solution/hui-su-suan-fa-tu-wen-xiang-jie-by-sdwwld/

https://leetcode-cn.com/problems/path-with-maximum-gold/solution/c-python3-jing-dian-hui-su-cyong-functio-f4rk/

"""
from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def trace_back(r, c):
            if r < 0 or r == m or c < 0 or c == n or grid[r][c] == 0:
                return 0
            origin = grid[r][c]
            grid[r][c] = 0
            maxGold = 0
            for nr, nc in ((r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)):
                maxGold = max(trace_back(nr, nc), maxGold)
            grid[r][c] = origin
            return maxGold + origin

        m = len(grid)
        n = len(grid[0])
        return max([trace_back(i, j) for j in range(n) for i in range(m)])