#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/28 22:18
# @Author  : tc
# @File    : SortList.py
"""
题号 148 排序链表
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5

实际是对链表做归并排序

通过链表的快慢指针来得到链表的中间节点

注意快慢指针划分中间节点的代码细节

解法1参考:https://leetcode-cn.com/problems/sort-list/solution/zi-di-xiang-shang-de-gui-bing-pai-xu-java-dai-ma-b/
解法2参考:https://leetcode-cn.com/problems/sort-list/solution/sort-list-gui-bing-pai-xu-lian-biao-by-jyd/

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None  # 让head节点和slow节点断开分别进行递归

        left = self.sortList(head)
        right = self.sortList(head2)

        return self.__merge_two_sorted_list(left, right)

    # 合并两个有序链表
    def __merge_two_sorted_list(self,head1,head2):
        if not head1:
            return head2
        if not head2:
            return head1

        if head1.val < head2.val:
            head1.next = self.__merge_two_sorted_list(head1.next,head2)
            return head1
        else:
            head2.next = self.__merge_two_sorted_list(head1,head2.next)
            return head2

    # 解法2
    def sortList2(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head  # termination.
        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None  # save and cut.
        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)
        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next


if __name__ == '__main__':
    node1 = ListNode(-1)
    node2 = ListNode(5)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(0)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    solution = Solution()
    root = solution.sortList(node1)
    while root:
        print(root.val)
        root = root.next

