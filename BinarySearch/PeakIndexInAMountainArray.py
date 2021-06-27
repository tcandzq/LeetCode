# -*- coding: utf-8 -*-
# @File    : PeakIndexInAMountainArray.py
# @Date    : 2021-06-28
# @Author  : tc
"""
题号 852. 山脉数组的峰顶索引
符合下列属性的数组 arr 称为 山脉数组 ：
arr.length >= 3
存在 i（0 < i < arr.length - 1）使得：
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
给你由整数组成的山脉数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i 。

示例 1：

输入：arr = [0,1,0]
输出：1
示例 2：

输入：arr = [0,2,1,0]
输出：1
示例 3：

输入：arr = [0,10,5,2]
输出：1
示例 4：

输入：arr = [3,4,5,1]
输出：2
示例 5：

输入：arr = [24,69,100,99,79,78,67,36,26,19]
输出：2

二分查找，有两种写法

思路参考：https://leetcode-cn.com/problems/peak-index-in-a-mountain-array/solution/man-hua-suan-fa-er-fen-cha-zhao-yi-shou-shi-jie-ju/

"""
from typing import List

class Solution:
    def peakIndexInMountainArray1(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            m = (l + r) // 2
            if arr[m] < arr[m + 1]:
                l = m + 1
            else:
                r = m
        return r

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid + 1] > arr[mid]:
                left = mid + 1
            elif arr[mid - 1] > arr[mid]:  # A[mid+1] > A[mid] 必须写在 A[mid-1]>A[mid] 前面判断，否则 mid-1可能越界
                right = mid - 1
            else:
                return mid
        return -1