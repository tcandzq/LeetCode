# -*- coding: utf-8 -*-
# @File    : TrimABinarySearchTree.py
# @Date    : 2022-08-14
# @Author  : tc
"""
669. 修剪二叉搜索树
给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。修剪树 不应该 改变保留在树中的元素的相对结构 (即，如果没有被移除，原有的父代子代关系都应当保留)。 可以证明，存在 唯一的答案 。
所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。
示例 1：
输入：root = [1,0,2], low = 1, high = 2
输出：[1,null,2]
示例 2：


输入：root = [3,0,4,null,2,null,null,1], low = 1, high = 3
输出：[3,2,null,1]


提示：
树中节点数在范围 [1, 104] 内
0 <= Node.val <= 104
树中每个节点的值都是 唯一 的
题目数据保证输入是一棵有效的二叉搜索树
0 <= low <= high <= 104

思路
令 trim(node) 作为该节点上的子树的理想答案。我们可以递归地构建该答案。

算法
当 node.val > R，那么修剪后的二叉树必定出现在节点的左边。

类似地，当node.val < L，那么修剪后的二叉树出现在节点的右边。否则，我们将会修剪树的两边。

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return root

        #因为是二叉搜索树,节点.left < 节点 < 节点.right
        #节点数字比low小,就把左节点全部裁掉,因此左节点必然也low小.
        if root.val < low:
            root = root.right
            #裁掉之后,继续看右节点的剪裁情况.剪裁后重新赋值给root.
            root = self.trimBST(root, low, high)
        #如果数字比high大,就把右节点全部裁掉，因此右节点也必然比high大.
        elif root.val > high:
            root = root.left
            #裁掉之后,继续看左节点的剪裁情况
            root = self.trimBST(root, low, high)
        else:
            #如果数字在区间内,就去裁剪左右子节点.
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        return root