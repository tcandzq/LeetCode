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

解法2和leetcode40题 组合总和II的解法很像

"""
from typing import List

class Solution:
    #  解法1 没看懂
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

    # 解法2
    def removeInvalidParentheses2(self, s: str) -> List[str]:
        res = []

        left = 0
        right = 0

        for char in s:  # 统计不合法的左括号和右括号的数量
            if char == '(':
                left += 1
            if char == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        def check(s: str) -> bool:  # 检验括号是否有效
            cnt = 0
            for char in s:
                if char == '(':
                    cnt += 1
                if char == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        def dfs(s, st, left, right):
            if left == 0 and right == 0:
                if check(s):  # 如果左边和右边非法的括号已经删除结束，且剩下的字符串s是有效的
                    res.append(s)
                return

            for i in range(st, len(s)):
                if i - 1 >= st and s[i] == s[i - 1]:
                    continue

                if left > 0 and s[i] == '(':
                    dfs(s[0:i]+s[i+1:i+1 + len(s) - i - 1], i, left - 1,right)

                if right > 0 and s[i] == ')':
                    dfs(s[0:i]+s[i+1:i+1 + len(s) - i - 1], i, left, right - 1)

        dfs(s,0,left,right)
        return res
if __name__ == '__main__':
    s = "()())()"
    solution = Solution()
    print(solution.removeInvalidParentheses2(s))