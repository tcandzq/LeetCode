#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/14 22:18
# @Author  : tc
# @File    : BalancedBinaryTree.py
"""
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
示例 1:
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

#无非就是三种情况:
1.左子树不平衡;
2.右子树不平衡:
3.左子树的与右子树的高度差大于1

"""
def isBalanced(root):
    if not root:
        return True  # 注意这里也要写上递归出去的条件,因为后面调用了递归函数isBalanced(root)
    return True if abs(helper(root.left) - helper(root.right)) <=1 and isBalanced(root.left) and isBalanced(root.right) else False

def helper(root):

    if not root:
        return 0

    return max(helper(root.left),helper(root.right)) + 1






