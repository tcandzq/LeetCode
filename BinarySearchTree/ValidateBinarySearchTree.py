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

注意二叉搜索树的定义:对树上的每个结点都满足其左子树上所有结点的数据域均小于或等于根结点,右子树的所有结点的数据域均大于根结点的数据域
即不仅仅右结点要大于根结点,而且以该右结点为根的右子树的元素都要大于该结点

参考:https://leetcode-cn.com/problems/validate-binary-search-tree/solution/yan-zheng-er-cha-sou-suo-shu-by-leetcode/
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#解法1参考:https://leetcode-cn.com/problems/validate-binary-search-tree/solution/die-dai-yu-di-gui-by-powcai/
def isValidBST(root):
    res = []
    def helper(root):
        if not root:
            return
        helper(root.left)
        res.append(root.val)
        helper(root.right)
    helper(root)
    return res == sorted(res)

if __name__ == '__main__':
    root = TreeNode(5)
    node2 = TreeNode(1)
    node3 = TreeNode(4)
    node4 = TreeNode(3)
    node5 = TreeNode(6)

    root.left = node2
    root.right = node3
    node3.left = node4
    node3.right = node5
    print(isValidBST(root))

