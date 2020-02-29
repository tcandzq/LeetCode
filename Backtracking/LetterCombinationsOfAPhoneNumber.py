# -*- coding: utf-8 -*-
# @File    : LetterCombinationsOfAPhoneNumber.py
# @Date    : 2020-02-29
# @Author  : tc
"""
题号 17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

经典的排列组合问题，参考：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/tong-su-yi-dong-dong-hua-yan-shi-17-dian-hua-hao-m/

"""
from typing import List
import string
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        res = []
        if not digits:
            return res

        def dfs(i, d, digits, temp):
            if len(temp) == len(digits):
                res.append(temp)
                return
            for c in d[digits[i]]:
                dfs(i+1,d,digits,temp+c)
        dfs(0,d,digits,'')
        return res


if __name__ == '__main__':
    digits = "234"
    solution = Solution()
    print(solution.letterCombinations(digits))