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

中心扩展法:因为要求的是回文子串,所以一个字符串从0,1,2,3,4...n位都要判断,而中心扩展法受限于字符串长度的奇偶性需要分开求解,比如奇数从
一点扩展,只能得到长度为1,3,5...等奇数长度子串的回文的数量;偶数从两点扩展,只能得到长度为2,4,6..等偶数长度子串的回文的数量。只有把奇数和偶数的结果全部加起来,才算一个完整的结果

"""
# 暴力法会超时
def countSubstrings(s: str) -> int:
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if helper(s[i:j+1]):
                count += 1
    return count

def helper(s):
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

#  动态规划求解


# 中心扩展法求解
def countSubstrings2(s):
    result = 0
    for i in range(len(s)):
        result += helper2(s,i,i)  # 奇数的中心扩展
        result += helper2(s,i,i+1)  # 偶数的中心扩展
    return result

def helper2(s,start,end):
    count = 0
    while start >= 0 and end <= len(s) - 1 and s[start] == s[end]:
        count += 1
        start -= 1
        end += 1
    return count


if __name__ == '__main__':
    print(countSubstrings2('aba'))
