#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/2 11:05
# @Author  : tc
# @File    : ConstructBinaryTreeFromInorderAndPostorderTraversal.py
"""
题号 106 从中序与后序遍历序列构造二叉树
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7


利用分治的思想，也是递归的思想。先构建左子树，再构建右子树。构建左子树函数的入参是左子树的中序和后续遍历数组，构建右子树函数的入参是右子树
的中序和后序遍历数组。

参考:https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/qian-xu-bian-li-python-dai-ma-java-dai-ma-by-liwei/

注意:左子树在中序遍历和后序遍历序列中的位置相同，所以当从后序遍历确定根结点在中序遍历序列的位置pos后，posorder[:pos]表示后序遍历数组中左子树的位置。


"""
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        assert len(inorder) == len(postorder)

        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[-1])
        root = TreeNode(postorder[-1])  # 后序遍历的最后一个结点就是根结点

        # 在中序遍历中找到根结点的索引，得到左右子树的一个划分
        pos = inorder.index(postorder[-1])

        # 注意左子树在中序遍历和后序遍历序列中的位置相同，后续遍历的顺序是左子树->右子树->根结点，所以postorder[:pos]表示左子树
        root.left = self.buildTree(inorder[:pos], postorder[:pos])

        # pos是左子树的位置，-1是根结点的位置，所以postorder[pos:-1]表示右子树
        root.right = self.buildTree(inorder[pos+1:], postorder[pos:-1])

        return root


if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]

    solution = Solution()
    print(solution.buildTree(inorder,postorder))

