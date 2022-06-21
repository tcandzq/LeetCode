# -*- coding: utf-8 -*-
# @File    : FindCommonCharacters.py
# @Date    : 2022-06-21
# @Author  : tc
"""
1002. 查找共用字符
给你一个字符串数组 words ，请你找出所有在 words 的每个字符串中都出现的共用字符（ 包括重复字符），并以数组形式返回。你可以按 任意顺序 返回答案。

示例 1：
输入：words = ["bella","label","roller"]
输出：["e","l","l"]

示例 2：
输入：words = ["cool","lock","cook"]
输出：["c","o"]

collections.Counter 的& 是取两个字典的交集，并且出现频率最小的那个key。
"""
import collections
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = collections.Counter(words[0])
        for word in words:
            res &= collections.Counter(word)
        return list(res.elements())
