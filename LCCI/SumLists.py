# -*- coding: utf-8 -*-
# @File    : SumListsLcci.py
# @Date    : 2022-08-21
# @Author  : tc
"""
给定两个用链表表示的整数，每个节点包含一个数位。
这些数位是反向存放的，也就是个位排在链表首部。
编写函数对这两个整数求和，并用链表形式返回结果。

示例：
输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
输出：2 -> 1 -> 9，即912
进阶：思考一下，假设这些数位是正向存放的，又该如何解决呢?

示例：
输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
输出：9 -> 1 -> 2，即912
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre = ListNode(0)
        cur = pre
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0  # 这个很巧妙,当短链表遍历完时,直接返回0,对结果没有影响,还能很好的处理异常情况
            y = l2.val if l2 else 0
            sum = x + y + carry
            carry = sum // 10
            sum = sum % 10
            cur.next = ListNode(sum)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            cur.next = ListNode(1)

        return pre.next