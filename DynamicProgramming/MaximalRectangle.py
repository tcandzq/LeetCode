#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 9:27
# @Author  : tc
# @File    : MaximalRectangle.py
"""
题号:85 最大矩形
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6

不会做,参考:https://leetcode-cn.com/problems/maximal-rectangle/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-1-8/

从这题开始要做到一题多解,做题的目的不是为了刷题,是为了增加做题的技巧,不是为了和别人说我刷了XX题,而是真的能够提升自己。

本题的一种解法需要利用84题(柱状图中最大的矩形)写好的函数

"""
from typing import List


class Solution:
    #  单调栈解法(利用84题的结果)
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        max_rectangle = 0
        heights = [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1" and not heights[j]:
                    heights[j] = 1
                elif matrix[i][j] == "1" and heights[j] :
                    heights[j] += 1
                elif matrix[i][j] == "0":
                    heights[j] = 0
            print(heights)
            max_rectangle = max(max_rectangle,self.largestRectangleArea(heights))
        return max_rectangle

    def largestRectangleArea(self,heights):
        stack = []
        p = 0
        max_area = 0
        while p < len(heights):
            if not stack:
                stack.append(p)
                p += 1
            else:
                if heights[p] >= heights[stack[-1]]:
                    stack.append(p)
                    p += 1
                else:
                    height = heights[stack.pop()]
                    left_less_min = -1 if not stack else stack[-1]  # 左边以第一个小于柱子的下标
                    right_less_min = p
                    max_area = max(max_area,(right_less_min - left_less_min - 1)*height)
        while stack:
            height = heights[stack.pop()]
            left_less_min = -1 if not stack else stack[-1]  # 左边以第一个小于柱子的下标
            right_less_min = len(heights)
            max_area = max(max_area,(right_less_min - left_less_min - 1)*height)
        return max_area

if __name__ == '__main__':
    matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
    solution = Solution()
    print(solution.maximalRectangle(matrix))

