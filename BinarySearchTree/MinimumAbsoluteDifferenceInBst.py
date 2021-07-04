# -*- coding: utf-8 -*-
# @File    : MinimumAbsoluteDifferenceInBst.py
# @Date    : 2021-07-05
# @Author  : tc
"""
题号 530. 二叉搜索树的最小绝对差
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。
示例：

输入：

   1
    \
     3
    /
   2

输出：
1

解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。


提示：

树中至少有 2 个节点。
本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同

使用二叉树的迭代版层序遍历

解法二参考：https://leetcode.com/problems/minimum-absolute-difference-in-bst/discuss/99926/Python-Inorder-Solution


"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:

        stack = []
        p = root
        pre = float("-inf")
        ans = float("inf")
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            ans = min(p.val - pre, ans)
            pre = p.val
            p = p.right
        return ans

    def getMinimumDifference2(self, root: TreeNode) -> int:
        def fn(node,low, high):
            if not node:
                return high - low
            left = fn(node.left, low, node.val)
            right = fn(node.right, node.val, high)
            return min(left, right)
        return fn(root, float('-inf'), float('inf'))