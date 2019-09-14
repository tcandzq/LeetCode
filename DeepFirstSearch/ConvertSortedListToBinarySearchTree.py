#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 11:13
# @Author  : tc
# @File    : ConvertSortedList-toBinarySearchTree.py
"""
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

解法1:可以参考有序数组转换为二叉平衡树那题,直接把有序链表转换为有序数组
解法2:利用快慢指针+递归,先占个坑,后面有时间再补上

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedListToBST(head):
    nums = []
    while head:
        nums.append(head.val)
        head = head.next
    return helper(nums,0,len(nums))

def helper(nums,start,end):
    if start == end:
        return None
    mid = start + (end - start) // 2
    root = TreeNode(nums[mid])
    root.left = helper(nums,start,mid)
    root.right = helper(nums,mid+1,end)
    return root

if __name__ == '__main__':
    head = ListNode(-10)
    node1 = ListNode(-3)
    node2 = ListNode(0)
    node3 = ListNode(5)
    node4 = ListNode(9)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    print(sortedListToBST(head))
