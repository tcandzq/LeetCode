# -*- coding: utf-8 -*-
# @File    : ExcelSheetColumnTitle.py
# @Date    : 2021-07-05
# @Author  : tc
"""
168. Excel表列名称
给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。

例如：

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

示例 1：

输入：columnNumber = 1
输出："A"
示例 2：

输入：columnNumber = 28
输出："AB"
示例 3：

输入：columnNumber = 701
输出："ZY"
示例 4：

输入：columnNumber = 2147483647
输出："FXSHRXW"

问题实际是10进制转26进制

参考：https://leetcode.com/problems/excel-sheet-column-title/discuss/51404/Python-solution-with-explanation

"""
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        result = []
        while columnNumber > 0:
            result.append(capitals[(columnNumber - 1) % 26])
            columnNumber = (columnNumber - 1) // 26
        result.reverse()
        return "".join(result)