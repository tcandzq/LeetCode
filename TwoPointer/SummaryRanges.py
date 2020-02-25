# -*- coding: utf-8 -*-
# @File    : SummaryRanges.py
# @Date    : 2020-02-21
# @Author  : tc
"""
题号 228 汇总区间
给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。

示例 1:

输入: [0,1,2,4,5,7]
输出: ["0->2","4->5","7"]
解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。
示例 2:

输入: [0,2,3,4,6,8,9]
输出: ["0","2->4","6","8->9"]
解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。

"""
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        while i < len(nums):
            index = i  # 这一步很关键
            while index+1 < len(nums) and nums[index+1] == nums[index] + 1:
                index += 1
            if index != i:
                res.append('{}->{}'.format(nums[i],nums[index]))
                i = index
            else:
                res.append(str(nums[i]))
            i += 1
        return res

if __name__ == '__main__':
    nums = [0,2,3,4,6,8,9]
    solution = Solution()
    print(solution.summaryRanges(nums))