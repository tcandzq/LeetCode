# -*- coding: utf-8 -*-
# @File    : CreateMaximumNumber.py
# @Date    : 2020-02-19
# @Author  : tc
"""
题号 321 拼接最大数
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。

求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。

说明: 请尽可能地优化你算法的时间和空间复杂度。

示例 1:

输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]
示例 2:

输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]
示例 3:

输入:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
输出:
[9, 8, 9]

思路：用nums1 组成最大的i位数，则nums2组成最大的k-i位(i=0,...,k)，然后得到最大的那位数

思路参考:https://leetcode-cn.com/problems/create-maximum-number/solution/dan-diao-zhan-by-powcai/

代码参考：https://leetcode.com/problems/create-maximum-number/discuss/77286/Short-Python-Ruby-C%2B%2B

"""
from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def prep(nums,k):
            drop = len(nums) - k  # 表示可以从nums中移除的数，这样剩下的数就构成了k位数
            stack = []
            for num in nums:
                # 维护一个单调递减栈
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(a, b): # 字典序较大的那个数组的第一位
            return [max(a,b).pop(0) for _ in a+b]

        res = [0] * k
        for i in range(k+1):
            if i <= len(nums1) and k - i <= len(nums2):
                temp = merge(prep(nums1,i),prep(nums2,k-i))
                if temp > res:
                    res = temp
        return res

if __name__ == '__main__':
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5
    solution = Solution()
    print(solution.maxNumber(nums1,nums2,k))
    a = [3,2,1]
    b = [4,3,2]
    for num in a+b:
        print(max(a,b))
        print(max(a,b).pop(0))
