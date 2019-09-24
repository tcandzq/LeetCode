#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 22:35
# @Author  : tc
# @File    : LowestCommonAncestorOfABinaryTree.py


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
    if not root or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left,p,q)
    right = lowestCommonAncestor(root.right,p,q)
    if not left:
        return right
    elif not right:
        return left
    else:
        return root