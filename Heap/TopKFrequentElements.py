#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 22:32
# @Author  : tc
# @File    : TopKFrequentElements.py
"""
题号 347 前K个高频元素
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
说明：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。

解决方法很简单，但优化的话需要用到堆排序

参考:https://leetcode-cn.com/problems/top-k-frequent-elements/solution/leetcode-di-347-hao-wen-ti-qian-k-ge-gao-pin-yuan-/

"""
from typing import List

class Solution:

    # 是个人都能想到的版本
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        return [x[0] for x in sorted(count_dict.items(), reverse=True, key=lambda count_dict: count_dict[1])][:k]

    # 小顶堆
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        heap = []
        for key in count_dict.keys():
            if len(heap) < k:
                heap.append(key)
            elif count_dict[key] > heap[-1]:
                heap.pop(-1)
                heap.append(key)
        res = []
        while heap:
            res.append(heap.pop(-1))
        return res
if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    solution = Solution()
    print(solution.topKFrequent2(nums,k))