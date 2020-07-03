# -*- coding: utf-8 -*-
# @File    : ShortestPathVisitingAllNodes.py
# @Date    : 2020-07-03
# @Author  : tc
"""
题号 847. 访问所有节点的最短路径
给出 graph 为有 N 个节点（编号为 0, 1, 2, ..., N-1）的无向连通图。

graph.length = N，且只有节点 i 和 j 连通时，j != i 在列表 graph[i] 中恰好出现一次。

返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。


示例 1：

输入：[[1,2,3],[0],[0],[0]]
输出：4
解释：一个可能的路径为 [1,0,2,0,3]
示例 2：

输入：[[1],[0,2,4],[1,3,4],[2],[1,2]]
输出：4
解释：一个可能的路径为 [0,1,4,2,3]


提示：

1 <= graph.length <= 12
0 <= graph[i].length < graph.length

参考：https://leetcode.com/problems/shortest-path-visiting-all-nodes/discuss/147123/Python-8-lines-Heapq-and-BFS-and-Deque-solutions

"""
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        memo, final, q, steps = set(), (1 << len(graph)) - 1, [(i, 1 << i) for i in range(len(graph))], 0
        while True:
            new = []
            for node, state in q:
                if state == final: return steps
                for v in graph[node]:
                    if (state | 1 << v, v) not in memo:
                        new.append((v, state | 1 << v))
                        memo.add((state | 1 << v, v))
            q = new
            steps += 1



if __name__ == '__main__':
    pass
