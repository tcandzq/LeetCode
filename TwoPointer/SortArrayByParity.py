# -*- coding: utf-8 -*-
# @File    : SortArrayByParity.py
# @Date    : 2022-08-21
# @Author  : tc
"""
905. 按奇偶排序数组
给你一个整数数组 nums，将 nums 中的的所有偶数元素移动到数组的前面，后跟所有奇数元素。
返回满足此条件的 任一数组 作为答案。

示例 1：
输入：nums = [3,1,2,4]
输出：[2,4,3,1]
解释：[4,2,3,1]、[2,4,1,3] 和 [4,2,1,3] 也会被视作正确答案。

示例 2：
输入：nums = [0]
输出：[0]

双指针 + 原地交换

"""
from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                # i表示偶数所在的索引
                i += 1
        return nums