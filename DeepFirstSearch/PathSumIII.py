#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 23:07
# @Author  : tc
# @File    : PathSumIII.py
"""
题号 437 路径总和 III
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11


参考:https://leetcode-cn.com/problems/path-sum-iii/solution/leetcode-437-path-sum-iii-by-li-xin-lei/

1.双递归,今天第一次看到,长见识了
2.巧用sum-root.val
3.递归一定要多debug,不要盯着代码想,想不通的
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.paths(root,sum) + self.pathSum(root.left,sum) + self.pathSum(root.right,sum)  # 一个完整的递归子结构


    def paths(self,root:TreeNode,sum:int) -> int:
        if not root:
            return 0
        res = 0
        if root.val == sum:
            res += 1
        res += self.paths(root.left, sum - root.val)  # sum 作为函数入参,在递归过程中不断改变,不是一成不变的
        res += self.paths(root.right, sum - root.val)
        return res

if __name__ == '__main__':
    node1 = TreeNode(10)
    node2 = TreeNode(5)
    node3 = TreeNode(-3)
    node4 = TreeNode(3)
    node5 = TreeNode(2)
    node6 = TreeNode(11)
    node7 = TreeNode(3)
    node8 = TreeNode(-2)
    node9 = TreeNode(1)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6
    node4.left = node7
    node4.right = node8
    node5.right = node9


    solution = Solution()
    sum = 8
    print(solution.pathSum(node1,sum))

