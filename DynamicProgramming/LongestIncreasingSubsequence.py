#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 20:54
# @Author  : tc
# @File    : LongestIncreasingSubsequence.py
"""
题号 300 最长上升子序列
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?


示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(NlogN) 吗?


dp[i]的值代表以nums[i]结尾的最长子序列长度,一定是以nums[i]结尾!!!

二分解法参考:https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/

参考:https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/

利用了贪心的思想:越小的上升子序列就越容易构成最长的上升子序列

"""
from typing import List

class Solution:
    # dp解法
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1,dp[i])
        print(dp)
        return max(dp)

    # 二分解法
    def lengthOfLIS2(self, nums: List[int]) -> int:
        # tail[i] 表示长度为 i + 1 （因为 i 表示索引，i + 1 表示长度）的所有“上升子序列”里结尾最小的元素。
        size = len(nums)
        # 特判
        if size < 2:
            return size
        # tail 数组的定义：长度为 i + 1 的上升子序列的末尾最小是几
        # 遍历第 1 个数，直接放在有序数组 tail 的开头
        tail = [nums[0]]
        for i in range(1, size):
            # 找到大于等于 num 的第 1 个数，试图让它变小
            left = 0
            # 因为有可能 num 比 tail 数组中的最后一个元素还要大，所以右边界应该设置为 tail 数组的长度
            right = len(tail)
            while left < right:
                # 选左中位数
                mid = (left + right) >> 1
                if tail[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            # 如果找不到第一个大于nums[i]的数
            if left == len(tail):
                tail.append(nums[i])
            else:
                # 第一个大于nums[i]的数位于tail内部则直接替换那个数
                tail[left] = nums[i]
        return len(tail)

    # 利用python的biset模块
    def lengthOfLIS3(self, nums: List[int]) -> int:
        import bisect
        tail = []
        for num in nums:
            left_insort = bisect.bisect_left(tail,num)
            if left_insort == len(tail):
                tail.append(num)
            else:
                tail[left_insort] = num
        return len(tail)

if __name__ == '__main__':
    nums = [2,5,3,1]
    solution = Solution()
    print(solution.lengthOfLIS2(nums))