# -*- coding: utf-8 -*-
# @File    : MaximumProductOfWordLengths.py
# @Date    : 2020-02-20
# @Author  : tc
"""
题号 318 最大单词长度乘积
给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。

示例 1:

输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
输出: 16
解释: 这两个单词为 "abcw", "xtfn"。
示例 2:

输入: ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4
解释: 这两个单词为 "ab", "cd"。
示例 3:

输入: ["a","aa","aaa","aaaa"]
输出: 0
解释: 不存在这样的两个单词。

用二进制表示字符串，这样对长度相同，字符顺序不同的字符串就行能避免重复计算，例如'abc'和'bac'实际上是一样的。

代码参考：https://leetcode.com/problems/maximum-product-of-word-lengths/discuss/76970/Python-solution-beats-99.67

思路参考：Can you please explain how did you come up with this approach? is there a known algorithm?

"""
from typing import List

class Solution:
    # 暴力
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        _max = 0
        for i in range(n):
            for j in range(i+1,n):
                if not set(words[i]).intersection(set(words[j])):
                    length = len(words[i]) * len(words[j])
                    if length > _max:
                        _max = length
        return _max

    # 优化
    def maxProduct2(self, words: List[str]) -> int:
        d = {}
        for w in words:
            mask = 0
            for c in w:
                mask |= (1 << (ord(c) - 97))
            d[mask] = max(d.get(mask,0),len(w))
        return max([d[x] * d[y] for x in d for y in d if not x&y] or [0])
if __name__ == '__main__':
    words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    solution = Solution()
    print(solution.maxProduct2(words))