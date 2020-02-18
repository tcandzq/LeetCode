# -*- coding: utf-8 -*-
# @File    : JumpGameIII.py
# @Date    : 2020-02-18
# @Author  : tc
"""
题号 1306 跳跃游戏III
这里有一个非负整数数组 arr，你最开始位于该数组的起始下标 start 处。当你位于下标 i 处时，你可以跳到 i + arr[i] 或者 i - arr[i]。

请你判断自己是否能够跳到对应元素值为 0 的 任意 下标处。

注意，不管是什么情况下，你都无法跳到数组之外。


示例 1：

输入：arr = [4,2,3,0,3,1,2], start = 5
输出：true
解释：
到达值为 0 的下标 3 有以下可能方案：
下标 5 -> 下标 4 -> 下标 1 -> 下标 3
下标 5 -> 下标 6 -> 下标 4 -> 下标 1 -> 下标 3
示例 2：

输入：arr = [4,2,3,0,3,1,2], start = 0
输出：true
解释：
到达值为 0 的下标 3 有以下可能方案：
下标 0 -> 下标 4 -> 下标 1 -> 下标 3
示例 3：

输入：arr = [3,0,2,1,2], start = 2
输出：false
解释：无法到达值为 0 的下标 1 处。
 

提示：

1 <= arr.length <= 5 * 10^4
0 <= arr[i] < arr.length
0 <= start < arr.length

"""
from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        queue = [start]
        visited = set()
        while queue:
            temp = []
            for loc in queue:
                if arr[loc] == 0:
                    return True
                if 0 <= loc + arr[loc] < n and loc + arr[loc] not in visited:
                    temp.append(loc + arr[loc])
                    visited.add(loc + arr[loc])
                if 0 <= loc - arr[loc] < n and loc - arr[loc] not in visited:
                    temp.append(loc - arr[loc])
                    visited.add(loc - arr[loc])
            queue = temp
        return False

    # 官方题解
    def canReach2(self, arr: List[int], start: int) -> bool:
        from collections import deque
        n = len(arr)
        queue = deque([start])
        visited = {start}
        while queue:
            loc = queue.popleft()
            for v in [loc+arr[loc],loc-arr[loc]]:
                if 0 <= v < n and v not in visited:
                    if arr[v] == 0:
                        return True
                    queue.append(v)
                    visited.add(v)
        return False

if __name__ == '__main__':
    arr = [3,0,2,1,2]
    start = 2
    solution = Solution()
    print(solution.canReach(arr,start))