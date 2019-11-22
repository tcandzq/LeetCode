#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 20:20
# @Author  : tc
# @File    : DeleteNodeInALinkedList.py
"""
题号 237 删除链表中的节点
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

现有一个链表 -- head = [4,5,1,9]，它可以表示为:


示例 1:

输入: head = [4,5,1,9], node = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], node = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
 

说明:

链表至少包含两个节点。
链表中所有节点的值都是唯一的。
给定的节点为非末尾节点并且一定是链表中的一个有效节点。
不要从你的函数中返回任何结果。

题目只给定了要删除的结点,但不知道删除结点的前一个结点,但我们操作值啊,用删除结点的后一个结点的值覆盖删除结点.

参考:https://leetcode-cn.com/problems/delete-node-in-a-linked-list/solution/shan-chu-lian-biao-zhong-de-jie-dian-by-leetcode/

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node:ListNode) ->None:
        node.val = node.next.val
        node.next = node.next.next



if __name__ == '__main__':
    node1 = ListNode(4)
    node2 = ListNode(5)
    node3 = ListNode(1)
    node4 = ListNode(9)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    solution = Solution()
    print(solution.deleteNode(node1))