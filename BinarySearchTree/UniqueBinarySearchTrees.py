#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 20:07
# @Author  : tc
# @File    : UniqueBinarySearchTrees.py

"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
Input1:3
Output1:5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

关键:充分利用二叉搜索树的特性
动态规划

假设n个节点存在二叉排序树的个数是G(n)，令f(i)为以i为根的二叉搜索树的个数
即有:G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)
n为根节点，当i为根节点时，其左子树节点个数为[1,2,3,...,i-1]，右子树节点个数为[i+1,i+2,...n]，所以当i为根节点时，其左子树节点个数为i-1个，右子树节点为n-i，即f(i) = G(i-1)*G(n-i),
上面两式可得:G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)

详细解答参考:https://leetcode-cn.com/problems/unique-binary-search-trees/solution/bu-tong-de-er-cha-sou-suo-shu-by-leetcode/
"""
def numTrees(n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        for j in range(1, i+1):
            dp[i] += dp[j - 1] * dp[i - j]
    print(dp)
    return dp[-1]

if __name__ == '__main__':
    n = 3
    print(numTrees(n))
