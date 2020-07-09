# -*- coding: utf-8 -*-
# @File    : MinimumInsertionStepsToMakeAStringPalindrome.py
# @Date    : 2020-07-07
# @Author  : tc
"""
题号 1312. 让字符串成为回文串的最少插入次数
给你一个字符串 s ，每一次操作你都可以在字符串的任意位置插入任意字符。

请你返回让 s 成为回文串的 最少操作次数 。

「回文串」是正读和反读都相同的字符串。

示例 1：

输入：s = "zzazz"
输出：0
解释：字符串 "zzazz" 已经是回文串了，所以不需要做任何插入操作。
示例 2：

输入：s = "mbadm"
输出：2
解释：字符串可变为 "mbdadbm" 或者 "mdbabdm" 。
示例 3：

输入：s = "leetcode"
输出：5
解释：插入 5 个字符后字符串变为 "leetcodocteel" 。
示例 4：

输入：s = "g"
输出：0
示例 5：

输入：s = "no"
输出：1


提示：

1 <= s.length <= 500
s 中所有字符都是小写字母。

参考：https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/discuss/470706/JavaC%2B%2BPython-Longest-Common-Sequence

将问题转化为最长公共序列的长度：
(1)初始化dp[n+1][n+1]，其中dp[i][j]表示s1的第一个字母i与s2的第一个字母j之间的最长公共序列的长度
(2)计算s1和s2的最长公共序列，其中s1=s，s2=reversed(s)
(3)返回 n - dp[n][n]

"""

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i][j] + 1 if s[i] == s[~j] else max(dp[i][j + 1], dp[i + 1][j])
        return n - dp[n][n]


if __name__ == '__main__':
    s = "leetcode"
    solution = Solution()
    print(solution.minInsertions(s))
    print(~0)