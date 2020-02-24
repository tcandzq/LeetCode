# -*- coding: utf-8 -*-
# @File    : MaximumWidthOfBinaryTree.py
# @Date    : 2020-02-24
# @Author  : tc
"""
题号 662. 二叉树最大宽度
给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary tree）结构相同，但一些节点为空。

每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。

示例 1:

输入:

           1
         /   \
        3     2
       / \     \
      5   3     9

输出: 4
解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。
示例 2:

输入:

          1
         /
        3
       / \
      5   3

输出: 2
解释: 最大值出现在树的第 3 层，宽度为 2 (5,3)。
示例 3:

输入:

          1
         / \
        3   2
       /
      5

输出: 2
解释: 最大值出现在树的第 2 层，宽度为 2 (3,2)。
示例 4:

输入:

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
输出: 8
解释: 最大值出现在树的第 4 层，宽度为 8 (6,null,null,null,null,null,null,7)。

BFS 二叉树的层次遍历

https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/106650/Python...

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return []
        width, level = 0, [(root, 1)]
        while len(level):

            width = max(width, level[-1][1] - level[0][1] + 1) # 注意这里要加1。因为相邻两个节点如(5,3)的宽度是2，参考题目中的例子2
            next_level = []
            for item, num in level:
                if item.left:
                    next_level.append((item.left, num * 2))
                if item.right:
                    next_level.append((item.right, num * 2 + 1))
            level = next_level
        return width
