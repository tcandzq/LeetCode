#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 1:07
# @Author  : tc
# @File    : PathSum.py
"""
题号 112 路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

参考:https://leetcode-cn.com/problems/path-sum/solution/dfs-by-powcai/

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
         if not root:
             return False  # 递归的边界条件
         if not root.left and not root.right and sum - root.val == 0:
             return True  # 到达叶子节点,此时累加和等于目标和
         return self.hasPathSum(root.left,sum - root.val) or self.hasPathSum(root.right,sum - root.val)

if __name__ == '__main__':

    node1 = TreeNode(5)
    node2 = TreeNode(4)
    node3 = TreeNode(8)
    node4 = TreeNode(11)
    node5 = TreeNode(13)
    node6 = TreeNode(4)
    node7 = TreeNode(7)
    node8 = TreeNode(2)
    node9 = TreeNode(1)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.left = node5
    node3.right = node6
    node4.left = node7
    node4.right = node8
    node6.right = node9

    solution = Solution()
    print(solution.hasPathSum(node1,22))










