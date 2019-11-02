#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 0:46
# @Author  : tc
# @File    : DiameterOfBinaryTree.py
"""
题号 543 二叉树的直径
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。


又是一道新型递归题，在递归(二叉树的后序遍历)中寻找最大值，值得回味

参考:https://leetcode-cn.com/problems/diameter-of-binary-tree/solution/er-cha-shu-de-zhi-jing-by-leetcode/

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.res = 0

        def depth(root: TreeNode):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            self.res = max(self.res, left+right+1)  # 利用全局变量在递归中求出最大值
            return max(left, right) + 1
        depth(root)
        return self.res - 1





if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    solution = Solution()
    print(solution.diameterOfBinaryTree(node1))