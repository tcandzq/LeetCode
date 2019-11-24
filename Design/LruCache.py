#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/24 14:47
# @Author  : tc
# @File    : lruCache.py
"""
题号 146 LRU缓存机制

运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？

示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4

LRU 缓存算法的核心数据结构就是哈希链表，双向链表和哈希表的结合体.
哈希表查找快，但是数据无固定顺序；链表有顺序之分，插入删除快，但是查找慢。所以结合一下，形成一种新的数据结构：哈希链表。

使用双向链表的目的是因为删除一个节点不光要得到该节点本身的指针，也需要操作其前驱节点的指针，而双向链表才能支持直接查找前驱，保证操作的时间复杂度 O(1)

思路参考:https://leetcode-cn.com/problems/lru-cache/solution/lru-ce-lue-xiang-jie-he-shi-xian-by-labuladong/

代码参考:https://leetcode-cn.com/problems/lru-cache/solution/pythonde-ordereddict-huo-zhe-ha-xi-shuang-xiang-li/
"""
class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0,0)
        self.tail = Node(0,0)  # 头尾虚节点

        self.head.next = self.tail
        self.tail.prev = self.head
        self.lookup = dict()
        self.size = capacity  # 链表元素的数量

    def get(self, key: int) -> int:
        if key in self.lookup:
            node = self.lookup[key]
            self.remove(node)
            self.add(node)  # 保证数据 (key, val) 提到开头
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.remove(self.lookup[key])  # 把旧的数据删除；将新节点key插入到开头；
        if len(self.lookup) == self.size:
            self.remove(self.tail.prev)  # 如果已经满了,需要删除底部节点,并将新加入的节点插到头节点后面
            # del self.lookup[self.tail.prev.key] # remove函数里已经操作了这一步了,不要画蛇添足,引起报错

        # 在头部插入结点
        self.add(Node(key, value))
        # self.lookup[key] = Node(key, value) # add函数里已经操作了这一步了,不要画蛇添足,引起报错

    def remove(self,node):  # 删除表节点
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.lookup[node.key]

    def add(self,node):  # 在链表头部增加节点(在链表头部插入节点,不要和尾虚节点)
        self.lookup[node.key] = node

        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        #  下面这种写法是错误,而且错误很难debug,一定要牢记!!!
        # node.next = self.head.next
        # self.head.next = node
        # self.head.next.prev = node
        # node.prev = self.head


if __name__ == '__main__':

    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    cache.get(2)
    cache.put(4, 4)
    cache.get(1)
    cache.get(3)
    cache.get(4)

