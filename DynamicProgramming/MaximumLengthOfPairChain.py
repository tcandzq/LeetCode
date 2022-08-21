# -*- coding: utf-8 -*-
# @File    : MaximumLengthOfPairChain.py
# @Date    : 2022-08-21
# @Author  : tc
"""
646. 最长数对链
给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。
现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。
给定一个数对集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。


示例：
输入：[[1,2], [2,3], [3,4]]
输出：2
解释：最长的数对链是 [1,2] -> [3,4]

思路
在一个长度为 k，以 pairs[i]结尾的数对链中，如果 pairs[i][1] < pairs[j][0]，则将该数对加入链中，数对链长度变为 k+1。

算法
根据数对的第一个数排序所有的数对，dp[i] 存储以 pairs[i] 结尾的最长链的长度。
当 i < j 且 pairs[i][1] < pairs[j][0] 时，扩展数对链，更新 dp[j] = max(dp[j], dp[i] + 1)。

来自:https://leetcode.cn/problems/maximum-length-of-pair-chain/solution/zui-chang-shu-dui-lian-by-leetcode/
"""
from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[0])
        n = len(pairs)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[n - 1]