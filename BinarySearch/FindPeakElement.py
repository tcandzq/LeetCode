#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 16:46
# @Author  : tc
# @File    : FindPeakElement.py
"""
题号 162 寻找峰值
峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

示例 1:

输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。
示例 2:

输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5
解释: 你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。


题目要求用log(N),很明显是用二分求解，一开始没怎么理解，后来恍然大悟

为什么二分查找大的那一半一定会有峰值呢？（即nums[mid]<nums[mid+1]时，mid+1~N一定存在峰值）
我的理解是，首先已知 nums[mid+1]>nums[mid]，那么mid+2只有两种可能，一个是大于mid+1，一个是小于mid+1，小于mid+1的情况，那么mid+1就是峰值，
大于mid+1的情况，继续向右推，如果一直到数组的末尾都是大于的，那么可以肯定最后一个元素是峰值，因为nums[nums.length]=负无穷

看讨论有评论说:
"很简单，上坡必有坡顶"
"确实，上坡的话有两种可能，一种是下坡，一种还是上坡，但是最后也算是峰顶"


其实这题使用二分查找得益于题目给出的两个充要条件:
1.nums[-1] = nums[n] = -∞;

这样哪怕nums只有一个元素例如[1]实际也是[-∞,1,-∞],峰值是1。

2.返回任何一个峰值所在位置即可

3.nums[i]≠nums[i+1]

因此任意两个相连的数字必定会有大小关系,我只要锁定大的那个就行了，而二分是最快的查找方法

参考:https://leetcode-cn.com/problems/find-peak-element/solution/hua-jie-suan-fa-162-xun-zhao-feng-zhi-by-guanpengc/

"""
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:  # 1.nums[i]≠nums[i+1],考虑下 为什么不是left <= right?
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:  # 同2
                left = mid + 1  # 3. mid 肯定不是峰值
            else:
                right = mid
        return right  # 跳出while循环时,left = right,所以这里改成return left是一样的


if __name__ == '__main__':
    nums = [1,2,3,1]
    solution = Solution()
    print(solution.findPeakElement(nums))