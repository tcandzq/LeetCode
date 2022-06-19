# -*- coding: utf-8 -*-
# @File    : SortArrayByParityII.py
# @Date    : 2022-06-20
# @Author  : tc
"""
922. 按奇偶排序数组 II
给定一个非负整数数组 nums，  nums 中一半整数是 奇数 ，一半整数是 偶数 。
对数组进行排序，以便当 nums[i] 为奇数时，i 也是 奇数 ；当 nums[i] 为偶数时， i 也是 偶数 。
你可以返回 任何满足上述条件的数组作为答案 。

示例 1：
输入：nums = [4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。

示例 2：
输入：nums = [2,3]
输出：[2,3]

如果原数组可以修改，则可以使用就地算法求解。
为数组的偶数下标部分和奇数下标部分分别维护指针 i, j。
随后，在每一步中，如果nums[i]为奇数，则不断地向前移动 j（每次移动两个单位），直到遇见下一个偶数。
此时，可以直接将 nums[i]与nums[j]交换。我们不断进行这样的过程，最终能够将所有的整数放在正确的位置上。

"""
from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        size = len(nums)
        i = 0 # 指向偶数位置
        j = 1 # 指向奇数位置
        while i < size and j < size:
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                # nums[i] % 2 == 1 and nums[j] % 2 == 0
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j +=2
        return nums