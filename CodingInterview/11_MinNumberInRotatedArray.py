# -*- coding: utf-8 -*-
# @File    : 11_MinNumberInRotatedArray.py
# @Date    : 2020-04-12
# @Author  : tc
"""
面试题11. 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/

参考：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/solution/er-fen-fa-fen-zhi-fa-python-dai-ma-by-liweiwei1419/

"""
from typing import List

class Solution:
    def minArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return Exception('程序出错')

        left = 0
        right = size - 1
        while left < right:
            # mid = left + (right - left) // 2
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                # mid 肯定不是最小值
                # [7,8,9,10,11,1,2,3]
                left = mid + 1
            elif nums[mid] < nums[right]:
                # mid 有可能是最小值
                # [7,8,1,2,3]
                right = mid
            else:
                # 都有可能，所以就把 right 排除了
                # [1,1,1,1,1,0,1]
                assert nums[mid] == nums[right]
                right = right - 1
        # 无需后处理
        return nums[left]





