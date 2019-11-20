#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 16:34
# @Author  : tc
# @File    : FindMedianFromDataStream.py
"""
题号 295 数据流的中位数

中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
进阶:

如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？

使用优先队列,参考:https://leetcode-cn.com/problems/find-median-from-data-stream/solution/you-xian-dui-lie-python-dai-ma-java-dai-ma-by-liwe/

大顶堆:存储前有序数组;
小顶堆:存储后有序数组。

1.当数据流的数量为奇数时，保证大顶堆的元素数量比小顶堆多一个;
2.当数据流的数量为偶数时，保证大顶堆与小顶堆的元素数量一样多。

"""
import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 当前大顶堆和小顶堆的元素个数之和
        self.count = 0
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        self.count += 1
        # 因为 Python 中的堆默认是小顶堆，所以要传入一个 tuple，用于比较的元素需是相反数，
        # 才能模拟出大顶堆的效果
        heapq.heappush(self.max_heap, (-num, num))
        _, max_heap_top = heapq.heappop(self.max_heap)  # 返回大顶堆的最大值
        heapq.heappush(self.min_heap, max_heap_top)  # 将大顶堆的最大值插入到小顶堆
        if self.count & 1:  # 如果数据流有奇数个需要保证大顶堆的元素个数比小顶堆多一个
            min_heap_top = heapq.heappop(self.min_heap)  # 刚加入小顶堆的元素pop出去
            heapq.heappush(self.max_heap, (-min_heap_top, min_heap_top))  # 小顶堆的元素又重新回到大顶堆


    def findMedian(self) -> float:
        if self.count & 1:  # 判断count的奇偶
            # 如果两个堆合起来的元素个数是奇数，数据流的中位数大顶堆的堆顶元素
            return self.max_heap[0][1]
        else:
            # 如果两个堆合起来的元素个数是偶数，数据流的中位数就是各自堆顶元素的平均值
            return (self.min_heap[0] + self.max_heap[0][1]) / 2


if __name__ == '__main__':
    median_finder = MedianFinder()
    median_finder.addNum(1)
    median_finder.addNum(2)
    print(median_finder.findMedian())

