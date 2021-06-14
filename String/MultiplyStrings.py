# -*- coding: utf-8 -*-
# @File    : MultiplyStrings.py
# @Date    : 2021-06-14
# @Author  : tc
"""
题号 43. 字符串相乘
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

注意：
要额外处理：
1.乘数中有一个为"0"的情况，如;
2.第一个字符为"0"的情况，如"2" * "3" = "6"。

参考1：https://leetcode-cn.com/problems/multiply-strings/solution/you-hua-ban-shu-shi-da-bai-994-by-breezean/
参考2:https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m = len(num1)
        n = len(num2)

        pos = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                _sum = mul + pos[p2]

                pos[p1] += _sum / 10
                pos[p2] = _sum % 10
        res = []
        for i in range(len(pos)):
            if i == 0 and pos[i] == '0':
                continue
            res.append(pos[i])
        return ''.join(map(str, res))