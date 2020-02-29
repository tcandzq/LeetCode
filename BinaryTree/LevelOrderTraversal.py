#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/4 21:14
# @Author  : tc
# @File    : BinaryTree-LevelOrderTraversal.py
"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

二叉树的中序遍历,这是基本技能,关键是记住要用队列实现

1.一定要善用while,比如当你用for循环遍历数组nums时,想在for循环里修改nums,此时循环的条件会被破坏,而用while的话会动态改变
2.善用临时变量传值

其他解答参考:https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/er-cha-shu-de-ceng-ci-bian-li-by-leetcode/

"""
from typing import List
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 迭代解法
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        nums = []
        while queue:
            new_queue = []
            new_tmp = []
            while queue:
                node = queue.pop(0)
                new_tmp.append(node.val)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            nums.append(new_tmp)
            queue = new_queue  # 临时变量传值,这个技巧很巧妙
        return nums

    # DFS解法(使用双端队列)
    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        nums = []
        while queue:
            tmp_queue = deque()
            tmp = []
            while queue:
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: tmp_queue.append(node.left)
                if node.right: tmp_queue.append(node.right)
            nums.append(tmp)
            queue = tmp_queue
        return nums

    # DFS解法(使用双端队列)优化版,善用了for循环记录次数
    def levelOrder3(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        nums = []
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            nums.append(tmp)
        return nums

    # 迭代版
    def levelOrder4(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels

        level = 0
        queue = deque([root, ])
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)

                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # go to next level
            level += 1

        return levels

    # 递归
    def levelOrder5(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels

        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels


if __name__ == '__main__':
    root = TreeNode(3)
    node1 = TreeNode(9)
    node2 = TreeNode(20)
    node3 = TreeNode(15)
    node4 = TreeNode(7)
    node5 = TreeNode(8)
    node6 = TreeNode(11)


    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4
    node1.left = node5
    node1.right = node6


    solution = Solution()
    print(solution.levelOrder5(root))






