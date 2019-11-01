#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 22:08
# @Author  : tc
# @File    : MinimumDepthOfBinaryTree.py
"""
题号 111 二叉树的最小深度
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

所以到底什么是叶子结点?为什么[1,2]的最小深度是2，最大深度也是2?

和二叉树最大深度的代码比较，你会发现代码都是一样的，同样的[1,2]为什么结果不一样？

其实是min()和max()的区别,仔细想想。

这题和leetcode104二叉树的最大深度很像，但区别很大

参考:https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/solution/minimum-depth-of-binary-tree-di-gui-jie-fa-by-jin4/

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    #  正确结果
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left:  # 左子树为空
            return self.minDepth(root.right) + 1
        if not root.right:  # 右子树为空
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1  # 左右子树均不空


    #  错误解答
    def minDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        return min(self.minDepth2(root.left),self.minDepth2(root.right)) + 1
if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)

    # node1.left = node2
    # node1.right = node3
    # node3.left = node4
    # node3.right = node5

    solution = Solution()
    print(solution.minDepth2(node1))
