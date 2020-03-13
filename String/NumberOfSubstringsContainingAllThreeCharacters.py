# -*- coding: utf-8 -*-
# @File    : NumberOfSubstringsContainingAllThreeCharacters.py
# @Date    : 2020-03-12
# @Author  : tc
"""
题号 1358. 包含所有三种字符的子字符串数目
给你一个字符串 s ，它只包含三种字符 a, b 和 c 。

请你返回 a，b 和 c都至少出现过一次的子字符串数目。



示例 1：

输入：s = "abcabc"
输出：10
解释：包含 a，b 和 c 各至少一次的子字符串为 "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" 和 "abc" (相同字符串算多次)。
示例 2：

输入：s = "aaacb"
输出：3
解释：包含 a，b 和 c 各至少一次的子字符串为 "aaacb", "aacb" 和 "acb" 。
示例 3：

输入：s = "abc"
输出：1


提示：

3 <= s.length <= 5 x 10^4
s 只包含字符 a，b 和 c 。

参考：https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/discuss/516977/JavaC%2B%2BPython-Easy-and-Concise

"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = i = 0
        count = {c: 0 for c in 'abc'}
        for j in range(len(s)):
            count[s[j]] += 1
            while all(count.values()):
                count[s[i]] -= 1
                i += 1
            res += i
        return res


if __name__ == '__main__':
    s = "aaacb"
    solution = Solution()
    print(solution.numberOfSubstrings(s))

