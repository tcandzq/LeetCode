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

"""
from typing import List


class Solution:
    directions = [(-1,-1),(-1,0),(0,-1)]
    #  暴力解
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        pass

    # 优化暴力解

