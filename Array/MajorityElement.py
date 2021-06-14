# -*- coding: utf-8 -*-
# @File    : MajorityElement.py
# @Date    : 2021-06-14
# @Author  : tc
"""
题号：169. 多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1：

输入：[3,2,3]
输出：3
示例 2：

输入：[2,2,1,1,1,2,2]
输出：2

进阶：

尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。

使用摩尔投票法

"""
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                count = 1
                majority = nums[i]
            elif nums[i] == majority:
                count += 1
            else:
                count -= 1
        return majority