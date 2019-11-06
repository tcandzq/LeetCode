#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 11:33
# @Author  : tc
# @File    : CombinationSumI.py
"""
题号 40 组合总和 II
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

可以从两个角度来解决问题
1.累加和=target;
2.target递减 = 0

参考1:https://leetcode-cn.com/problems/combination-sum-ii/solution/hui-su-xi-lie-by-powcai/
参考2:https://leetcode-cn.com/problems/combination-sum-ii/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-3/
"""
from typing import List


class Solution:

    # 第一种方法累加和=target
    def combinationSum2_1(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(i, tmp_sum, tmp_list):
            if tmp_sum == target:
                res.append(tmp_list)
                return
            for j in range(i, n):
                if tmp_sum + candidates[j] > target : break
                if j > i and candidates[j] == candidates[j - 1]: continue
                backtrack(j+1, tmp_sum + candidates[j], tmp_list + [candidates[j]])

        backtrack(0, 0, [])
        return res

    def combinationSum2_2(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        res = []

        self.__dfs(candidates, size, 0, [], target, res)
        return res

    def __dfs(self, candidates, size, start, path, residue, res):
        if residue == 0:
            res.append(path[:])
            return

        for index in range(start, size):
            if candidates[index] > residue:
                break

            # 剪枝的前提是数组升序排序
            if index > start and candidates[index - 1] == candidates[index]:
                # [1, 1, 2, 5, 6, 7, 10]
                # 0 号索引的 1 ，从后面 6 个元素中搜索
                # 1 号索引也是 1 ，从后面 5 个元素（是上面 6 个元素的真子集）中搜索，这种情况显然上面已经包含
                continue

            path.append(candidates[index])
            # 这里要传入 index + 1，因为当前元素不能被重复使用
            # 如果 index + 1 越界，传递到下一个方法中，什么也不执行
            self.__dfs(candidates, size, index + 1, path, residue - candidates[index], res)
            path.pop()

    def combinationSum2_3(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        res = []
        self.__dfs2(candidates,size,0,[],0,res)
        return res

    def __dfs2(slef, candidates, size, start, path, sum, res):
        if sum == target:
            res.append(path[:])

        for index in range(start,size):
            if sum > target:
                break
            if index > start and candidates[index - 1] == candidates[index]:
                continue
            path.append(candidates[index])


if __name__ == '__main__':
    candidates = [2, 5, 2, 1, 2]
    target = 5
    solution = Solution()
    print(solution.combinationSum2_1(candidates, target))
