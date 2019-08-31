#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 15:31
# @Author  : tc
# @File    : longestConsecutiveSequence.py

"""
给定一个未排序的整数数组，找出最长连续序列的长度。
要求算法的时间复杂度为 O(n)。

Input1:[100, 4, 200, 1, 3, 2]
Output1:4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

参考:https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/zui-chang-lian-xu-xu-lie-by-leetcode/

这题的解法比较朴素，但优化的点很有意思:
1.查询某个数是否在数组当中可以用 HashSet 实现O(1)时间的查询;
2.我们只查找最长连续序列开头那个数字,这样就减少了作为序列一部分的数字的判断.

"""
#超时解答
def longestConsecutive(nums):
    num_set = set(nums)
    longest_streak = 0
    for num in nums:
        current_long = 1
        current_num = num + 1
        while current_num in num_set:
            current_long += 1
            current_num += 1
        longest_streak = max(current_long, longest_streak)
    return longest_streak


#参考解答:
def longestConsecutive2(nums):
    num_set = set(nums)
    longest_streak = 0
    for num in nums:
        current_long = 1
        if num - 1 not in num_set:
            current_num = num+1
            while current_num in num_set:
                current_long += 1
                current_num += 1
            longest_streak = max(current_long,longest_streak)
    return longest_streak


#官方解答
def longestConsecutive3(nums):
    longest_streak = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
                print(current_num)
            longest_streak = max(longest_streak, current_streak)

    return longest_streak



if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    print(longestConsecutive3(nums))