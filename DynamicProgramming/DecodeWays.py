#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 16:29
# @Author  : tc
# @File    : DecodeWays.py
"""
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

这是瓜子二手车2020届算法工程师校招编程题第2题

详细解答请参考:https://leetcode-cn.com/problems/decode-ways/solution/c-wo-ren-wei-hen-jian-dan-zhi-guan-de-jie-fa-by-pr/

这里如果用dp[]数组来存的话,空间度复杂度是O(n),可以用单变量来代替,空间复杂度降低

"""
def numDecodings(s):
    if s[0] == '0':
        return 0
    pre = 1
    curr = 1  # dp[-1] = dp[0] = 1
    for i in range(1,len(s)):
        tmp = curr
        if s[i] == '0':
            if s[i-1] == '1' or s[i-1] == '2':
                curr = pre  # dp[i] = dp[i-2]
            else:
                return 0
        elif s[i-1] == '1' or (s[i-1] == '2' and s[i] >= '1' and s[i] <= '6'):
            curr = curr + pre  # dp[i] = dp[i-1] + dp[i]
        pre = tmp
    return curr

if __name__ == '__main__':
    s = '12'
    print(numDecodings(s))