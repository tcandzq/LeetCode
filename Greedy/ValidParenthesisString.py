# -*- coding: utf-8 -*-
# @File    : ValidParenthesisString.py
# @Date    : 2021-06-28
# @Author  : tc
"""
题号 678. 有效的括号字符串
给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

任何左括号 ( 必须有相应的右括号 )。
任何右括号 ) 必须有相应的左括号 ( 。
左括号 ( 必须在对应的右括号之前 )。
* 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
一个空字符串也被视为有效字符串。
示例 1:

输入: "()"
输出: True
示例 2:

输入: "(*)"
输出: True
示例 3:

输入: "(*))"
输出: True

参考：https://leetcode.com/problems/valid-parenthesis-string/discuss/543521/Java-Count-Open-Parenthesis-O(n)-time-O(1)-space-Picture-Explain

使用cmin和cmax分别记录左括号的最少和最多的数量

"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = 0  # open parentheses count in range [cmin, cmax]
        cmax = 0
        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin -= 1
                cmax -= 1
            else:
                cmin -= 1  # if `*` become `)` then openCount--
                cmax += 1  # if `*` become `(` then openCount++
                # So openCount will be in new range [cmin-1, cmax+1]
            if cmax < 0:  # Currently, don't have enough open parentheses to match close parentheses-> Invalid
                # For example: ())(
                return False
            cmin = max(0, cmin)  # It's invalid if open parentheses count < 0 that's why cmin can't be negative
        return cmin == 0  # Return true if can found `openCount == 0` in range [cmin, cmax]