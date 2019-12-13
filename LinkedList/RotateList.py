#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 21:38
# @Author  : tc
# @File    : RotateList.py
"""
题号 61 旋转链表
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

参考:https://leetcode-cn.com/problems/rotate-list/solution/chuan-zhen-yin-xian-by-liweiwei1419/

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 丑陋版
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or not k:
            return head
        length = 0
        cur = head
        while cur.next:
            length += 1
            cur = cur.next
        length += 1
        if not (k % length):
            return head
        times = length - (k % length) - 1
        fast = head
        while times:
            times -= 1
            fast = fast.next
        new_head = fast.next
        fast.next = None
        cur.next = head
        return new_head

    # 稍微美化版
    def rotateRight2(self, head: ListNode, k: int) -> ListNode:
        # 特判
        if head is None or head.next is None or k <= 0:
            return head

        # 先看链表有多少元素
        node = head
        # 先数这个链表的长度
        counter = 1
        while node.next:
            node = node.next
            counter += 1

        k = k % counter
        if k == 0:
            return head

        node.next = head
        node = head
        # 可以取一些极端的例子找到规律
        # counter - k - 1
        for _ in range(counter - k - 1):
            node = node.next
        new_head = node.next
        node.next = None
        return new_head

if __name__ == '__main__':
    node1 = ListNode(0)
    node2 = ListNode(1)
    node3 = ListNode(2)
    # node4 = ListNode(4)
    # node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    # node3.next = node4
    # node4.next = node5

    solution = Solution()
    root = solution.rotateRight(node1,6)
    while root:
        print(root.val)
        root = root.next
