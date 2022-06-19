# -*- coding: utf-8 -*-
# @File    : SmallestRangeCoveringElementsFromKLists.py
# @Date    : 2022-06-19
# @Author  : tc
"""
632. 最小区间
你有 k 个 非递减排列 的整数列表。找到一个 最小 区间，使得 k 个列表中的每个列表至少有一个数包含在其中。
我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。

示例 1：

输入：nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
输出：[20,24]
解释：
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
示例 2：

输入：nums = [[1,2,3],[1,2,3],[1,2,3]]
输出：[1,1]

堆+双指针+贪心
"""
from typing import List
import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # 初始化堆的数组为所有区间第一个元素
        # 堆中元素的格式为:(区间某个元素,区间在列表的位置,该元素在区间的位置)
        pq = [(row[0], i, 0) for i, row in enumerate(nums)]
        # 将数组转为堆，这是一个原地操作
        heapq.heapify(pq)
        # 初始化区间范围
        ans = -1e9, 1e9
        # 初始化右指针的值为所有区间第一个元素的最大值
        right = max(row[0] for row in nums)
        while pq:
            # 弹出所有区间元素中的最小值以及对应的位置，left为左指针
            left, i, j = heapq.heappop(pq)
            # 是否需要更新区间范围
            if right - left < ans[1] - ans[0]:
                ans = left, right
            # 如果已经达到了某个区间的边界,直接返回结果
            if j == len(nums[i]) - 1:
                return ans

            v = nums[i][j + 1]
            # 计算当前区间元素的最大值
            right = max(v, right)
            # 将已经弹出最小值对应元素所在的区间的下一个数加入堆中
            heapq.heappush(pq, (v, i, j + 1))