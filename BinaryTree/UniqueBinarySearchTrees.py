# -*- coding: utf-8 -*-
# @File    : UniqueBinarySearchTrees.py
# @Date    : 2021-06-14
# @Author  : tc
"""
96. 不同的二叉搜索树
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

示例 1：


输入：n = 3
输出：5
示例 2：

输入：n = 1
输出：1

实际用动态规划求解，状态转移方程为:
以k为根节点的 BST种类数 = 左子树 BST种类数 * 右子树BST种类数

参考:https://leetcode-cn.com/problems/unique-binary-search-trees/solution/shou-hua-tu-jie-san-chong-xie-fa-dp-di-gui-ji-yi-h/
"""
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[-1]