#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 23:35
# @Author  : tc
# @File    : PalindromicSubstrings.py
"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
注意:
输入的字符串长度不会超过1000。
"""
#暴力法会超时
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.helper(s[i:j+1]):
                    count += 1
        return count

    def helper(self,s):
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

#动态规划求解

if __name__ == '__main__':
    solution = Solution()
    print(solution.countSubstrings("abc"))
