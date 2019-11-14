#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 11:03
# @Author  : tc
# @File    : BinaryIndexTree.py
"""
树状数组的python 实现
参考:https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/shu-zhuang-shu-zu-by-liweiwei1419/
"""

class FenwickTree:
    def __init__(self,n):
        self.size = 0
        self.tree = [0 for _ in range(n+1)]  # 初始化,长度为n+1

    def __lowbit(self,index):
        return index & (-index)

    def update(self,index,delta):  # 单点更新
        while index <= self.size:
            self.tree[index] += delta
            index += self.__lowbit(index)

    def query(self, index):  # 区间查询
        ans = 0
        while index > 0:  # 至少到1,可以取等
            ans += self.tree[index]
            index -= self.__lowbit(index)


