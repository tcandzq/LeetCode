#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 20:32
# @Author  : tc
# @File    : KthSmallestElementInABst.py
"""
题号 230 二叉搜索树中第K小的元素
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3
进阶：
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？

二叉树的中序遍历是一个递增数组

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res[k-1]

    #  更简洁的写法(在遍历到第k次时停止，这个技巧要牢记)
    def kthSmallest2(self, root: TreeNode, k: int) -> int:
        res = None

        def helper(root):
            nonlocal k, res
            if root.left: helper(root.left)
            k -= 1
            if k == 0:
                res = root.val
                return
            if root.right: helper(root.right)

        helper(root)
        return res


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)

    node3.left = node1
    node3.right = node4
    node1.right = node2

    solution = Solution()
    k = 1
    print(solution.kthSmallest2(node1,k))