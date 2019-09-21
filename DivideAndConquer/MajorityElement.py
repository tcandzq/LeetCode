#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 21:54
# @Author  : tc
# @File    : MajorityElement.py

"""
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

max(dict,dict.get):https://blog.csdn.net/weixin_41788255/article/details/79634142
"""
# Hash表解法
def majorityElement(nums):
    if not nums:
        return 0
    appear_dict = {}
    for num in nums:
        if appear_dict.get(num):
            appear_dict[num] += 1
        else:
            appear_dict[num] = 1
    return max(appear_dict,key=appear_dict.get)  # 这个max(dict,dict.get)是最骚的

if __name__ == '__main__':
    nums = [3,2,3]
    print(majorityElement(nums))