# -*- coding: utf-8 -*-
# @File    : MajorityElementII.py
# @Date    : 2019-12-19
# @Author  : tc
"""
题号 229 求众数II
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例 1:

输入: [3,2,3]
输出: [3]
示例 2:

输入: [1,1,1,3,3,2,2,2]
输出: [1,2]

参考:https://leetcode-cn.com/problems/majority-element-ii/solution/majority-voting-algorithm-by-powcai/

"""
from typing import List
import collections

class Solution:
    # 作弊过
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        counter = collections.Counter(nums)
        return [item[0] for item in counter.most_common(2) if item[1] > (n // 3 )]

    # Boyer-Moore算法
    def majorityElement2(self, nums: List[int]) -> List[int]:
        candiate1 = candiate2 = None
        cnt1 = cnt2 = 0
        for num in nums:
            if num == candiate1:
                cnt1 += 1
            elif num == candiate2:
                cnt2 += 1
            elif cnt1 == 0:
                candiate1 = num
                cnt1 = 1
            elif cnt2 == 0:
                candiate2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        return [n for n in (candiate1, candiate2) if nums.count(n) > len(nums) // 3]


if __name__ == '__main__':
    nums = [1,1,1,3,3,2,2,2]
    solution = Solution()
    print(solution.majorityElement2(nums))