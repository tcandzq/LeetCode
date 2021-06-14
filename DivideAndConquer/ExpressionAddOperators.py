# -*- coding: utf-8 -*-
# @File    : ExpressionAddOperators.py
# @Date    : 2021-06-09
# @Author  : tc
"""
题号:282. 给表达式添加运算符
给定一个仅包含数字 0-9 的字符串和一个目标值，在数字之间添加 二元 运算符（不是一元）+、- 或 * ，返回所有能够得到目标值的表达式。
示例 1:

输入: num = "123", target = 6
输出: ["1+2+3", "1*2*3"]
示例 2:

输入: num = "232", target = 8
输出: ["2*3+2", "2+3*2"]
示例 3:

输入: num = "105", target = 5
输出: ["1*0+5","10-5"]
示例 4:

输入: num = "00", target = 0
输出: ["0+0", "0-0", "0*0"]
示例 5:

输入: num = "3456237490", target = 9191
输出: []

链接：https://leetcode-cn.com/problems/expression-add-operators

dfs() parameters:
num: remaining num string
temp: temporally string with operators added
cur: current result of "temp" string
last: last multiply-level number in "temp". if next operator is "multiply", "cur" and "last" will be updated
res: result to return

参考：https://leetcode.com/problems/expression-add-operators/discuss/71968/Clean-Python-DFS-with-comments

"""
from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res, self.target = [], target
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != "0"):
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res)
        return res

    def dfs(self, num, temp, cur, last, res):
        if not num:
            if cur == self.target:
                res.append(temp)
            return
        for i in range(1, len(num) + 1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != "0"):
                self.dfs(num[i:], temp + "+" + val, cur+int(val), int(val), res)
                self.dfs(num[i:], temp + "-" + val, cur - int(val), -int(val), res)
                self.dfs(num[i:], temp + "*" + val, cur - last + last * int(val), last * int(val), res)

if __name__ == '__main__':
    num = "105"
    target = 5
    solution = Solution()
    print(solution.addOperators(num, target))