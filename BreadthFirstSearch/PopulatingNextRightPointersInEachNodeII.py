# -*- coding: utf-8 -*-
# @File    : PopulatingNextRightPointersInEachNodeII.py
# @Date    : 2022-07-11
# @Author  : tc
"""
117. 填充每个节点的下一个右侧节点指针 II
给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

进阶：
你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。


示例：
输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next 指针连接），'#' 表示每层的末尾。

实际是二叉树的层序遍历：
https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/solution/bfsjie-jue-zui-hao-de-ji-bai-liao-100de-yong-hu-by/
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        d = collections.deque([root])

        while d:
            size = len(d)
            for i in range(size):
                node = d.popleft()
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
                if i == size - 1:
                    break
                node.next = d[0]
        return root
