# -*- coding: utf-8 -*-
# @File    : RansomNote.py
# @Date    : 2020-02-26
# @Author  : tc
"""
题号 383. 赎金信
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)

注意：

你可以假设两个字符串均只含有小写字母。

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        r = Counter(ransomNote)
        m = Counter(magazine)

        for word,freq in r.items():
            if word not in m or m[word] < freq:
                return False
        return True


if __name__ == '__main__':
    ransomNote = "aa"
    magazine = "aab"
    solution = Solution()
    print(solution.canConstruct(ransomNote,magazine))