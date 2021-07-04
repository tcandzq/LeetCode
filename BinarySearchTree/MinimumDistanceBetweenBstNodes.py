# -*- coding: utf-8 -*-
# @File    : MinimumDistanceBetweenBstNodes.py
# @Date    : 2021-07-05
# @Author  : tc
"""
783. 二叉搜索树节点最小距离
给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。

注意：本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/ 相同

示例 1：


输入：root = [4,2,6,1,3]
输出：1
示例 2：


输入：root = [1,0,48,null,null,12,49]
输出：1

二叉搜索树的迭代版中序遍历,使用pre记录上一个节点

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        pre = float("-inf")
        ans = float("inf")

        p = root
        stack = []
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            ans = min(p.val - pre, ans)
            pre = p.val
            p = p.right
        return ans