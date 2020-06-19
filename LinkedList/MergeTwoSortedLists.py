#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 12:36
# @Author  : tc
# @File    : MergeTwoSortedLists.py
"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
Input:1->2->4, 1->3->4
Output:1->1->2->3->4->4

这道题关键地方有两个:1.使用哨兵节点prehead 不断指向最新的合并后的结点，返回合并后的链表;
                   2.当其中某个链表遍历结束后，由于链表是有序的，它包含的所有元素都比前面已经合并的链表中的所有元素都要大
                     这样我们就可以直接把非空链表接在合并链表的后面。


参考：https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/yi-kan-jiu-hui-yi-xie-jiu-fei-xiang-jie-di-gui-by-/

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 解法1：迭代，递归我不是很理解，所以写不出来

def mergeTwoListsGov(l1,l2):
    dummy = ListNode(-1)  # 哑结点
    prev = dummy  # 哨兵结点
    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next
    prev.next = l1 if l1 is not None else l2  # 麻烦熟悉下python的三元组写法
    return dummy.next


# 解法2:很暴力，很蠢，遍历两个链表，将值收集起来塞进一个列表，排序，最后将列表转为链表

def mergeTwoLists(l1, l2):
    l1_list = []
    l2_list = []
    while l1:
        l1_list.append(l1.val)
        l1 = l1.next
    while l2:
        l2_list.append(l2.val)
        l2 = l2.next
    end = l1_list + l2_list
    dummy = ListNode(-1)
    tem_node = dummy
    end = sorted(end)
    for num in end:
        tem_node.next = ListNode(num)
        tem_node = tem_node.next

    return dummy.next

class Solution:

    # 优雅
    def mergeTwoLists2(self,l1:ListNode,l2:ListNode) -> ListNode:
        if not l1:return l2
        if not l2:return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists2(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists2(l1,l2.next)
            return l2
if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(4)

    a.next = b
    b.next = c

    d = ListNode(1)
    e = ListNode(3)
    f = ListNode(4)

    d.next = e
    e.next = f

    res = mergeTwoListsGov(a, d)

    while res:
        print(res.val)
        res = res.next