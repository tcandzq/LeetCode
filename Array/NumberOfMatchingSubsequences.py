#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/4 17:10
# @Author  : tc
# @File    : NumberOfMatchingSubsequences.py
"""
题号 792 匹配子序列的单词数
给定字符串 S 和单词字典 words, 求 words[i] 中是 S 的子序列的单词个数。

示例:
输入:
S = "abcde"
words = ["a", "bb", "acd", "ace"]
输出: 3
解释: 有三个是 S 的子序列的单词: "a", "acd", "ace"。
注意:

所有在words和 S 里的单词都只由小写字母组成。
S 的长度在 [1, 50000]。
words 的长度在 [1, 5000]。
words[i]的长度在[1, 50]。

leetcode中文网没有python提交成功的答案，从leetcode英文版找到了题解：
https://leetcode.com/problems/number-of-matching-subsequences/discuss/117634/Efficient-and-simple-go-through-words-in-parallel-with-explanation

利用字典树的思想

"""
from collections import defaultdict
from typing import List

class Solution:
    #  超时
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        count = 0
        for word in words:
            if self.isSubsequence(word,S):
                count += 1

        return count

    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        for _t in t:
            if not s:
                return True
            if _t == s[0]:
                s.pop(0)
        return len(s) == 0

    #  成功解法
    def numMatchingSubseq2(self, S: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        for w in words:
            # 存储以w[0]开头的前缀字典。此时waiting = {'a': [[], ['c', 'd'], ['c', 'e']], 'b': [['b']]}
            waiting[w[0]].append(iter(w[1:]))
        print(waiting)
        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)  # 在本题的例子中 it 分别为[]、['c', 'd']、['c', 'e']
        print(waiting)
        return len(waiting[None])

if __name__ == '__main__':
    S = "abcde"
    words = ["a", "bb", "acd", "ace"]
    solution = Solution()
    print(solution.numMatchingSubseq2(S, words))