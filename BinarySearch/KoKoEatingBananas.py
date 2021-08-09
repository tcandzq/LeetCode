# -*- coding: utf-8 -*-
# @File    : KoKoEatingBananas.py
# @Date    : 2021-08-10
# @Author  : tc
"""
875. 爱吃香蕉的珂珂
珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。

示例 1：

输入: piles = [3,6,7,11], H = 8
输出: 4
示例 2：

输入: piles = [30,11,23,4,20], H = 5
输出: 30
示例 3：

输入: piles = [30,11,23,4,20], H = 6
输出: 23

思路：
使用二分查找，KOKO的速度在[1, max(piles)]之间，在能吃完香蕉的前提下尽可能用最小的速度。

"""
from typing import List

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(speed) -> bool:
            return sum(math.ceil(pile / speed) for pile in piles) <= h  # slower
            #return sum((pile - 1) / speed  + 1 for pile in piles) <= h  # faster

        left, right = 1, max(piles)
        while left < right:
            mid = left  + (right - left) // 2
            # 如果香蕉吃完了,尝试以更小的速度
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
