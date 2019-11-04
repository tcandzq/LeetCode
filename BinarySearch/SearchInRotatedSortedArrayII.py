#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/4 21:32
# @Author  : tc
# @File    : SearchInRotatedSortedArrayII.py
"""
题号 81 搜索旋转排序数组 II
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

(例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2])。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
进阶:

这是 搜索旋转排序数组 的延伸题目，本题中的 nums 可能包含重复元素。
这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？

看到有序就要首先想到二分查找。

本题可以基于二分搜索代码的模板，但关键要确定mid在哪个递增区间。

tips:由于 nums[left]>=nums[right] 一定成立。nums[left]、nums[mid]、nums[right]之间关系如下:
1.nums[left] == nums[mid] == nums[right] 需要进一步缩小mid的范围;

2.nums[left] >= nums[right] >= nums[mid] mid过小 位于右侧递增区域;

3.nums[mid] >= nums[left] >= nums[right] mid过大 位于右侧递增区域;

参考:https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/solution/er-fen-by-powcai/

"""
from typing import List

class Solution:
    #  模板代码1
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:  # 注意:判断一定要写在最外层
                return True

            if nums[left] == nums[mid] == nums[right]:  # 需要进一步缩小mid的范围
                left += 1
                right -= 1

            elif nums[left] <= nums[mid]:  # 说明是在左半边的递增区域
                if nums[left] <= target < nums[mid]:  # 说明target在left和mid之间
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # 说明是在右半边的递增区域
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False

if __name__ == '__main__':
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    solution = Solution()
    print(solution.search(nums,target))