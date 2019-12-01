#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 17:28
# @Author  : tc
# @File    : PalindromeLinkedList.py
"""
题号 234 回文链表
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

快慢指针+反转链表可以做到O(n) 时间复杂度和 O(1) 空间复杂度

参考:https://leetcode-cn.com/problems/palindrome-linked-list/solution/dong-hua-yan-shi-234-hui-wen-lian-biao-by-user7439/

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 辅助列表解法
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        left = 0
        right = len(tmp) - 1
        print(tmp)
        while left < right:
            if tmp[left] != tmp[right]:
                return False
            left += 1
            right -= 1
        return True

    # 双指针 + 反转
    def isPalindrome2(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        cur = head
        slow,fast = cur,cur.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        new_head = slow.next
        slow.next = None
        second_head = self.reverse_list(new_head)
        while second_head:
            if head.val != second_head.val:
                return False
            head,second_head = head.next,second_head.next
        return True
    # 反转链表
    def reverse_list(self,head):
        if not head or not head.next:
            return head
        p = self.reverse_list(head.next)
        head.next.next = head
        head.next = None
        return p


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(1)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    solution = Solution()
    print(solution.isPalindrome2(node1))

