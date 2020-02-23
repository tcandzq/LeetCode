# -*- coding: utf-8 -*-
# @File    : ReverseVowelsOfAString.py
# @Date    : 2020-02-23
# @Author  : tc
"""
345 反转字符串中的元音字母
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"
说明:
元音字母不包含字母"y"。

"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a','e','i','o','u']


if __name__ == '__main__':
    s = "leetcode"
    solution = Solution()
    print(solution.reverseVowels(s))