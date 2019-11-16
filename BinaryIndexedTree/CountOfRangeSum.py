#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 1:12
# @Author  : tc
# @File    : CountOfRangeSum.py
"""
题号 327 区间和的个数

给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。

说明:
最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。

示例:

输入: nums = [-2,5,-1], lower = -2, upper = 2,
输出: 3
解释: 3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。


使用前缀和sum[i] 区间数组[0,i]的和

lower <= sum[j] - sum[i] <= upper 那么sum[i] + lower <= sum[j] <= sum[i] + upper

因此在sum[i]+lower和sum[i]+upper之间的范围内的值都是满足要求的。

没有完全理解，要继续消化

"""
from typing import List
import bisect
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        p = [0]  # 前缀和初始化，前缀和p[x]，就是区间数组[0, x)的和
        for i in nums:
            p += [p[-1] + i]  # 前缀和计算
        ans = 0
        q = []  # 维护一个有序的前缀和队列
        for pi in p[:: -1]:  # 逆序遍历前缀和
            i, j = pi + lower, pi + upper  # 给出当前前缀和两个对应边界
            l = bisect.bisect_left(q, i)  # 二分查找
            r = bisect.bisect_right(q, j)  # 找到对应边界在前缀和数组里的插入位置
            ans += r - l  # 序号大于自己的前缀和里有多少个前缀和在边界里面，就是以当前区间为起点，符合区间和条件的个数
            bisect.insort(q, pi)  # 二分插入更新队列
        return ans


if __name__ == '__main__':
    nums = [-2,5,-1]
    lower = -1
    upper = 0
    solution = Solution()
    print(solution.countRangeSum(nums,lower,upper))