#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/4 22:02
# @Author  : tc
# @File    : RemoveDuplicatesFromSortedList.py
"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
1.Input:1->1->2
  Output: 1->2

2.Input:1->1->2->3->3
  Output:1->2->3

https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/submissions/

注意： 1.问题是已经排序了,所以所有重复的结点会连在一起

      2.当前结点遇到与下一个结点值一样的结点时，需要让当前结点的前一个结点指向重复结点的下一个结点，而这个前
       一个结点不能向后滑动，需要与新指向的结点再次比较。

      3.if语句中的cur.next可能会空

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(head):
    if not head or not head.next:
        return head
    headNode = ListNode(1)
    headNode.next = head  # 创建一个哑结点
    cur = headNode.next  # 创建一个当前结点
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return headNode.next

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(1)
    c = ListNode(2)
    d = ListNode(3)
    e = ListNode(3)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    result = deleteDuplicates(a)

    while (result):
        print(result.val)
        result = result.next