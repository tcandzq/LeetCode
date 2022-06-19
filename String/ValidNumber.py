# -*- coding: utf-8 -*-
# @File    : ValidNumber.py
# @Date    : 2022-06-19
# @Author  : tc
"""
65. 有效数字
有效数字（按顺序）可以分成以下几个部分：

一个 小数 或者 整数
（可选）一个 'e' 或 'E' ，后面跟着一个 整数
小数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
下述格式之一：
至少一位数字，后面跟着一个点 '.'
至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
一个点 '.' ，后面跟着至少一位数字
整数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
至少一位数字
部分有效数字列举如下：["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]

部分无效数字列举如下：["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。
示例 1：

输入：s = "0"
输出：true
示例 2：

输入：s = "e"
输出：false
示例 3：

输入：s = "."
输出：false


有限状态自动机解法，需要先定义要状态转移矩阵
"""
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #define a DFA
        state = [{},
                {'blank': 1, 'sign': 2, 'digit':3, '.':4},
                {'digit':3, '.':4},
                {'digit':3, '.':5, 'e':6, 'blank':9},
                {'digit':5},
                {'digit':5, 'e':6, 'blank':9},
                {'sign':7, 'digit':8},
                {'digit':8},
                {'digit':8, 'blank':9},
                {'blank':9}]
        currentState = 1
        for c in s:
            c = c.lower()
            if c >= '0' and c <= '9':
                c = 'digit'
            if c == ' ':
                c = 'blank'
            if c in ['+', '-']:
                c = 'sign'
            if c not in state[currentState].keys():
                return False
            currentState = state[currentState][c]
        if currentState not in [3,5,8,9]:
            return False
        return True