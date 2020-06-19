#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 21:46
# @Author  : tc
# @File    : SortColors.py
"""
题号 75 颜色分类
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

直观方法的话，其实就是计数排序，注意可以使用python的默认字典

优化方法参考:https://leetcode-cn.com/problems/sort-colors/solution/kuai-su-pai-xu-partition-guo-cheng-she-ji-xun-huan/

其实就是一个三指针问题。

"""
from typing import List
from collections import defaultdict

class Solution:

    #  直观的解法
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        count_dict = defaultdict(int)  # int表示默认值是
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        nums[:] = [0] * count_dict[0] + [1] * count_dict[1] + [2] * count_dict[2]

    def sortColors2(self, nums: List[int]) -> None:
        '''
        荷兰三色旗问题解
        '''
        # 对于所有 index < p0 : nums[idx < p0] = 0

        # 对于所有 index > p2 : nums[idx > p2] = 2

        p0, curr, p2 = 0, 0, len(nums) - 1  # p0:指向0的最右边界，curr指向当前元素，p2指向2的最左边界

        while curr <= p2:  # 当前元素没有到达2的最左侧边界
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]  # 交换第 curr个 和 第p0个 元素，。
                p0 += 1  # 将p0指针向右移，表示当前p0指向的位置已经插入了一个0
                curr += 1  # 将curr指针向右移，指向下一个元素
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]  # 交换第 curr个和第 p2个元素，并将 p2指针左移
                p2 -= 1   # 将p2往左移，表示刚插入了一个2
            else:
                curr += 1  # 当nums[curr] == 1时，不需要做任何操作

if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    solution = Solution()
    solution.sortColors2(nums)
    print(nums)