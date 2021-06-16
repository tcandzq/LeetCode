# -*- coding: utf-8 -*-
# @File    : UniquePaths.py
# @Date    : 2021-06-14
# @Author  : tc
"""
题号:62. 不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

示例 1：

输入：m = 3, n = 7
输出：28
示例 2：

输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
示例 3：

输入：m = 7, n = 3
输出：28
示例 4：

输入：m = 3, n = 3
输出：6

经典的动态规划问题，可以一步一步优化，将空间复杂度从O(m*n)降低到O(n)

注意:python中的数组的深拷贝和浅拷贝。

代码参考:https://leetcode-cn.com/problems/unique-paths/solution/dong-tai-gui-hua-by-powcai-2/
想法参考:https://leetcode.com/problems/unique-paths/discuss/22954/C%2B%2B-DP

"""
class Solution:
    # 版本1
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1,n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    # 优化1
    def uniquePaths(self, m: int, n: int) -> int:
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1,n):
                cur[j] = pre[j] + cur[j - 1]
            pre = cur[:]
        return pre[n - 1]

    # 优化2
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1,n):
                cur[j] += cur[j - 1]
        return cur[n - 1]
