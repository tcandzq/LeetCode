# -*- coding: utf-8 -*-
# @File    : LongestSubarrayOf1sAfterDeletingOneElement.py
# @Date    : 2021-06-27
# @Author  : tc
"""
题号 1493. 删掉一个元素以后全为 1 的最长子数组
给你一个二进制数组 nums ，你需要从中删掉一个元素。

请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。

如果不存在这样的子数组，请返回 0 。
提示 1：

输入：nums = [1,1,0,1]
输出：3
解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。
示例 2：

输入：nums = [0,1,1,1,0,1,1,0,1]
输出：5
解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。
示例 3：

输入：nums = [1,1,1]
输出：2
解释：你必须要删除一个元素。
示例 4：

输入：nums = [1,1,0,0,1,1,1,0,1]
输出：4
示例 5：

输入：nums = [0,0,0]
输出：0

a存中间有一个“非1”的和，b存连续1的和，遇1两数自增，遇“非1” a=b;b=0。
扫描过程保存最大的 a 值，最后处理一下全1特例即可。

参考:https://leetcode-cn.com/problems/longest-subarray-of-1s-after-deleting-one-element/solution/ci-ti-zui-you-suan-fa-bu-jie-shou-fan-bo-by-lao-sa/

"""
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        a = 0
        b = 0
        for num in nums:
            if num == 1:
                a += 1  # a 存储含有一个0的1的数量
                b += 1  # b 存储连续1的数量
                res = max(res, a)
            else:
                a = b
                b = 0
        return res - 1 if res == len(nums) else res