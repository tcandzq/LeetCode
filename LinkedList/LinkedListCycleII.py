#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 14:11
# @Author  : tc
# @File    : LinkedListCycleII.py
"""
题号 142 环形链表 II
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。

进阶：
你是否可以不用额外空间解决此题？

参考:https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # hashMap解法
    def detectCycle(self, head: ListNode) -> ListNode:
        tmp = []
        while head:
            if head in tmp:
                return head
            else:
                tmp.append(head)
                head = head.next
        return None

    # 快慢指针解法
    def detectCycle2(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return  # 链表中没有环
            fast, slow = fast.next.next, slow.next  # 快指针的速度是慢指针速度的两倍
            if fast == slow: break  # 第一次相遇
        fast = head
        while fast != slow:  # 第二次相遇 slow指针 位置不变 ，将fast指针重新 指向链表头部节点
            fast, slow = fast.next, slow.next  # 快指针和慢指针的速度一致
        return fast


