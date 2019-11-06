#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 22:47
# @Author  : tc
# @File    : FindBottomLeftTreeValue.py
"""
题号 513 找树左下角的值
给定一个二叉树，在树的最后一行找到最左边的值。

示例 1:

输入:

    2
   / \
  1   3

输出:
1
 

示例 2:

输入:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

输出:
7

层次遍历,直接用自己的模板套http://www.taochao.online/leetcode/BinaryTree/%E4%BA%8C%E5%8F%89%E6%A0%91.html,真舒服。

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        res,cur_level = [],[root]
        while cur_level:
            tmp = []
            next_level = []
            for i in cur_level:
                tmp.append(i.val)
                if i.left :
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            res.append(tmp)
            cur_level = next_level
        return res[-1][0]


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.left = node5
    node3.right = node6
    node5.left = node7

    solution = Solution()
    print(solution.findBottomLeftValue(node1))