#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/22 15:31
# @Author  : tc
# @File    : AddTwoNumbers.py
"""
题号:2 两数之和
给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

1.这题要注意[5]和[5] 要输出[0,1]的结果,我自己写的代码输出[0]是错的
2.注意一个链表长,一个链表表的情况,处理技巧是在短的后面加0

参考:https://leetcode-cn.com/problems/add-two-numbers/solution/hua-jie-suan-fa-2-liang-shu-xiang-jia-by-guanpengc/
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #  我写的错误版本
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(-1)
        dummy = root
        carry = False
        while l1 and l2:
            if carry:  # 判断是否需要进1
                if (l1.val + l2.val + 1) // 10:
                    root.next = ListNode((l1.val + l2.val + 1) % 10)
                    carry = True
                else:
                    root.next = ListNode((l1.val + l2.val + 1))
                    carry = False
            else:
                if (l1.val + l2.val) // 10:
                    root.next = ListNode((l1.val + l2.val) % 10)
                    carry = True
                else:
                    root.next = ListNode((l1.val + l2.val))
                    carry = False
            l1 = l1.next
            l2 = l2.next
            root = root.next
        while l1:
            if carry:
                if (l1.val + 1) // 10:
                    root.next = ListNode((l1.val + 1) % 10)
                    carry = True
                else:
                    root.next = ListNode((l1.val + 1))
            root = root.next
            l1 = l1.next
        while l2:
            root.next = ListNode(l2.val)
            root = root.next
            l2 = l2.next
        return dummy.next
    #  参考答案
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
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

if __name__ == '__main__':
    l1 = ListNode(5)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)

    l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)

    solution = Solution()
    root = solution.addTwoNumbers2(l1, l2)
    while root:
        print(root.val)
        root = root.next