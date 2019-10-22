#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 18:00
# @Author  : tc
# @File    : CombinationSum.py
"""
题号 437 路径总和 III
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]

示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

"做搜索、回溯问题的套路是画图，代码其实就是根据画出的树形图写出来的。"

又是一套拥有标准模板写法的题。这种题就是在所有可能的情况中选出满足target的组合,通过画图可以比较详细罗列所有的情况

参考1:https://leetcode-cn.com/problems/combination-sum/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-2/
参考2:https://leetcode-cn.com/problems/combination-sum/solution/xue-yi-tao-zou-tian-xia-hui-su-suan-fa-by-powcai/
"""
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []

        # 剪枝的前提是数组元素排序
        # 深度深的边不能比深度浅的边还小
        # 要排序的理由：1、前面用过的数后面不能再用；2、下一层边上的数不能小于上一层边上的数。
        candidates.sort()
        # 在遍历的过程中记录路径，一般而言它是一个栈
        path = []  # 使用栈
        res = []
        # 注意要传入 size ，在 range 中， size 取不到
        self.__dfs(candidates, 0, size, path, res, target)
        return res

    def __dfs(self, candidates, begin, size, path, res, target):
        # 先写递归终止的情况
        if target == 0:
            # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
            # 或者使用 path.copy()
            res.append(path[:])

        for index in range(begin, size):
            residue = target - candidates[index]
            # “剪枝”操作，不必递归到下一层，并且后面的分支也不必执行
            if residue < 0:
                break
            path.append(candidates[index])
            # 因为下一层不能比上一层还小，起始索引还从 index 开始
            self.__dfs(candidates, index, size, path, res, residue)
            path.pop()  # 状态重置

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        print(candidates)
        # 在遍历的过程中记录路径，一般而言它是一个栈
        path = []  # 使用栈
        res = []
        # 注意要传入 size ，在 range 中， size 取不到
        self.__dfs2(candidates,  path, res, 0,target)
        return res

    def __dfs2(self, candidates,path, res, _sum, target):
        # 先写递归终止的情况
        if _sum == target:
            # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
            # 或者使用 path.copy()
            res.append(path[:])
        if _sum > target:
            return
        for i in range(len(candidates)):
            # “剪枝”操作，不必递归到下一层，并且后面的分支也不必执行
            if _sum + candidates[i]> target:
                return
            path.append(candidates[i])
            # 因为下一层不能比上一层还小，起始索引还从 index 开始
            self.__dfs2(candidates, path, res, _sum + candidates[i],target)
            path.pop()  # 状态重置

    def combinationSum3(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(tmp_sum, tmp):
            if tmp_sum > target:
                return
            if tmp_sum == target:
                res.append(tmp)
                return
            for j in range(n):
                if tmp_sum > target:
                    break
                backtrack(tmp_sum +candidates[j] , tmp + [candidates[j]])
        backtrack(0, [])
        return res

if __name__ == '__main__':
    candidates = [2, 3, 5]
    target = 8
    solution = Solution()
    print(solution.combinationSum3(candidates,target))
