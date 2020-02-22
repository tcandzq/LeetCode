# -*- coding: utf-8 -*-
# @File    : ReconstructOriginalDigitsFromEnglish.py
# @Date    : 2020-02-22
# @Author  : tc
"""
题号 423 从英文中重建数字
给定一个非空字符串，其中包含字母顺序打乱的英文单词表示的数字0-9。按升序输出原始的数字。

注意:

输入只包含小写英文字母。
输入保证合法并可以转换为原始的数字，这意味着像 "abc" 或 "zerone" 的输入是不允许的。
输入字符串的长度小于 50,000。
示例 1:

输入: "owoztneoer"

输出: "012" (zeroonetwo)
示例 2:

输入: "fviefuro"

输出: "45" (fourfive)

参考：https://leetcode.com/problems/reconstruct-original-digits-from-english/discuss/91191/Python-solution-that-beats-100...

"""
class Solution:
    def originalDigits(self, s: str) -> str:
        res = ""
        res += "0" * s.count('z')  # zero
        res += "1" * (s.count('o') - s.count('z') - s.count('w') - s.count('u'))
        res += "2" * s.count('w')  # two
        res += "3" * (s.count('h') - s.count('g'))
        res += "4" * s.count('u')  # four
        res += "5" * (s.count('f') - s.count('u'))
        res += "6" * s.count('x')  # six
        res += "7" * (s.count('s') - s.count('x'))
        res += "8" * s.count("g")  # eight
        res += "9" * (s.count('i') - s.count('x') - s.count("g") - s.count('f') + s.count('u'))
        return res

if __name__ == '__main__':
    s = "owoztneoer"
    solution = Solution()
    print(solution.originalDigits(s))