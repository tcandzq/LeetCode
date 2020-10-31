#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/15 15:41
# @Author  : tc
# @File    : ReverseLinkedList.py
"""
反转一个单链表。
示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

参考:https://leetcode-cn.com/problems/reverse-linked-list/solution/fan-zhuan-lian-biao-by-leetcode/

递归:记住递归要返回的是什么,以及递归出栈后,后面的代码要怎么写？

不妨假设链表为1，2，3，4，5。按照递归，当执行reverseList（5）的时候返回了5这个节点，reverseList(4)中的p就是5这个节点，
我们看看reverseList（4）接下来执行完之后，5->next = 4, 4->next = null。这时候返回了p这个节点，也就是链表5->4->null，
接下来执行reverseList（3）代码解析为4->next = 3,3->next = null，这个时候p就变成了，5->4->3->null, reverseList(2),
reverseList(1)依次类推，p就是:5->4->3->2->1->null

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 递归版本
def reverseList(head):
    if not head or not head.next:
        return head
    p = reverseList(head.next)
    head.next.next = head  # 这里head指向的节点是最关键的,
    head.next = None
    return p

# 迭代版本
def reverseList2(head):
    cur = head
    next = head
    prev = None
    while cur:
        next = cur.next   # 保留当前节点的下一个节点
        cur.next = prev  # 让当前节点指向上一个节点
        prev = cur      # 前一个节点向后移动
        cur = next        # 当前结点向后移
    return prev           # 注意返回的是prev 不是curr


if __name__ == '__main__':
    root = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    root.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    res = reverseList2(root)



