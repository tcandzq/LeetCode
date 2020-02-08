# -*- coding: utf-8 -*-
# @File    : WordBreakII.py
# @Date    : 2020-02-08
# @Author  : tc

"""
题号 140 单词拆分II

给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]
示例 2：

输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。
示例 3：

输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]

分两步解决：

1.可以利用leetcode139 单词拆分的代码来作为功能函数得到s可能的空格分隔点即dp数组;
2.对所有可能的空格分隔使用dfs进行组合即通过dp数组，构建递归树
3.遍历这棵递归树就能得到对应的排列
参考：https://leetcode-cn.com/problems/word-break-ii/solution/dong-tai-gui-hua-hui-su-qiu-jie-ju-ti-zhi-python-d/

"""
from typing import List
from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        size = len(s)

        # 题目中说非空字符串，以下 assert 一定通过
        assert size > 0

        # 预处理，把 wordDict 放进一个哈希表中
        word_set = {word for word in wordDict}
        dp = [False] * (size + 1)
        dp[0] = True
        for i in range(1, size + 1):
            for j in range(i - 1, -1, -1):
                # dp[j] 写在前面会更快一点，否则还要去切片，然后再放入 hash 表判重
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        print(dp)
        res = []
        if dp[-1]:
            queue = deque()
            self.__dfs(s,size,word_set,res,queue,dp)

        return res

    def __dfs(self,s,length,word_set,res,path,dp):
        if length == 0:
            res.append(' '.join(path))
            return
        for i in range(length):
            if dp[i]:
                suffix = s[i:length]
                if suffix in word_set:
                    path.appendleft(suffix)
                    self.__dfs(s,i,word_set,res,path,dp)
                    path.popleft()

if __name__ == '__main__':
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    solution = Solution()
    print(solution.wordBreak(s,wordDict))

