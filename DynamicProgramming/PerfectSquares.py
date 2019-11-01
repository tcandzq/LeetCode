#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 1:22
# @Author  : tc
# @File    : PerfectSquares.py
"""
题号 279 完全平方数
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

本题解法较多有动态规划、BFS等

参考:https://leetcode-cn.com/problems/perfect-squares/solution/bfs-dong-tai-gui-hua-shu-xue-by-powcai/

其实这个问题也可以转化为一个树问题来解决:
https://leetcode-cn.com/problems/perfect-squares/solution/bu-zhi-shi-da-an-er-shi-dong-tai-gui-hua-lei-ti-de/


"""
class Solution:

    # 动态规划解法(超时)
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]

    # 动态规划解法(优化，目前没看懂)
    _dp = [0]
    def numSquares_2(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i * i] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1,
        return dp[n]

    # BFS + 剪枝解法
    def numSquares_3(self, n):
        from collections import deque
        if n == 0: return 0
        queue = deque([n])
        step = 0
        visited = set()
        while queue:
            step += 1
            l = len(queue)
            for _ in range(l):
                tmp = queue.pop()
                for i in range(1, int(tmp ** 0.5) + 1):
                    diff = tmp - i ** 2
                    if diff == 0:
                        return step
                    if diff not in visited:
                        visited.add(diff)
                        queue.appendleft(diff)
        return step

if __name__ == '__main__':
    n = 12
    solution = Solution()
    print(solution.numSquares_3(n))