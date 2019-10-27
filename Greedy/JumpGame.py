#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 22:11
# @Author  : tc
# @File    : JumpGame.py
"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

能否到达最后一个位置 <==>能跳得最远的位置>=最后一个位置,跳得最远的位置 += 每一步跳得最远的位置


参考:https://leetcode-cn.com/problems/jump-game/solution/55-by-ikaruga/

参考题解的分析非常精彩，代码非常简洁，值得细细品味。

"""
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = 0
        for i in range(len(nums)):
            if i > end:
                return False
            end = max(end,i+nums[i])
        return True

if __name__ == '__main__':
    nums = [3,2,1,0,4]
    solution = Solution()
    print(solution.canJump(nums))