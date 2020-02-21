# -*- coding: utf-8 -*-
# @File    : ShortestPalindrome.py
# @Date    : 2020-02-20
# @Author  : tc
"""
题号 214 最短回文串
给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

示例 1:

输入: "aacecaaa"
输出: "aaacecaaa"
示例 2:

输入: "abcd"
输出: "dcbabcd"

代码参考：https://leetcode.com/problems/shortest-palindrome/solution/

思路参考：https://leetcode-cn.com/problems/shortest-palindrome/solution/c-li-yong-kmpsuan-fa-xiang-xi-tui-dao-zhuan-hua-gu/

"""
from typing import List

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        if not n:
            return ''
        rs = s[::-1]
        i = 0
        while True:
            if rs[i:] == s[:n-i]:
                break
            i += 1
        return rs[:i]+s

    # KMP算法
    def shortestPalindrome2(self, s: str) -> str:
        n = len(s)
        rev = s[::-1]
        s_new = s + "#" + rev
        n_new = len(s_new)
        f = [0] * n_new
        for i in range(1,n_new):
            t = f[i - 1]
            while t > 0 and s_new[i] != s_new[t]:
                t = f[t - 1]
            if s_new[i] == s_new[t]:
                t += 1
            f[i] = t
        return rev[:n-f[n_new - 1]] + s

if __name__ == '__main__':
    s = "aacecaaa"
    solution = Solution()
    print(solution.shortestPalindrome2(s))