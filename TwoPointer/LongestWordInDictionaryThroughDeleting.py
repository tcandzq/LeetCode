# -*- coding: utf-8 -*-
# @File    : LongestWordInDictionaryThroughDeleting.py
# @Date    : 2022-08-14
# @Author  : tc
"""
524.通过删除字母匹配到字典里最长单词
给你一个字符串 s 和一个字符串数组 dictionary ，找出并返回 dictionary 中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。

示例 1：

输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
输出："apple"
示例 2：

输入：s = "abpcplea", dictionary = ["a","b","c"]
输出："a"

提示：

1 <= s.length <= 1000
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 1000
s 和 dictionary[i] 仅由小写英文字母组成

双指针解法

代码参考:https://leetcode.cn/problems/longest-word-in-dictionary-through-deleting/solution/tong-guo-shan-chu-zi-mu-pi-pei-dao-zi-di-at66/
"""

from typing import List
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res = ""
        for t in dictionary:
            i = 0
            j = 0
            while i < len(s) and j < len(t):

                if s[i] == t[j]:
                    j += 1
                i += 1
            if j == len(t):
                if len(t) > len(res) or (len(t) == len(res) and t < res):
                    res = t
        return res