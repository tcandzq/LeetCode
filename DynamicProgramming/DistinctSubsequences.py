#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 18:23
# @Author  : tc
# @File    : DistinctSubsequences.py

"""
给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。
一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

Input1:S = "rabbbit", T = "rabbit"
Output1:3
如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)
rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^

Input1:S = "babgbag", T = "bag"
Output1:5
如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。
(上箭头符号 ^ 表示选取的字母)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^

我自己写不出来，具体参考1:https://leetcode-cn.com/problems/distinct-subsequences/solution/cong-bao-li-di-gui-dao-dong-tai-gui-hua-cong-dong-/
                  参考2:https://leetcode-cn.com/problems/distinct-subsequences/solution/dong-tai-gui-hua-si-yao-su-by-a380922457-2/
注意：1.数组不要越界 由于dp矩阵是行和列都扩充了一维，所以判断条件应该是A[i-1] == B[j-1]
     2.扩充一列的数值如何初始化
"""
def numDistinct(s,t):
    m = len(s)

    n = len(t)

    if m < n:
        return 0

    A = list(s)

    B = list(t)

    dp = [[0] * (m+1) for _ in range(n+1)]

    for j in range(m+1):
        dp[0][j] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i][j - 1]
            if A[j-1] == B[i-1]:
                dp[i][j] += dp[i - 1][j-1]
    return dp[-1][-1]


if __name__ == '__main__':
    s = "babgbag"

    t = "bag"

    print(numDistinct(s,t))


