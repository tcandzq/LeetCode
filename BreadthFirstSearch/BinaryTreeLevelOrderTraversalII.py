#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 20:57
# @Author  : tc
# @File    : BinaryTreeLevelOrderTraversalII.py
"""
题号 107 二叉树的层次遍历II
给定一个二叉树，返回其节点值自底向上的层次遍历。（即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

使用list的insert方法,倒序插入元素,运行速度更快

"""
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 先层次遍历 然后倒序数组
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res,cur_level = [],[root]
        while cur_level:
            tmp,next_level = [],[]
            for node in cur_level:
                tmp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                cur_level = next_level
            res.append(tmp)
        return res[::-1]

    # 在层次遍历过程中不断往前插入
    def levelOrderBottom2(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res,cur_level = [],[root]
        while cur_level:
            tmp,next_level = [],[]
            for node in cur_level:
                tmp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                cur_level = next_level
            res.insert(0,tmp)  # 巧用insert 运行速度比方法1更快
        return res

if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5

    solution = Solution()
    print(solution.levelOrderBottom2(node1))