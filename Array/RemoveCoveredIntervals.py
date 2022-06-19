# -*- coding: utf-8 -*-
# @File    : RemoveCoveredIntervals.py
# @Date    : 2022-06-19
# @Author  : tc
"""
1288. 删除被覆盖区间
给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。
只有当 c <= a 且 b <= d 时，我们才认为区间 [a,b) 被区间 [c,d) 覆盖。

在完成所有删除操作后，请你返回列表中剩余区间的数目。

示例：

输入：intervals = [[1,4],[3,6],[2,8]]
输出：2
解释：区间 [3,6] 被区间 [2,8] 覆盖，所以它被删除了。

当区间左端点相同的时候，右端点靠后的应该放在前面。

"""
from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        size = len(intervals)
        if size < 2:
            return size
        intervals.sort(key=lambda x: (x[0], -x[1]))

        remove_count = 0
        max_right = intervals[0][1]
        for i in range(1, size):
            if intervals[i][1] <= max_right:
                remove_count += 1
            else:
                max_right = intervals[i][1]
        return size - remove_count