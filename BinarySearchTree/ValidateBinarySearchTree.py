#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 21:17
# @Author  : tc
# @File    : ValidateBinarySearchTree.py

"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

注意:二叉搜索树的中序遍历是一个有序数组!!!

Input1:
    2
   / \
  1   3

Output1:true

Input2:
    5
   / \
  1   4
     / \
    3   6
Output2:false
输入为: [5,1,4,null,null,3,6]。
根节点的值为 5 ，但是其右子节点值为 4 。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidBST(root):

    if not root:
        return True

    if isValidBST(root.left) and isValidBST(root.right):

        return

    if root.left.val < root.val and root.right.val > root.val:

        return True

