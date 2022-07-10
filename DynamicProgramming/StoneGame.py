# -*- coding: utf-8 -*-
# @File    : StoneGame.py
# @Date    : 2022-07-11
# @Author  : tc
"""
877. 石子游戏
Alice 和 Bob 用几堆石子在做游戏。一共有偶数堆石子，排成一行；每堆都有 正 整数颗石子，数目为 piles[i] 。

游戏以谁手中的石子最多来决出胜负。石子的 总数 是 奇数 ，所以没有平局。

Alice 和 Bob 轮流进行，Alice 先开始 。 每回合，玩家从行的 开始 或 结束 处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中 石子最多 的玩家 获胜 。

假设 Alice 和 Bob 都发挥出最佳水平，当 Alice 赢得比赛时返回 true ，当 Bob 赢得比赛时返回 false 。

示例 1：
输入：piles = [5,3,4,5]
输出：true
解释：
Alice 先开始，只能拿前 5 颗或后 5 颗石子 。
假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
如果 Bob 拿走前 3 颗，那么剩下的是 [4,5]，Alice 拿走后 5 颗赢得 10 分。
如果 Bob 拿走后 5 颗，那么剩下的是 [3,4]，Alice 拿走后 4 颗赢得 9 分。
这表明，取前 5 颗石子对 Alice 来说是一个胜利的举动，所以返回 true 。

示例 2：
输入：piles = [3,7,2,3]
输出：true

dp[i][j] 表示当剩下的石子堆为下标i到下标j时，即在下标范围 [i, j]中，当前玩家与另一个玩家的石子数量之差的最大值
https://leetcode.cn/problems/stone-game/solution/shi-zi-you-xi-by-leetcode-solution/
"""
from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * (n + 2) for i in range(n + 2)]
        for size in range(1, n + 1):
            for left in range(1, (n + 1) - size + 1):
                right = left + size - 1
                dp[left][right] = max(piles[left - 1] - dp[left + 1][right], piles[right - 1] - dp[left][right - 1])
        return dp[1][n] > 0