#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 11:03
# @Author  : tc
# @File    : PathSumII.py
"""
题号113 路径总和 II
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if not root:
            return []
        def dfs(root,tmp_sum,tmp):
            if not root:
                return
            if not root.left and not root.right and tmp_sum + root.val== sum:
                tmp += [root.val]
                res.append(tmp)
                return
            dfs(root.left, tmp_sum + root.val, tmp + [root.val])
            dfs(root.right, tmp_sum + root.val, tmp + [root.val])
        dfs(root,0,[])
        return res

if __name__ == '__main__':
    node1 = TreeNode(5)
    node2 = TreeNode(4)
    node3 = TreeNode(8)
    node4 = TreeNode(11)
    node5 = TreeNode(13)
    node6 = TreeNode(4)
    node7 = TreeNode(7)
    node8 = TreeNode(2)
    node9 = TreeNode(5)
    node10 = TreeNode(1)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.left = node5
    node3.right = node6
    node4.left = node7
    node4.right = node8
    node6.left = node9
    node6.right = node10

    solution = Solution()
    print(solution.storePath(node1))
