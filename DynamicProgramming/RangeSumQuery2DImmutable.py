# -*- coding: utf-8 -*-
# @File    : RangeSumQuery2DImmutable.py
# @Date    : 2020-03-01
# @Author  : tc
"""
题号 304. 二维区域和检索 - 矩阵不可变
给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2)。

Range Sum Query 2D
上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。

示例:

给定 matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
说明:

你可以假设矩阵不可变。
会多次调用 sumRegion 方法。
你可以假设 row1 ≤ row2 且 col1 ≤ col2。

参考：https://leetcode.com/problems/range-sum-query-2d-immutable/discuss/75350/Clean-C%2B%2B-Solution-and-Explaination-O(mn)-space-with-O(1)-time

"""
from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix) if len(matrix) else 0
        cols = len(matrix[0]) if len(matrix[0]) else 0
        self.sums = [[0] * (cols+1) for _ in range(rows+1)]
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                self.sums[i][j] = matrix[i-1][j-1] + self.sums[i-1][j] + self.sums[i][j-1] - self.sums[i-1][j-1]
        print(self.sums)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return self.sums[row2+1][col2+1] - self.sums[row2+1][col1] - self.sums[row1][col2+1] + self.sums[row1][col1]

if __name__ == '__main__':
    matrix = [
          [3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]
        ]

    num_matrix = NumMatrix(matrix)
    print(num_matrix.sumRegion(2, 1, 4, 3))







# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)