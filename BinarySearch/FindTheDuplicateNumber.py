#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 21:27
# @Author  : tc
# @File    : FindTheDuplicateNumber.py
"""
题号 287 寻找重复数

给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

1.不能更改原数组（假设数组是只读的）。
2.只能使用额外的 O(1) 的空间。
3.时间复杂度小于 O(n2) 。
4.数组中只有一个重复的数字，但它可能不止重复出现一次。

正常的二分是对数组的索引进行二分，而本题的关键是对数组中的数进行二分，很巧妙

我写的二分先排序很蠢,大佬的就很简洁但貌似时间还没有我的快。

参考:https://leetcode-cn.com/problems/find-the-duplicate-number/solution/er-fen-fa-si-lu-ji-dai-ma-python-by-liweiwei1419/

"""

from typing import List

class Solution:
    # 丑陋代码()
    def findDuplicate(self, nums: List[int]) -> int:
        res = 0
        if not nums:
            return res
        nums.sort()
        res = self.binary_search(nums)
        return res

    def binary_search(self,nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == mid + 1:   # 前半部分正常,后半部分存在重复数
                if nums[mid] == nums[mid-1] or nums[mid] == nums[mid+1]:
                    return nums[mid]
                left = mid
            elif nums[mid] > mid + 1:  # 后半部分存在重复数
                left = mid
            elif nums[mid] < mid + 1:  # 前半段存在重复数
                right = mid

    def findDuplicate2(self, nums: List[int]) -> int:
        size = len(nums)
        left = 1
        right = size - 1

        while left < right:
            # mid = left + (right - left) // 2
            mid = (left + right) >> 1
            counter = 0
            for num in nums:
                if num <= mid:
                    counter += 1

            # 【注意】如果小于等于 mid 的个数如果多于 mid，例如：
            # 8 个萝卜 放在 7 个坑里，就至少有 1 个坑里至少有 2 个萝卜
            # 这个坑的位置可能是 1、2、3、4、5、6、7
            # 重复的数就一定在 [1, mid] 里面，包括 1 和 mid
            # 此时，不排除中位数的分支逻辑好想，因此写在前面

            if counter > mid:
                right = mid
            else:
                # 我认为这个逻辑太难想了，但我知道这样写一定对
                left = mid + 1

        return left


if __name__ == '__main__':
    nums = [3,1,3,4,2]
    solution = Solution()
    print(solution.findDuplicate(nums))