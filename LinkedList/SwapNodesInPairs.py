#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/6 12:49
# @Author  : tc
# @File    : SwapNodesInPairs.py

"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表
注:不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换
Input: 1->2->3->4
Output: 2->1->4->3

本题有递归和迭代两种解法，我只会迭代这一种，但也是写了很久才写出来，而且相对递归来说却复杂很多，不够简洁。
在网上看到了大神用递归的解法，比较简单，讲解的也很透彻，具体链接如下:
http://lylblog.cn/blog/4
https://draw.mdnice.com/algorithm/24.html#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%A1%88

递归解法思路:
递归写法要观察本级递归的解决过程，形成抽象模型。递归本质就是反复调用自身，不断重复相同的事情，说明它每一级的功能都是一样的。
因此我们只需要关注一级调用小单元的清情况而不是去思考完整的调用栈，否则一级又一级无从下手。
用递归求解要考虑以下三步:
1.整个递归的终止条件:递归应该在什么时候结束？;2.一级递归需要做什么:在这一级递归中应该完成什么任务？;3.应该返回给上一级的返回值是什么？

针对本题，回答如下:
1.终止条件，当链表没有结点或者只剩下一个结点无法进行交换时，递归结束;

2.单看一级递归的处理，其实只有三个结点组成。前一个结点head，后一个结点head.next，已经完成交换的链表部分，本级递归的任务也就是
交换前两个结点;

3.返回给上一级递归的是已经完成交换处理好的链表

迭代解法:
首先确定需要几个指针。因为是两两结点交换，所以需要前一个指针pre_head和后一个指针next_head两两交换，并不断向后滑动。由于链表在交换的时候
不断变化，所以还有一个cur_head指针来返回当前已经交换完成的链表(这个和递归解法的第二步很相似)。

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 递归解法:

def swapPairs1(head):

    if not head or not head.next:
        return head        # 第一步,递归的终止条件

    #一共三个结点:head,head.next,swapPairs(next.next)(已经完成交换,处理好的结点,看成一个黑盒子,关心输入输出就行了)
    next_head = head.next

    head.next = swapPairs1(next_head.next)  # 这个入参的确定需要注意:记住你本级递归返回给上级递归的是已经完成交换处理的链表，
                                            # 所以入参当然是指向已经完成交换处理链表的指针???(待确定)

    next_head.next = head

    #根据第二步:返回给上一级递归的是当前已经完成交换后，即处理好了的链表部分
    return next_head

#跌代解法:

def swapPairs2(head):
    dummy = ListNode(-1)
    dummy.next = head     # 哑结点
    cur_head = dummy      # 当前节点
    while cur_head.next and cur_head.next.next:
        pre_head = cur_head.next   # 前一个结点
        next_head = cur_head.next.next  # 后一个结点
        cur_head.next = next_head       # 当前节点指向后一个结点
        pre_head.next = next_head.next  # 前一个结点指向下一个结点的下一个结点
        next_head.next = pre_head       # 后一个结点指向前一个结点
        cur_head = pre_head             # 当前节点向后移动一位
    return dummy.next

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)

    a.next = b
    b.next = c
    c.next = d

    res = swapPairs2(a)

    while res:
        print(res.val)
        res = res.next