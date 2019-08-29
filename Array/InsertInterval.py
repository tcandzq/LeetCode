#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 11:26
# @Author  : tc
# @File    : InsertInterval.py
"""
给出一个无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

Input1:intervals = [[1,3],[6,9]], newInterval = [2,5]
Output1:[[1,5],[6,9]]

Input2:intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output2:[[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

这题主要是还是参考LeetCode56题:合并区间的答案

"""
def insert(intervals,newInterval):
    intervals.append(newInterval)
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1],interval[1])
    return merged

if __name__ == '__main__':
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]

    newInterval = [4,8]

    print(insert(intervals,newInterval))