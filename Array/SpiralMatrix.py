#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 21:47
# @Author  : tc
# @File    : SpiralMatrix.py
"""
题号 54 螺旋矩阵
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

参考:https://leetcode-cn.com/problems/spiral-matrix/solution/cxiang-xi-ti-jie-by-youlookdeliciousc-3/

"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res
        up = 0
        down = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while True:
            for i in range(left,right+1):  # 1.从左边移动到最右
                res.append(matrix[up][i])
            up += 1  # 2.重新设定上边界，若上边界大于下边界，则遍历遍历完成，下同
            if up > down:
                break
            for i in range(up,down+1):
                res.append(matrix[i][right]) # 3. 从上到下
            right -= 1  # 重新设定右边界
            if left > right:
                break
            for i in range(right,left-1,-1): # 从右往左
                res.append(matrix[down][i])
            down -= 1  # 重新设定下边界
            if down < up:
                break
            for i in range(down,up-1,-1):  # 从下往上
                res.append(matrix[i][left])
            left += 1  # 重新设定左边界
            if left > right:
                break
        return res


if __name__ == '__main__':
    matrix = [
             [1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]
            ]

    solution = Solution()
    print(solution.spiralOrder(matrix))