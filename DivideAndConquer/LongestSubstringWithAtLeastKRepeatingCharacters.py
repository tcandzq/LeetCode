# -*- coding: utf-8 -*-
# @File    : LongestSubstringWithAtLeastKRepeatingCharacters.py
# @Date    : 2020-02-23
# @Author  : tc
"""
题号 395. 至少有K个重复字符的最长子串
找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。

示例 1:

输入:
s = "aaabb", k = 3

输出:
3

最长子串为 "aaa" ，其中 'a' 重复了 3 次。
示例 2:

输入:
s = "ababbc", k = 2

输出:
5

最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。

分治法，牛逼

https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/87768/4-lines-Python

"""
class Solution:
    # 超时
    def longestSubstring(self, s: str, k: int) -> int:
        max_len = 0
        n = len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                if s[i:j].count((min(s[i:j],key=s.count))) >= k and (j - i) > max_len:
                    max_len = j - i
                    print(j,i)
        return max_len

    # 分治法
    def longestSubstring2(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring2(t,k) for t in s.split(c))
        return len(s)  # 此时返回，表明没有进入if条件，即s中的所有字符的频率都至少为k

if __name__ == '__main__':
    s = "aaabb"
    k = 3
    solution = Solution()
    print(solution.longestSubstring(s,k))
