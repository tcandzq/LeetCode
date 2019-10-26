#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 18:41
# @Author  : tc
# @File    : CombinationSumIV.py
"""
题号 377 组合总和 Ⅳ
给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。

示例:

nums = [1, 2, 3]
target = 4

所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

请注意，顺序不同的序列被视作不同的组合。

因此输出为 7。
进阶：
如果给定的数组中含有负数会怎么样？
问题会产生什么变化？
我们需要在题目中添加什么限制来允许负数的出现？

回溯法会超时,要用动态规划求解,但我还是写不出来
参考:https://leetcode-cn.com/problems/combination-sum-iv/solution/dong-tai-gui-hua-python-dai-ma-by-liweiwei1419/

dp[i]：对于给定的由正整数组成且不存在重复数字的数组，和为 i 的组合的个数。

很明显当和为0，即target=0时，只有空集[]满足，这也是一种解法且是唯一解，所以dp[0] = 1。

"""
from typing import List
class Solution:
    # 超时版本
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        nums.sort()
        size = len(nums)
        res = []
        def traceback(i,tmp_sum,tmp_list):
            if tmp_sum == target:
                res.append(tmp_list)
            for j in range(i,size):
                if tmp_sum + nums[j] > target:
                    break
                traceback(0, tmp_sum+nums[j], tmp_list+[nums[j]])
        traceback(0, 0, [])
        return len(res)

    # 动态规划版本
    def combinationSum4_2(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if not size or target < 0:
            return 0
        dp = [0 for _ in range(target+1)]
        # 这一步很关键，想想为什么 dp[0] 是 1
        # 因为 0 表示空集，空集和它"前面"的元素凑成一种解法，所以是 1。毕竟空集也是一个集合，一个答案啊！
        # 这一步要加深体会
        dp[0] = 1

        for i in range(1, target+1):
            for num in nums:
                if i >= num:  # target必定为正整数
                    dp[i] += dp[i - num]
        return dp[-1]

if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 4
    solution = Solution()
    print(solution.combinationSum4_2(nums,target))
