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

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?


dp[i]的值代表以nums[i]结尾的最长子序列长度,一定是以nums[i]结尾!!!

二分解法参考:https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/

参考:https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/

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
        # tails[k] 的值代表 长度为 k+1的子序列尾部元素的值
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else:
                    j = m
            tails[i] = num
            if j == res: res += 1
        return res



if __name__ == '__main__':
    nums = [1,3,6,7,9,4,10,5,6]
    solution = Solution()
    print(solution.lengthOfLIS(nums))