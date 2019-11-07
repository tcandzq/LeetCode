#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 19:13
# @Author  : tc
# @File    : MaxiMumDepthOfNAryTree.py
"""
题号559 N叉树的最大深度

给定一个 N 叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

例如，给定一个 3叉树 :

图片请参考:https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/

我们应返回其最大深度，3。

说明:

树的深度不会超过 1000。
树的节点总不会超过 5000。

"""
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    # 正确
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        depth = 0
        for node in root.children:
            depth = max(self.maxDepth(node),depth)
        return depth+1

    #  更简洁
    def maxDepth2(self, root: 'Node') -> int:
        if not root:
            return 0
        return max([self.maxDepth(node) for node in root.children] or[0]) + 1  # 防止出现max([])的情况
