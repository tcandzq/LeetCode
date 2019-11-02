#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/2 23:23
# @Author  : tc
# @File    : RemoveInvalidParentheses.py
"""
题号 301 删除无效的括号

删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。

说明: 输入可能包含了除 ( 和 ) 以外的字符。

示例 1:

输入: "()())()"
输出: ["()()()", "(())()"]
示例 2:

输入: "(a)())()"
输出: ["(a)()()", "(a())()"]
示例 3:

输入: ")("
输出: [""]


这是dfs除了在树遍历中的其他应用，要好好看。毫无思路
1.定义一个括号是否合法的函数(可以用栈实现);
2.

"""
from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # 找字符串最长有效括号的长度
        def longestVaildParentheses(s: str):
            res = 0
            stack = []
            for a in s:
                if a == "(":
                    stack.append("(")
                elif a == ")":
                    if stack:
                        res += 2
                        stack.pop()
            return res

        def helper(s, left_p, right_p, open, tmp):
            # 当都小于0 都不满足条件
            if left_p < 0 or right_p < 0 or open < 0:
                return
            # s剩余的括号都不够组成的
            if s.count("(") < left_p or s.count(")") < right_p:
                return
            if not s:
                # 输出
                if left_p == 0 and right_p == 0 and open == 0:
                    res.add(tmp)
                return
            if s[0] == "(":
                # 用 "("
                helper(s[1:], left_p - 1, right_p, open + 1, tmp + "(")
                # 不用 "("
                helper(s[1:], left_p, right_p, open, tmp)
            elif s[0] == ")":
                # 用 ")"
                helper(s[1:], left_p, right_p - 1, open - 1, tmp + ")")
                # 不用 ")"
                helper(s[1:], left_p, right_p, open, tmp)
            else:
                helper(s[1:], left_p, right_p, open, tmp + s[0])

        l = longestVaildParentheses(s)
        res = set()
        # 因为l是最长的, 所以左括号和右括号各一半, 再用open表示左右括号抵消多少
        helper(s, l // 2, l // 2, 0, "")
        return list(res)



if __name__ == '__main__':
    s = "()())()"
    solution = Solution()
    print(solution.removeInvalidParentheses(s))