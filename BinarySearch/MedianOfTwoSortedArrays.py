#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 14:31
# @Author  : tc
# @File    : MedianOfTwoSortedArrays.py

"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

Input1:nums1 = [1, 3]
      nums2 = [2]

Output1:中位数是 2.0

Input1:nums1 = [1, 2]
      nums2 = [3, 4]

Output1:中位数是 (2 + 3)/2 = 2.5

官方解答太复杂 看了半天那么看懂。参考题解：
https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/4-xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-shu/

"""
def findMedianSortedArrays(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    # 保证数组1一定最短
    if n > m:
        return findMedianSortedArrays(nums2, nums1)
    l_max1 = 0
    l_max2 = 0
    r_min1 = 0
    r_min2 = 0
    # 第一个数组的割 指的是数组下标 而非具体的数值
    c1 = 0

    # 第二个数组的割 指的是数组下标 而非具体的数值
    c2 = 0
    lo = 0

    # 数组1的长度是2n+1 hi是最大下标 故为2n+1-1=2n
    hi = 2 * n
    while (lo <= hi):
        # c1是二分的结果
        c1 = (lo + hi) // 2

        c2 = m + n - c1

        # 数组1整体都在右边了，所以都比中值大，中值在数组2中，简单的说就是数组1割后的左边是空了所以我们可以假定LMin1= INT_MIN，来保证l_max1 < r_max2
        l_max1 = float('-inf') if c1 == 0 else nums1[(c1 - 1) // 2]

        # 数组1整体都在左边了，所以都比中值小，中值在数组2中 ，简单的说就是数组1割后的右边是空了所以我们可以假定RMin1= INT_MAX，来保证LMax2<RMin1恒成立
        r_min1 = float('inf') if c1 == 2 * n else nums1[(c1) // 2]

        # 数组2整体都在右边了，所以都比中值大，中值在数组1中，简单的说就是数组2割后的左边是空了所以我们可以假定LMax2=INT_MIN，来保证l_max2 < r_max1
        l_max2 = float('-inf') if c2 == 0 else nums2[(c2 - 1) // 2]

        # 数组2整体都在左边了
        r_min2 = float('inf') if c2 == 2 * m else nums2[(c2) // 2]

        # c1太多太大了 需要把c1减小 往前移动
        if l_max1 > r_min2:
            hi = c1 - 1

        # c2太多太大了 意味着c1太小了 需要把c1增大 往后移动
        elif l_max2 > r_min1:
            lo = c1 + 1
        else:
            break

    return (max(l_max1, l_max2) + min(r_min1, r_min2)) / 2

if __name__ == '__main__':
    nums1 = [1,2]

    nums2 = [3,4]

    print(findMedianSortedArrays(nums1,nums2))