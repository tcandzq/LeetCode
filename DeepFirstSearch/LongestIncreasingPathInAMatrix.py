#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 15:17
# @Author  : tc
# @File    : LongestIncreasingPathInAMatrix.py
"""
题号 329 矩阵中的最长递增路径

给定一个整数矩阵，找出最长递增路径的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

示例 1:

输入: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
输出: 4
解释: 最长递增路径为 [1, 2, 6, 9]。
示例 2:

输入: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
输出: 4
解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。

本题有3种解法
1.DFS
2.DFS+记忆化
3.动态规划

思路：每个单元格可以看作图G中的一个定点。若两相邻两个单元格的值满足 a < b，则存在有向边 (a, b)。问题转化成：

寻找有向图G中的最长路径。

dfs部分的代码可以参考LeetCode 130题 被围绕的区域

解法1是对每个单元格都进行dfs，其中肯定有很多单元格都重复计算过了，在搜索过程中，如果未计算过单元格的结果，我们会计算并将其缓存；否则，直接从缓存中获取之。

"""
from typing import List

class Solution:

    # dfs(超时)
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, self.dfs1(i,j,matrix))

        return ans

    def dfs1(self, i, j, matrix):
        ans = 0
        for x, y in [(-1,0),(0,-1),(0,1),(1,0)]:
            tmp_i = x + i
            tmp_j = y + j

            if 0 <= tmp_i <= len(matrix) - 1 and 0 <= tmp_j <= len(matrix[0]) - 1:
                if matrix[tmp_i][tmp_j] > matrix[i][j]:
                    # dfs(tmp_i, tmp_j, tmp+[matrix[tmp_i][tmp_j]])
                    ans = max(ans, self.dfs1(tmp_i,tmp_j,matrix))
        return ans + 1  # 考虑下为什么这里要加1?

    #  dfs+记忆化
    def longestIncreasingPath2(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        cache = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, self.dfs2(matrix,i,j,cache))

        return ans

    def dfs2(self,matrix,i, j, cache):
        if cache[i][j]:
            return cache[i][j]
        for x, y in [(-1,0), (0,-1), (0,1), (1,0)]:
            tmp_i = x + i
            tmp_j = y + j

            if 0 <= tmp_i <= len(matrix) - 1 and 0 <= tmp_j <= len(matrix[0]) - 1:
                if matrix[tmp_i][tmp_j] > matrix[i][j]:
                    # dfs(tmp_i, tmp_j, tmp+[matrix[tmp_i][tmp_j]])
                    cache[i][j] = max(cache[i][j], self.dfs2(matrix,tmp_i,tmp_j,cache))
        cache[i][j] += 1
        return cache[i][j]


    # 拓扑排序


if __name__ == '__main__':
    nums =[
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]
    solution = Solution()
    print(solution.longestIncreasingPath2(nums))