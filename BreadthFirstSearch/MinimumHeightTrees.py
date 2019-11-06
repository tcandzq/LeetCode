#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 14:29
# @Author  : tc
# @File    : MinimumHeightTrees.py
"""
题号 310 最小高度树
对于一个具有树特征的无向图，我们可选择任何一个节点作为根。图因此可以成为树，在所有可能的树中，具有最小高度的树被称为最小高度树。给出这样的一个图，写出一个函数找到所有的最小高度树并返回他们的根节点。

格式

该图包含 n 个节点，标记为 0 到 n - 1。给定数字 n 和一个无向边 edges 列表（每一个边都是一对标签）。

你可以假设没有重复的边会出现在 edges 中。由于所有的边都是无向边， [0, 1]和 [1, 0] 是相同的，因此不会同时出现在 edges 里。

示例 1:

输入: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3

输出: [1]
示例 2:

输入: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5

输出: [3, 4]
说明:

根据树的定义，树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。
树的高度是指根节点和叶子节点之间最长向下路径上边的数量。

毫无思路,看网上的答案说是用"剥洋葱"的解法,不断删除叶子结点,逐渐逼近根结点,会有一些新的节点成为叶子节点，于是继续循环删除，直至不能删除为止，那么剩下的节点就是高度最小的根。

最小高度树的特点是根位于某条最长路径的中点

那么怎么得到中间的那一个或者两个点呢？

通过一层一层地将边缘的叶子节点去掉之后，最后保存下来的一个或者两个点就是结果。

"""
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        if not edges:
            return [0]
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        # 叶子节点
        leaves = [i for i in graph if len(graph[i]) == 1]  # 和叶子结点相连的点都只有一个
        while n > 2:
            n -= len(leaves)
            nxt_leaves = []
            for leave in leaves:
                # 与叶子节点相连的点找到
                tmp = graph[leave].pop()
                # 相连的点删去这个叶子节点
                graph[tmp].remove(leave)
                if len(graph[tmp]) == 1:
                    nxt_leaves.append(tmp)
            leaves = nxt_leaves
        return list(leaves)


if __name__ == '__main__':
    n = 6
    edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    solution = Solution()
    print(solution.findMinHeightTrees(n,edges))