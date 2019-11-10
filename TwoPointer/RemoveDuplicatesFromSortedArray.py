#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/10 14:58
# @Author  : tc
# @File    : RemoveDuplicatesFromSortedArray.py
"""
题号 26 删除排序数组中的重复项
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。
说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

快慢指针解法

优化版:https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/shuang-zhi-zhen-shan-chu-zhong-fu-xiang-dai-you-hu/

"""
from typing import List

class Solution:
    #  冗余版
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left,right = 0,1

        while right < len(nums):
            if nums[right] == nums[left]:
                nums.pop(left)
            if right == len(nums):
                return len(nums)
            if nums[right] > nums[left]:
                left += 1
                right += 1
        return len(nums)

    # 优化版
    def removeDuplicates2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        p, q = 0, 1
        while q < len(nums):
            if nums[p] != nums[q]:
                nums[p+1] = nums[q]  # 这一步很关键,可以去重后的数组new_nums排列在原始数组nums的前len(new_nums)的位置。
                p += 1
            q += 1
        return p + 1

if __name__ == '__main__':
    nums = [1,1,2]
    solution = Solution()
    print(solution.removeDuplicates2(nums))
    print(nums)