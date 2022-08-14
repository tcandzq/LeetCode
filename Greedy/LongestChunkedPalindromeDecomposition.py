# -*- coding: utf-8 -*-
# @File    : LongestChunkedPalindromeDecomposition.py
# @Date    : 2022-08-14
# @Author  : tc
"""
1147. 段式回文
你会得到一个字符串 text 。你应该把它分成 k 个子字符串 (subtext1, subtext2，…， subtextk) ，要求满足:
subtexti 是非空字符串
所有子字符串的连接等于 text ( 即subtext1 + subtext2 + ... + subtextk == text )
subtexti == subtextk - i + 1 表示所有 i 的有效值( 即 1 <= i <= k )
返回k可能最大值。

示例 1：

输入：text = "ghiabcdefhelloadamhelloabcdefghi"
输出：7
解释：我们可以把字符串拆分成 "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)"。
示例 2：

输入：text = "merchant"
输出：1
解释：我们可以把字符串拆分成 "(merchant)"。
示例 3：

输入：text = "antaprezatepzapreanta"
输出：11
解释：我们可以把字符串拆分成 "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)"。

参考：https://leetcode.com/problems/longest-chunked-palindrome-decomposition/discuss/350560/JavaC%2B%2BPython-Easy-Greedy-with-Prove
"""
class Solution:
    def longestDecomposition(self, text: str) -> int:
        res, l, r = 0, "", ""
        for i, j in zip(text, text[::-1]):

            l, r = l + i, j + r
            if l == r:
                print(l, r)
                res, l, r = res + 1, "", ""
        return res