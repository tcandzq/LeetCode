# -*- coding: utf-8 -*-
# @File    : MinimumCostToMergeStones.py
# @Date    : 2022-08-21
# @Author  : tc
"""
1000. 合并石头的最低成本
有 N 堆石头排成一排，第 i 堆中有 stones[i] 块石头。
每次移动（move）需要将连续的 K 堆石头合并为一堆，而这个移动的成本为这 K 堆石头的总数。
找出把所有石头合并成一堆的最低成本。如果不可能，返回 -1 。

示例 1：
输入：stones = [3,2,4,1], K = 2
输出：20
解释：
从 [3, 2, 4, 1] 开始。
合并 [3, 2]，成本为 5，剩下 [5, 4, 1]。
合并 [4, 1]，成本为 5，剩下 [5, 5]。
合并 [5, 5]，成本为 10，剩下 [10]。
总成本 20，这是可能的最小值。

示例 2：
输入：stones = [3,2,4,1], K = 3
输出：-1
解释：任何合并操作后，都会剩下 2 堆，我们无法再进行合并。所以这项任务是不可能完成的。.

示例 3：
输入：stones = [3,5,1,2,6], K = 3
输出：25
解释：
从 [3, 5, 1, 2, 6] 开始。
合并 [5, 1, 2]，成本为 8，剩下 [3, 8, 6]。
合并 [3, 8, 6]，成本为 17，剩下 [17]。
总成本 25，这是可能的最小值。

定义dp[i][j][k]为合并第i堆到第j堆石头为k堆的成本，状态转移方程有关键两点：

dp[i][j][1] = dp[i][j][k] + sum(i, j)。不能直接求出合并为1堆的成本，得先合并成k堆。
dp[i][j][m] = min(dp[i][p][1] + dp[p + 1][j][m - 1])，i <= p < j，2 <= m <= k。
这里m为堆数，不能直接用k是因为右部分的存在，要对右部分继续划分求解的话，子问题就必须有合并成m堆的情况。

参考：https://leetcode.cn/problems/minimum-cost-to-merge-stones/solution/yi-dong-you-yi-dao-nan-yi-bu-bu-shuo-ming-si-lu-he/

"""
from typing import List
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        inf = float('inf')
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        import functools

        @functools.lru_cache(None)
        def dp(i, j, m):
            if (j - i + 1 - m) % (K - 1):
                return inf
            if i == j:
                return 0 if m == 1 else inf
            if m == 1:
                return dp(i, j, K) + prefix[j + 1] - prefix[i]
            return min(dp(i, mid, 1) + dp(mid + 1, j, m - 1) for mid in range(i, j, K - 1))
        res = dp(0, n - 1, 1)
        return res if res < inf else -1