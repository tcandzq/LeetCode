# -*- coding: utf-8 -*-
# @File    : ReverseNodesInKGroup.py
# @Date    : 2019-12-21
# @Author  : tc
"""
题号 25 K个一组翻转链表
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

参考:https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/di-gui-si-wei-ru-he-tiao-chu-xi-jie-by-labuladong/

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        a = b = head
        for i in range(k):
            if not b:
                return head
            b = b.next
        new_head = self.reverse(a,b)
        a.next = self.reverseKGroup(b,k)
        return new_head

    # 反转区间[a, b) 的元素，注意是左闭右开(迭代版本)
    def reverse(self,a: ListNode,b: ListNode):
        pre = None
        cur = a
        next = a
        while cur != b:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


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
    print(solution.reverseKGroup(node1,2))