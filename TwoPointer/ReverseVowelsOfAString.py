# -*- coding: utf-8 -*-
# @File    : ReverseVowelsOfAString.py
# @Date    : 2020-02-23
# @Author  : tc
"""
题号 345 反转字符串中的元音字母
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"
说明:
元音字母不包含字母"y"。

参考：https://leetcode-cn.com/problems/reverse-vowels-of-a-string/solution/shuang-zhi-zhen-python-jie-fa-by-larger5/

"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}  # 使用字典更快
        i, j = 0,len(s) - 1
        s = list(s)
        while i < len(s) and j > 0 and j > i:
            while s[j] not in vowel and i < j:
                j -= 1
            while s[i] not in vowel and i < j:
                i += 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)


if __name__ == '__main__':
    s = "hello"
    solution = Solution()
    print(solution.reverseVowels(s))
