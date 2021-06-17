# -*- coding: utf-8 -*-
# @File    : 58_01_ReverseWordsInSentence.py
# @Date    : 2021-06-18
# @Author  : tc
"""
58. 最后一个单词的长度
给你一个字符串 s，由若干单词组成，单词之间用空格隔开。返回字符串中最后一个单词的长度。如果不存在最后一个单词，请返回 0 。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

示例 1：

输入：s = "Hello World"
输出：5
示例 2：

输入：s = " "
输出：0
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        nums = s.split(' ')
        for i in range(len(nums) - 1, -1, -1):
            if nums[i]:
                return len(nums[i])
        return 0