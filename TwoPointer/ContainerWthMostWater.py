#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 18:44
# @Author  : tc
# @File    : ContainerWthMostWater.py
"""
题号11 盛最多水的容器
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

图片请参考:https://leetcode-cn.com/problems/container-with-most-water/

示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49

双指针。一个指针指向头部，一个指针指向尾部，然后向内移动指针，直至两指针相遇。
关键：确定指针移动的规则，很明显S(i, j) = min(h[i], h[j]) × (j - i)S(i,j)=min(h[i],h[j])×(j−i)。如果向内移动短板，则容器面积可能会变大，
如果向内移动长板，容器面积肯定会减少，因为容器宽-1，而高不变。所以选择向内移动短板。


参考:https://leetcode-cn.com/problems/container-with-most-water/solution/container-with-most-water-shuang-zhi-zhen-fa-yi-do/

"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        res = 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1  # 向内移动短板
            else:
                res = max(res, height[j] * (j - i))
                j -= 1  # 向内移动短板
        return res


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    print(solution.maxArea(height))