#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 22:38
# @Author  : tc
# @File    : IntersectionOfTwoArrays.py
"""
题号 349 两个数组的交集
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [9,4]
说明:

输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。

"""
from typing import List

class Solution:

    # 一行代码搞定
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    solution = Solution()
    print(solution.intersection(nums1,nums2))