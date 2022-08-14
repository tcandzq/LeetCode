# -*- coding: utf-8 -*-
# @File    : NumberOfSubsequencesThatSatisfyTheGivenSumCondition.py
# @Date    : 2022-08-14
# @Author  : tc
"""
1498. 满足条件的子序列数目
给你一个整数数组 nums 和一个整数 target 。
请你统计并返回 nums 中能满足其最小元素与最大元素的 和 小于或等于 target 的 非空 子序列的数目。
由于答案可能很大，请将结果对 109 + 7 取余后返回。

示例 1：

输入：nums = [3,5,6,7], target = 9
输出：4
解释：有 4 个子序列满足该条件。
[3] -> 最小元素 + 最大元素 <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)
示例 2：

输入：nums = [3,3,6,8], target = 10
输出：6
解释：有 6 个子序列满足该条件。（nums 中可以有重复数字）
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
示例 3：

输入：nums = [2,3,3,4,6,7], target = 12
输出：61
解释：共有 63 个非空子序列，其中 2 个不满足条件（[6,7], [7]）
有效序列总数为（63 - 2 = 61）

提示：
1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= target <= 106

排序 + 双指针

https://leetcode.cn/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/solution/python-pai-xu-shuang-zhi-zhen-by-irruma/
"""

from typing import List
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        if nums[0] * 2 > target:
            return 0
        res = 0
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            # while left <= right and (nums[left] + nums[right]) <= target:
            #     res += 2 ** (right - left)
            #     left += 1
            # right -= 1
            if nums[left] + nums[right] <= target:
                res += 2 ** (right - left)
                left += 1
            else:
                right -= 1
        return res % (10 ** 9 + 7)
