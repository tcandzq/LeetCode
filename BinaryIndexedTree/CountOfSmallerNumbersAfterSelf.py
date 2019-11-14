#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 21:46
# @Author  : tc
# @File    : CountOfSmallerNumbersAfterSelf.py
"""
题号 315 计算右侧小于当前元素的个数
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例:

输入: [5,2,6,1]
输出: [2,1,1,0]
解释:
5 的右侧有 2 个更小的元素 (2 和 1).
2 的右侧仅有 1 个更小的元素 (1).
6 的右侧有 1 个更小的元素 (1).
1 的右侧有 0 个更小的元素.

二分查找:有序数组中新插入数字所在的索引等于该数组有多少个数字比新插入数字小
参考1:https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/315-by-ikaruga/
参考2:https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/duo-chong-fang-fa-by-powcai/

"""
from typing import List

class BinaryIndexedTree:
    def __init__(self,nums):
        self.bit_arr = [0] + nums
        for i in range(1,len(self.bit_arr)):
            j = i + (i & -i)
            if j < len(self.bit_arr):
                self.bit_arr[j] += self.bit_arr[i]

    def update(self,i,delta):
        i += 1
        while i < len(self.bit_arr):
            self.bit_arr[i] += delta
            i += (i & (-i))

    def set_val(self,i,val):
        i += 1
        self.update(i,val - self.bit_arr[i])

    def prefix(self,i):
        i += 1
        res = 0
        while i > 0:
            res += self.bit_arr[i]
            i -= (i & -i)
        return res


class Solution:
    # 二分查找解法
    def countSmaller(self, nums: List[int]) -> List[int]:
        import bisect
        queue = []
        res = []
        print(nums[::-1])
        for num in nums[::-1]:
            loc = bisect.bisect_left(queue, num)  # 二分查找有序数组中num所在的索引
            res.append(loc)
            queue.insert(loc, num)
        return res[::-1]

    #  树状数组解法2
    def countSmaller2(self, nums: List[int]) -> List[int]:
        hash_table = {v: i for i, v in enumerate(sorted(set(nums)))}
        tree = BinaryIndexedTree([0] * len(hash_table))
        res = []
        for i in range(len(nums) - 1, -1, -1):
            res.append(tree.prefix(hash_table[nums[i]] - 1))
            tree.update(hash_table[nums[i]], 1)
        return res[::-1]

    #  树状数组解法3
    def countSmaller3(self, nums: List[int]) -> List[int]:
        class FenwickTree:
            def __init__(self, n):
                self.size = n
                self.tree = [0 for _ in range(n + 1)]

            def __lowbit(self, index):
                return index & (-index)

            # 单点更新：将 index 这个位置 + 1
            def update(self, index, delta):
                # 从下到上，最多到 size，可以等于 size
                while index <= self.size:
                    self.tree[index] += delta
                    index += self.__lowbit(index)

            # 区间查询：查询小于等于 index 的元素个数
            # 查询的语义是"前缀和"
            def query(self, index):
                res = 0
                # 从上到下，最少到 1，可以等于 1
                while index > 0:
                    res += self.tree[index]
                    index -= self.__lowbit(index)
                return res

        # 特判
        size = len(nums)
        if size == 0:
            return []
        if size == 1:
            return [0]

        # 去重，方便离散化
        s = list(set(nums))

        s_len = len(s)

        # 离散化，借助堆
        import heapq
        heapq.heapify(s)

        rank_map = dict()
        rank = 1
        for _ in range(s_len):
            num = heapq.heappop(s)
            rank_map[num] = rank
            rank += 1

        fenwick_tree = FenwickTree(s_len)

        # 从后向前填表
        res = [None for _ in range(size)]
        # 从后向前填表
        for index in range(size - 1, -1, -1):
            # 1、查询排名
            rank = rank_map[nums[index]]
            # 2、在树状数组排名的那个位置 + 1
            fenwick_tree.update(rank, 1)
            # 3、查询一下小于等于“当前排名 - 1”的元素有多少
            res[index] = fenwick_tree.query(rank - 1)
        return res

if __name__ == '__main__':
    nums = [5,2,6,1]
    solution = Solution()
    print(solution.countSmaller2(nums))