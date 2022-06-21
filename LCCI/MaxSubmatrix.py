# -*- coding: utf-8 -*-
# @File    : MaxSubmatrix.py
# @Date    : 2022-06-21
# @Author  : tc
"""
面试题 17.24. 最大子矩阵
给定一个正整数、负整数和 0 组成的 N × M 矩阵，编写代码找出元素总和最大的子矩阵。

返回一个数组 [r1, c1, r2, c2]，其中 r1, c1 分别代表子矩阵左上角的行号和列号，r2, c2 分别代表右下角的行号和列号。若有多个满足条件的子矩阵，返回任意一个均可。

注意：本题相对书上原题稍作改动

示例：

输入：
[
   [-1,0],
   [0,-1]
]
输出：[0,1,0,1]
解释：输入中标粗的元素即为输出所表示的矩阵

和最大子序和类似：
https://leetcode.cn/problems/max-submatrix-lcci/solution/zhe-yao-cong-zui-da-zi-xu-he-shuo-qi-you-jian-dao-/

"""
from typing import  List

class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        ans = [0] * 4
        n = len(matrix)
        m = len(matrix[0])
        max_sum = float("-inf")
        bestrl, bestcl = 0, 0

        for i in range(n):
            b = [0] * m
            for j in range(i, n):
                sum = 0
                for k in range(m):
                    b[k] += matrix[j][k]
                    if sum > 0:
                        sum += b[k]
                    else:
                        sum = b[k]
                        bestrl = i
                        bestcl = k
                    if sum > max_sum:
                        max_sum = sum
                        ans[0] = bestrl
                        ans[1] = bestcl
                        ans[2] = j
                        ans[3] = k
        return ans