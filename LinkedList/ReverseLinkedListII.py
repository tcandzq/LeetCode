#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 18:56
# @Author  : tc
# @File    : ReverseLinkedListII.py
"""
题号 92 反转链表II
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

参考:https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/bu-bu-chai-jie-ru-he-di-gui-di-fan-zhuan-lian-biao/

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1:
            return self.reverseN(head,n)
        head.next = self.reverseBetween(head.next,m-1,n-1)
        return head

    successor = None
    def reverseN(self,head,n):
        if n == 1:
            self.successor = head.next
            return head
        last = self.reverseN(head.next, n-1)

        head.next.next = head
        head.next = self.successor
        return last


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    solution = Solution()
    root = solution.reverseBetween(node1,2,4)
    while root:
        print(root.val)
        root = root.next

