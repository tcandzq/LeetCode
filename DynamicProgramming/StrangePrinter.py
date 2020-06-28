# -*- coding: utf-8 -*-
# @File    : StrangePrinter.py
# @Date    : 2020-06-28
# @Author  : tc
"""
题号 664. 奇怪的打印机
有台奇怪的打印机有以下两个特殊要求：

打印机每次只能打印同一个字符序列。
每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。
给定一个只包含小写英文字母的字符串，你的任务是计算这个打印机打印它需要的最少次数。

示例 1:

输入: "aaabbb"
输出: 2
解释: 首先打印 "aaa" 然后打印 "bbb"。
示例 2:

输入: "aba"
输出: 2
解释: 首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。
提示: 输入字符串的长度不会超过 100。

思路参考：https://www.cnblogs.com/grandyang/p/8319913.html

代码参考：https://leetcode.com/problems/strange-printer/discuss/106795/Python-Straightforward-DP-with-Explanation

"""
class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}

        def dp(i, j):
            if i > j: return 0
            if (i, j) not in memo:
                ans = dp(i+1, j) + 1
                for k in range(i+1, j+1):
                    if s[k] == s[i]:
                        ans = min(ans, dp(i, k-1)+dp(k+1, j))
                memo[i, j] = ans
            return memo[i, j]

        return dp(0, len(s) - 1)

if __name__ == '__main__':
    s = "aba"
    solution = Solution()
    print(solution.strangePrinter(s))