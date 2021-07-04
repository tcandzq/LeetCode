# -*- coding: utf-8 -*-
# @File    : FindKClosestElements.py
# @Date    : 2021-07-05
# @Author  : tc
"""
题号 658. 找到K个最接近的元素
给定一个排序好的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。

整数 a 比整数 b 更接近 x 需要满足：

|a - x| < |b - x| 或者
|a - x| == |b - x| 且 a < b

示例 1：

输入：arr = [1,2,3,4,5], k = 4, x = 3
输出：[1,2,3,4]
示例 2：

输入：arr = [1,2,3,4,5], k = 4, x = -1
输出：[1,2,3,4]

维护一个大小为K的滑动窗口

"""
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo = 0
        hi = len(arr) - 1
        while hi - lo >= k:
            if (x - arr[lo] > arr[hi] - x):
                lo += 1
            else:
                hi -= 1

        return arr[lo: hi + 1]