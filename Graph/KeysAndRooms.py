# -*- coding: utf-8 -*-
# @File    : KeysAndRooms.py
# @Date    : 2020-02-27
# @Author  : tc
"""
题号 841. 钥匙和房间
有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。

在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，其中 N = rooms.length。 钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。

最初，除 0 号房间外的其余所有房间都被锁住。

你可以自由地在房间之间来回走动。

如果能进入每个房间返回 true，否则返回 false。

示例 1：

输入: [[1],[2],[3],[]]
输出: true
解释:
我们从 0 号房间开始，拿到钥匙 1。
之后我们去 1 号房间，拿到钥匙 2。
然后我们去 2 号房间，拿到钥匙 3。
最后我们去了 3 号房间。
由于我们能够进入每个房间，我们返回 true。
示例 2：

输入：[[1,3],[3,0,1],[2],[0]]
输出：false
解释：我们不能进入 2 号房间。
提示：

1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
所有房间中的钥匙数量总计不超过 3000。

参考：https://leetcode-cn.com/problems/keys-and-rooms/solution/7xing-dfs-8xing-bfs-liang-chong-fang-fa-san-chong-/

"""
from typing import List

class Solution:
    # dfs+递归
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        def dfs(room_index,visited):
            visited.add(room_index)
            for key in rooms[room_index]:
                if key not in visited:
                    dfs(key,visited)
        dfs(0,visited)
        return len(visited) == len(rooms)

    # dfs+迭代
    def canVisitAllRooms2(self, rooms: List[List[int]]) -> bool:
        visited,stack = {0},[0]
        while stack:
            room_index = stack.pop()
            for key in rooms[room_index]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)
        return len(visited) == len(rooms)

    # bfs+迭代
    def canVisitAllRooms3(self, rooms: List[List[int]]) -> bool:
        visited,queue = {0},[0]
        while queue:
            room_index = queue.pop()
            for key in rooms[room_index]:
                if key not in visited:
                    visited.add(key)
                    queue.insert(0,key)
        return len(visited) == len(rooms)

if __name__ == '__main__':
    rooms = [[1], [2], [3], []]
    solution = Solution()
    print(solution.canVisitAllRooms(rooms))