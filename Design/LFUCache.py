# -*- coding: utf-8 -*-
# @File    : LFUCache.py
# @Date    : 2022-06-20
# @Author  : tc
"""
460. LFU 缓存
请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。

实现 LFUCache 类：

LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象
int get(int key) - 如果键 key 存在于缓存中，则获取键的值，否则返回 -1 。
void put(int key, int value) - 如果键 key 已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量 capacity 时，则应该在插入新项之前，移除最不经常使用的项。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最近最久未使用 的键。
为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。

当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。对缓存中的键执行 get 或 put 操作，使用计数器的值将会递增。

函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。


双向链表+HashMap
https://leetcode.cn/problems/lfu-cache/solution/ha-xi-biao-shuang-xiang-lian-biao-java-by-liweiwei/
"""
import collections

class Node:
    def __init__(self, key, val, pre=None, nex=None, freq=0):
        self.pre = pre
        self.nex = nex
        self.freq = freq
        self.val = val
        self.key = key

    # 这里的节点插入是插入到self的next节点前
    def insert(self, nex):
        nex.pre = self
        nex.nex = self.nex
        self.nex.pre = nex
        self.nex = nex


def create_linked_list():
    # 额外加入了一个头节点和尾节点方便操作
    head = Node(0, 0)
    tail = Node(0, 0)
    head.nex = tail
    tail.pre = head
    return (head, tail)


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0
        # key是节点的频率,value是双向链表的(头节点,尾节点)
        self.freqMap = collections.defaultdict(create_linked_list)
        self.keyMap = {}

    def delete(self, node):
        if node.pre:
            node.pre.nex = node.nex
            node.nex.pre = node.pre
            # 如果key对应的双向链表只有头节点和尾节点,就删除对应的key和value
            if node.pre is self.freqMap[node.freq][0] and node.nex is self.freqMap[node.freq][-1]:
                self.freqMap.pop(node.freq)
        return node.key

    # 更新节点对应的频率，需要将该节点从freq对应的双向链表移动到freq+1对应的双向链表中，因此需要从freq对应的双向链表中删除该节点
    def increase(self, node):
        node.freq += 1
        # 这个地方为什么要delete?参考上面的注释
        self.delete(node)
        # 新节点插入到该频率对应的双向链表的第一个节点即head.next,因为tail.pre是head
        self.freqMap[node.freq][-1].pre.insert(node)
        if node.freq == 1:
            self.minFreq = 1

        elif self.minFreq == node.freq - 1:
            head, tail = self.freqMap[node.freq - 1]
            if head.nex is tail:
                self.minFreq = node.freq

    def get(self, key: int) -> int:
        if key in self.keyMap:
            # 每get一次，节点的使用频率就会增加一次，就需要对对freq_map中的节点操作
            self.increase(self.keyMap[key])
            return self.keyMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity != 0:
            if key in self.keyMap:
                node = self.keyMap[key]
                node.val = value
            else:
                node = Node(key, value)
                self.keyMap[key] = node
                self.size += 1
            if self.size > self.capacity:
                self.size -= 1
                # 如果容量超了就删除频率最低最久未使用的节点(双向链表的最后一个节点非尾节点)，链表尾的节点即为使用频率最小且插入时间最早的节点
                deleted = self.delete(self.freqMap[self.minFreq][0].nex)
                self.keyMap.pop(deleted)
            self.increase(node)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)