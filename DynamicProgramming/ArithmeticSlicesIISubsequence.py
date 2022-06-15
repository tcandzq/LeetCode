# -*- coding: utf-8 -*-
# @File    : ArithmeticSlicesIISubsequence.py
# @Date    : 2022-06-16
# @Author  : tc
"""
446. 等差数列划分 II - 子序列
给你一个整数数组 nums ，返回 nums 中所有 等差子序列 的数目。
如果一个序列中 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该序列为等差序列。

例如，[1, 3, 5, 7, 9]、[7, 7, 7, 7] 和 [3, -1, -5, -9] 都是等差序列。
再例如，[1, 1, 2, 5, 7] 不是等差序列。
数组中的子序列是从数组中删除一些元素（也可能不删除）得到的一个序列。

例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。
题目数据保证答案是一个 32-bit 整数。

示例 1：

输入：nums = [2,4,6,8,10]
输出：7
解释：所有的等差子序列为：
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
示例 2：

输入：nums = [7,7,7,7,7]
输出：16
解释：数组中的任意子序列都是等差子序列。
"""
from typing import List

import collections
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        # dp第i元素是一个字典，它的key是等差序列的公差，value是以nums[i]结尾组成的、公差为key大小的长度大于等于2的等差子序列的个数
        dp = [collections.defaultdict(int) for _ in range(n)]
        res = 0
        for i in range(n):
            # 寻找的是匹配的nums[j]
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
                # 这时候注意要加的是 dp[j][diff]因为只有j位置也出现了同样的diff的时候，才会和i一起形成长度> 3的等差数列。
                if dp[j][diff]:
                    res += dp[j][diff]
        return res