#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 22:26
# @Author  : tc
# @File    : PalindromePartitioning.py
"""
题号 131 分割回文串
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

参考:https://leetcode-cn.com/problems/palindrome-partitioning/solution/dong-tai-gui-hua-dfs-by-powcai/

这种回溯解法还是转化为树问题来求解

"""
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def helper(s, tmp):
            if not s:
                res.append(tmp)
            for i in range(1, len(s) + 1):  # 对"aba"的每个字符做切分,比如切分成:[['a','ab'],['a','b','a'],['ab','a']]
                if s[:i] == s[:i][::-1]:  # 如果是回文串
                    helper(s[i:], tmp + [s[:i]])

        helper(s, [])
        return res


if __name__ == '__main__':
    s = "aab"
    solution = Solution()
    print(solution.partition(s))