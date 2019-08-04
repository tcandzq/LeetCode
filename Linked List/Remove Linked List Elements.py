#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/4 17:33
# @Author  : tc
# @File    : Remove Linked List Elements.py

"""
删除链表中含有指定元素的节点例如：
 Input:1->2->6->3->4->5->6, val = 6
 OutPut:1->2->3->4->5

链表题主要大部分要借助三个节点:1.手动构造头节点(值无意义)；2.当前节点；3.当前节点的上一个节点

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    if not head:
        return None
    headNode = ListNode(1)  # 头节点
    headNode.next = head
    preNode = headNode  # 当前节点的上一个节点
    cur = headNode.next  # 当前节点
    while cur is not None:
        if cur.val == val:
            preNode.next = cur.next
            cur = cur.next
        else:
            preNode = preNode.next
            cur = cur.next
    return headNode.next


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(6)
    d = ListNode(3)
    e = ListNode(4)
    f = ListNode(5)
    g = ListNode(6)

    res = removeElements(a,6)

    while (res):
        print(res.val)
        result = res.next