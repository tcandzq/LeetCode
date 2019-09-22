#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 22:36
# @Author  : tc
# @File    : NextPermutation.py
"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

这题看了半天,不知所云,请参考:https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-by-powcai/
看了上面参考的链接也不太懂。
我的理解:
如果一个数组是降序的,其实是没有办法得到它的下一个更大的排列的。我们可以从右往左找到第一个不是降序排列的数组,以1 2 7 4 3 1为例
7 4 3 1都是降序排列的,所以你在这里面不管怎么交换都不会使得原始数组的排列变大。当走到2时发现,以2开头的数组不再是降序排列的,所以考虑2
是一个交换的地点,接下来我们就要从降序排列的数组中找到最小的大于2的数,结果是3,交换2和3。此时发现3以后的数组7 4 2 1依旧是降序排列的
我们可以通过反转这列数组使得该数组由降序变升序,这样就是从最大排序变成了最小排序了。这样我才能保证排列后的数组是最小最大的数组。
"""
def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    start = -1
    for i in range(len(nums)-1, -1, -1):
        if nums[i - 1] < nums[i]:
            start = i - 1
            break
    if start == -1:
        reverse(nums, 0, len(nums) - 1)
        return
    for j in range(start+1, len(nums)):
        if nums[j] > nums[start] and (j == len(nums)-1 or nums[j + 1] <= nums[start]):
            nums[start], nums[j] = nums[j], nums[start]
            reverse(nums, start + 1, len(nums) - 1)
            break


def reverse(nums,i,j):
    while i < j:
        nums[i],nums[j] = nums[j],nums[i]
        i += 1
        j -= 1


if __name__ == '__main__':
    nextPermutation([1,2,3])

