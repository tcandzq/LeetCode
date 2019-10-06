#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/4 19:17
# @Author  : tc
# @File    : SymmetricTree.py
"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

参考:https://leetcode-cn.com/problems/symmetric-tree/solution/dui-cheng-er-cha-shu-by-leetcode/

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归解法(中序遍历) 错误
    def isSymmetric1(self, root: TreeNode) -> bool:
        nums = []
        self.inorderTraversal(root,nums)
        return nums == list(reversed(nums))
    # 中序遍历
    def inorderTraversal(self,root,nums):
        if not root:
            return
        self.inorderTraversal(root.left,nums)
        nums.append(root.val)
        self.inorderTraversal(root.right,nums)
    #  递归解法 正确
    def isSymmetric2(self, root: TreeNode) -> bool:
        if not root:  # 注意这里的异常情况
            return True
        return self.helper(root.left,root.right)

    def helper(self,p,q):
        if p and q and p.val != q.val:
            return False
        if (p and not q) or (q and not p):
            return False
        if (not p) and (not q):
            return True
        print(p.val,q.val)
        return self.helper(p.left,q.right) and self.helper(p.right,q.left)

if __name__ == '__main__':
    # root = TreeNode(1)
    # node1 = TreeNode(2)
    # node2 = TreeNode(2)
    # node3 = TreeNode(3)
    # node4 = TreeNode(4)
    # node5 = TreeNode(4)
    # node6 = TreeNode(3)
    #
    # root.left = node1
    # root.right = node2
    # node1.left = node3
    # node1.right = node4
    # node2.left = node5
    # node2.right = node6

    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(3)

    root.left = node1
    root.right = node2
    node1.right = node3
    node2.right = node4

    solution = Solution()
    print(solution.isSymmetric2(root))
