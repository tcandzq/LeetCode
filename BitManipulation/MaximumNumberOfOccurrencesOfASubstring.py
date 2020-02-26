# -*- coding: utf-8 -*-
# @File    : MaximumNumberOfOccurrencesOfASubstring.py
# @Date    : 2020-02-25
# @Author  : tc
"""
题号 1297. 子串的最大出现次数
给你一个字符串 s ，请你返回满足以下条件且出现次数最大的任意子串的出现次数：

子串中不同字母的数目必须小于等于 maxLetters 。
子串的长度必须大于等于 minSize 且小于等于 maxSize 。


示例 1：

输入：s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
输出：2
解释：子串 "aab" 在原字符串中出现了 2 次。
它满足所有的要求：2 个不同的字母，长度为 3 （在 minSize 和 maxSize 范围内）。
示例 2：

输入：s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
输出：2
解释：子串 "aaa" 在原字符串中出现了 2 次，且它们有重叠部分。
示例 3：

输入：s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
输出：3
示例 4：

输入：s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
输出：0

思路：最有效的是minSize，如果在长字符串取得了最大值，那么最短字符串出现的次数>=长字符串出现次数

假设我们子字符串的长度范围为 [2,4]，并且允许的最大不同字符数为 4，那么所有满足需求的长度为 4 的子字符串，
它的每一次重复里一定至少包含一次长度为 2 的子字符串。例如对于字符串 "abcdefghabcd"，其中 "abcd" 重复了两次，那么至少 "ab" 也重复了两次

由于我们是为了求得最大的子字符串出现的次数，所以根据上面发现的事情，我们不难得到其实我们只需要去找出满足条件要求的最短的子字符串，然后完成计数即可。因为比它更长的子字符串的出现次数一定是小于或者等于它的。

参考：https://leetcode-cn.com/problems/maximum-number-of-occurrences-of-a-substring/solution/bao-bao-ye-neng-kan-dong-de-leetcode-ti-jie-wei-ca/

"""
import collections

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counts = dict()
        for j in range(len(s)-minSize+1):
            word = s[j:j+minSize]
            if word in counts:
                counts[word] += 1
            else:
                if len(collections.Counter(word)) <= maxLetters:
                    counts[word] = 1
        return max(counts.values()) if len(counts) != 0 else 0

if __name__ == '__main__':
    s = "aaaaaa"
    s.count('aaa')
    maxLetters = 1
    minSize = 3
    maxSize = 3
    solution = Solution()
    print(solution.maxFreq(s,maxLetters,minSize,maxSize))