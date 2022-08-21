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

算法步骤：
创建一个哈希表，用 key来储存cur值, value来储存当前index。
假设我们碰到0就将cur decrement (减一), 碰到1则increment (加一)。
如果我们能在哈希表中找到当前的 cur值, 则取出对应的pos, 在看当前的 index - pos 是否比 ans 大, 取其中的最优解。
核心：由于以上碰1加一，碰0减一的操作，当0与1数量一致时(连续数组), 其连续数组的和为零。
因此我们知道数组前面的cur值是什么，在到达该连续数组尾部时就不会变。
因此我们只需要检查哈希表中是否存在其相同的 cur值即可！(多读几遍)


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