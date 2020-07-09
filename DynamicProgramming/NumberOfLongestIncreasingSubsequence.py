# -*- coding: utf-8 -*-
# @File    : NumberOfLongestIncrenumssingSubsequence.py
# @Dnumste    : 2020-03-19
# @numsuthor  : tc
"""
题号 673. 最长递增子序列的个数
给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。

参考：https://leetcode.com/problems/number-of-longest-increasing-subsequence/discuss/107320/Python-DP-with-explanation-(Beats-88)

dp数组需要存储两个元素：
(1)以当前索引结尾的最长子序列的长度；
(2)以当前索引结尾的最长子序列的数量

"""
from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[1, 1] for i in range(len(nums))]
        print(dp)
        max_for_all = 1
        for i, num in enumerate(nums):
            max_len, count = 1, 0
            for j in range(i):
                if nums[j] < num:
                    if dp[j][0] + 1 > max_len:
                        max_len = dp[j][0] + 1
                        count = 0
                    if dp[j][0] == max_len - 1:
                        count += dp[j][1]
            dp[i] = [max_len, max(count, dp[i][1])]
            max_for_all = max(max_len, max_for_all)
        return sum([item[1] for item in dp if item[0] == max_for_all])

    def findNumberOfLIS2(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(n)
        dp, longest = [[1, 1] for i in range(len(nums))], 1
        for i, num in enumerate(nums):
            curr_longest, count = 1, 0
            for j in range(i):
                if nums[j] < num:
                    curr_longest = max(curr_longest, dp[j][0] + 1)
            for j in range(i):
                if dp[j][0] == curr_longest - 1 and nums[j] < num:
                    count += dp[j][1]
            dp[i] = [curr_longest, max(count, dp[i][1])]
            longest = max(curr_longest, longest)
        return sum([item[1] for item in dp if item[0] == longest])

if __name__ == '__main__':
    nums = [1, 3, 5, 4, 7]
    solution = Solution()
    print(solution.findNumberOfLIS2(nums))