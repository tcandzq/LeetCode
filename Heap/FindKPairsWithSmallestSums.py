#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 0:19
# @Author  : tc
# @File    : FindKPairsWithSmallestSums.py
""""
题号 373 查找和最小的K对数字
给定两个以升序排列的整形数组 nums1 和 nums2, 以及一个整数 k。

定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2。

找到和最小的 k 对数字 (u1,v1), (u2,v2) ... (uk,vk)。

示例 1:

输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
输出: [1,2],[1,4],[1,6]
解释: 返回序列中的前 3 对数：
     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
示例 2:

输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
输出: [1,1],[1,1]
解释: 返回序列中的前 2 对数：
     [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
示例 3:

输入: nums1 = [1,2], nums2 = [3], k = 3
输出: [1,3],[2,3]
解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]

思路：一般遇到求第k大，第k小，前k大，前k小，会用到优先对列，即大顶堆，小顶堆
这一题求前k小，所以用小顶堆

对暴力版的优化思路:
1.先初始化好需要做堆排序的数组，然后一次性返回堆顶元素，而不是像暴力法中的那样,一边插入,一边做堆排

2.因为数组是有序,所以尽量靠前拿最有可能拿到最小的组合值

3.代码上的优化,比如,我要返回一个数组nums的k个值,当len(nums)不足k时,就全部返回
那这样写会非常精简:
    while k and nums:
        pass
"""
from typing import  List

class Solution:
    # 暴力版
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        k = k if k <= len(nums1)*len(nums2) else len(nums1)*len(nums2)
        import heapq
        queue = []
        for num1 in nums1:
            for num2 in nums2:
                heapq.heappush(queue,(num1+num2,[num1,num2]))
        res = []
        while k > 0:
            k -= 1
            _,pairs = heapq.heappop(queue)
            print(pairs)
            res.append(pairs)
        return res

    #  优化版从别人提交的代码上看到的:https://leetcode-cn.com/submissions/detail/37333508/
    def kSmallestPairs2(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq
        res = []
        len1,len2 = len(nums1),len(nums2)
        if not len1 or not  len2:
            return []
        heap = [[nums1[0] + nums2[i],0,i] for i in range(len2)]
        while k and heap:  # 这种判断很精简,比如当k>len(heap)时以len(heap)为准,反之亦然
            val,i,j = heapq.heappop(heap)
            res.append([nums1[i],nums2[j]])
            if i + 1 < len1:  # 注意
                heapq.heappush(heap, [nums1[i + 1] + nums2[j], i + 1, j])
            k -= 1
        return res
if __name__ == '__main__':
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 10
    solution = Solution()
    print(solution.kSmallestPairs(nums1,nums2,k))