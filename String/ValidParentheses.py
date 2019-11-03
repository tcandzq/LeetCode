#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 20:25
# @Author  : tc
# @File    : ValidParentheses.py
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

可以用栈解决
优雅版的代码请参考:https://leetcode-cn.com/problems/valid-parentheses/solution/valid-parentheses-fu-zhu-zhan-fa-by-jin407891080/

"""
class Solution:
    #  丑陋版
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        d = {'(': ')','[': ']','{': '}'}
        stack = []
        for string in s:
            if string in ['(','{','[']:
                stack.append(string)
            if string in [')','}',']']:
                if not stack:
                    return False
                if string == d[stack[-1]]:
                    stack.pop(-1)
                else:
                    return False
        return False if stack else True

    # 优雅版
    def isValid2(self,  s: str) -> bool:
        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1


if __name__ == '__main__':
    s = "(])"
    solution = Solution()
    print(solution.isValid2(s))