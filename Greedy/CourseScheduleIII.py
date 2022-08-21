# -*- coding: utf-8 -*-
# @File    : CourseScheduleIII.py
# @Date    : 2022-08-21
# @Author  : tc
"""
630. 课程表 III
这里有 n 门不同的在线课程，按从 1 到 n 编号。给你一个数组 courses ，其中 courses[i] = [durationi, lastDayi] 表示第 i 门课将会 持续 上 durationi 天课，并且必须在不晚于 lastDayi 的时候完成。
你的学期从第 1 天开始。且不能同时修读两门及两门以上的课程。
返回你最多可以修读的课程数目。

示例 1：
输入：courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
输出：3
解释：
这里一共有 4 门课程，但是你最多可以修 3 门：
首先，修第 1 门课，耗费 100 天，在第 100 天完成，在第 101 天开始下门课。
第二，修第 3 门课，耗费 1000 天，在第 1100 天完成，在第 1101 天开始下门课程。
第三，修第 2 门课，耗时 200 天，在第 1300 天完成。
第 4 门课现在不能修，因为将会在第 3300 天完成它，这已经超出了关闭日期。
示例 2：
输入：courses = [[1,2]]
输出：1

示例 3：
输入：courses = [[3,2],[4,3]]
输出：0

贪心+优先队列(堆)

按结束时间排序，可以保证我们优先考虑加入先结束的课程。
在课程塞满的时候，用当前的(如果耗时更短)替换耗时最长的那一个(所以使用优先队列维护时长)，
这样做的意义在于我们用更少的时间完成了相同数量的课程，可以保证后面加入更多课程且不可能比原来的方案的课程少。

"""
import heapq
from typing import List
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        start = 0
        s = []
        courses.sort(key=lambda x:x[1])
        for duration, end in courses:
            start += duration
            heapq.heappush(s, -duration)
            if start > end:
                start += heapq.heappop(s)
        return len(s)