# -*- coding: utf-8 -*-
# @File    : CouplesHoldingHands.py
# @Date    : 2022-08-14
# @Author  : tc
"""
765. 情侣牵手
n 对情侣坐在连续排列的 2n 个座位上，想要牵到对方的手。
人和座位由一个整数数组 row 表示，其中 row[i] 是坐在第 i 个座位上的人的 ID。情侣们按顺序编号，
第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2n-2, 2n-1)。
返回 最少交换座位的次数，以便每对情侣可以并肩坐在一起。 每次交换可选择任意两人，让他们站起来交换座位。


示例 1:
输入: row = [0,2,1,3]
输出: 1
解释: 只需要交换row[1]和row[2]的位置即可。

示例 2:
输入: row = [3,2,0,1]
输出: 0
解释: 无需交换座位，所有的情侣都已经可以手牵手了。


提示:
2n == row.length
2 <= n <= 30
n 是偶数
0 <= row[i] < 2n
row 中所有元素均无重复

「首尾相连」这件事情可以使用 并查集 表示

参考:https://leetcode.cn/problems/couples-holding-hands/solution/qing-lu-qian-shou-by-leetcode-gl1c/
"""
from typing import List
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2
        dsu = DSU(n)
        for i in range(0, len(row), 2):
            dsu.union(row[i] // 2, row[i + 1] // 2)
        return n - dsu.regions()
class DSU:
    def __init__(self, N):
        self.par_ = [i for i in range(N)]
        self.region_ = N

    def find(self, x):
        # if x != self.par_[x]:
        #     x = self.find(self.par_[x])
        # return self.par_[x]
        while x != self.par_[x]:
            x = self.par_[x]
        return self.par_[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        self.par_[px] = py
        self.region_ -= 1

    def regions(self):
        return self.region_