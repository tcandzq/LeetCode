#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 21:26
# @Author  : tc
# @File    : ReverseWordsInAStringIII.py
"""
题号 557 反转字符串中的单词 III
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

简洁版参考:https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/solution/python-1xing-by-knifezhu-2/

"""
class Solution:
    #  冗余版代码
    def reverseWords(self, s: str) -> str:
        res = []
        for s in s.split(' '):
            res.append(s[::-1])
        return ' '.join(res)

    # 简洁版
    def reverseWords2(self, s: str) -> str:
        return ' '.join(s.split(' ')[::-1])[::-1]




if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    solution = Solution()
    print(solution.reverseWords(s))