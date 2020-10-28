# -*- coding: utf-8 -*-
# @File    : 39_MoreThanHalfNumber.py.py
# @Date    : 2020-10-28
# @Author  : tc
"""
剑指 Offer 39. 数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

参考：https://leetcode-cn.com/problems/majority-element/solution/duo-shu-yuan-su-by-leetcode-solution/

Boyer-Moore 投票算法

"""
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = nums
            count += (1 if num == candidate else -1)
        return candidate

if __name__ == '__main__':
    pass
