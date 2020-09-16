# -*- coding: utf-8 -*-
# @File    : DistinctSubsequencesII.py
# @Date    : 2020-09-16
# @Author  : tc
"""
题号 940. 不同的子序列II
给定一个字符串 S，计算 S 的不同非空子序列的个数。

因为结果可能很大，所以返回答案模 10^9 + 7.

示例 1：

输入："abc"
输出：7
解释：7 个不同的子序列分别是 "a", "b", "c", "ab", "ac", "bc", 以及 "abc"。
示例 2：

输入："aba"
输出：6
解释：6 个不同的子序列分别是 "a", "b", "ab", "ba", "aa" 以及 "aba"。
示例 3：

输入："aaa"
输出：3
解释：3 个不同的子序列分别是 "a", "aa" 以及 "aaa"。

提示：

S 只包含小写字母。
1 <= S.length <= 2000

参考：https://leetcode.com/problems/distinct-subsequences-ii/discuss/192017/C%2B%2BJavaPython-4-lines-O(N)-Time-O(1)-Space

"""
import collections

class Solution:
    def distinctSubseqII(self, S: str) -> int:
        res, end = 0, collections.Counter()
        for c in S:
            res, end[c] = res * 2 + 1 - end[c], res + 1
        return res % (10 ** 9 + 7)


if __name__ == '__main__':
    pass