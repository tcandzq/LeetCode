#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/23 23:09
# @Author  : tc
# @File    : ContainsDuplicate.py
"""
题号 217 存在重复元素
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

参考:https://leetcode-cn.com/problems/contains-duplicate/solution/ha-xi-pai-xu-python3-by-zhu_shi_fu/

"""
from typing import List
class Solution:
    # 丑陋写法
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        d = defaultdict(int)
        for num in nums:
            if d[num] >= 2:
                return True
            elif num in d:
                d[num] += 1
            else:
                d[num] = 1
        return False

    # 优雅写法
    def containsDuplicate2(self, nums: List[int]) -> bool:
        hash = {}
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = 1
            else:
                return True
        return False




if __name__ == '__main__':
    nums = [1,2,3,4]
    solution = Solution()
    print(solution.containsDuplicate(nums))