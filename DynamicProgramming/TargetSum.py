#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/3 11:31
# @Author  : tc
# @File    : TargetSum.py
"""
题号:494 目标和
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例 1:

输入: nums: [1, 1, 1, 1, 1], S: 3
输出: 5
解释:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。
注意:
数组非空，且长度不会超过20。
初始的数组的和不会超过1000。
保证返回的最终结果能被32位整数存下。

本题有三种解法:https://leetcode-cn.com/problems/target-sum/solution/python-dfs-xiang-jie-by-jimmy00745/
1.DFS 每个数都有在前面加上"+"和"-"两种选择;
2.01背包问题 把加号和减号和转换程对应的正数和负数,我没想到;
3.动态规划 用字典和元组来表示dp的状态,真巧妙.

我只想到了第一种和第三种,递归方程式和DP方程都写出来了,但苦于代码写不出来,看来还是代码写少了。

"""
from typing import List

class Solution:
    #  1.深度优先遍历解法(每一个数的前面都有加+和加-两种选择)
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        count = 0

        self.dfs(0,nums,S,count)
        return count

    def dfs(self,index,nums,S,count):
        if index == len(nums)-1:
            count += 1
            return
        self.dfs(index+1,nums[index+1:],S-nums[index],count)  # 在该数字前加+
        self.dfs(index+1,nums[index+1:],S+nums[index],count)  # 在该数字前面加-

    #  3.动态规划解法
    def findTargetSumWays3(self, nums: List[int], S: int) -> int:
        start = -sum(nums)
        end = sum(nums)
        dp = {(0,0): 1}  # 用字典的好处就是当字典没有查找到对应位置的元素时(即异常值),可以返回默认值,这条就省去了复杂的边界处理
        if end < S or start > S:
            return 0
        for i in range(1, len(nums)+1):
            for j in range(start, end+1):
                dp[(i, j)] = dp.get((i-1, j-nums[i-1]), 0) + dp.get((i-1, j+nums[i-1]), 0)
        return dp.get((len(nums), S), 0)


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    S = 3
    solution = Solution()
    print(solution.findTargetSumWays3(nums,S))