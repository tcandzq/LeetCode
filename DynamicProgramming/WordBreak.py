#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 23:21
# @Author  : tc
# @File    : WordBreak.py
"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

参考1:https://leetcode-cn.com/problems/word-break/solution/dong-tai-gui-hua-zi-ding-xiang-xia-he-zi-di-xiang-/
参考2:https://leetcode-cn.com/problems/word-break/solution/dan-ci-chai-fen-by-leetcode/


"""
# 自己写的代码想法和注释里是一样的,但是我写的太复杂了
def wordBreak(s, wordDict):
    n = len(s)
    dp = [0] * len(s)
    count = 0
    for i in range(n):
        if s[:i+1] in wordDict:
            dp[i] = 1
            count = i
            break
        else:
            dp[i] = 0

    for j in range(count,n):
        if s[:j+1] in wordDict:
            dp[j] = 1
            continue
        for k in range(j, -1, -1):
            if dp[k] and s[k+1:j+1] in wordDict:
                dp[j] = 1
                break
    if dp[-1]:
        return True
    return False

# 官方题解就是简洁,佩服
def wordBreak2(s,wordDict):
    n = len(s)
    if not wordDict:
        return not s  # 当s为空时直接返回
    dp = [False] * (n+1)
    dp[0] = True # 初始化 dp[0] 为 true ，这是因为空字符串总是字典的一部分
    for i in range(1,n+1):
        for j in range(i - 1,-1,-1):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[-1]

if __name__ == '__main__':
    s = "goalspecial"
    wordDict = ["go","goal","goals","special"]
    print(wordBreak(s,wordDict))
