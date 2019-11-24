#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/24 10:39
# @Author  : tc
# @File    : BinaryTreeZigZagLevelOrderTraversal.py
"""
题号 103 二叉树的锯齿形层次遍历
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

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

层次遍历加入奇偶性判断,参考:https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/solution/pythonshuang-zhan-shi-xian-by-yao-chao/

双栈解法：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/solution/liang-ge-stackde-jie-fa-bu-xu-fan-zhuan-queuehuo-z/

"""
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # BFS解法
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        cur_level = [root]
        depth = 0
        while cur_level:
            tmp = []
            next_level = []
            for node in cur_level:
                tmp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if depth % 2 == 1:
                res.append(tmp[::-1])
            else:
                res.append(tmp)
            depth += 1
            cur_level = next_level
        return res

    # 双栈解法
    def zigzagLevelOrder2(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        d1 = [root]  # 从左向右存储的栈d1
        d2 = []  # 从右向左存储的栈 d2
        res = []  # 保存输出结果
        tmp = []  # 临时存储结果
        while True:
            while d1:
                curr = d1.pop(-1)
                tmp.append(curr.val)
                if curr.left:  # 左边的节点先入栈
                    d2.append(curr.left)
                if curr.right:
                    d2.append(curr.right)
            if tmp:
                res.append(tmp)
                tmp = []
            else:
                break

            while d2:
                curr = d2.pop(-1)
                tmp.append(curr.val)
                if curr.right:  # 这里是右边的节点先入栈
                    d1.append(curr.right)
                if curr.left:
                    d1.append(curr.left)
            if tmp:
                res.append(tmp)
                tmp = []
            else:
                break

        return res


if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5

    solution = Solution()
    print(solution.zigzagLevelOrder2(node1))