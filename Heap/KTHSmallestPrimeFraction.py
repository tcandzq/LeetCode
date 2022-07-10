# -*- coding: utf-8 -*-
# @File    : KTHSmallestPrimeFraction.py
# @Date    : 2022-07-11
# @Author  : tc
"""
786. 第 K 个最小的素数分数
给你一个按递增顺序排序的数组 arr 和一个整数 k 。数组 arr 由 1 和若干 素数  组成，且其中所有整数互不相同。
对于每对满足 0 <= i < j < arr.length 的 i 和 j ，可以得到分数 arr[i] / arr[j] 。
那么第 k 个最小的分数是多少呢?  以长度为 2 的整数数组返回你的答案, 这里 answer[0] == arr[i] 且 answer[1] == arr[j] 。

示例 1：
输入：arr = [1,2,3,5], k = 3
输出：[2,5]
解释：已构造好的分数,排序后如下所示:
1/5, 1/3, 2/5, 1/2, 3/5, 2/3
很明显第三个最小的分数是 2/5

示例 2：
输入：arr = [1,7], k = 1
输出：[1,7]

利用优先队列(堆)
https://leetcode.cn/problems/k-th-smallest-prime-fraction/solution/di-k-ge-zui-xiao-de-su-shu-fen-shu-by-le-argw/
"""
import  heapq
from typing import List
class Frac:
	def __init__(self, idx, idy, x, y):
		self.idx = idx
		self.idy = idy
		self.x = x
		self.y = y

	def __lt__(self, other:"Frac"):
		return self.x * other.y < self.y * other.x


import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        q = [Frac(0, i, arr[0], arr[i]) for i in range(1, n)]
        heapq.heapify(q)

        for _ in range(k - 1):
            frac = heapq.heappop(q)
            i, j = frac.idx, frac.idy
            if i + 1 < j:
                heapq.heappush(q, Frac(i + 1, j, arr[i + 1], arr[j]))
        return [q[0].x, q[0].y]