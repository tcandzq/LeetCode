# -*- coding: utf-8 -*-
# @File    : 14_CuttingRope.py
# @Date    : 2020-06-19
# @Author  : tc

"""
面试题14-I.剪绳子
给你一根长度为n的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1]。
请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
提示：

2 <= n <= 58
注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/

参考：https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/xiang-jie-bao-li-di-gui-ji-yi-hua-ji-zhu-dong-tai-/

"""
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0,1,1]

        for i in range(3,n+1):
            dp[i % 3] = max(max(dp[(i-1) % 3],i - 1),
                            2*max(dp[(i - 2) % 3],i - 2),
                            3*max(dp[(i - 3) % 3],i - 3))
        return dp[n % 3]



