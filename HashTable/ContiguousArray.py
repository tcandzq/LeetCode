# -*- coding: utf-8 -*-
# @File    : ContiguousArray.py
# @Date    : 2021-06-14
# @Author  : tc
"""
题号 525. 连续数组
给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。

示例 1:

输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。
示例 2:

输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。

核心思想:
1.将所有的0看成-1，这样问题就变成了求和为0的最大连续子数组;
2.使用前缀和，如果两个前缀和的值一样，表明这两个前缀和对应下标之间的数组和为0;
3.考虑极端情况，比如[0，1],需要index=0时的前缀为{0：-1}

参考；https://leetcode-cn.com/problems/contiguous-array/solution/dong-tu-yan-shi-qian-zhui-he-si-xiang-by-z2no/
"""
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_length = 0
        table = {0: -1}
        for index, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in table:
                max_length = max(max_length, index - table[count])
            else:
                table[count] = index

        return max_length