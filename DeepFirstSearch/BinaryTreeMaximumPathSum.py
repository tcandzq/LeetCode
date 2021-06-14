# -*- coding: utf-8 -*-
# @File    : BinaryTreeMaximumPathSum.py
# @Date    : 2021-06-14
# @Author  : tc
"""
题号:124. 二叉树中的最大路径和
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和。
 
示例 1：

输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
示例 2：


输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42

思路参考：https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_path = float("-inf")

        def get_max_gain(node):
            nonlocal max_path
            if node is None:
                return 0
            gain_on_left = max(get_max_gain(node.left), 0)
            gain_on_right = max(get_max_gain(node.right), 0)

            current_max_path = node.val + gain_on_left + gain_on_right
            max_path = max(max_path, current_max_path)

            return node.val + max(gain_on_left, gain_on_right)

        get_max_gain(root)
        return max_path