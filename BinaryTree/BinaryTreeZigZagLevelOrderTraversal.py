# -*- coding: utf-8 -*-
# @File    : BinaryTreeZigZagLevelOrderTraversal.py.py
# @Date    : 2020-02-27
# @Author  : tc
"""
题号 103. 二叉树的锯齿形层次遍历
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

参考：https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/33834/Python-simple-BFS

"""
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        res,temp,queue,flag = [],[],[root],1
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                temp += [node.val]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res += [temp[::flag]]
            temp = []
            flag *= -1
        return res

if __name__ == '__main__':
    pass