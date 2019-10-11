#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 22:44
# @Author  : tc
# @File    : FlattenBinaryTreeToLinkedList.py
"""
题号114 二叉树展开为链表
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

参考:https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/flatten-binary-tree-to-linked-list-qian-xu-bian-li/

一看就是先序遍历,boring

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    pre = None
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        if self.pre:
            self.pre.right = root
            self.pre.left = None
        self.pre = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)



