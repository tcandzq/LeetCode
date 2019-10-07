#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/6 22:01
# @Author  : tc
# @File    : BinaryTreeMaximumPathSum.py
"""
题号:124  二叉树中的最大路径和
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42

1.C++版递归求解,参考:https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/solution/er-cha-shu-zhong-de-zui-da-lu-jing-he-by-ikaruga/

2.python版递归求解,参考:https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/solution/quan-ju-bian-liang-by-powcai/
                       https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/solution/binary-tree-maximum-path-sum-bottom-up-di-gui-jie-/

这题要注意对于任何一棵二叉树,不管你要达到左结点还是右结点,一定会现经过根结点(相当于联络点),因此根结点必须要考虑到递归的情况中去。

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float("-inf")
        def helper(root):
            if not root: return 0
            # 右边最大值
            left = helper(root.left)
            # 左边最大值
            right = helper(root.right)
            # 和全局变量比较
            self.res = max(left + right + root.val, self.res)
            # >0 说明都能使路径变大
            return max(0, max(left, right) + root.val)
        helper(root)
        return int(self.res)

if __name__ == '__main__':
    root = TreeNode(-10)
    node1 = TreeNode(9)
    node2 = TreeNode(20)
    node3 = TreeNode(15)
    node4 = TreeNode(7)

    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4

    solution = Solution()
    print(solution.maxPathSum(root))