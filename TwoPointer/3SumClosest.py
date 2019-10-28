#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 23:02
# @Author  : tc
# @File    : 3SumClosest.py
"""
题号 16 最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).


参考15题 三数之和的代码。双指针的核心是尽可能的逼近目标值，此题相当于在双指针过程中不断比较每个的大小。

"""
from typing import List

class Solution:
    # 我写的 其实已经解决了，但就是无法返回sum
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        _min = float('inf')
        for k in range(len(nums) - 2):  # 1.固定指针K，并不断遍历
            i, j = k + 1, len(nums) - 1
            while i < j:  # 3. 内核为双指针
                s = nums[k] + nums[i] + nums[j]
                if s < target:
                    i += 1
                    _min = min(_min, abs(s - target))
                    while i < j and nums[i] == nums[i - 1]:  # 原因和2是一样的
                        i += 1
                elif s > target:
                    j -= 1
                    _min = min(_min, abs(s - target))
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    return target
        return _min

    def threeSumClosest2(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        for k in range(len(nums) - 2):  # 1.固定指针K，并不断遍历
            i, j = k + 1, len(nums) - 1
            while i < j:  # 3. 内核为双指针
                cur = nums[k] + nums[i] + nums[j]
                if abs(res - target) > abs(cur - target):
                    res = cur
                if cur < target:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:  # 原因和2是一样的
                        i += 1
                elif cur > target:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    return target
        return int(res)



if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    solution = Solution()
    print(solution.threeSumClosest(nums, target))