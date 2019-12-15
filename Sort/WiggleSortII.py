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
    # 穿插解法
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        # nums[::2]得到nums位于偶数索引的数，nums[1::2]得到nums位于奇数索引的数
        nums[::2], nums[1::2] = nums[len(nums) // 2:], nums[:len(nums) // 2]

    #  超时
    def wiggleSort2(self, nums: List[int]) -> None:
        def kth(arr, left, right, k):  # O(n)时间求第k大数，改自快排，常数因子约为2
            if left >= right:
                return arr[left]
            key = arr[right]
            j = left - 1
            for i in range(left, right):
                if arr[i] < key:
                    j += 1
                    arr[i], arr[j] = arr[j], arr[i]
            j += 1
            arr[j], arr[right] = arr[right], arr[j]
            if k == j:
                return arr[j]
            elif k < j:
                return kth(arr, left, j - 1, k)
            else:
                return kth(arr, j + 1, right, k)

        def median(arr, n):
            return kth(arr, 0, n - 1, n // 2)

        n = len(nums)
        if n <= 1:
            return
        mid = median(nums, n)  # O(n)时间求中位数
        # O(n)时间原地修改，类似三色荷兰国旗排序算法，但数组是全部奇数位下标和偶数位下标的拼接
        i = j = 0
        k = n - 1
        n |= 1  # 取向上离n最近的奇数
        while j <= k:
            ii, jj, kk = map(lambda x: (x * 2 + 1) % n, [i, j, k])
            if nums[jj] > mid:
                nums[jj], nums[ii] = nums[ii], nums[jj]
                i += 1
                j += 1
            elif nums[jj] < mid:
                nums[jj], nums[kk] = nums[kk], nums[jj]
                k -= 1
            else:
                j += 1

if __name__ == '__main__':
    nums = [1, 5, 1, 1, 6, 4]
    solution = Solution()
    solution.wiggleSort2(nums)
    print(nums)