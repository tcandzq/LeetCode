# -*- coding: utf-8 -*-
# @File    : MinimumNumberOfRefuelingStops.py
# @Date    : 2022-08-21
# @Author  : tc
"""
871. 最低加油次数
汽车从起点出发驶向目的地，该目的地位于出发位置东面 target 英里处。
沿途有加油站，每个 station[i] 代表一个加油站，它位于出发位置东面 station[i][0] 英里处，并且有 station[i][1] 升汽油。
假设汽车油箱的容量是无限的，其中最初有 startFuel 升燃料。它每行驶 1 英里就会用掉 1 升汽油。
当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。
为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 -1 。
注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。

示例 1：
输入：target = 1, startFuel = 1, stations = []
输出：0
解释：我们可以在不加油的情况下到达目的地。

示例 2：
输入：target = 100, startFuel = 1, stations = [[10,100]]
输出：-1
解释：我们无法抵达目的地，甚至无法到达第一个加油站。

示例 3：
输入：target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
输出：2
解释：
我们出发时有 10 升燃料。
我们开车来到距起点 10 英里处的加油站，消耗 10 升燃料。将汽油从 0 升加到 60 升。
然后，我们从 10 英里处的加油站开到 60 英里处的加油站（消耗 50 升燃料），
并将汽油从 10 升加到 50 升。然后我们开车抵达目的地。
我们沿途在1两个加油站停靠，所以返回 2 。

思路:
路上的不是加油站，而是一桶桶的油，每次经过的时候，就把油带上，
当油不够的时候我们就取身上最大的那桶油加上，这样如果身上没油了，那么就到不了了.

贪心 + 优先队列(堆)
"""
import heapq
from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if target <= startFuel:
            return 0

        heap = []
        remainFuel = startFuel  # 剩余的汽油
        pos = 0  # 经过的加油站
        res = 0  # 加油次数
        while remainFuel < target:
            for i in range(pos, len(stations)):
                if remainFuel >= stations[i][0]:  # 可以到达这个加油站
                    heapq.heappush(heap, -stations[i][1])  # 带上这桶油
                    pos += 1  # 这个加油站已经路过了
            # 已经路过了能到达到最远加油站
            if remainFuel < target:
                if not heap:  # 身上没有油了
                    return -1
                remainFuel -= heapq.heappop(heap)
                res += 1  # 加油次数加一
        return res
