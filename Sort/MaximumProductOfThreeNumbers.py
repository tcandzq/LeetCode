# -*- coding: utf-8 -*-
# @File    : MaximumProductOfThreeNumbers.py
# @Date    : 2022-06-20
# @Author  : tc
"""
628. 三个数的最大乘积
给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1：
输入：nums = [1,2,3]
输出：6

示例 2：
输入：nums = [1,2,3,4]
输出：24

示例 3：
输入：nums = [-1,-2,-3]
输出：-6

如果数组中全是非负数，则排序后最大的三个数相乘即为最大乘积；如果全是非正数，则最大的三个数相乘同样也为最大乘积。

如果数组中有正数有负数，则最大乘积既可能是三个最大正数的乘积，也可能是两个最小负数（即绝对值最大）与最大正数的乘积。

"""
from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
       nums.sort()
       return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])