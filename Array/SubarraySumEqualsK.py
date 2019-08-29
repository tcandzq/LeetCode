#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 14:40
# @Author  : tc
# @File    : ShortestSubarrayWithSumAtLeastK.py

"""
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
Input1:nums = [1,1,1], k = 2
Output1:2, [1,1] 与 [1,1] 为两种不同的情况。
说明:1.数组的长度为 [1, 20,000]。
    2.数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

两数之和的简单变种,暴力求解后会超时,要考虑用空间换时间

注意:1.python中从字典中获取key对应的value,用{}.get(key) 不要用{}[key]
     2.因为返回的是满足条件子数组的个数,所以字典对应的value是每个数出现的次数

详解参考:https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/c-nshi-jian-nkong-jian-xiang-jie-by-charon____/
"""
def subarraySum(nums,k):
    count = 0
    num_dict = {}
    #注意这里前缀和多了一个0，防止漏掉数组的前缀和刚好等于k的情况
    num_dict[0] = 1
    num_sum = 0
    for num in nums:
        num_sum += num
        if num_dict.get(num_sum - k):
            count += num_dict[num_sum - k]
        if num_dict.get(num_sum):
            num_dict[num_sum] += 1
        else:
            num_dict[num_sum] = 1
    return count
if __name__ == '__main__':
    nums = [0,0,0,0,0,0,0,0,0,0]
    k = 0
    print(subarraySum(nums, k))