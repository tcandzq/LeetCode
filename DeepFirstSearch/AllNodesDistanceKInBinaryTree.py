#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 21:35
# @Author  : tc
# @File    : AllNodesDistanceKInBinaryTree.py
"""
题号 863 二叉树中所有距离为 K 的结点
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。

 

示例 1：

输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

输出：[7,4,1]

解释：
所求结点为与目标结点（值为 5）距离为 2 的结点，
值分别为 7，4，以及 1


BFS解法:给结点新增一个辅助属性,这个方法很巧妙

DFS解法:根据target在node的左子树 还是右子树分情况讨论

参考:https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/solution/er-cha-shu-zhong-suo-you-ju-chi-wei-k-de-jie-dian-/

"""
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #  BFS解法
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        from collections import deque

        def dfs(root,parents = None):
            if root:
                root.parents =parents
                dfs(root.left, root)
                dfs(root.right,root)

        dfs(root)
        queue = deque([(target,0)])  # queue存储与target相关的所有结点
        seen = {target}
        while queue:
            if queue[0][1] == K:
                return [node.val for node,d in queue]
            node,d = queue.popleft()
            for neighbor in (node.left,node.right,node.parents):  # 从一个结点的三个方向遍历:左结点,右结点,父结点
                if neighbor and neighbor not in seen:  # 如果结点存在,且结点没有访问过
                    seen.add(neighbor)
                    queue.append((neighbor,d+1))  # 距离加1
        return []


    #  DFS 解法
    def distanceK2(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        ans = []

        # Return distance from node to target if exists, else -1
        # Vertex distance: the # of vertices on the path from node to target
        def dfs(node):
            if not node:
                return -1
            elif node is target:
                subtree_add(node, 0)
                return 1
            else:
                L, R = dfs(node.left), dfs(node.right)
                if L != -1:
                    if L == K: ans.append(node.val)
                    subtree_add(node.right, L + 1)
                    return L + 1
                elif R != -1:
                    if R == K: ans.append(node.val)
                    subtree_add(node.left, R + 1)
                    return R + 1
                else:
                    return -1

        # Add all nodes 'K - dist' from the node to answer.
        def subtree_add(node, dist):
            if not node:
                return
            elif dist == K:
                ans.append(node.val)
            else:
                subtree_add(node.left, dist + 1)
                subtree_add(node.right, dist + 1)

        dfs(root)
        return ans




if __name__ == '__main__':
    node0 = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)

    node3.left = node5
    node3.right = node1
    node5.left = node6
    node5.right = node2
    node2.left = node7
    node2.right = node4
    node1.left = node0
    node1.right = node8

    target = node5
    K = 2

    solution = Solution()
    print(solution.distanceK(node0,target,K))