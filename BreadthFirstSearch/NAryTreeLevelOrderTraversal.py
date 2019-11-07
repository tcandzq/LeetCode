#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 23:29
# @Author  : tc
# @File    : NAryTreeLevelOrderTraversal.py
"""
题号 429 N叉树的层序遍历
给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

例如，给定一个 3叉树 :

 图详见:https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/
 返回其层序遍历:

[
     [1],
     [3,2,4],
     [5,6]
]
 

说明:

树的深度不会超过 1000。
树的节点总数不会超过 5000。

其实node.children是list类型

"""
from typing import List

class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:

    def levelOrder1(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res, curr_level = [], [root]
        while curr_level:
            next_level, tmp = [], []
            for node in curr_level:
                tmp.append(node.val)
                for children_node in node.children:
                    if children_node:
                        next_level.append(children_node)
            res.append(tmp)
            curr_level = next_level
        return res

    #  更简洁的代码
    def levelOrder2(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        cur = [root]
        while cur:
            next = []
            temp = []
            for node in cur:
                temp.append(node.val)
                next += node.children
            res.append(temp)
            cur = next
        return res



