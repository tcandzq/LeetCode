# -*- coding: utf-8 -*-
# @File    : WordLadderII.py
# @Date    : 2020-02-22
# @Author  : tc
"""
题号 126. 单词接龙II
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

解法二的本质是，存储一棵树中根节点到每个节点的路径
参考：https://leetcode.com/problems/word-ladder-ii/discuss/40482/Python-simple-BFS-layer-by-layer

解法一参考：https://leetcode.com/problems/word-ladder-ii/discuss/40549/FAST-AND-CLEAN-PythonC%2B%2B-Solution-using-Double-BFS-beats-98

"""
from typing import List
import collections
import string

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []


        def construct_paths(source, dest, tree):
            if source == dest:
                return [[source]]
            return [[source] + path for succ in tree[source]
                    for path in construct_paths(succ, dest, tree)]

        def add_path(tree, word, neigh, is_forw):
            if is_forw:
                tree[word] += neigh,
            else:
                tree[neigh] += word,

        def bfs_level(this_lev, oth_lev, tree, is_forw, words_set):
            if not this_lev: return False
            if len(this_lev) > len(oth_lev):
                return bfs_level(oth_lev, this_lev, tree, not is_forw, words_set)
            for word in (this_lev | oth_lev):
                words_set.discard(word)
            next_lev, done = set(), False
            while this_lev:
                word = this_lev.pop()
                for c in string.ascii_lowercase:
                    for index in range(len(word)):
                        neigh = word[:index] + c + word[index + 1:]
                        if neigh in oth_lev:
                            done = True
                            add_path(tree, word, neigh, is_forw)
                        if not done and neigh in words_set:
                            next_lev.add(neigh)
                            add_path(tree, word, neigh, is_forw)
            return done or bfs_level(next_lev, oth_lev, tree, is_forw, words_set)

        tree, path, paths = collections.defaultdict(list), [beginWord], []
        is_found = bfs_level({beginWord}, {endWord}, tree, True, set(wordList))
        return construct_paths(beginWord, endWord, tree)

    def findLadders2(self, beginWord, endWord, wordList):

        if endWord not in wordList:
            return []

        word_set = set(wordList)  # 加速查询
        layer = {}
        layer[beginWord] = [[beginWord]]  # 存储当前单词和所有可能得到这个单词的序列(包括当前单词)

        while layer:
            new_layer = collections.defaultdict(list)  # returns [] on missing keys, just to simplify code
            for word in layer:
                if word == endWord:
                    return layer[word]  # 返回所有可能的序列

                for i in range(len(word)):  # 改变单词中的每一个字符，并且检查是否在字典里
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in word_set:
                            new_layer[new_word] += [j + [new_word] for j in layer[
                                word]]  # 增加新的单词到这个单词序列，组成新的layer
            word_set -= set(new_layer.keys())  # 从集合钟删除已经使用的单词,保证BFS
            layer = new_layer  # 向下移动到下一个layer
        return []

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    solution = Solution()
    print(solution.findLadders2(beginWord,endWord,wordList))