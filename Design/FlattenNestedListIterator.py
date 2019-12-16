# -*- coding: utf-8 -*-
# @File    : FlattenNestedListIterator.py
# @Date    : 2019-12-16
# @Author  : tc
"""
题号 341 扁平化嵌套列表迭代器
给定一个嵌套的整型列表。设计一个迭代器，使其能够遍历这个整型列表中的所有整数。

列表中的项或者为一个整数，或者是另一个列表。

示例 1:

输入: [[1,1],2,[1,1]]
输出: [1,1,2,1,1]
解释: 通过重复调用 next 直到 hasNext 返回false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
示例 2:

输入: [1,[4,[6]]]
输出: [1,4,6]
解释: 通过重复调用 next 直到 hasNext 返回false，next 返回的元素的顺序应该是: [1,4,6]。

参考：https://leetcode-cn.com/problems/flatten-nested-list-iterator/solution/python-die-dai-qi-ban-ben-chao-99-by-user2198v/

"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """


class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        def build_generator(nestedList):  # 利用yield把nestedList 转化为生成器
            for i in nestedList:
                if i.isInteger():
                    yield i.getInteger()
                else:
                    i = i.getList()
                    for j in build_generator(i):
                        yield j
        self.g = build_generator(nestedList)

    def next(self):
        """
        :rtype: int
        """
        return self.v

    def hasNext(self):
        """
        :rtype: bool
        """
        try:
            self.v = next(self.g)  # 注意这里是python内置的next()函数，返回迭代器的下一项
            return True
        except:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


if __name__ == '__main__':
    i, v = NestedIterator([[1,1],2,[1,1]]), []
    while i.hasNext():
        v.append(i.next())
    print(v)


