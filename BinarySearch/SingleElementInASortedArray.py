# -*- coding: utf-8 -*-
# @File    : SingleElementInASortedArray.py
# @Date    : 2022-06-20
# @Author  : tc
"""
540. 有序数组中的单一元素
给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。
请你找出并返回只出现一次的那个数。

你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。

示例 1:

输入: nums = [1,1,2,3,3,4,4,8,8]
输出: 2
示例 2:

输入: nums =  [3,3,7,7,10,11,11]
输出: 10

二分法：
由于数组是有序的，因此数组中相同的元素一定相邻。
对于下标x左边的下标y，如果 nums[y]=nums[y+1]，则 y 一定是偶数；
对于下标x右边的下标z，如果 nums[z]=nums[z+1]，则z一定是奇数。
由于下标x是相同元素的开始下标的奇偶性的分界，因此可以使用二分查找的方法寻找下标x。

初始时，二分查找的左边界是 0，右边界是数组的最大下标。每次取左右边界的平均值mid作为待判断的下标，
根据mid 的奇偶性决定和左边或右边的相邻元素比较：

- 如果mid是偶数，则比较nums[mid] 和 nums[mid+1] 是否相等；

- 如果 mid 是奇数，则比较 nums[mid−1] 和 nums[mid] 是否相等。

细节

利用按位异或的性质，可以得到 mid 和相邻的数之间的如下关系，其中⊕ 是按位异或运算符：

当mid 是偶数时，mid+1=mid⊕1；

当mid 是奇数时，mid−1=mid⊕1。

代码来自：https://leetcode.cn/problems/single-element-in-a-sorted-array/solution/you-xu-shu-zu-zhong-de-dan-yi-yuan-su-by-y8gh/
"""
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == nums[mid ^ 1]:
                low = mid + 1
            else:
                high = mid
        return nums[low]