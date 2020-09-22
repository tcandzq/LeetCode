# -*- coding: utf-8 -*-
# @File    : PartitionArrayForMaximumSum.py
# @Date    : 2020-09-23
# @Author  : tc
"""
题号 1043. 分隔数组以得到最大和
给出整数数组 A，将该数组分隔为长度最多为 K 的几个（连续）子数组。分隔完成后，每个子数组的中的值都会变为该子数组中的最大值。

返回给定数组完成分隔后的最大和。

示例：

输入：A = [1,15,7,9,2,5,10], K = 3
输出：84
解释：A 变为 [15,15,15,9,10,10,10]

提示：

1 <= K <= A.length <= 500
0 <= A[i] <= 10^6

参考：https://leetcode.com/problems/partition-array-for-maximum-sum/discuss/290863/JavaC%2B%2BPython-DP
"""
from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        dp = [0] * (N + 1)
        for i in range(N):
            curMax = 0
            for j in range(1, min(k, i + 1) + 1):
                curMax = max(curMax, arr[i - j + 1])
                dp[i] = max(dp[i], dp[i - j] + curMax * j)
        return dp[N - 1]

if __name__ == '__main__':
    pass