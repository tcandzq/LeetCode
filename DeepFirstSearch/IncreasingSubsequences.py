# -*- coding: utf-8 -*-
# @File    : IncreasingSubsequences.py
# @Date    : 2020-02-13
# @Author  : tc
"""
题号 491 递增子序列
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:

输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:

给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。

"""
from typing import List

class Solution:
    # 使用set可以去重
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = set()
        n = len(nums)

        def dfs(nums,i,temp):
            if len(temp) >= 2 :
                res.add(tuple(temp)) # 这里使用tuple，否则会报错
            for j in range(i,n):
                if temp and nums[j] < temp[-1]: # 剪枝
                    continue
                dfs(nums,j+1,temp+[nums[j]])
        dfs(nums,0,[])
        return list(res)



if __name__ == '__main__':
    nums = [4, 6, 7, 7]
    solution = Solution()
    print(solution.findSubsequences(nums))
