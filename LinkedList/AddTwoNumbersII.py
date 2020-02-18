# -*- coding: utf-8 -*-
# @File    : AddTwoNumbersII.py
# @Date    : 2020-02-18
# @Author  : tc
"""
题号 445 两数相加II
给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶:

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

示例:

输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出: 7 -> 8 -> 0 -> 7

使用头插法

参考：https://leetcode-cn.com/problems/add-two-numbers-ii/solution/zui-po-su-jing-jian-de-shuang-zhan-jie-fa-zhu-shi-/

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1,stack2 = [],[]
        dummy = ListNode(-1)
        carry = 0
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        while stack1 or stack2 or carry:
            a = 0 if not stack1 else stack1.pop()
            b = 0 if not stack2 else stack2.pop()
            _sum = a + b + carry
            carry = _sum // 10
            _sum = _sum % 10
            # 使用头插法
            temp = ListNode(_sum)
            temp.next = dummy.next
            dummy.next = temp
        return dummy.next


if __name__ == '__main__':
    node1 = ListNode(7)
    node2 = ListNode(2)
    node3 = ListNode(4)
    node4 = ListNode(3)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(4)

    node5.next = node6
    node6.next = node7


    solution = Solution()
    res = solution.addTwoNumbers(node1,node5)

    while res:
        print(res.val)
        res = res.next