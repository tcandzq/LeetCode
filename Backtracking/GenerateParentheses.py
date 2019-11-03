#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 23:14
# @Author  : tc
# @File    : GenerateParentheses.py
"""
题号22 括号生成

给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

回溯算法又一经典应用
参考:https://leetcode-cn.com/problems/generate-parentheses/solution/hui-su-suan-fa-by-liweiwei1419/

"""
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if not n:
            return res
        self.dfs("",n,n,res)
        return res
    def dfs(self,cur_str,left,right,res):
        if left == 0 and right == 0:
            res.append(cur_str)

        if left > 0:
            self.dfs(cur_str + '(', left - 1, right,res)
        if right > 0 and left < right :
            self.dfs(cur_str + ')', left, right - 1, res)


if __name__ == '__main__':
    n = 3
    solution = Solution()
    print(solution.generateParenthesis(n))
