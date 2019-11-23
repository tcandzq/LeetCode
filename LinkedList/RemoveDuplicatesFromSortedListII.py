#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/23 15:37
# @Author  : tc
# @File    : RemoveDuplicatesFromSortedListII.py
"""
题号 82 删除排序链表中的重复元素II
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3

使用快慢指针是最优雅的解法
参考:https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/solution/kuai-man-zhi-zhen-by-powcai-2/

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 思路一 通过flag 来表示链表中是否有重复
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev,cur = dummy,head
        while cur:
            flag = False
            while cur.next and cur.val == cur.next.val:
                flag = True
                cur = cur.next
            if flag:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next

    # 思路二 通过 快慢指针来表示是否链表中是否有重复
    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head  # 哑结点
        prev,cur = dummy,head # prev:前一个指针, cur:当前指针
        while cur:
            while cur.next and prev.next.val == cur.next.val:
                cur = cur.next
            if prev.next == cur:  # 如果没有重复的结点 前一个指针和当前指针是相连的
                prev = cur
            else:
                prev.next = cur.next
            cur = cur.next
        return dummy.next

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(3)
    node5 = ListNode(4)
    node6 = ListNode(4)
    node7 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7

    solution = Solution()
    print(solution.deleteDuplicates(node1))