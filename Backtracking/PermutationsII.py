#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/31 10:27
# @Author  : tc
# @File    : PermutationsII.py
"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。
Input1:[1,1,2]
Output1:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

关键:回溯+剪枝
"一个数组中去掉重复元素，除了使用哈希表，更容易想到的是将原始数组排序"
参考:https://leetcode-cn.com/problems/permutations-ii/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liwe-2/
"""
def permuteUnique(nums):
    if not len(nums):
        return []
    # 修改 1：首先排序，之后才有可能发现重复分支，升序、倒序均可
    nums.sort()
    res = []
    used = [False] * len(nums)
    __dfs(0, nums, used, [], res)
    return res

def __dfs(index, nums, used, pre, res):
    if index == len(nums):
        res.append(pre.copy())
        return

    for i in range(len(nums)):
        if not used[i]:
            # 修改 2：因为排序以后重复的数一定不会出现在开始，故 i > 0
            # 和之前的数相等，并且之前的数还未使用过，只有出现这种情况，才会出现相同分支
            # 这种情况跳过即可
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            pre.append(nums[i])
            __dfs(index + 1, nums, used, pre, res)
            used[i] = False
            pre.pop()

