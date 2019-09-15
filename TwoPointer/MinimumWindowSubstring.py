#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 23:05
# @Author  : tc
# @File    : MinimumWindowSubstring.py

"""
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
Input1:S = "ADOBECODEBANC", T = "ABC"
Output1:"BANC"
说明：
    如果 S 中不存这样的子串，则返回空字符串 ""。
    如果 S 中存在这样的子串，我们保证它是唯一的答案。

这是LeetCode76题

滑动窗口系列详解参考:https://leetcode-cn.com/problems/minimum-window-substring/solution/hua-dong-chuang-kou-suan-fa-tong-yong-si-xiang-by-/

滑动窗口的思想很简单,但最重要的是如何判断你的条件已经满足题目的要求了,这题用两个Hash表来解决问题。

python里面的字典是真的坑,注意set_default()并不是你想的那样,它竟然和get()方法类似,你敢信？

"""


def minWindow(s, t):
    window = {}
    need = {}
    start = 0
    end = 0
    left = 0
    match = 0
    min_len = float('inf')
    for char in t:
        if need.get(char):
            need[char] += 1
        else:
            need[char] = 1  # 初始化字符串t的字典
    while end < len(s):
        c1 = s[end]
        if need.get(c1):
            if window.get(c1):
                window[c1] += 1
            else:
                window[c1] = 1
            if window[c1] == need[c1]:
                match += 1  # 一个字符已经满足条件了
        end += 1  # 右边的指针逐步往后移动
        print(window)
        while match == len(need):  # 所有字符都已经满足条件了
            if end - start < min_len:
                left = start
                min_len = end - start  # 记住这里需要加一个中间变量left存一下每步最优的结果,如果直接用min(min_len,end-start)会得不到想要的结果,
                                       # 因为start是负责向左滑动的指针,它不一定是最终最优的结果,而中间变量left肯定是最优的结果,因为它在每次取最优结果的判断语句中。
            c2 = s[start]
            if need.get(c2):
                window[c2] -= 1
                if window[c2] < need[c2]:
                    match -= 1
            start += 1
    return s[left:left + min_len] if min_len != float('inf') else ''


if __name__ == '__main__':
    s = "ab"
    t = "a"
    print(minWindow(s, t))
