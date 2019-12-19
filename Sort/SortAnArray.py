# -*- coding: utf-8 -*-
# @File    : SortAnArray.py
# @Date    : 2019-12-19
# @Author  : tc
"""
题号 912 排序数组
给定一个整数数组 nums，将该数组升序排列。
示例 1：

输入：[5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：[5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
 

提示：

1 <= A.length <= 10000
-50000 <= A[i] <= 50000

"""
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)

