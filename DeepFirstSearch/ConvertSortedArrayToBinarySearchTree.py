#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/14 8:49
# @Author  : tc
# @File    : ConvertSortedArrayToBinarySearchTree.py
"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

参考:https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-24/

一定要善用二分+递归
边界处理无脑用左闭右开就完了
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sortedArrayToBST(nums):
    return helper(nums,0,len(nums))


def helper(nums,left,right):
    if left == right:
        return None
    mid = left + (right - left) // 2
    root = TreeNode(nums[mid])
    root.left = helper(nums, left, mid)
    root.right = helper(nums, mid+1, right)  # 这里其实蕴含了二分查找模板中的left = mid + 1和right = mid
    return root

if __name__ == '__main__':
    nums = [-10,-3,0,5,9]
    print(sortedArrayToBST(nums))