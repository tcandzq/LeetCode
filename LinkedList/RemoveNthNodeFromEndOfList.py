#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 1:03
# @Author  : tc
# @File    : RemoveNthNodeFromEndOfList.py

"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

Input: 1->2->3->4->5, 和 n = 2
Output:  1->2->3->5

这个问题一看就是快慢指针的问题，但有很多细节需要注意，否则代码写起来非常冗余比如我这样的

解法1：我自己的解法
解法2: leetcode官网的接答，巧妙使用了哑结点的功能，规避在链表长度为n，删除倒数n个结点即头结点的异常情况
       代码比较优雅

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#解法1
def removeNthFromEnd(head, n):
    if not head or not head.next:
        return None
    dummy = ListNode(0)
    dummy.next = head
    #快指针
    first_pointer = dummy.next
    #慢指针
    second_pointer = dummy.next
    for i in range(n):
        first_pointer = first_pointer.next
    #需要考虑first_pointer为None时的情况
    if not first_pointer:
        return head.next
    while first_pointer.next:
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next

    second_pointer.next = second_pointer.next.next

    return dummy.next

#官方解法
def removeNthFromEndGov(head, n):
    dummy = ListNode(0)
    dummy.next = head
    #快慢指针直接指向哑结点，规避了删除头结点的情况，使得代码看起来很简洁
    first_pointer = dummy
    second_pointer = dummy
    for i in range(n + 1):
        first_pointer = first_pointer.next
    while first_pointer:
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next

    second_pointer.next = second_pointer.next.next

    return dummy.next

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    result1 = removeNthFromEnd(a, 2)

    # result2 = removeNthFromEndGov(a, 2)

    while (result1):
        print(result1.val)
        result1 = result1.next