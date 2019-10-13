#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 15:25
# @Author  : tc
# @File    : CourseSchedule.py
"""
题号:207 课程表
现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？

示例 1:

输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
说明:

输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
提示:

这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
拓扑排序也可以通过 BFS 完成。


这个问题是经典的通过拓扑排序判断一个图G是否是有向无环图(DAG)
拓扑排序的三大步骤:
1.定义一个队列queue,并把所有入度为0的结点加入队列;
2.当queue非空时,取出队首结点pre,然后依次删除所有从它出发的边,并令这些边到达的顶点的入度减1,如果某个顶点的入度为0,说明该结点的
所有前驱结点已经被删除,将该结点入队;
3.反复进行2的操作,直到队列为空。如果队列为空时入过队的结点数目恰好为N(结点的数量),说明拓扑排序成功,图G是有向无环图。否则,拓扑排序失败,
图G中有环,换个角度说,若图中存在环,一定有结点的入度始终不为0;

"""
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = []
        for cur, pre in prerequisites:
            indegrees[cur] += 1  # 计算每个结点的入度
            adjacency[pre].append(cur)  # 构造邻接矩阵,list的元素是指向该顶点的所有顶点
        print(indegrees)
        print(adjacency)
        for i in range(len(indegrees)):
            if not indegrees[i]:queue.append(i)  # 将所有入度为0的顶点入队
        while queue:  # 拓扑排序
            pre = queue.pop(0)  # 取队首顶点u
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1  # 顶点cur的入度减1
                if not indegrees[cur]:queue.append(cur)  # 顶点cur的入度减为0则入队
        return not numCourses

if __name__ == '__main__':
    numCourses = 2

    prerequisites = [[1,0],[0,1]]

    solution = Solution()

    print(solution.canFinish(numCourses,prerequisites))







