# -*- coding: utf-8 -*-
# @File    : FindTheClosestPalindrome.py
# @Date    : 2022-06-19
# @Author  : tc
"""
564. 寻找最近的回文数
给定一个表示整数的字符串 n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。
“最近的”定义为两个整数差的绝对值最小。
示例 1:

输入: n = "123"
输出: "121"
示例 2:

输入: n = "1"
输出: "0"
解释: 0 和 2是最近的回文，但我们返回最小的，也就是 0。

贪心解法：

例如对于 abcde来说，最近的回文数值的前三位可能是 abc、abc+1和 abc-1三者之一，
其他位置的数值随着前三位的确定而唯一确定。

1.用原数的前半部分替换后半部分得到的回文整数。

2.用原数的前半部分加一后的结果替换后半部分得到的回文整数。

3.用原数的前半部分减一后的结果替换后半部分得到的回文整数。

为防止位数变化导致构造的回文整数错误，因此直接构造999…999 和 100…001 作为备选答案。
"""

class Solution:
    def nearestPalindromic(self, S: str) -> str:
        K = len(S)
        candidates = [str(10 ** k + d) for k in (K - 1, K) for d in (-1, 1)]
        prefix = S[:(K + 1) // 2]
        P = int(prefix)
        for start in map(str, (P - 1, P, P + 1)):
            candidates.append(start + (start[:-1] if K % 2 else start)[::-1])

        def delta(x):
            return abs(int(S) - int(x))

        ans = None
        for cand in candidates:
            if cand != S and not cand.startswith('00'):
                if (ans is None or delta(cand) < delta(ans) or
                        delta(cand) == delta(ans) and int(cand) < int(ans)):
                    ans = cand
        return ans