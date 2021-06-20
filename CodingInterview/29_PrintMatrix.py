# -*- coding: utf-8 -*-
# @File    : 29_PrintMatrix.py
# @Date    : 2021-06-21
# @Author  : tc
"""
剑指 Offer 29. 顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。



示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]


限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100

参考：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/solution/mian-shi-ti-29-shun-shi-zhen-da-yin-ju-zhen-she-di/

"""
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        top = 0
        while True:
            # 从左到右
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                break
            # 从上到下
            for j in range(top, bottom + 1):
                res.append(matrix[j][right])
            right -= 1
            if left > right:
                break
            # 从右到左
            for k in range(right, left - 1, -1):
                res.append(matrix[bottom][k])
            bottom -= 1
            if top > bottom:
                break
            # 从下到上
            for m in range(bottom, top - 1, -1):
                res.append(matrix[m][left])
            left += 1
            if left > right:
                break
        return res
