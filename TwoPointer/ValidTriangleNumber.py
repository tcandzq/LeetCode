# -*- coding: utf-8 -*-
# @File    : ValidTriangleNumber.py
# @Date    : 2022-07-11
# @Author  : tc
"""
611. 有效三角形的个数
给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数。

示例 1:
输入: nums = [2,2,3,4]
输出: 3
解释:有效的组合是:
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3

示例 2:
输入: nums = [4,2,3,4]
输出: 4

1.首先对数组排序。
2.固定最长的一条边，运用双指针扫描
3.如果 nums[l] + nums[r] > nums[i]，同时说明 nums[l + 1] + nums[r] > nums[i], ..., nums[r - 1] + nums[r] > nums[i]，
满足的条件的有 r - l 种，r 左移进入下一轮。
3.如果 nums[l] + nums[r] <= nums[i]，l 右移进入下一轮。
4.枚举结束后，总和就是答案。
https://leetcode.cn/problems/valid-triangle-number/solution/ming-que-tiao-jian-jin-xing-qiu-jie-by-jerring/
"""
from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    res += right - left
                    right -= 1
                else:
                    left += 1
        return res