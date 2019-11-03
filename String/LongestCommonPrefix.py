#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 17:12
# @Author  : tc
# @File    : LongestCommonPrefix.py
"""
题号 14 最长公共前缀

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。


可以用字典树解决

"""
from typing import List

class Solution:
    # 暴力解法
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        min_str = min(strs)
        common_prefix = ''
        for i in range(len(min_str)):
            for _str in strs:
                if _str[i] != min_str[i]:
                    return common_prefix
            common_prefix += min_str[i]

        return common_prefix



if __name__ == '__main__':
    strs = ["dog","racecar","car"]
    solution = Solution()
    print(solution.longestCommonPrefix(strs))