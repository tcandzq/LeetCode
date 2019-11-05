#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 19:25
# @Author  : tc
# @File    : TwoSumII InputArrayIsSorted.py
"""
题号167 两数之和 II - 输入有序数组
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

本题可以用双指针和二分查找两种方法

参考:https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/solution/shuang-zhi-zhen-dui-zhuang-er-fen-fa-python-dai-ma/

"""
from typing import List

class Solution:
    #  双指针
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:

                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

        return []

    #  二分查找
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        for left in range(size - 1):
            right = self.binary_search(left+1,size - 1,numbers,target-numbers[left])
            if right != -1:
                return [left+1,right+1]

    def binary_search(self,left,right,numbers,target):
        while left < right:
            mid = left + ((right - left)>>1)
            if numbers[mid] == target:
                right = mid
            elif numbers[mid] > target:
                right = mid
            elif numbers[mid] < target:
                left = mid + 1
        return left if numbers[left] == target else -1

if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    print(solution.twoSum2(numbers,target))