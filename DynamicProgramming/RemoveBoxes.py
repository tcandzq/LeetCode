# -*- coding: utf-8 -*-
# @File    : RemoveBoxes.py
# @Date    : 2020-06-28
# @Author  : tc
"""
题号 546.移除盒子
给出一些不同颜色的盒子，盒子的颜色由数字表示，即不同的数字表示不同的颜色。
你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 k*k 个积分。
当你将所有盒子都去掉之后，求你能获得的最大积分和。

示例 1：
输入:

[1, 3, 2, 2, 2, 3, 4, 3, 1]
输出:

23
解释:

[1, 3, 2, 2, 2, 3, 4, 3, 1]
----> [1, 3, 3, 4, 3, 1] (3*3=9 分)
----> [1, 3, 3, 3, 1] (1*1=1 分)
----> [1, 1] (3*3=9 分)
----> [] (2*2=4 分)


提示：盒子的总数 n 不会超过 100。

dp[i][j][k] 表示当boxes[i]左边有k个数字跟其相等时，区间[i,j]中能获得的最大积分

状态转移方程：

dp[i][j][k] = dp[i+1][m-1][0] + dp[m][j][k+1] (if boxes[i] == dp[m])

思路参考：https://www.cnblogs.com/grandyang/p/6850657.html

代码参考：https://leetcode.com/problems/remove-boxes/discuss/101311/Python-Fast-DP-with-Explanation

"""
from typing import List

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        N = len(boxes)
        memo = [[[0] * N for _ in range(N)] for _ in range(N)]

        def dp(i,j,k):
            if i > j:return 0
            if not memo[i][j][k]:
                m = i
                while m + 1 <= j and boxes[m+1] == boxes[i]:
                    m += 1
                i, k = m, k + m - i
                ans = dp(i+1, j, 0) + (k+1)**2
                for m in range(i+1, j+1):
                    if boxes[i] == boxes[m]:
                        ans = max(ans,dp(i+1,m-1,0) + dp(m,j,k+1))
                memo[i][j][k] = ans
            return memo[i][j][k]
        return dp(0,N-1,0)



if __name__ == '__main__':
    boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]
    solution = Solution()
    print(solution.removeBoxes(boxes))
