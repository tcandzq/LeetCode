#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/24 18:55
# @Author  : tc
# @File    : ImplementStrstr.py
"""
题号 28 实现 strStr()

实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

实际就是KMP算法的实现

非常通俗易懂的KMP算法讲解:https://www.zhihu.com/question/21923021/answer/281346746


"""
class Solution:


    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        _next = [0] * len(needle)

        def get_next(p, _next):  # 得到模式串的next数组
            _next[0] = -1
            i = 0
            j = -1
            while i < len(p) - 1:
                if j == -1 or p[i] == p[j]:
                    i += 1
                    j += 1
                    _next[i] = j
                else:
                    j = _next[j]

        get_next(needle, _next)
        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1 # 主串的指针保持一直向后移
                j += 1
            else:
                j = _next[j]
        if j == len(needle):
            return i - j
        return -1


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    solution = Solution()
    print(solution.strStr(haystack,needle))