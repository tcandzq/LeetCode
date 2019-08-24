#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/24 12:39
# @Author  : tc
# @File    : MaximumProductSubarray.py

"""
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
Input1:[2,3,-2,4]
Output1:6
解释: 子数组 [2,3] 有最大乘积 6。

Input2:[-2,0,-1]
Output2:0
解释: [-2,0,-1]
结果不能为 2, 因为 [-2,-1] 不是子数组。

做不出来 具体代码参考:
          https://leetcode-cn.com/problems/maximum-product-subarray/solution/duo-chong-si-lu-qiu-jie-by-powcai-3/
总结得不错:https://leetcode-cn.com/problems/maximum-product-subarray/solution/er-wei-dong-tai-gui-hua-by-liweiwei1419/

"""
def maxProduct(nums):
    if not nums: return
    res = nums[0]
    pre_max = nums[0]
    pre_min = nums[0]
    for num in nums[1:]:
        cur_max = max(pre_max * num, pre_min * num, num)
        cur_min = min(pre_max * num, pre_min * num, num)
        res = max(res, cur_max)
        pre_max = cur_max
        pre_min = cur_min
    return res









if __name__ == '__main__':
    nums = [2, -5, -2, -4, 3]

    print(maxProduct(nums))
