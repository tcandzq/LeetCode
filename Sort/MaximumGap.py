#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 9:26
# @Author  : tc
# @File    : MaximumGap.py
"""
题号 164 最大间距

给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。

示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
示例 2:

输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
说明:

你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。

注意题目要求的是O(n)解法

关键:相邻的最大差值一定不小于该数组的最大值减去最小值除以间隔个数

"""
from typing import List
from math import ceil

class Bucket:
    def __init__(self):
        self.min_val = float('inf')
        self.max_val = float('-inf')


class Solution:
    # 解法1
    def maximumGap(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return 0
        min_num = min(nums)
        max_num = max(nums)
        gap = ceil((max_num - min_num)/(size - 1))  # 向上取整,得到每个桶之间的间距
        bucket = [[float('inf'), float('-inf')] for _ in range(size - 1)]  # 初始化桶bucket,每个桶里满存储桶内元素的最小值和最大值
        print(bucket)
        for num in nums:
            if num == max_num or num == min_num:
                continue
            loc = (num - min_num) // gap
            bucket[loc][0] = min(num, bucket[loc][0])
            bucket[loc][1] = max(num, bucket[loc][1])
        pre_min = min_num
        res = float('-inf')
        for x, y in bucket:
            if x == float('inf'):
                continue
            res = max(res,x-pre_min)
            pre_min = y
        res = max(res,max_num - pre_min)
        return res

    # 解法2
    def maximumGap2(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return 0
        min_num = min(nums)
        max_num = max(nums)
        # 得到桶的容积,max(1)防止出现分母为0的情况,当nums中的所有元素都相等时,桶的容积为1,桶的数量为1
        bucket_size = max(1, (max_num - min_num) // (size - 1))
        bucket_num = (max_num - min_num) // bucket_size + 1
        bucket_list = [0 for _ in range(bucket_num)]
        for i in range(size):
            loc = (nums[i] - min_num) // bucket_size
            if not bucket_list[loc]:  # 防止同一个桶内的数据被覆盖
                bucket_list[loc] = Bucket()

            bucket_list[loc].min_val = min(nums[i],bucket_list[loc].min_val)
            bucket_list[loc].max_val = max(nums[i],bucket_list[loc].max_val)

        # for i in range(size):  # 注意下面的代码是有bug的
        #     loc = (nums[i] - min_num) // bucket_size
        #     if not bucket_list[loc]:  # 防止同一个桶内的数据被覆盖
        #         bucket = Bucket()
        #         bucket_list[loc] = bucket
        #     bucket_list[loc].min_val = min(nums[i],bucket.min_val)
        #     bucket_list[loc].max_val = max(nums[i],bucket.max_val)

        pre_max = float('inf')
        max_gap = float('-inf')
        for i in range(len(bucket_list)):
            if bucket_list[i] and pre_max != float('inf'):
                max_gap = max(bucket_list[i].min_val - pre_max, max_gap)

            if bucket_list[i]:
                pre_max = bucket_list[i].max_val
                max_gap = max(max_gap, bucket_list[i].max_val - bucket_list[i].min_val)
        return max_gap


if __name__ == '__main__':
    nums =[15252,16764,27963,7817,26155,20757,3478,22602,20404,6739,16790,10588,16521,6644,20880,15632,27078,25463,20124,15728,30042,16604,17223,4388,23646,32683,23688,12439,30630,3895,7926,22101,32406,21540,31799,3768,26679,21799,23740]
    solution = Solution()
    print(solution.maximumGap2(nums))