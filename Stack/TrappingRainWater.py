#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 0:05
# @Author  : tc
# @File    : TrappingRainWater.py
"""
题号:42 接雨水
图片挂了,详细题目请见:https://leetcode-cn.com/problems/trapping-rain-water/
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

这题的关键是如何找到凹形数组,需要记录递减数组和递增数组

直接上终极解法——单调递减栈 关键地方在于要对雨水的面积进行横向划分,这样可以看到雨水面积=宽度*高度


参考:https://leetcode-cn.com/problems/trapping-rain-water/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-8/

"""
from typing import List

class Solution:
    #  双指针解法
    def trap(self, height: List[int]) -> int:
        sum = 0
        max_left = 0
        max_right = [0 for _ in range(len(height))]
        for i in range(len(height) - 2,-1,-1):
            print(max_right)
            max_right[i] = max(max_right[i+1],height[i+1])
        print(max_right)
        for i in range(1,len(height) - 1):
            max_left = max(max_left,height[i-1])
            _min = min(max_left,max_right[i])
            if _min > height[i]:
                print(_min)
                sum = sum + (_min - height[i])
        return sum

    # 栈解法
    def trap2(self, height: List[int]) -> int:
        sum = 0
        stack = []
        current = 0
        while current < len(height):
            while stack and height[current] > height[stack[-1]]:
                h = height[stack[-1]]
                stack.pop()
                if not stack:
                    break
                distance = current - stack[-1] - 1  # 计算两堵墙之间的距离
                _min = min(height[stack[-1]], height[current])  # 用底乘以高
                sum += distance * (_min - h)
            stack.append(current)
            current += 1
        return sum

if __name__ == '__main__':

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    solution = Solution()
    print(solution.trap2(height))
