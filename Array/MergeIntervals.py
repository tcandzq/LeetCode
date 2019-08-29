#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 23:23
# @Author  : tc
# @File    : MergeIntervals.py
"""
给出一个区间的集合，请合并所有重叠的区间。
Input1:[[1,3],[2,6],[8,10],[15,18]]
Output1:[[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

Input1:[[1,4],[4,5]]
Output1:[[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

注意:要充分利用好合并后的区间merged

这是360搜索引擎核心算法工程师二面的代码题目

答案参考:https://leetcode.com/problems/merge-intervals/solution/

"""

def merge(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # if the list of merged intervals is empty or if the current
        # interval does not overlap with the previous, simply append it.
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


if __name__ == '__main__':
    nums = [[1, 3], [2, 6], [8, 10], [15, 18]]

    print(merge(nums))
