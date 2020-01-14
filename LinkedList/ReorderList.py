# -*- coding: utf-8 -*-
# @File    : ReorderList.py
# @Date    : 2020-01-14
# @Author  : tc
"""
题号 143 重排链表
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

参考:https://leetcode-cn.com/problems/reorder-list/solution/yong-zhan-fan-zhuan-huo-zhe-zhi-jie-fan-zhuan-by-p/

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return None
        p = head
        stack = []
        # 把所有节点压入栈中
        while p:
            stack.append(p)
            p = p.next
        # 长度
        n = len(stack)
        # 找到中点前一个位置
        count = (n - 1) // 2
        p = head
        while count:
            # 弹出栈顶
            tmp = stack.pop()
            # 与链头拼接
            tmp.next = p.next
            p.next = tmp
            # 移动一个位置
            p = tmp.next
            count -= 1
        stack.pop().next = None
