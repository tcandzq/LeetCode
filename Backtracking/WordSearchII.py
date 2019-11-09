#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/8 19:45
# @Author  : tc
# @File    : WordSearchII.py
"""
题号 212 单词搜索II
给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]

暴力求解代码参考LeetCode 79单词搜索

优化:字典树+回溯
参考:https://leetcode-cn.com/problems/word-search-ii/solution/qian-zhui-shu-dfs-by-powcai/
"""
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        res = []
        for word in words:
            masked = [[False] * len(board[0]) for _ in range(len(board))]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if self.search(board,word,masked,i,j,0):
                        print(word)
                        res.append(word)
        return res

    directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    def search(self, board, word,masked,i, j, k):
        if k == len(word) - 1:
            return board[i][j] == word[k]  # 记得写递归的终止条件
        if board[i][j] == word[k]:
            masked[i][j] = True  # 同一个单元格内的字母不能重复使用,先占住这个位置，搜索不成功的话，要释放掉
            for direction in self.directions:  #
                new_i = i + direction[0]
                new_j = j + direction[1]
                # 注意：如果这一次 search word 成功的话，就返回
                # 这里的if条件中的not masked[new_i][new_j] 就是为了防止字母被重复利用
                if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]) and not masked[new_i][new_j] \
                        and self.search(board, word, masked,new_i, new_j, k + 1):
                    return True
            masked[i][j] = False  # 记住这里要回溯,这里要释放,此时已经搜索不成功了
        return False

    #  优化
    def findWords2(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            t = trie
            for w in word:
                t = t.setdefault(w,{})
            t['end'] = 1
        res = []
        row = len(board)
        col = len(board[0])

        def dfs(i,j,trie,s):
            c = board[i][j]
            if c not in trie:
                return
            trie = trie[c]
            if 'end' in trie and trie['end'] == 1:
                res.append(s + c)
                trie['end'] = 0
            board[i][j] = '#'
            for x,y in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and board[tmp_i][tmp_j] != '#':
                    dfs(tmp_i,tmp_j,trie,s+c)
            board[i][j] = c
        for i in range(row):
            for j in range(col):
                dfs(i,j,trie,"")
        return res




if __name__ == '__main__':
    words = ["oath","pea","eat","rain"]
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    solution = Solution()
    print(solution.findWords2(board,words))
