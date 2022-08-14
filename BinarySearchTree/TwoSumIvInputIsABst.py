# -*- coding: utf-8 -*-
# @File    : TwoSumIvInputIsABst.py
# @Date    : 2022-08-14
# @Author  : tc
"""
653. 两数之和 IV - 输入 BST
给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

 示例 1：

输入: root = [5,3,6,2,4,null,7], k = 9
输出: true
示例 2：


输入: root = [5,3,6,2,4,null,7], k = 28
输出: false

提示:
二叉树的节点个数的范围是  [1, 104].
-104 <= Node.val <= 104
root 为二叉搜索树
-105 <= k <= 105

深度优先搜索 + 中序遍历 + 双指针

参考:https://leetcode.cn/problems/two-sum-iv-input-is-a-bst/solution/liang-shu-zhi-he-iv-shu-ru-bst-by-leetco-b4nl/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nodes = list()

        def helper(node):
            if not node:
                return
            helper(node.left)
            nodes.append(node.val)
            helper(node.right)
        helper(root)
        left, right = 0, len(nodes) - 1
        while left < right:
            if nodes[left] + nodes[right] == k:
                return True
            if nodes[left] + nodes[right] > k:
                right -= 1
            else:
                left += 1
        return False