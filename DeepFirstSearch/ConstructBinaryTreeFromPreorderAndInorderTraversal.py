#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 20:17
# @Author  : tc
# @File    : ConstructBinaryTreeFromPreorderAndInorderTraversal.py
"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7


这是2020届美团NLP算法工程师一面的面试题
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(preorder,inorder):
    if len(inorder) == 0:
        return None
        # 前序遍历第一个值为根节点
    root = TreeNode(preorder[0])
    # 因为没有重复元素，所以可以直接根据值来查找根节点在中序遍历中的位置
    mid = inorder.index(preorder[0])
    # 构建左子树
    root.left = buildTree(preorder[1:mid + 1], inorder[:mid])
    # 构建右子树
    root.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])

    return root


