#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 23:11
# @Author  : tc
# @File    : ValidPalindrome.py
"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

中心扩展法,从中间位置向两边扩散
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        s = ''.join([x for x in s if x.isalpha() or x.isdigit()])
        if not s:
            return True
        i = 0
        j = len(s) - 1
        if not s:
            return False
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome('0P'))