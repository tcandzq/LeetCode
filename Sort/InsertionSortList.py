#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 23:19
# @Author  : tc
# @File    : InsertionSortList.py
"""
题号 147 对链表进行插入排序
对链表进行插入排序。

动图请参考:https://leetcode-cn.com/problems/insertion-sort-list/

插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

 

插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。
 

示例 1：

输入: 4->2->1->3
输出: 1->2->3->4
示例 2：

输入: -1->5->3->4->0
输出: -1->0->3->4->5

插入排序而已

代码的细节还需慢慢琢磨

参考1:https://leetcode-cn.com/problems/insertion-sort-list/solution/jia-ge-tailsu-du-jiu-kuai-liao-by-powcai/
参考2:https://leetcode-cn.com/problems/insertion-sort-list/comments/

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 解法1(标准的写法)
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 找个排头
        dummy = ListNode(-1)
        # 依次拿head节点
        cur = head
        while cur:
            # 把下一次节点提前保持下来
            tmp = cur.next
            pre = dummy
            # 找到插入的位置
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            # 进行插入操作
            cur.next = pre.next
            pre.next = cur
            cur = tmp
        return dummy.next

    # 解法2(优化)
    def insertionSortList2(self, head: ListNode) -> ListNode:
        # 找个排头
        dummy = ListNode(float("-inf"))
        pre = dummy
        tail = dummy
        # 依次拿head节点
        cur = head
        while cur:
            if tail.val < cur.val:
                tail.next = cur
                tail = cur
                cur = cur.next
            else:
                # 把下一次节点保持下来
                tmp = cur.next
                tail.next = tmp
                # 找到插入的位置
                while pre.next and pre.next.val < cur.val:
                    pre = pre.next
                # 进行插入操作
                cur.next = pre.next
                pre.next = cur
                pre = dummy
                cur = tmp
        return dummy.next

    # 解法3
    def insertionSortList3(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val <= head.next.val:
                head = head.next
                continue
            pre = dummy
            while pre.next.val < head.next.val:
                pre = pre.next
            curr = head.next
            head.next = curr.next
            curr.next = pre.next
            pre.next = curr
        return dummy.next

if __name__ == '__main__':
    node1 = ListNode(-1)
    node2 = ListNode(5)
    node3 = ListNode(3)
    node4 = ListNode(4)


    node1.next = node2
    node2.next = node3
    node3.next = node4

    solution = Solution()
    root = solution.insertionSortList3(node1)

    while root:
        print(root.val)
        root = root.next


