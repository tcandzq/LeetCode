# -*- coding: utf-8 -*-
# @File    : SumOfLeftLeaves.py
# @Date    : 2021-06-14
# @Author  : tc
"""
题号:404. 左叶子之和
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

dfs,用一个标志位 标记节点是否是左节点

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res = 0
        def sumOfLeftLeaves(self, root: TreeNode) -> int:
            self.dfs(root, False)
            return self.res

        def dfs(self, node, flag):
            if not node:
                return
            if not node.left and not node.right and flag:
                self.res += node.val
            self.dfs(node.left, True)
            self.dfs(node.right, False)