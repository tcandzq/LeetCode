# -*- coding: utf-8 -*-
# @File    : ShortestSubarrayToBeRemovedToMakeArraySorted.py
# @Date    : 2022-08-21
# @Author  : tc
"""
1574. 删除最短的子数组使剩余数组有序
给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得arr中剩下的元素是非递减的。
一个子数组指的是原数组中连续的一个子序列。

请你返回满足题目要求的最短子数组的长度。

 示例 1：
输入：arr = [1,2,3,10,4,2,3,5]
输出：3
解释：我们需要删除的最短子数组是 [10,4,2] ，长度为 3 。剩余元素形成非递减数组 [1,2,3,3,5] 。
另一个正确的解为删除子数组 [3,10,4] 。

示例 2：
输入：arr = [5,4,3,2,1]
输出：4
解释：由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除 [5,4,3,2]，要么删除 [4,3,2,1]。

示例 3：
输入：arr = [1,2,3]
输出：0
解释：数组已经是非递减的了，我们不需要删除任何元素。

示例 4：
输入：arr = [1]
输出：0

使用二分查找

分成三段S_1, S_2, S_3,S_1和S_3是最长的递增序列；
然后对S_1中的每一个数字S_1[i]，用二分查找在S_3中找到插入的位置j，
得到递增序列S_1[:i] + S_3[j:]

"""
import bisect
from typing import List
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        right = len(arr) - 1

        while left < n - 1 and arr[left + 1] >= arr[left]:
            left += 1

        if left >= n - 1:
            return 0

        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1
        if right == 0:
            return n - 1
        ans = right
        for i in range(left + 1):
            # 得到的递增子序列的长度
            j = bisect.bisect_left(arr[right:], arr[i]) + right
            ans = min(j - i - 1, ans)
        return ans