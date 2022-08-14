# -*- coding: utf-8 -*-
# @File    : InsertDeleteGetrandomO1DuplicatesAllowed.py
# @Date    : 2022-08-14
# @Author  : tc
"""
381. O(1) 时间插入、删除和获取随机元素 - 允许重复
RandomizedCollection 是一种包含数字集合(可能是重复的)的数据结构。它应该支持插入和删除特定元素，以及删除随机元素。

实现 RandomizedCollection 类:

RandomizedCollection()初始化空的 RandomizedCollection 对象。
bool insert(int val) 将一个 val 项插入到集合中，即使该项已经存在。如果该项不存在，则返回 true ，否则返回 false 。
bool remove(int val) 如果存在，从集合中移除一个 val 项。如果该项存在，则返回 true ，否则返回 false 。注意，如果 val 在集合中出现多次，我们只删除其中一个。
int getRandom() 从当前的多个元素集合中返回一个随机元素。每个元素被返回的概率与集合中包含的相同值的数量 线性相关 。
您必须实现类的函数，使每个函数的 平均 时间复杂度为 O(1) 。

注意：生成测试用例时，只有在 RandomizedCollection 中 至少有一项 时，才会调用 getRandom 。

示例 1:

输入
["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
[[], [1], [1], [2], [], [1], []]
输出
[null, true, false, true, 2, true, 1]

解释
RandomizedCollection collection = new RandomizedCollection();// 初始化一个空的集合。
collection.insert(1);// 向集合中插入 1 。返回 true 表示集合不包含 1 。
collection.insert(1);// 向集合中插入另一个 1 。返回 false 表示集合包含 1 。集合现在包含 [1,1] 。
collection.insert(2);// 向集合中插入 2 ，返回 true 。集合现在包含 [1,1,2] 。
collection.getRandom();// getRandom 应当有 2/3 的概率返回 1 ，1/3 的概率返回 2 。
collection.remove(1);// 从集合中删除 1 ，返回 true 。集合现在包含 [1,2] 。
collection.getRandom();// getRandom 应有相同概率返回 1 和 2 。

哈希表+列表+set()

参考：https://leetcode.cn/problems/insert-delete-getrandom-o1-duplicates-allowed/solution/o1-shi-jian-cha-ru-shan-chu-he-huo-qu-sui-ji-yua-5/
"""
import random

class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []   # 元素列表
        self.index = {}  # 元素—索引 集合
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.vals.append(val)                       # 先在列表添加元素
        if val in self.index:
            self.index[val].add(len(self.vals)-1)   # 若元素已经存在，在元素的索引集合中添加索引
            return False
        else:
            self.index[val] = {len(self.vals)-1}   # 若元素不存在，添加元素索引
            return True
    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.index:
            return False
        last = len(self.vals)-1            # 最后一个元素的索引
        idx = self.index[val].pop()        # 待删除元素的索引
        if len(self.index[val]) == 0:      # 若待删除元素弹出之后，其索引集合为空，则删除其索引集合
            del self.index[val]
        # 思路：悟空：斗战圣佛；六耳：野猴子。佛祖要干掉孙悟空：直接干他说不过去，让
        # 六耳：野猴子 复制包装成 悟空：斗战圣佛，然后干掉：六耳：野猴子，合情合理。
        if idx != last:                    # 若待删除元素不是最后一个元素
            self.vals[idx] = self.vals[last]      # 用最后一个元素覆盖他
            self.index[self.vals[idx]].remove(last) # 删除最后一个元素的索引
            self.index[self.vals[idx]].add(idx)   # 添加待删除元素的索引
        self.vals.pop()   # 删除最后一个元素
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        if self.vals:
            return self.vals[random.randint(0,len(self.vals)-1)]