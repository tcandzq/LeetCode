#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 22:11
# @Author  : tc
# @File    : BinaryTreeInorderTraversal.py
"""
给定一个二叉树，返回它的中序遍历。
Input:[1,null,2,3]
   1
    \
     2
    /
   3

Output:[1,3,2]

本题需要用递归和非递归两种解法

递归解法:说白了，就是先左，然后中， 最后右

"""
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

#解法1:递归

def inorderTraversal(root):
    node_list = []
    helper(root,node_list)
    return node_list

def helper(root,node_list):
    if root:
        if root.left:
            helper(root.left,node_list)
        node_list.append(root.val)
        if root.right:
            helper(root.right,node_list)
#解法2:

if __name__ == '__main__':

    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    root.left = node2
    root.right = node3
    node3.left = node4
    node4.right = node5

    for num in inorderTraversal(root):
        print(num)