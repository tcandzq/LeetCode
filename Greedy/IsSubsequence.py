#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/4 16:46
# @Author  : tc
# @File    : isSubsequence.py
"""
题号 392 判断子序列
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1:
s = "abc", t = "ahbgdc"

返回 true.

示例 2:
s = "axc", t = "ahbgdc"

返回 false.

后续挑战 :

如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

这哪里看出来有贪心算法的影子了？不过代码值得学习，由于len(t)>>len(s)，因此把i当做全局变量，省得做双重for循环了。

优雅代码也太厉害了吧。

"""
class Solution:
    #  正常代码
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i = 0
        for j in range(len(t)):
            if s[i] == t[j]:
                i += 1
            if i == len(s):
                return True
        return False

    #  优雅代码
    def isSubsequence2(self, s: str, t: str) -> bool:
        s = list(s)
        for _t in t:
            if not s:
                return True
            if _t == s[0]:
                s.pop(0)
        return len(s) == 0



if __name__ == '__main__':
    s = "ace"
    t = "abcde"
    solution = Solution()
    print(solution.isSubsequence2(s,t))