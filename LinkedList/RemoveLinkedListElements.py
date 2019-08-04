#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/4 17:33
# @Author  : tc
# @File    : Remove Linked List Elements.py

"""
删除链表中含有指定元素的结点例如：
 Input:1->2->6->3->4->5->6, val = 6
 OutPut:1->2->3->4->5

链表题主要大部分要借助三个结点:1.手动构造哑结点(值无意义)；2.当前结点；3.当前结点的上一个结点

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeElements(head, value):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    dummy = ListNode(0)  # 头结点
    dummy.next = head
    pre_node = dummy  # 当前结点的上一个结点
    cur = dummy.next  # 当前结点
    while cur:
        if cur.val == value:
            pre_node.next = cur.next
            cur = cur.next
        else:
            pre_node = pre_node.next
            cur = cur.next
    return dummy.next


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(6)
    d = ListNode(3)
    e = ListNode(4)
    f = ListNode(5)
    g = ListNode(6)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    res = removeElements(a,6)

    while (res):
        print(res.val)
        res = res.next
