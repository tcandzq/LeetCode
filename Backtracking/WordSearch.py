#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/29 19:36
# @Author  : tc
# @File    : WordSearch.py
"""
题号:79  单词搜索
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.

这个人讲解回溯和dfs特别清晰:https://leetcode-cn.com/problems/word-search/solution/zai-er-wei-ping-mian-shang-shi-yong-hui-su-fa-pyth/

1.擅于使用masked数组使得状态可以回溯
2.偏移量数组在二维平面内是经常使用的，可以把它的设置当做一个技巧，并且在这个问题中，偏移量数组内的 4 个偏移的顺序无关紧要
"""
class Solution:
    directions = [(0,-1),(0,1),(1,0),(-1,0)]
    def exist(self,board, word):
        rows = len(board)
        cols = len(board[0])
        masked = [[False] * cols for _ in range(rows)]  # 这里的masked很巧妙,这个套路要牢记
        for i in range(rows):
            for j in range(cols):
                if self.search(board, word, masked,i, j, 0):  # 对每一个格子都从头开始搜索
                    return True
        return False

    def search(self,board, word,masked,i, j, k):
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

if __name__ == '__main__':
    board = [['A','B','C','E'],
              ['S','F','C','S'],
              ['A','D','E','E']]
    word = "ABCCED"
    solution = Solution()
    print(solution.exist(board,word))

