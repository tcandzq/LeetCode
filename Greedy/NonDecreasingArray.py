# -*- coding: utf-8 -*-
# @File    : NonDecreasingArray.py
# @Date    : 2022-02-20
# @Author  : tc

"""
665. 非递减数列
给你一个长度为 n 的整数数组 nums ，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中任意的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。

示例 1:

输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个 4 变成 1 来使得它成为一个非递减数列。
示例 2:

输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。

提示：

n == nums.length
1 <= n <= 104
-105 <= nums[i] <= 105

思路：
使用贪心算法
https://leetcode.com/problems/non-decreasing-array/discuss/1190763/JS-Python-Java-C%2B%2B-or-Simple-Solution-w-Visual-Explanation

"""
from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        err = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if err or (i > 1 and i < len(nums) - 1 and nums[i-2] > nums[i] and nums[i+1] < nums[i-1]):
                    return False
                err = 1
        return True