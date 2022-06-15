# -*- coding: utf-8 -*-
# @File    : ConcatenatedWords.py
# @Date    : 2022-06-16
# @Author  : tc
"""
472. 连接词
给你一个 不含重复 单词的字符串数组 words ，请你找出并返回 words 中的所有 连接词 。
连接词 定义为：一个完全由给定数组中的至少两个较短单词组成的字符串。

示例 1：

输入：words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
输出：["catsdogcats","dogcatsdog","ratcatdogcat"]
解释："catsdogcats" 由 "cats", "dog" 和 "cats" 组成;
     "dogcatsdog" 由 "dog", "cats" 和 "dog" 组成;
     "ratcatdogcat" 由 "rat", "cat", "dog" 和 "cat" 组成。
示例 2：

输入：words = ["cat","dog","catdog"]
输出：["catdog"]

提示：

1 <= words.length <= 104
0 <= words[i].length <= 30
words[i] 仅由小写字母组成
0 <= sum(words[i].length) <= 105

动态规划,使用单词拆分的模板
"""
from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ans = []
        # 对数组进行升序排序，因为长字符串是由两个较短的字符串组成，排序后字符串words[i]肯定是words[:i]集合里的较短字符串构成
        words.sort(key=len)
        # 较短字符串的集合
        pre_words = set()
        for word in words:
            if self.wordBreak(word, pre_words):
                ans.append(word)
            pre_words.add(word)
        return ans

    # 单词拆分题的模版
    def wordBreak(self, s, words):
        # 这行代码很关键
        if not words:
            return False
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if s[j:i] in words and dp[j]:
                    dp[i] = True
                    break
        return dp[-1]