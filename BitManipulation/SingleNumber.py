#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 19:34
# @Author  : tc
# @File    : SingleNumber.py
"""
题号 136 只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

位运算解法最牛逼
参考:https://leetcode-cn.com/problems/single-number/solution/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode/


"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a = a ^ num
        return a


if __name__ == '__main__':
    nums = [4,1,2,1,2]
    solution = Solution()
    print(solution.singleNumber(nums))