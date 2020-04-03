# -*- coding: utf-8 -*-
# @File    : 42_GreatestSumOfSubarrays.py
# @Date    : 2020-04-03
# @Author  : tc
"""
面试题42. 连续子数组的最大和
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。


示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


提示：

1 <= arr.length <= 10^5
-100 <= arr[i] <= 100
注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/

"""
class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)



if __name__ == '__main__':
    nums = [-2, -1]
    solution = Solution()
    print(solution.maxSubArray(nums))

