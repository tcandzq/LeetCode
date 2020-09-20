# -*- coding: utf-8 -*-
# @File    : NumberOfMusicPlaylists.py
# @Date    : 2020-09-21
# @Author  : tc
"""
题号 920. 播放列表的数量
你的音乐播放器里有 N 首不同的歌，在旅途中，你的旅伴想要听 L 首歌（不一定不同，即，允许歌曲重复）。请你为她按如下规则创建一个播放列表：

每首歌至少播放一次。
一首歌只有在其他 K首歌播放完之后才能再次播放。
返回可以满足要求的播放列表的数量。由于答案可能非常大，请返回它模 10^9 + 7 的结果。



示例 1：

输入：N = 3, L = 3, K = 1
输出：6
解释：有 6 种可能的播放列表。[1, 2, 3]，[1, 3, 2]，[2, 1, 3]，[2, 3, 1]，[3, 1, 2]，[3, 2, 1].
示例 2：

输入：N = 2, L = 3, K = 0
输出：6
解释：有 6 种可能的播放列表。[1, 1, 2]，[1, 2, 1]，[2, 1, 1]，[2, 2, 1]，[2, 1, 2]，[1, 2, 2]
示例 3：

输入：N = 2, L = 3, K = 1
输出：2
解释：有 2 种可能的播放列表。[1, 2, 1]，[2, 1, 2]


提示：

0 <= K < N <= L <= 100

参考:https://leetcode.com/problems/number-of-music-playlists/discuss/178415/C%2B%2BJavaPython-DP-Solution

"""
import math

class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        dp = [[0 for i in range(L + 1)] for j in range(N + 1)]
        for i in range(K + 1, N + 1):
            for j in range(i, L + 1):
                if i == j or i == K + 1:
                    dp[i][j] = math.factorial(i)
                else:
                    dp[i][j] = dp[i - 1][j - 1] * i + dp[i][j - 1] * (i - K)
        return dp[N][L] % (10 ** 9 + 7)


if __name__ == '__main__':
    pass