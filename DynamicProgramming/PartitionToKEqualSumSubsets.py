# -*- coding: utf-8 -*-
# @File    : PartitionToKEqualSumSubsets.py
# @Date    : 2020-03-25
# @Author  : tc
"""
题号 698. 划分为k个相等的子集
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

示例 1：

输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。


注意:

1 <= k <= len(nums) <= 16
0 < nums[i] < 10000

参考：https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/146579/Easy-python-28-ms-beats-99.5

"""
from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sums = [0] * k
        sub_sum = sum(nums) / k
        nums.sort(reverse=True)
        l = len(nums)

        def walk(i):
            if i == l:
                return len(set(sums)) == 1
            for j in range(k):
                sums[j] += nums[i]
                if sums[j] <= sub_sum and walk(i + 1):
                    return True
                sums[j] -= nums[i]
                if sums[j] == 0:
                    break
            return False

        return walk(0)

if __name__ == '__main__':
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    solution = Solution()
    print(solution.canPartitionKSubsets(nums,k))


