#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 12:00
# @Author  : tc
# @File    : MaximumLengthOfRepeatedSubarray.py

"""
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
Input1: A: [1,2,3,2,1]
        B: [3,2,1,4,7]

Output1:3   长度最长的公共子数组是 [3, 2, 1]。

说明:
    1.1 <= len(A), len(B) <= 1000
    2.0 <= A[i], B[i] < 100

这是一道典型的最长公共子串问题

1.动态规划的越界问题可以通过新增一个哑结点
优化的代码参考:https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/zui-chang-gong-gong-zi-chuan-dong-tai-gui-hua-you-/

"""

#优化前
def find_length(a, b):

    dp = [[0] * len(a) for i in range(len(b))]

    for i in range(len(a)):
        dp[0][i] = 1 if a[i] == b[0] else 0

    for j in range(len(b)):
        dp[j][0] = 1 if b[j] == a[0] else 0

    max_len = 0
    for i in range(1, len(b)):
        for j in range(1, len(a)):
            if dp[i-1][j-1] and b[i] == a[j]:
                dp[i][j] = dp[i-1][j-1] + 1

            if (dp[i-1][j-1] == 0) and b[i] == a[j]:
                dp[i][j] = 1
            max_len = max(max_len, dp[i][j])
    print(dp)
    return max_len

#优化后
def find_length2(a,b):
    m = len(a)

    n = len(b)
    #0的位置初始化为0，省的判断越界问题了
    dp = [[0] * (m+1) for _ in range(n+1)]

    max_len = 0

    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                dp[i+1][j+1] = dp[i][j]+1
                max_len = max(max_len, dp[i+1][j+1])
            else:
                dp[i+1][j+1] = 0
    return max_len


if __name__ == '__main__':

    a = [1,2,3,2,1]

    b = [3,2,1,4,7]

    print(find_length2(a,b))