# -*- coding: utf-8 -*-
# @File    : 07_ConstructBinaryTree.py
# @Date    : 2020-10-11
# @Author  : tc
"""
剑指 Offer 07.重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

限制：

0 <= 节点个数 <= 5000

注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

preorder第一个元素为root，在inorder里面找到root，在它之前的为左子树（长l1），之后为右子树（长l2）。
preorder[1]到preorder[l1]为左子树,之后为右子树，分别递归。

"""
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        root = TreeNode(preorder[0])

        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])

        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])

        return root


if __name__ == '__main__':
    pass

