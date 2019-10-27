#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 23:14
# @Author  : tc
# @File    : MaximalSquare.py
"""
题号 221 最大正方形
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4

参考1:https://leetcode-cn.com/problems/maximal-square/solution/zui-da-zheng-fang-xing-by-leetcode/
参考2:https://leetcode-cn.com/problems/maximal-square/solution/dong-tai-gui-hua-by-powcai-9/

在 matrix[i][j] == "1"，情况下

dp[i][j]表示0~i，0~j范围内的二维矩阵内最大右下角正方形边长

dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

"""
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        res = 0
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    res = max(res, dp[i][j] ** 2)
        return res

if __name__ == '__main__':
    matrix = [
        ['1', '0', '1', '0', '0'],
        ['1', '0', '1', '1', '1'],
        ['1', '1', '1', '1', '1'],
        ['1', '0', '0', '1', '0']
    ]
    solution = Solution()
    print(solution.maximalSquare(matrix))