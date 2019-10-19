#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 15:47
# @Author  : tc
# @File    : ProductOfArrayExceptSelf.py
"""
题号 238 除自身以外数组的乘积
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

就是用左右两个数组先预先存好要计算的值

"""
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        left[0] = nums[0]
        right[0] = nums[-1]
        res = [0] * len(nums)
        for i in range(1,len(nums)):
            left[i] = left[i-1] * nums[i]
            right[i] = right[i-1] * nums[len(nums) - i -1]

        for k in range(0, len(nums)):
            if k == 0:
                res[0] = right[len(nums) - 2]
            elif k == len(nums) - 1:
                res[-1] = left[len(nums) - 2]
            else:
                res[k] = left[k-1] * right[len(nums) - k - 2]
        return res
if __name__ == '__main__':
    solution = Solution()
    nums = [4,3,2,1,2]
    print(solution.productExceptSelf(nums))