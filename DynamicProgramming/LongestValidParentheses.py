#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 21:45
# @Author  : tc
# @File    : LongestValidParentheses.py
"""
题号 32 最长有效括号
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

和LeetCode20题 有效的括号很相似，用DP解决。

注意仔细看题 其实题目暗含了另外一个要求，最长有效括号子串一定是连续的，而不是让你求有效括号的数量。比如：
输入："()(()"
输出：2

参考:https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-powcai/

dp[i]表示以以s[i]结尾的字符串的最长有效括号长度(这里是说s[i]必须是最长有效括号的末尾)，则在s[i]等于'('或者')'下的情况进行讨论。

"""
class Solution:

    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        size = len(s)
        dp = [0] * size
        for i in range(1,size):
            if s[i] == '(':
                dp[i] = 0
            elif s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ')':
                    if s[i - dp[i-1] - 1] == '(' and i - dp[i-1] - 1 >= 0:
                        dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]

        return max(dp)


if __name__ == '__main__':
    s = ")()())"
    solution = Solution()
    print(solution.longestValidParentheses(s))