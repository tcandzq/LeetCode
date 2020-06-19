# -*- coding: utf-8 -*-
# @File    : 03_01_DuplicationInArray.py
# @Date    : 2020-06-16
# @Author  : tc

"""
面试题03. 数组中重复的数字
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3


限制：

2 <= n <= 100000

参考：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/solution/pythonti-jie-san-chong-fang-fa-by-xiao-xue-66/

"""
from typing import List

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                nums[nums[i]] ,nums[i] = nums[i],nums[nums[i]]
        return None


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]

    solution = Solution()

    print(solution.findRepeatNumber(nums))