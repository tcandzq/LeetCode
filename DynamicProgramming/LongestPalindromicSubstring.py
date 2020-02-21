# -*- coding: utf-8 -*-
# @File    : LongestPalindromicSubstring.py
# @Date    : 2020-02-20
# @Author  : tc
"""
题号 5 最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

"""
class Solution:
    # 动态规划
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        dp = [[False] * (n) for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        max_len = 1  # 注意这要初始化为1，因为单个字符一定是回文串，比如"ac"
        start = 0
        for j in range(1,n):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    cur_len = j - i + 1  # 注意这里要加1，因为dp[i][j]是s[i:j]的状态，这是包括s[j]在内的
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start+max_len]

    # 中心扩展法
    def longestPalindrome2(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # 奇数情况 例如"aba"
            odd = self.helper(s,i,i)
            # 偶数情况，like "abba"
            even = self.helper(s,i,i+1)
            res = max(res,odd, even, key=len)
        return res

    # 从中心向两边扩散
    def helper(self,s,l,r):
        while 0 <= l and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

if __name__ == '__main__':
    s = "abcd"
    solution = Solution()
    print(solution.longestPalindrome2(s))
