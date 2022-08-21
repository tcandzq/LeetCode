# -*- coding: utf-8 -*-
# @File    : NetworkDelayTime.py
# @Date    : 2022-08-21
# @Author  : tc
"""
743. 网络延迟时间
有 n 个网络节点，标记为 1 到 n。
给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。
现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。

示例 1：
输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
输出：2

示例 2：
输入：times = [[1,2,1]], n = 2, k = 1
输出：1

示例 3：
输入：times = [[1,2,1]], n = 2, k = 2
输出：-1

题目实际是求节点K到其他所有点中最远的距离，那么首先需要求出节点K到其他所有点的最短路，然后取最大值即可。
单源最短路问题可以使用 Dijkstra 算法，其核心思路是贪心算法。流程如下：

1.首先，Dijkstra 算法需要从当前全部未确定最短路的点中，找到距离源点最短的点x。

2.其次，通过点x更新其他所有点距离源点的最短距离。例如目前点A距离源点最短，距离为 3；
  有一条 A->B 的有向边，权值为 1，那么从源点先去A点再去B点距离为 3 + 1 = 4，
  若原先从源点到B的有向边权值为 5，那么我们便可以更新B到源点的最短距离为 4。

3.当全部其他点都遍历完成后，一次循环结束，将x标记为已经确定最短路。进入下一轮循环，直到全部点被标记为确定了最短路。

本质是Dijkstra算法的实现
https://leetcode.cn/problems/network-delay-time/solution/gtalgorithm-dan-yuan-zui-duan-lu-chi-tou-w3zc/
"""
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 邻接矩阵
        g = [[float('inf')] * n for _ in range(n)]
        for x, y, time in times:
            g[x - 1][y - 1] = time

        # 距离数组，存储源点k到点 i 的最短距离，初始值也全部设为inf。
        dist = [float('inf')] * n
        # 由于本题源点为K，所以该点距离设为0。
        dist[k - 1] = 0

        # 标记数组，表示是否已确定最短距离
        used = [False] * n
        for _ in range(n):
            # 找到未标记最近的点
            x = -1
            for y, u in enumerate(used):
                # 在没有确定最小距离的点中找到距离源点最近的点
                if not u and (x == -1 or dist[y] < dist[x]):
                    x = y

            # 更新，x已经被确定最短距离
            used[x] = True
            for y, time in enumerate(g[x]):
                # x是新加入到已更新集合中的点，源点到x的最小距离是dist[x]；
                # 那么源点到剩下点y的最小距离 = min(源点到y的距离，源点到x的距离 + 点x到点y的距离)
                dist[y] = min(dist[y], dist[x] + time)
        # 选出源点到所有点中的最远距离
        ans = max(dist)
        return ans if ans < float('inf') else -1