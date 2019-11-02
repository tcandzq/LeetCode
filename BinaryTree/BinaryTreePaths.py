#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/2 22:50
# @Author  : tc
# @File    : BinaryTreePaths.py
"""
题号 257 二叉树的所有路径
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3


又是回溯解法，直接用之前的回溯模板套用就行了

"""
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        def dfs(root,tmp):
            if not root:
                return
            if not root.left and not root.right:
                tmp += str(root.val)
                res.append(tmp)
                return
            dfs(root.left,tmp+str(root.val) + '->')
            dfs(root.right,tmp+str(root.val) + '->')
        dfs(root,'')
        return res


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(5)

    node1.left = node2
    node1.right = node3
    node2.right = node4

    solution = Solution()
    print(solution.binaryTreePaths(node1))
