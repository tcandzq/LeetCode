# -*- coding: utf-8 -*-
# @File    : DesignHashmap.py
# @Date    : 2022-06-20
# @Author  : tc
"""
706. 设计哈希映射
不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
实现 MyHashMap 类：

MyHashMap() 用空映射初始化对象
void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。

示例：

输入：
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
输出：
[null, null, null, 1, -1, null, 1, null, -1]

解释：
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]]
myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]]
myHashMap.get(1);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
myHashMap.get(3);    // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
myHashMap.get(2);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
myHashMap.get(2);    // 返回 -1（未找到），myHashMap 现在为 [[1,1]]

设计 hash 函数需要考虑两个问题：

通过 hash 方法把键 key 转成数组的索引：设计合适的 hash 函数，一般都是对分桶数取模 % 。
处理碰撞冲突问题：拉链法 和 线性探测法。
下面我用了两个方法：

超大数组：简便。
拉链法：大多数编程语言选择的方法。

不定长的拉链数组是说拉链会根据分桶中的 key 动态增长，更类似于真正的链表。
分桶数一般取质数，这是因为经验上来说，质数个的分桶能让数据更加分散到各个桶中。
下面的代码中把分桶数去了 1009，是因为 1009 是大于 1000 的第一个质数。


代码来自:https://leetcode.cn/problems/design-hashmap/solution/xiang-jie-hashmap-de-she-ji-zai-shi-jian-85k9/
"""

class MyHashMap:

    def __init__(self):
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]
        print(self.table)

    def hash(self, key):
        return key % self.buckets

    def put(self, key: int, value: int) -> None:
        hashkey = self.hash(key)
        for item in self.table[hashkey]:
            if item[0] == key:
                item[1] = value
                return
        self.table[hashkey].append([key, value])

    def get(self, key: int) -> int:
        hashkey = self.hash(key)
        print(hashkey)
        for item in self.table[hashkey]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        for i, item in enumerate(self.table[hashkey]):
            if item[0] == key:
                self.table[hashkey].pop(i)
                return