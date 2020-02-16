# -*- coding: utf-8 -*-
# @File    : LinkedListRandomNode.py
# @Date    : 2020-02-15
# @Author  : tc
"""
替换 382 链表随机节点
给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。

进阶:
如果链表十分大且长度未知，如何解决这个问题？你能否使用常数级空间复杂度实现？

示例:

// 初始化一个单链表 [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom()方法应随机返回1,2,3中的一个，保证每个元素被返回的概率相等。
solution.getRandom();

思路参考：

代码参考：https://leetcode.com/problems/linked-list-random-node/discuss/85662/java-solution-with-cases-explain

思考参考：https://leetcode.com/problems/linked-list-random-node/discuss/85659/Brief-explanation-for-Reservoir-Sampling
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        import random
        c = self.head
        r = c.val
        i = 1
        while c.next:
            c = c.next
            if random.randint(0, i) == i:
                r = c.val
            i += 1
        return r



