# -*- coding: utf-8 -*-
# @File    : ErectTheFence.py
# @Date    : 2022-06-19
# @Author  : tc
"""
587. 安装栅栏
在一个二维的花园中，有一些用 (x, y) 坐标表示的树。由于安装费用十分昂贵，你的任务是先用最短的绳子围起所有的树。
只有当所有的树都被绳子包围时，花园才能围好栅栏。你需要找到正好位于栅栏边界上的树的坐标。

输入: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
输出: [[1,1],[2,0],[4,2],[3,3],[2,4]]

输入: [[1,2],[2,2],[4,2]]
输出: [[1,2],[2,2],[4,2]]

二维凸包模板问题,完全看不懂问题
"""
from typing import List

class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        n = len(points)
        if n < 3: return points
        points.sort(key = lambda x:(x[0],x[1]))
        cross = lambda a,b,c:(b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0])
        lower = []
        for p in points:
            while len(lower) > 1 and cross(lower[-2],lower[-1],p) < 0: lower.pop()
            lower.append((p[0],p[1]))
        upper = []
        for p in reversed(points):
            while len(upper) > 1 and cross(upper[-2],upper[-1],p) < 0: upper.pop()
            upper.append((p[0],p[1]))
        return list(set(lower[:-1] + upper[:-1]))
