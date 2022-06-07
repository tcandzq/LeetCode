# -*- coding: utf-8 -*-
# @File    : CutOffTreesForGolfEvent.py
# @Date    : 2022-06-08
# @Author  : tc
"""
675. 为高尔夫比赛砍树
你被请来给一个要举办高尔夫比赛的树林砍树。树林由一个 m x n 的矩阵表示， 在这个矩阵中：

0 表示障碍，无法触碰
1 表示地面，可以行走
比 1 大的数 表示有树的单元格，可以行走，数值表示树的高度
每一步，你都可以向上、下、左、右四个方向之一移动一个单位，如果你站的地方有一棵树，那么你可以决定是否要砍倒它。

你需要按照树的高度从低向高砍掉所有的树，每砍过一颗树，该单元格的值变为 1（即变为地面）。

你将从 (0, 0) 点开始工作，返回你砍完所有树需要走的最小步数。 如果你无法砍完所有的树，返回 -1 。

可以保证的是，没有两棵树的高度是相同的，并且你至少需要砍倒一棵树。

 示例 1：
输入：forest = [[1,2,3],[0,0,4],[7,6,5]]
输出：6
解释：沿着上面的路径，你可以用 6 步，按从最矮到最高的顺序砍掉这些树。

示例 2：
输入：forest = [[1,2,3],[0,0,0],[7,6,5]]
输出：-1
解释：由于中间一行被障碍阻塞，无法访问最下面一行中的树。
示例 3：

输入：forest = [[2,3,4],[0,0,5],[8,7,6]]
输出：6
解释：可以按与示例 1 相同的路径来砍掉所有的树。
(0,0) 位置的树，可以直接砍去，不用算步数。

经典BFS解法，注意只能从低往高砍树，所以每次的终点都在不断更新。
"""
import  collections
from typing import List

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        M = len(forest)
        N = len(forest[0])
        trees = []
        for i in range(M):
            for j in range(N):
                if (forest[i][j] > 1):
                    trees.append((forest[i][j], i, j))
        trees.sort()
        preX, preY = 0, 0
        res = 0
        for height, curX, curY in trees:
            steps = self.bfs(forest, preX, preY, curX, curY)
            if steps == -1:
                return -1
            res += steps
            preX, preY = curX, curY
        return res

    def bfs(self, forest, startX, startY, targetX, targetY):
        M = len(forest)
        N = len(forest[0])
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        steps = 0
        queue = collections.deque()
        queue.append((startX, startY))
        visited = set()
        visited.add((startX, startY))
        while queue:
            size = len(queue)
            for _ in range(size):
                curX, curY = queue.popleft()
                if curX == targetX and curY == targetY:
                    return steps
                for d in dirs:
                    nX = curX + d[0]
                    nY = curY + d[1]
                    if 0 <= nX < M and 0 <= nY < N and forest[nX][nY] != 0 and ((nX, nY) not in visited):
                        queue.append((nX, nY))
                        visited.add((nX, nY))
            steps +=1
        return -1
