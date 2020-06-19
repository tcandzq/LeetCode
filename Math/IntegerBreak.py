# -*- coding: utf-8 -*-
# @File    : IntegerBreak.py
# @Date    : 2020-02-09
# @Author  : tc
"""
题号 343 整数拆分
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。

解法1：参考：https://leetcode-cn.com/problems/integer-break/solution/343-zheng-shu-chai-fen-tan-xin-by-jyd/

解法2：参考：https://leetcode-cn.com/problems/integer-break/solution/tan-xin-xuan-ze-xing-zhi-de-jian-dan-zheng-ming-py/

完全是一道数学题。。。

"""
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return pow(3, a)
        if b == 1: return pow(3, a - 1) * 4
        return pow(3, a) * 2

    def integerBreak2(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[2] = 1
        for i in range(3,n+1):
            for j in range(i):
                dp[i] = max(dp[i],max((i - j) * j,j*dp[i -j]))
        return dp[n]

    def integerBreak3(self, n: int) -> int:
        dp = [1 for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = max(max(dp[i - 1], i - 1),
                        2 * max(dp[i - 2], i - 2),
                        3 * max(dp[i - 3], i - 3))
        return dp[n]

if __name__ == '__main__':
    n = 10
    solution = Solution()
    print(solution.integerBreak(n))
    print(solution.integerBreak2(n))
    print(solution.integerBreak3(n))