#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 23:43
# @Author  : tc
# @File    : SameTree.py
"""
题号100 相同的树
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if not p and q:
            return False

        if not q and p:
            return False

        if not p and not q:
            return True

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)


if __name__ == '__main__':
    p = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(1)
    p.left = node1
    # p.right = node2

    q = TreeNode(1)
    node3 = TreeNode(1)
    node4 = TreeNode(2)
    # q.left = node3
    q.right = node4

    solution = Solution()
    print(solution.isSameTree(p,q))

