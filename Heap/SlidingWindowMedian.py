# -*- coding: utf-8 -*-
# @File    : SlidingWindowMedian.py
# @Date    : 2022-06-19
# @Author  : tc
"""
480. 滑动窗口中位数
中位数是有序序列最中间的那个数。如果序列的长度是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。

例如：
[2,3,4]，中位数是 3
[2,3]，中位数是 (2 + 3) / 2 = 2.5
给你一个数组 nums，有一个长度为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。

示例：

给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。

窗口位置                      中位数
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7      -1
 1  3 [-1  -3  5] 3  6  7      -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
 因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。

使用大顶堆和小顶堆
"""
import heapq
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small = []  # 大顶堆，存储的都是小于等于中位数的元素
        large = []  # 小顶堆，存储的搜是大于等于中位数的元素

        # 第一步初始化的时候，让数组的前k个元素进入大顶堆
        # python中只有小顶堆，在元素中加个负号就变成了大顶堆,因此小顶堆里面存的都是正数,大顶堆里面存的都是正数
        for index, value in enumerate(nums[:k]):
            heapq.heappush(small, (-value, index))

        # 让大顶堆的前k/2个元素进入小顶堆
        for _ in range(k - (k >> 1)):
            self.move(small, large)

        ans = [self.get_median(small, large, k)]

        for index, value in enumerate(nums[k:]):

            # 如果数组的当前值大于小顶堆的最小值(比中位数大)，则加入小顶堆
            if value >= large[0][0]:
                heapq.heappush(large, (value, index + k))
                # nums[index] 是当前滑动窗口之外的元素，它后面需要出堆
                # 此时小顶堆和大顶堆中的元素数量就不平衡了，
                if nums[index] <= large[0][0]:  # 窗口之外的这个元素小于等于小顶堆的最小值，说明它属于大顶堆，它应该从大顶堆中移出，但是先不急删除(lazy deleting)
                    self.move(large, small)  # 小顶堆需要出堆一个元素进入大顶堆，保持两个堆之间的数量平衡

            # 否则加入大顶堆
            else:
                # 大顶堆新增一个元素
                heapq.heappush(small, (-value, index + k))
                # 窗口之外的这个元素大于等于小顶堆的最小值，说明它属于小顶堆，它应该从小顶堆中移出，但是先不急删除(lazy deleting)
                if nums[index] >= large[0][0]:  #
                    self.move(small, large)  # 大顶堆出堆一个元素进入小顶堆，保持两个堆之间的数量平衡

            # 这里把所有窗口之外的元素统一都删除掉(lazey deleting)
            # 移除大顶堆窗口之外的所有元素
            while small and small[0][1] <= index:
                heapq.heappop(small)
            # 移除小顶堆窗口之外的所有元素
            while large and large[0][1] <= index:
                heapq.heappop(large)
            ans.append(self.get_median(small, large, k))
        return ans

    def get_median(self, small, large, k):
        # 注意small里的元素都是负数
        # 如果k是奇数，那么小顶堆的最小值就是中位数;如果k是偶数，那么取小顶堆的最小值和大顶堆的最大值的平均值
        return large[0][0] * 1 if k & 1 else (large[0][0] - small[0][0]) / 2

    def move(self, hp1, hp2):
        value, index = heapq.heappop(hp1)
        heapq.heappush(hp2, (-value, index))
