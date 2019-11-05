#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 20:02
# @Author  : tc
# @File    : CountCompleteTreeNodes.py
"""
题号 222 完全二叉树的节点个数
给出一个完全二叉树，求出该树的节点个数。

说明：

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

示例:

输入:
    1
   / \
  2   3
 / \  /
4  5 6

输出: 6

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #  二叉树的中序遍历(没有用到完全二叉的树的性质)
    def countNodes(self, root: TreeNode) -> int:
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return len(res)

    #  二叉树遍历(一个更简洁的方式)
    def countNodes2(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.countNodes2(root.left) + self.countNodes2(root.right)

    def countNodes3(self, root: TreeNode) -> int:
        pass

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6

    solution = Solution()
    print(solution.countNodes2(node1))