# -*- coding: utf-8 -*-
# @File    : SubstringWithConcatenationOfAllWords.py
# @Date    : 2019-12-21
# @Author  : tc
"""
题号 30 串联所有单词的子串
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]

参考1:https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/solution/chuan-lian-suo-you-dan-ci-de-zi-chuan-by-powcai/

判断一个长串是否由短串数组构成，等价于判断长串中短串出现的频率是否与短串数组中短串的频率相等。这样问题就可以借用HashMap


"""
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words: return []
        one_word = len(words[0])
        all_len = len(words) * one_word
        n = len(s)
        words = Counter(words)
        res = []
        for i in range(0, n - all_len + 1):
            tmp = s[i:i + all_len]  # 在s上做滑动窗口
            c_tmp = []
            for j in range(0, all_len, one_word):
                c_tmp.append(tmp[j:j + one_word])  # 计算滑动窗口内单词的数量
            if Counter(c_tmp) == words:  # 判断滑动窗口内单词的数量是否和words相等
                res.append(i)
        return res


if __name__ == '__main__':
    s = "foobarfoobar"
    words = ["foo","bar"]
    solution = Solution()
    print(solution.findSubstring(s,words))