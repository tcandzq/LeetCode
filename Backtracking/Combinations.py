#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 23:21
# @Author  : tc
# @File    : Combinations.py
"""
题号 77 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

leetcode 216 组合总和III 的弱鸡版

参考1:https://leetcode-cn.com/problems/combinations/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-ma-/
参考2:https://leetcode-cn.com/problems/combinations/solution/hui-su-suan-fa-by-powcai-4/

依然是两套模板解法，不过我更偏向于解法二和解法三，代码简洁，容易理解。

"""
from typing import List

class Solution:

    def combine1(self, n: int, k: int) -> List[List[int]]:
        # 先把不符合条件的情况去掉
        if n <= 0 or k <= 0 or k > n:
            return []
        res = []
        self.__dfs(1, k, n, [], res)
        return res

    def __dfs(self, start, k, n, pre, res):
        # 当前已经找到的组合存储在 pre 中，需要从 start 开始搜索新的元素
        # 在第 k 层结算
        if len(pre) == k:
            res.append(pre[:])
            return

        for i in range(start, n + 1):
            pre.append(i)
            # 因为已经把 i 加入到 pre 中，下一轮就从 i + 1 开始
            # 注意和全排列问题的区别，因为按顺序选择，因此无须使用 used 数组
            self.__dfs(i + 1, k, n, pre, res)
            # 回溯的时候，状态重置
            pre.pop()

    # k 递减为 0
    def combine2(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i, k, tmp):
            if k == 0:
                res.append(tmp)
                return
            for j in range(i, n + 1):
                backtrack(j + 1, k - 1, tmp + [j])

        backtrack(1, k, [])
        return res

    # 累加和为count
    def combine3(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i, count, tmp):
            if count == k:
                res.append(tmp)
                return
            for j in range(i, n + 1):  # 从候选数组的当前索引值的下一位开始，保证1到n的数不会被重复使用
                backtrack(j + 1, count+1, tmp + [j])

        backtrack(1, 0, [])
        return res


if __name__ == '__main__':
    n = 4
    k = 2
    solution = Solution()
    print(solution.combine3(n,k))
