#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/7 14:23
# @Author  : tc
# @File    : ShortestUnsortedContinuousSubarray.py
"""
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
你找到的子数组应是最短的，请输出它的长度。
Input1:[2, 6, 4, 8, 10, 9, 15]
Output:5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

暴力解法是排序+双指针。时间复杂度:O(nlogn)，排序消耗 n(logn)n的时间。空间复杂度:O(n)，我们拷贝了一份原数组来进行排序。

使用栈可以达到时间复杂度和空间复杂度均为O(n)
"""
# 暴力法1
def findUnsortedSubarray(nums):
    if not len(nums):
        return 0
    n = len(nums)
    sorted_nums = sorted(nums)
    if nums == sorted_nums:
        return 0
    i = 0
    j = n - 1
    while i <= n - 1 and nums[i] == sorted_nums[i]:
        i += 1

    while j >= 0 and nums[j] == sorted_nums[j]:
        j -= 1
    return j - i + 1

#暴力法1的优化版
def findUnsortedSubarray2(nums):
    if not len(nums):
        return 0
    n = len(nums)
    sorted_nums = sorted(nums)
    start = n - 1 # 注意:start,end 分别表示列表的最后一个位置和第一次位置,这样方便使用min和max 代码看起来更优雅
    end = 0
    for i in range(n):
        if nums[i] != sorted_nums[i]:
            start = min(start,i)
            end = max(end,i)
    return end - start + 1 if (end - start) >= 0 else 0  # (end - start) >= 0 可以检查原始数组已经升序的情况

# 使用栈可以达到O(n) python中list的pop()和append() [-1]可以完成栈的压入和弹出及返回栈顶元素
def findUnsortedSubarray3(nums):
    stack = []  # 新建一个栈
    left = len(nums) - 1
    right = 0
    for i in range(len(nums)):  # 确定子数组的左下标
        while stack and nums[stack[-1]] > nums[i]:
            left = min(left, stack.pop())
        stack.append(i)
    stack.clear()  # 清空列表
    for j in range(len(nums) - 1,-1,-1):  # 确定子数组的右下标
        while stack and nums[stack[-1]] < nums[j]:
            right = max(right, stack.pop())
        stack.append(j)
    return right - left + 1 if right - left > 0 else 0

if __name__ == '__main__':
    nums = [2, 6, 4, 8, 10, 9, 15]
    print(findUnsortedSubarray3(nums))

