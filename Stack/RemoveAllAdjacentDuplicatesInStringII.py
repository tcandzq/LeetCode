# -*- coding: utf-8 -*-
# @File    : RemoveAllAdjacentDuplicatesInStringII.py
# @Date    : 2020-03-13
# @Author  : tc
"""
题号 1209. 删除字符串中的所有相邻重复项II
给你一个字符串 s，「k 倍重复项删除操作」将会从 s 中选择 k 个相邻且相等的字母，并删除它们，使被删去的字符串的左侧和右侧连在一起。

你需要对 s 重复进行无限次这样的删除操作，直到无法继续为止。

在执行完所有删除操作后，返回最终得到的字符串。

本题答案保证唯一。

示例 1：

输入：s = "abcd", k = 2
输出："abcd"
解释：没有要删除的内容。
示例 2：

输入：s = "deeedbbcccbdaa", k = 3
输出："aa"
解释：
先删除 "eee" 和 "ccc"，得到 "ddbbbdaa"
再删除 "bbb"，得到 "dddaa"
最后删除 "ddd"，得到 "aa"
示例 3：

输入：s = "pbbcggttciiippooaais", k = 2
输出："ps"


提示：

1 <= s.length <= 10^5
2 <= k <= 10^4
s 中只含有小写英文字母。

参考：https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string-ii/solution/zhan-python3-by-smoon1989/

"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])  # 使用pair对 更方便
            elif stack[-1][1] + 1 < k:
                stack[-1][1] += 1
            else:
                stack.pop()
        res = ""
        for c, count in stack:
            res += c * count
        return res