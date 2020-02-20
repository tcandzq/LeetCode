# -*- coding: utf-8 -*-
# @File    : NonOverlappingIntervals.py
# @Date    : 2020-02-20
# @Author  : tc
"""
题号 435 无重叠区间
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。
示例 2:

输入: [ [1,2], [1,2], [1,2] ]

输出: 2

解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
示例 3:

输入: [ [1,2], [2,3] ]

输出: 0

解释: 你不需要移除任何区间，因为它们已经是无重叠的了。

代码参考：https://leetcode.com/problems/non-overlapping-intervals/discuss/91721/Short-Ruby-and-Python

算法参考：https://leetcode-cn.com/problems/non-overlapping-intervals/solution/tan-xin-suan-fa-zhi-qu-jian-diao-du-wen-ti-by-labu/

"""
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end = float('-inf')
        erased = 0
        intervals.sort(key=lambda i:i[1])
        for i in intervals:
            if i[0] >= end:
                end = i[1]
            else:
                erased += 1
        return erased


if __name__ == '__main__':
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    solution = Solution()
    print(solution.eraseOverlapIntervals(intervals))