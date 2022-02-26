# -*- coding: utf-8 -*-
# @File    : PalindromePairs.py
# @Date    : 2022-02-20
# @Author  : tc
"""
336. 回文对
给定一组 互不相同 的单词， 找出所有 不同 的索引对 (i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。

示例 1：
输入：words = ["abcd","dcba","lls","s","sssll"]
输出：[[0,1],[1,0],[3,2],[2,4]]
解释：可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]

示例 2：
输入：words = ["bat","tab","cat"]
输出：[[0,1],[1,0]]
解释：可拼接成的回文串为 ["battab","tabbat"]

示例 3：
输入：words = ["a",""]
输出：[[0,1],[1,0]]

提示：

1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] 由小写英文字母组成

字典树解法：
https://leetcode.com/problems/palindrome-pairs/discuss/79195/O(n-*-k2)-java-solution-with-Trie-structure
但用python会超时

实际的代码来自：
https://leetcode.com/problems/palindrome-pairs/discuss/79219/Python-solution~
上面解法中的评论"Python 3 , beats 99%"

"""
from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        d = {}
        for i, w in enumerate(words):
            d[w[::-1]] = i
        indices = set()
        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                prefix = w[:j]
                postfix = w[j:]
                if prefix in d and i != d[prefix] and postfix == postfix[::-1]:
                    indices.add((i, d[prefix]))
                if postfix in d and i != d[postfix] and prefix == prefix[::-1]:
                    indices.add((d[postfix], i))

        return [list(p) for p in indices]