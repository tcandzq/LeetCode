# -*- coding: utf-8 -*-
# @File    : KSimilarStrings.py
# @Date    : 2022-08-21
# @Author  : tc
"""
854. 相似度为 K 的字符串
字符串 s1 和 s2 是 k 相似 的(对于某些非负整数 k )，如果我们可以交换 s1 中两个字母的位置正好 k 次，使结果字符串等于 s2 。
给定两个字谜游戏 s1 和 s2 ，返回 s1 和 s2 与 k 相似 的最小 k 。


示例 1：
输入：s1 = "ab", s2 = "ba"
输出：1

示例 2：
输入：s1 = "abc", s2 = "bca"
输出：2

广度优先搜索

我们可以每次截断从左到右第一个A[i] != B[i]对应的那条边。
即在字符串A和 B中，我们每次找到最左侧满足A[i] != B[i]的i，
并搜索满足 j > i 且 A[j] == B[i]的 j。


代码和思路来自:https://leetcode.cn/problems/k-similar-strings/solution/xiang-si-du-wei-k-de-zi-fu-chuan-by-leetcode/
"""
import collections

class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        def neighbors(S):
            # 找到最左侧满足A[i] != B[i]的字符
            for i, c in enumerate(S):
                if c != B[i]:
                    break

            T = list(S)
            # 搜索i右侧第一个满足S[j] == B[i]的字符
            for j in range(i+1, len(S)):
                if S[j] == B[i]:
                    # 交换两个字符
                    T[i], T[j] = T[j], T[i]
                    yield "".join(T)
                    # 然后恢复
                    T[j], T[i] = T[i], T[j]

        queue = collections.deque([A])
        # 记录已经访问过的状态
        seen = {A: 0}
        while queue:
            S = queue.popleft()
            if S == B: return seen[S]
            for T in neighbors(S):
                print(T)
                if T not in seen:
                    seen[T] = seen[S] + 1
                    queue.append(T)