"""
题号 380 常数时间插入、删除和获取随机元素
设计一个支持在平均时间复杂度 O(1) 下，执行以下操作的数据结构。

insert(val)：当元素 val 不存在时，向集合中插入该项。
remove(val)：元素 val 存在时，从集合中移除该项。
getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。
示例 :

// 初始化一个空的集合。
RandomizedSet randomSet = new RandomizedSet();

// 向集合中插入 1 。返回 true 表示 1 被成功地插入。
randomSet.insert(1);

// 返回 false ，表示集合中不存在 2 。
randomSet.remove(2);

// 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
randomSet.insert(2);

// getRandom 应随机返回 1 或 2 。
randomSet.getRandom();

// 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
randomSet.remove(1);

// 2 已在集合中，所以返回 false 。
randomSet.insert(2);

// 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
randomSet.getRandom();

Hash + List

这里在删除val的时候要记得在数组中把排在val后面的索引变掉，因为删除一个元素后，数组变短了。

代码中删除val的操作很牛逼：
1.把字典中：把val的索引赋给list[-1];
2.在数组中：把list[-1]赋给val,然后直接删除list[-1]。

这种思想在剑值offer第18题 删除链表是一致的。即通过将待删除值赋给其他值，然后直接删除重复值即可。

"""
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.d = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.d:
            return False
        else:
            self.d[val] = len(self.data)
            self.data.append(val)
            return True
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.d:
            return False
        else:
            self.d[self.data[-1]] = self.d[val]  # 把val的索引赋给data[-1];
            self.data[self.d.pop(val)] = self.data[-1]  # 把data[-1]赋给val
            self.data.pop()  # 直接删除data[-1]
            return True
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.data[random.randint(0, len(self.data)-1)]