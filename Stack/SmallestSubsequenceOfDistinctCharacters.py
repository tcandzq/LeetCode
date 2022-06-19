# -*- coding: utf-8 -*-
# @File    : SmallestSubsequenceOfDistinctCharacters.py
# @Date    : 2022-06-20
# @Author  : tc
"""
1081. 不同字符的最小子序列
返回 s 字典序最小的子序列，该子序列包含 s 的所有不同字符，且只包含一次。

注意：该题与 316 https://leetcode.com/problems/remove-duplicate-letters/ 相同

示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"

用last_appear_index 存储字符串中字符最后一次出现的位置。
使用单调栈保证字典序最小，但前提是不能缺少唯一的字符，例如:addcbd，前面两个dd可以直接pop出去，因为后面还有一个d。

"""
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        n = len(s)
        last_appear_index = [0] * 26
        for i in range(n):
            last_appear_index[ord(s[i]) - 97] = i
        stack = []
        for i in range(n):
            if s[i] in stack:
                continue
            # 使用单调栈保证字符串的字典序最小，如果ord(stack[-1]) - 97 在后面还会出现，在这里可以直接pop掉
            while stack and ord(stack[-1]) > ord(s[i]) and last_appear_index[ord(stack[-1]) - 97] > i:
                stack.pop()
            stack.append(s[i])
        return ''.join(stack)