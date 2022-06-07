# -*- coding: utf-8 -*-
# @File    : SimilarStringGroups.py
# @Date    : 2022-06-08
# @Author  : tc
"""
839. 相似字符串组
如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。
例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)； "rats" 和 "arts" 也是相似的，但是 "star" 不与 "tars"，"rats"，或 "arts" 相似。
总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。注意，"tars" 和 "arts" 是在同一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。
给你一个字符串列表 strs。列表中的每个字符串都是 strs 中其它所有字符串的一个字母异位词。请问 strs 中有多少个相似字符串组？
示例 1：

输入：strs = ["tars","rats","arts","star"]
输出：2
示例 2：

输入：strs = ["omv","ovm"]
输出：1

提示：

1 <= strs.length <= 300
1 <= strs[i].length <= 300
strs[i] 只包含小写字母。
strs 中的所有单词都具有相同的长度，且是彼此的字母异位词。

将每一个字符串看成是图中的一个节点，如果两个字符串是相似的，那么对应这两个节点就是连通的。
"""
from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        N = len(strs)
        dsu = DSU(N)
        for i in range(N):
            for j in range(i + 1, N):
                if self.isSimilar(strs[i], strs[j]):
                    dsu.union(i, j)
        return dsu.regions()

    def isSimilar(self, str1, str2):
        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
        return count == 2 or count == 0


class DSU:
    def __init__(self, N):
        self.par_ = [i for i in range(N)]
        self.region_ = N

    def find(self, x):
        # if x != self.par_[x]:
        #     x = self.find(self.par_[x])
        # return self.par_[x]
        while x != self.par_[x]:
            x = self.par_[x]
        return self.par_[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        self.par_[px] = py
        self.region_ -= 1

    def regions(self):
        return self.region_