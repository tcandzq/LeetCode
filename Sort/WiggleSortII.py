"""
题号 324 摆动排序II
给定一个无序的数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。

示例 1:

输入: nums = [1, 5, 1, 1, 6, 4]
输出: 一个可能的答案是 [1, 4, 1, 5, 1, 6]
示例 2:

输入: nums = [1, 3, 2, 2, 3, 1]
输出: 一个可能的答案是 [2, 3, 1, 3, 1, 2]
说明:
你可以假设所有输入都会得到有效的结果。

进阶:
你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？

这题用C++求解会更好

参考:https://leetcode.com/problems/wiggle-sort-ii/discuss/77677/O(n)%2BO(1)-after-median-Virtual-Indexing

"""
from typing import List

class Solution:
    #
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        # nums[::2]得到nums位于偶数索引的数，nums[1::2]得到nums位于奇数索引的数
        nums[::2], nums[1::2] = nums[len(nums) // 2:], nums[:len(nums) // 2]

if __name__ == '__main__':
    nums = [1, 5, 1, 1, 6, 4]
    solution = Solution()
    print(solution.wiggleSort(nums))