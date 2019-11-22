#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 12:49
# @Author  : tc
# @File    : LinkedListCycle.py
"""
题号 141 环形链表
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。

参考:https://leetcode-cn.com/problems/linked-list-cycle/solution/dong-hua-yan-shi-141-huan-xing-lian-biao-by-user74/
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # hashMap解法
    def hasCycle(self, head: ListNode) -> bool:
        tmp = []
        while head:
            if head in tmp:
                return True
            else:
                tmp.append(head)
                head = head.next
        return False

    # 快慢指针(可以做标准写法)
    def hasCycle2(self, head: ListNode) -> bool:
        fast,slow = head,head
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False



