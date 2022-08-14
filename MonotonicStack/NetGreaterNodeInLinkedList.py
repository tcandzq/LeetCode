# -*- coding: utf-8 -*-
# @File    : NetGreaterNodeInLinkedList.py
# @Date    : 2022-08-14
# @Author  : tc
"""
1019. 链表中的下一个更大节点
给定一个长度为 n 的链表 head

对于列表中的每个节点，查找下一个 更大节点 的值。也就是说，对于每个节点，找到它旁边的第一个节点的值，这个节点的值 严格大于 它的值。

返回一个整数数组 answer ，其中 answer[i] 是第 i 个节点( 从1开始 )的下一个更大的节点的值。如果第 i 个节点没有下一个更大的节点，设置 answer[i] = 0 。

示例 1：
输入：head = [2,1,5]
输出：[5,5,0]

示例 2：
输入：head = [2,7,4,3,5]
输出：[7,0,5,5,0]

提示：

链表中节点数为 n
1 <= n <= 104
1 <= Node.val <= 109

单调栈解法

https://leetcode.cn/problems/next-greater-node-in-linked-list/solution/5chong-jie-jue-fang-shi-tu-wen-xiang-jie-by-sdwwld/
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List,Optional
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # 右边第一个比它的元素,很明显使用单调栈,由于是链表，只能正序遍历了,用栈内元素模式
        index = 0
        stack = []
        ans = []
        while head:
            ans.append(0)
            while stack and stack[-1][1] < head.val:
                ans[stack[-1][0]] = head.val
                stack.pop()

            stack.append((index, head.val))
            head = head.next
            index += 1
        return ans