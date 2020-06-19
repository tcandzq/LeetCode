#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 22:26
# @Author  : tc
# @File    : MergeKSortedLists.py
"""
题号 23 合并K个排序链表
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6


最精彩的是用小顶堆来解决,注意python里的heapq默认是小顶堆

参考1:https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/leetcode-23-he-bing-kge-pai-xu-lian-biao-by-powcai/

参考2：https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/leetcode-23-he-bing-kge-pai-xu-lian-biao-by-powcai/

"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head, (lists[i].val, i))
        while head:
            val, idx = heapq.heappop(head)  # 弹出最小值
            p.next = ListNode(val)
            p = p.next
            if lists[idx].next:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next

    # 分治法
    def mergeKLists2(self,lists:List[ListNode]):
        if not lists:
            return
        n = len(lists)
        return self.merge(lists,0,n-1)

    def merge(self,lists,left,right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists,left,mid)
        l2 = self.merge(lists,mid+1,right)
        return self.mergeTwoLists(l1,l2)

    def mergeTwoLists(self,l1,l2):
        if not l1:return l2
        if not l2:return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2

if __name__ == '__main__':
    pass
