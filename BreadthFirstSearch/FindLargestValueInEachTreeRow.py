#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 23:11
# @Author  : tc
# @File    : FindLargestValueInEachTreeRow.py
"""
题号 515 在每个树行中找最大值
您需要在二叉树的每一行中找到最大的值。

示例：

输入:

          1
         / \
        3   2
       / \   \
      5   3   9

输出: [1, 3, 9]

还是层次遍历,模板请参考:http://www.taochao.online/leetcode/BinaryTree/%E4%BA%8C%E5%8F%89%E6%A0%91.html

"""
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res,cur_level = [],[root]
        while cur_level:
            tmp,next_level = [],[]
            for node in cur_level:
                tmp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(max(tmp))
            cur_level = next_level
        return res



if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(3)
    node5 = TreeNode(5)
    node6 = TreeNode(9)

    node1.left = node3
    node1.right = node2
    node3.left = node5
    node3.right = node4
    node2.right = node6

    solution = Solution()
    print(solution.largestValues(node1))
