# -*- coding: utf-8 -*-
# @File    : InterleavingString.py
# @Date    : 2021-07-03
# @Author  : tc
"""
题号 97. 交错字符串
给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
提示：a + b 意味着字符串 a 和 b 连接。
示例 1：
输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true
示例 2：

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false
示例 3：

输入：s1 = "", s2 = "", s3 = ""
输出：true

不知道大家对不同路径的题还有没有印象，本题也可以利用其思想求解：
target 的每个字符都是从 s1（向下）或者 s2（向右）拿到的，所以只要判断是否存在这条 target 路径即可；

思路参考：https://leetcode-cn.com/problems/interleaving-string/solution/lei-si-lu-jing-wen-ti-zhao-zhun-zhuang-tai-fang-ch/

代码参考：https://leetcode-cn.com/problems/interleaving-string/solution/dong-tai-gui-hua-zhu-xing-jie-shi-python3-by-zhu-3/

"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if len1 + len2 != len3:
            return False
        dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]
        dp[0][0] = True
        for i in range(1, len1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for i in range(1, len2 + 1):
            dp[0][i] = dp[0][i - 1] and s2[i - 1] == s3[i - 1]

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                dp[i][j] = (dp[i - 1][j] and s3[i + j - 1] == s1[i - 1]) or (
                            dp[i][j - 1] and s3[i + j - 1] == s2[j - 1])
        return dp[-1][-1]