# -*- coding: utf-8 -*-
# @File    : StickersToSpellWord.py
# @Date    : 2020-10-09
# @Author  : tc
"""
题号 691. 贴纸拼词
我们给出了 N 种不同类型的贴纸。每个贴纸上都有一个小写的英文单词。

你希望从自己的贴纸集合中裁剪单个字母并重新排列它们，从而拼写出给定的目标字符串 target。

如果你愿意的话，你可以不止一次地使用每一张贴纸，而且每一张贴纸的数量都是无限的。

拼出目标 target 所需的最小贴纸数量是多少？如果任务不可能，则返回 -1。

示例 1：

输入：

["with", "example", "science"], "thehat"
输出：

3
解释：

我们可以使用 2 个 "with" 贴纸，和 1 个 "example" 贴纸。
把贴纸上的字母剪下来并重新排列后，就可以形成目标 “thehat“ 了。
此外，这是形成目标字符串所需的最小贴纸数量。
示例 2：

输入：

["notice", "possible"], "basicbasic"
输出：

-1
解释：

我们不能通过剪切给定贴纸的字母来形成目标“basicbasic”。


提示：

stickers 长度范围是 [1, 50]。
stickers 由小写英文单词组成（不带撇号）。
target 的长度在 [1, 15] 范围内，由小写字母组成。
在所有的测试案例中，所有的单词都是从 1000 个最常见的美国英语单词中随机选取的，目标是两个随机单词的串联。
时间限制可能比平时更具挑战性。预计 50 个贴纸的测试案例平均可在35ms内解决。

参考：https://leetcode.com/problems/stickers-to-spell-word/discuss/108318/C%2B%2BJavaPython-DP-%2B-Memoization-with-optimization-29-ms-(C%2B%2B)

"""
from typing import List
import sys

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        m = len(stickers)
        mp = [[0] * 26 for y in range(m)]
        for i in range(m):
            for c in stickers[i]:
                mp[i][ord(c) - ord('a')] += 1
        dp = {}
        dp[""] = 0

        def helper(dp, mp, target):
            if target in dp:
                return dp[target]
            n = len(mp)
            tar = [0] * 26
            for c in target:
                tar[ord(c) - ord('a')] += 1
            ans = sys.maxsize
            for i in range(n):
                if mp[i][ord(target[0]) - ord('a')] == 0:
                    continue
                s = ''
                for j in range(26):
                    if tar[j] > mp[i][j]:
                        s += chr(ord('a') + j) * (tar[j] - mp[i][j])
                tmp = helper(dp, mp, s)
                if (tmp != -1):
                    ans = min(ans, 1 + tmp)
            dp[target] = -1 if ans == sys.maxsize else ans
            return dp[target]

        return helper(dp, mp, target)


if __name__ == '__main__':
    pass