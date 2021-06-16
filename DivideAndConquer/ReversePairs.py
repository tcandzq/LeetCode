# -*- coding: utf-8 -*-
# @File    : ReversePairs.py
# @Date    : 2021-06-17
# @Author  : tc
"""
题号 493. 翻转对
给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。

你需要返回给定数组中的重要翻转对的数量。

示例 1:

输入: [1,3,2,3,1]
输出: 2
示例 2:

输入: [2,4,3,5,1]
输出: 3

归并排序

参考:https://leetcode-cn.com/problems/reverse-pairs/solution/c-python3-tao-gui-bing-pai-xu-kuang-jia-16u90/

"""
from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.cnt = 0
        self.mergesort(nums, 0, len(nums) - 1)
        return self.cnt

    def mergesort(self, nums: List[int], L: int, R: int) -> None:
        if L >= R:
            return
        mid = L + (R - L) // 2
        self.mergesort(nums, L, mid)
        self.mergesort(nums, mid + 1, R)
        self.merge(nums, L, mid, R)

    def merge(self, nums: List[int], L: int, mid: int, R: int) -> None:
        i, j = L, mid + 1
        tmp = []
        while i <= mid and j <= R:
            if nums[i] <= nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1
        ######################## 借助归并排序  本题的特殊计算
        ii, jj = L, mid + 1
        while ii <= mid and jj <= R:
            if nums[ii] <= 2 * nums[jj]:
                ii += 1
            else:
                self.cnt += (mid - ii) + 1
                jj += 1
        ########################
        if i <= mid:
            tmp += nums[i: mid + 1]
        if j <= R:
            tmp += nums[j: R]
        for i in range(len(tmp)):
            nums[L + i] = tmp[i]

