# -*- coding: utf-8 -*-
# @File    : SumOfSubarrayMinimums.py
# @Date    : 2021-06-27
# @Author  : tc
"""
题号 907. 子数组的最小值之和
给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。

由于答案可能很大，因此 返回答案模 10^9 + 7 。

示例 1：

输入：arr = [3,1,2,4]
输出：17
解释：
子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
示例 2：

输入：arr = [11,81,94,43,3]
输出：444

单调递增栈

参考：https://leetcode-cn.com/problems/sum-of-subarray-minimums/solution/dan-diao-zhan-python3-by-smoon1989/

"""
from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = 0
        left = [0] * len(arr)
        right = [0] * len(arr)
        stack = []
        for index in range(len(arr)):
            while stack and arr[stack[-1]] > arr[index]:
                stack.pop()
            if not stack:  # 说明栈内的元素都大于当前元素，因此该元素是目前最小的元素
                left[index] = -1
            else:
                left[index] = stack[-1]
            stack.append(index)

        stack = []
        for index in range(len(arr) - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[index]:
                stack.pop()
            if not stack:
                right[index] = len(arr)
            else:
                right[index] = stack[-1]
            stack.append(index)

        for index in range(len(arr)):
            ans += arr[index] * (index - left[index]) * (right[index] - index)
            ans %= 1000000007
        return ans