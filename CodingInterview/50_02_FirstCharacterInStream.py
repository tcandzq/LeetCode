# -*- coding: utf-8 -*-
# @File    : 50_02_FirstCharacterInStream.py
# @Date    : 2020-05-10
# @Author  : tc
"""
面试题50. 第一个只出现一次的字符
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。

示例:

s = "abaccdeff"
返回 "b"

s = ""
返回 " "


限制：

0 <= s 的长度 <= 50000

参考：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/solution/mian-shi-ti-50-di-yi-ge-zhi-chu-xian-yi-ci-de-zi-3/

"""


class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for k,v in dic.items(): # 注意：字典默认有序
            if v:
                return k
        return ' '

if __name__ == '__main__':
    s = "abaccdeff"
    solution = Solution()
    print(solution.firstUniqChar(s))


