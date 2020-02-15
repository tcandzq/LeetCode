# -*- coding: utf-8 -*-
# @File    : MinimumMovesToEqualArrayElementsII.py
# @Date    : 2020-02-15
# @Author  : tc

"""
题号 462 最少移动次数使数组元素相等II
给定一个非空整数数组，找到使所有数组元素相等所需的最小移动数，其中每次移动可将选定的一个元素加1或减1。 您可以假设数组的长度最多为10000。

例如:

输入:
[1,2,3]

输出:
2

说明：
只有两个动作是必要的（记得每一步仅可使其中一个元素加1或减1）：

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

在中位数处，需要的次数是最少的

"""
from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        index = len(nums) // 2
        return nums[index] * index - sum(nums[:index]) + sum(nums[index+1:]) -  nums[index] * (len(nums) - 1- index)







if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    print(solution.minMoves2(nums))