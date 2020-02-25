# -*- coding: utf-8 -*-
# @File    : ArithmeticSlices.py
# @Date    : 2020-02-25
# @Author  : tc
"""
题号 413. 等差数列划分
如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，以下数列为等差数列:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
以下数列不是等差数列。

1, 1, 2, 5, 7


数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。

如果满足以下条件，则称子数组(P, Q)为等差数组：

元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。

函数要返回数组 A 中所有为等差数组的子数组个数。



示例:

A = [1, 2, 3, 4]

返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。

参考：https://leetcode-cn.com/problems/arithmetic-slices/solution/deng-chai-shu-lie-hua-fen-by-leetcode/

"""
from typing import List

class Solution:
    # 动态规划
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        num = 0
        dp = [0] * n
        for i in range(2,n):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1
                num += dp[i]
        print(dp)
        return num


    # 空间优化
    def numberOfArithmeticSlices2(self, A: List[int]) -> int:
        n = len(A)
        dp =0
        num = 0
        for i in range(2, n):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp += 1
                num += dp
            else:
                dp = 0
        return num

if __name__ == '__main__':
    A = [1,2,3,7,8,9,10]
    solution = Solution()
    print(solution.numberOfArithmeticSlices2(A))