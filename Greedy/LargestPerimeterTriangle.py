# -*- coding: utf-8 -*-
# @File    : LargestPerimeterTriangle.py
# @Date    : 2021-08-09
# @Author  : tc
"""
976. 三角形的最大周长
给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。

如果不能形成任何面积不为零的三角形，返回 0。
示例 1：

输入：[2,1,2]
输出：5
示例 2：

输入：[1,2,1]
输出：0
示例 3 ：

输入：[3,2,3,4]
输出：10
示例 4：

输入：[3,6,2,3]
输出：8


思路：
我们可以选择枚举三角形的最长边c，而从贪心的角度考虑，
我们一定是选「小于c的最大的两个数」作为边长a和b，此时最有可能满足 a+b>c，使得三条边能够组成一个三角形，且此时的三角形的周长是最大的

思路参考：
https://leetcode-cn.com/problems/largest-perimeter-triangle/solution/san-jiao-xing-de-zui-da-zhou-chang-by-leetcode-sol/

"""
from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(len(nums) - 1, 1, -1):
            if nums[i - 1] + nums[i - 2] > nums[i]:
                return nums[i] + nums[i - 1] + nums[i - 2]
        return 0