#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 11:42
# @Author  : tc
# @File    : LargestRectangleInHistogram.py
"""
题号: 84   柱状图中最大的矩形
注:由于图片无法粘贴,详细题目参考:https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

 
以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

 

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。


示例:

输入: [2,1,5,6,2,3]
输出: 10

本题比较经典,分治、单调栈1请参考:https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/zhu-zhuang-tu-zhong-zui-da-de-ju-xing-by-leetcode/

单调栈2解法参考:https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/zhao-liang-bian-di-yi-ge-xiao-yu-ta-de-zhi-by-powc/

关于单调栈的概念可以参考：
https://cloud.tencent.com/developer/news/433986https://cloud.tencent.com/developer/news/433986
https://blog.csdn.net/Prasnip_/article/details/83690038

本题的单调栈解法可作为一个模板套用

"""
from typing import List

class Solution:
    #  暴力版本(超时)
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(n):
            for j in range(i,n):
                min_val = min(heights[i:j+1])
                width = len(heights[i:j+1])
                max_area = max(max_area,width*min_val)

        return max_area

    #  分治(超内存)
    def largestRectangleArea2(self, heights: List[int]) -> int:
        if not heights:
            return 0
        min_index = heights.index(min(heights))

        return max(self.largestRectangleArea2(heights[:min_index]),self.largestRectangleArea2(heights[min_index+1:]),
                   heights[min_index]*len(heights))

    #   单调栈(最优)第一种写法
    def largestRectangleArea3(self, heights: List[int]) -> int:
        stack = [-1]  # 利用数组构造栈
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:  # 如果栈里的元素开始递减
                max_area = max(max_area,heights[stack.pop()]*(i-stack[-1] - 1))  # 弹出元素作为高,
            stack.append(i)
        while stack[-1] != -1:
            max_area = max(max_area,heights[stack.pop()]*(len(heights)-stack[-1] - 1))
        return max_area

    #   单调栈(最优)第二种写法
    def largestRectangleArea4(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        p = 0
        while(p < len(heights)):
            if not stack:  #  栈空入栈
                stack.append(p)
                p += 1
            else:
                top = stack[-1]
                if heights[p] > heights[top]:  # 当前高度大于栈顶,入栈
                    stack.append(p)
                    p += 1
                else:
                    height = heights[stack.pop()]  # 保存栈顶高度
                    left_less_min = -1 if not stack else stack[-1]  # 左边以第一个小于柱子的下标
                    right_less_min = p  # 右边第一个小于当前柱子的下标
                    area = (right_less_min - left_less_min - 1) * height
                    max_area = max(area,max_area)
        while stack:
            height = heights[stack.pop()]
            left_less_min = -1 if not stack else stack[-1]  # 左边以第一个小于柱子的下标
            right_less_min = len(heights)  # 右边没有小于当前高度的柱子，所以赋值为数组的长度便于计算
            area = (right_less_min - left_less_min - 1) * height
            max_area = max(max_area,area)
        return max_area

if __name__ == '__main__':
    heights = [2,1,5,6,2,3]
    solution = Solution()
    print(solution.largestRectangleArea4(heights))
