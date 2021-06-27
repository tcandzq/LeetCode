# -*- coding: utf-8 -*-
# @File    : FindInMountainArray.py
# @Date    : 2021-06-28
# @Author  : tc
"""
1095. 山脉数组中查找目标值
（这是一个 交互式问题 ）

给你一个 山脉数组 mountainArr，请你返回能够使得 mountainArr.get(index) 等于 target 最小 的下标 index 值。

如果不存在这样的下标 index，就请返回 -1。

何为山脉数组？如果数组 A 是一个山脉数组的话，那它满足如下条件：

首先，A.length >= 3

其次，在 0 < i < A.length - 1 条件下，存在 i 使得：

A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

你将 不能直接访问该山脉数组，必须通过 MountainArray 接口来获取数据：

MountainArray.get(k) - 会返回数组中索引为k 的元素（下标从 0 开始）
MountainArray.length() - 会返回该数组的长度

注意：

对 MountainArray.get 发起超过 100 次调用的提交将被视为错误答案。此外，任何试图规避判题系统的解决方案都将会导致比赛资格被取消。

为了帮助大家更好地理解交互式问题，我们准备了一个样例 “答案”：https://leetcode-cn.com/playground/RKhe3ave，请注意这 不是一个正确答案。

示例 1：

输入：array = [1,2,3,4,5,3,1], target = 3
输出：2
解释：3 在数组中出现了两次，下标分别为 2 和 5，我们返回最小的下标 2。
示例 2：

输入：array = [0,1,2,4,2,1], target = 3
输出：-1
解释：3 在数组中没有出现，返回 -1。

使用三次二分查找，第一次先找到山顶所在的索引，第二次找正序的数组，第三次找逆序的数组

参考：https://leetcode.com/problems/find-in-mountain-array/discuss/317607/JavaC%2B%2BPython-Triple-Binary-Search

"""
class MountainArray:
   def get(self, index: int) -> int:
       pass
   def length(self) -> int:
       pass

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        l = 0
        r = n - 1
        peak = 0
        while l < r:
            m = (l + r) // 2
            if mountain_arr.get(m) < mountain_arr.get(m + 1):
                l = m + 1
            else:
                r = m
        peak = l
        l = 0
        r = peak
        while l <= r:
            m = (l + r) // 2
            if mountain_arr.get(m) > target:
                r = m - 1
            elif mountain_arr.get(m) < target:
                l = m + 1
            else:
                return m
        l = peak
        r = n - 1
        while l <= r:
            m = (l + r) // 2
            if mountain_arr.get(m) > target:
                l = m + 1
            elif mountain_arr.get(m) < target:
                r = m - 1
            else:
                return m
        return -1