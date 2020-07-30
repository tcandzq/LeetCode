# -*- coding: utf-8 -*-
# @File    : MinimumSwapsToMakeSequencesIncreasing.py
# @Date    : 2020-07-14
# @Author  : tc
"""
题号 801. 使序列递增的最小交换次数
我们有两个长度相等且不为空的整型数组 A 和 B 。

我们可以交换A[i]和B[i]的元素。注意这两个元素在各自的序列中应该处于相同的位置。

在交换过一些元素之后，数组A和B都应该是严格递增的（数组严格递增的条件仅为A[0] < A[1] < A[2] < ... < A[A.length - 1]）。

给定数组A和B，请返回使得两个数组均保持严格递增状态的最小交换次数。假设给定的输入总是有效的。

示例:
输入: A = [1,3,5,4], B = [1,2,3,7]
输出: 1
解释:
交换 A[3] 和 B[3] 后，两个数组如下:
A = [1, 3, 5, 7] ， B = [1, 2, 3, 4]
两个数组均为严格递增的。
注意:

A, B 两个数组的长度总是相等的，且长度的范围为 [1, 1000]。
A[i], B[i] 均为 [0, 2000]区间内的整数。

参考：https://leetcode-cn.com/problems/minimum-swaps-to-make-sequences-increasing/solution/shi-xu-lie-di-zeng-de-zui-xiao-jiao-huan-ci-shu-by/

"""
from typing import List

class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n1,s1 = 0,1
        for i in range(1,len(A)):
            n2 = s2 = float('inf')
            if A[i-1] < A[i] and B[i-1] < B[i]:
                n2 = min(n2,n1)
                s2 = min(s2,s1+1)
            if A[i-1] < B[i] and B[i-1] < A[i]:
                n2 = min(n2,s1)
                s2 = min(s2,n1+1)
            n1,s1 = n2,s2
        return min(n1,s1)
if __name__ == '__main__':
    A = [1,3,5,4]
    B = [1,2,3,7]
    solution =  Solution()
    print(solution.minSwap(A,B))
