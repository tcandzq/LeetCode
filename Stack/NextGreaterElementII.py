# -*- coding: utf-8 -*-
# @File    : NextGreaterElementII.py
# @Date    : 2020-02-24
# @Author  : tc
"""
题号 503. 下一个更大元素II
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

示例 1:

输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数；
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

单调递减栈

参考：https://leetcode.com/problems/next-greater-element-ii/discuss/98270/JavaC%2B%2BPython-Loop-Twice

"""
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums += nums
        stack = []
        n = len(nums)
        res = [-1] * n
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack[-1]] = nums[i]
                stack.pop()
            stack.append(i)
        return res[:n // 2]

    def nextGreaterElements2(self, nums: List[int]) -> List[int]:
        stack,res = [],[-1] * len(nums)
        for i in list(range(len(nums))) * 2:
            # 维护一个单调递减栈
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res

if __name__ == '__main__':
    nums = [1,2,1]
    solution = Solution()
    print(solution.nextGreaterElements(nums))
