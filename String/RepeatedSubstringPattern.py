# -*- coding: utf-8 -*-
# @File    : RepeatedSubstringPattern.py
# @Date    : 2022-08-14
# @Author  : tc
"""
459. 重复的子字符串
给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。
示例 1:

输入: s = "abab"
输出: true
解释: 可由子串 "ab" 重复两次构成。
示例 2:

输入: s = "aba"
输出: false
示例 3:

输入: s = "abcabcabcabc"
输出: true
解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)

假设字符串s是由s1+s2组成的，s+s后，str就变成了s1+s2+s1+s2，去掉首尾，破环了首尾的s1和s2，变成了s3+s2+s1+s4,
此时str中间就是s2+s1,如果s是循环字串，也就是s1=s2,所以str中间的s2+s1就和原字符串相等。
如果s不是循环字串，s1!=s2，那么s1+s2是不等于s2+s1的，也就是str中间不包含s
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)