# -*- coding: utf-8 -*-
# @File    : 24_ReverseList.py
# @Date    : 2020-10-31
# @Author  : tc
"""
剑指 Offer 24. 反转链表
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL


限制：

0 <= 节点个数 <= 5000

注意：本题与主站 206 题相同：https://leetcode-cn.com/problems/reverse-linked-list/

递归参考：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/solution/ru-guo-ni-kan-wan-ping-lun-he-ti-jie-huan-you-wen-/

迭代法参考：https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        print(p.val)
        head.next.next = head
        head.next = None
        return p

    def reverseList2(self,head:ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre








if __name__ == '__main__':
    pass