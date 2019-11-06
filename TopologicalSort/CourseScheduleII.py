#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 16:25
# @Author  : tc
# @File    : CourseScheduleII.py
"""
题号 210 课程表II
现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。

可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

示例 1:

输入: 2, [[1,0]]
输出: [0,1]
解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
示例 2:

输入: 4, [[1,0],[2,0],[3,1],[3,2]]
输出: [0,1,2,3] or [0,2,1,3]
解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
     因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
说明:

输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
提示:

这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
拓扑排序也可以通过 BFS 完成。

实际就是对课程进行拓扑排序,直接套用拓扑排序的模板

DFS解法参考:

"""
from typing import List


class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            in_degrees[cur] += 1  # 计算每个结点的入度
            adjacency[pre].append(cur)  # 构造邻接矩阵,list的元素是从该顶点出发的所有边

        queue = [i for i in range(len(in_degrees)) if not in_degrees[i]]
        print(queue)
        res = []
        while queue:
            pre = queue.pop()
            res.append(pre)
            for cur in adjacency[pre]:
                in_degrees[cur] -= 1
                if in_degrees[cur] == 0:
                    queue.append(cur)

        return [] if queue else res

if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    solution = Solution()
    print(solution.findOrder(numCourses, prerequisites))
