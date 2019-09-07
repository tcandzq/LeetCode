#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 22:12
# @Author  : tc
# @File    : KthSmallestElementInASortedMatrix.py
"""
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
请注意，它是排序后的第k小元素，而不是第k个元素。

Input1:matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

Output1=13。

这题主要有两种解法。第一种是用优先队列,需要用到C++里的优先队列priority_queue;
第二种利用二分的解法,比较巧妙,具体参考:https://github.com/grandyang/leetcode/issues/378
参考答案的二分其实是标准解法二分解法的第二种,即不返回中间结果,而且本题的二分解法一定会有结果,所以left == right时结果一定是正确的。
"""
#二分解法1
def kthSmallest(matrix, k):
    n = len(matrix)
    lo = matrix[0][0]
    hi = matrix[n-1][n-1]
    while lo < hi:
        mid = lo + (hi - lo) // 2
        count = 0
        j = n - 1
        for i in range(n):
            while j >= 0 and matrix[i][j] > mid:
                j -= 1
            count += (j+1)
        if count < k:
            lo = mid + 1
        else:
            hi = mid
    return lo

if __name__ == '__main__':
    matrix = [[1, 5, 9],
              [10, 11, 13],
              [12, 13, 15]]
    k = 8
    print(kthSmallest(matrix,k))


