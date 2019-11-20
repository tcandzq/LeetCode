#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 1:19
# @Author  : tc
# @File    : TopKFrequentWords.py
"""
题号 692 前K个高频单词
给一非空的单词列表，返回前 k 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。

示例 1：

输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。
 

示例 2：

输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
输出: ["the", "is", "sunny", "day"]
解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
    出现次数依次为 4, 3, 2 和 1 次。

参考:https://leetcode-cn.com/problems/top-k-frequent-words/solution/qian-kge-gao-pin-dan-ci-by-leetcode/

记住要善用collections

另外 heapq.heapify(heap) 是怎么实现按字母顺序排序的？没搞懂

"""
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import collections,heapq
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

if __name__ == '__main__':
    solution = Solution()
    words = ["love", "i", "leetcode", "love", "i", "coding"]
    k = 2
    print(solution.topKFrequent(words,k))
