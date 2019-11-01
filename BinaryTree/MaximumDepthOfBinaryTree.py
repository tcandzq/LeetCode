#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/7 16:21
# @Author  : tc
# @File    : MaximumDepthOfBinaryTree.py
"""
题号 104 二叉树的最大深度
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
示例：
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3。

使用DFS
参考:https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/solution/hua-jie-suan-fa-104-er-cha-shu-de-zui-da-shen-du-b/

"""
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def maxDepth(root):
    if not root:
        return 0

    return max(maxDepth(root.left),maxDepth(root.right)) + 1  # 注意这里的加1。加1表示当前节点的高度

if __name__ == '__main__':
    root = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)

    # root.left = node2
    # root.right = node3
    # node3.left = node4
    # node3.right = node5

    print(maxDepth(root))
