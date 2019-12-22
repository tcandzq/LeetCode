# -*- coding: utf-8 -*-
# @File    : AddBinary.py
# @Date    : 2019-12-22
# @Author  : tc
"""
题号 67 二进制求和
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"

"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2)).replace('0b','')


if __name__ == '__main__':
    a = "11"
    b = "1"
    solution = Solution()
    print(solution.addBinary(a,b))
    print(int("100111",base=2))
