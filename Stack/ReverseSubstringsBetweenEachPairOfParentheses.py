# -*- coding: utf-8 -*-
# @File    : ReverseSubstringsBetweenEachPairOfParentheses.py
# @Date    : 2020-02-25
# @Author  : tc
"""
题号 1190. 反转每对括号间的子串
给出一个字符串 s（仅含有小写英文字母和括号）。

请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。

注意，您的结果中 不应 包含任何括号。



示例 1：

输入：s = "(abcd)"
输出："dcba"
示例 2：

输入：s = "(u(love)i)"
输出："iloveu"
示例 3：

输入：s = "(ed(et(oc))el)"
输出："leetcode"
示例 4：

输入：s = "a(bcdefghijkl(mno)p)q"
输出："apmnolkjihgfedcbq"
"""
class Solution:
    def reverseParentheses(self, s: str) -> str:
        s = list(s)
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
                s[i] = ''
            if s[i] == ')' and stack:
                s[i] = ''
                start = stack.pop()
                s[start:i] = s[start:i][::-1]
        return ''.join(s)

if __name__ == '__main__':
    s = "(ed(et(oc))el)"
    solution = Solution()
    print(solution.reverseParentheses(s))