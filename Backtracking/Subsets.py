#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/31 10:20
# @Author  : tc
# @File    : Subsets.py
"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
Input1:nums = [1,2,3]
Output1:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

思路参考1:https://leetcode-cn.com/problems/subsets/solution/zi-ji-python3di-gui-fa-by-pandawakaka/
思路参考2:https://leetcode-cn.com/problems/subsets/solution/hui-su-python-dai-ma-by-liweiwei1419/
1.f([1,2]) = [[], [1,2], [2], [1]]
2.f([1,2,3]) = [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
3.f([1,2,3])是在f([1,2])的元素基础上，对每个元素多加一个3

"""
#解法1
def subsets(nums):
    size = len(nums)
    if size == 0:
        return []

    res = []
    __dfs(nums, 0, [], res)
    return res


def __dfs(nums, start, path, res):
    res.append(path[:])
    for i in range(start, len(nums)):
        path.append(nums[i])
        # 因为 nums不包含重复元素，并且每一个元素只能使用一次
        # 所以下一次搜索从 i + 1 开始
        __dfs(nums, i + 1, path, res)
        path.pop()

