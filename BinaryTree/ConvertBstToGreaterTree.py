#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 23:39
# @Author  : tc
# @File    : ConvertBstToGreaterTree.py
"""
题号 538 把二叉搜索树转换为累加树
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

例如：

输入: 二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13

二叉树的中序遍历是一个递增的数组，所以我们可以从尾部开始遍历，依次往左累加。这样遍历顺序就是右子树->根结点->左子树

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

        if root:
            self.dfs(root,0)

        return root

    def dfs(self,root, sum):
        if not root:
            return sum
        sum = self.dfs(root.right,sum)

        root.val += sum

        sum = self.dfs(root.left,root.val)

        return sum

if __name__ == '__main__':
    node1 = TreeNode(5)
    node2 = TreeNode(2)
    node3 = TreeNode(13)

    node1.left = node2
    node1.right = node3

    solution = Solution()
    print(solution.convertBST(node1))