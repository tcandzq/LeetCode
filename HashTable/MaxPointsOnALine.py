# -*- coding: utf-8 -*-
# @File    : MaxPointsOnALine.py
# @Date    : 2020-10-11
# @Author  : tc
"""
题号 149. 直线上最多的点数
给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。

示例 1:

输入: [[1,1],[2,2],[3,3]]
输出: 3
解释:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4
示例 2:

输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出: 4
解释:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
"""
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)
        max_val = 0
        for i in range(len(points)):
            same = 1
            for j in range(i+1,len(points)):
                count = 0
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    same += 1
                else:
                    count += 1
                    x_diff = points[i][0] - points[j][0]
                    y_diff = points[i][1] - points[j][1]
                    for k in range(j+1, len(points)):
                        if x_diff * (points[i][1] - points[k][1]) == y_diff * (points[i][0] - points[k][0]):
                            count += 1
                max_val = max(max_val,same+count)
            # 若某次最大个数超过所有点的一半，则不可能存在其他直线通过更多的点
            if max_val > len(points) // 2:
                return max_val

        return max_val

if __name__ == '__main__':
    points = [[1,1],[2,2],[3,3]]

    solution = Solution()

    print(solution.maxPoints(points))
