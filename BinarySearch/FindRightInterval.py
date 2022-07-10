# -*- coding: utf-8 -*-
# @File    : FindRightInterval.py
# @Date    : 2022-07-11
# @Author  : tc
"""
436. 寻找右区间
给你一个区间数组 intervals ，其中 intervals[i] = [starti, endi] ，且每个 starti 都 不同 。

区间 i 的 右侧区间 可以记作区间 j ，并满足 startj >= endi ，且 startj 最小化 。

返回一个由每个区间 i 的 右侧区间 在 intervals 中对应下标组成的数组。如果某个区间 i 不存在对应的右侧区间 ，则下标 i 处的值设为 -1 。

示例 1：
输入：intervals = [[1,2]]
输出：[-1]
解释：集合中只有一个区间，所以输出-1。

示例 2：
输入：intervals = [[3,4],[2,3],[1,2]]
输出：[-1,0,1]
解释：对于 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间[3,4]具有最小的“右”起点;
对于 [1,2] ，区间[2,3]具有最小的“右”起点。

示例 3：
输入：intervals = [[1,4],[2,3],[3,4]]
输出：[-1,2,-1]
解释：对于区间 [1,4] 和 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间 [3,4] 有最小的“右”起点。

二分查找寻找大于等于target的第一个位置
https://leetcode.cn/problems/find-right-interval/solution/by-fuxuemingzhu-98m1/
"""
from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        start_map = {interval[0]:i for i, interval in enumerate(intervals)}
        starts = [interval[0] for interval in intervals]
        starts.sort()
        res = []
        for interval in intervals:
            pos = self.higher_find(interval[1], starts)
            res.append(start_map[starts[pos]] if pos != -1 else -1)
        return res

    def higher_find(self, target, nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        if left >= len(nums) or nums[left] < target:
            return -1
        return left