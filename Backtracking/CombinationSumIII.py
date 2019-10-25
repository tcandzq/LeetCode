#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 16:27
# @Author  : tc
# @File    : CombinationSumIII.py
"""
题号 216 组合总和III
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]

利用树列出所有的情况，根据题目的要求进行剪枝

"""
from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [1,2,3,4,5,6,7,8,9]
        res = []
        size = len(candidates)
        def traceback(i,tmp_sum,tmp_list):
            if tmp_sum == n and len(tmp_list) == k:
                res.append(tmp_list)
            for j in range(i,size):
                if tmp_sum + candidates[j] > n:
                    break
                traceback(j+1,tmp_sum+candidates[j],tmp_list+[candidates[j]])

        traceback(0,0,[])
        return res


if __name__ == '__main__':
    k = 3
    n = 7
    solution = Solution()
    print(solution.combinationSum3(k,n))

