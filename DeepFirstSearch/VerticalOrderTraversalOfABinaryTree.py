# -*- coding: utf-8 -*-
# @File    : VerticalOrderTraversalOfABinaryTree.py
# @Date    : 2022-08-14
# @Author  : tc
"""
987. 二叉树的垂序遍历
给你二叉树的根结点 root ，请你设计算法计算二叉树的 垂序遍历 序列。
对位于 (row, col) 的每个结点而言，其左右子结点分别位于 (row + 1, col - 1) 和 (row + 1, col + 1) 。树的根结点位于 (0, 0) 。
二叉树的 垂序遍历 从最左边的列开始直到最右边的列结束，按列索引每一列上的所有结点，形成一个按出现位置从上到下排序的有序列表。如果同行同列上有多个结点，则按结点的值从小到大进行排序。
返回二叉树的 垂序遍历 序列。
示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[9],[3,15],[20],[7]]
解释：
列 -1 ：只有结点 9 在此列中。
列  0 ：只有结点 3 和 15 在此列中，按从上到下顺序。
列  1 ：只有结点 20 在此列中。
列  2 ：只有结点 7 在此列中。
示例 2：

输入：root = [1,2,3,4,5,6,7]
输出：[[4],[2],[1,5,6],[3],[7]]
解释：
列 -2 ：只有结点 4 在此列中。
列 -1 ：只有结点 2 在此列中。
列  0 ：结点 1 、5 和 6 都在此列中。
          1 在上面，所以它出现在前面。
          5 和 6 位置都是 (2, 0) ，所以按值从小到大排序，5 在 6 的前面。
列  1 ：只有结点 3 在此列中。
列  2 ：只有结点 7 在此列中。
示例 3：

输入：root = [1,2,3,4,6,5,7]
输出：[[4],[2],[1,5,6],[3],[7]]
解释：
这个示例实际上与示例 2 完全相同，只是结点 5 和 6 在树中的位置发生了交换。
因为 5 和 6 的位置仍然相同，所以答案保持不变，仍然按值从小到大排序。

提示：
树中结点数目总数在范围 [1, 1000] 内
0 <= Node.val <= 1000


自定义排序

我们可以从根节点开始，对整棵树进行一次遍历，在遍历的过程中使用数组 nodes 记录下每个节点的行号row，列号col 以及值value。
在遍历完成后，我们按照col 为第一关键字升序，row 为第二关键字升序，value 为第三关键字升序，对所有的节点进行排序即可。
在排序完成后，我们还需要按照题目要求，将同一列的所有节点放入同一个数组中。
因此，我们可以对nodes 进行一次遍历，并在遍历的过程中记录上一个节点的列号lastcol。
如果当前遍历到的节点的列号col与 lastcol 相等，则将该节点放入与上一个节点相同的数组中，
否则放入不同的数组中。

代码参考:https://leetcode.cn/problems/vertical-order-traversal-of-a-binary-tree/solution/er-cha-shu-de-chui-xu-bian-li-by-leetcod-clsh/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodes = list()

        def dfs(node, row, col):
            if not node:
                return
            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        nodes.sort()
        ans = list()
        lastcol = float("-inf")

        for col, row, value in nodes:
            if col != lastcol:
                lastcol = col
                ans.append(list())
            ans[-1].append(value)
        return ans