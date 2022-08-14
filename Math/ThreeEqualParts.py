# -*- coding: utf-8 -*-
# @File    : ThreeEqualParts.py
# @Date    : 2022-08-15
# @Author  : tc
"""
927. 三等分
给定一个由 0 和 1 组成的数组 arr ，将数组分成  3 个非空的部分 ，使得所有这些部分表示相同的二进制值。
如果可以做到，请返回任何 [i, j]，其中 i+1 < j，这样一来：
arr[0], arr[1], ..., arr[i] 为第一部分；
arr[i + 1], arr[i + 2], ..., arr[j - 1] 为第二部分；
arr[j], arr[j + 1], ..., arr[arr.length - 1] 为第三部分。
这三个部分所表示的二进制值相等。
如果无法做到，就返回 [-1, -1]。

注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，[1,1,0] 表示十进制中的 6，而不会是 3。此外，前导零也是被允许的，所以 [0,1,1] 和 [1,1] 表示相同的值。

示例 1：
输入：arr = [1,0,1,0,1]
输出：[0,3]
示例 2：

输入：arr = [1,1,0,1,1]
输出：[-1,-1]
示例 3:

输入：arr = [1,1,0,0,1]
输出：[0,2]

参考:https://leetcode.cn/problems/three-equal-parts/solution/san-deng-fen-by-leetcode/
"""
from typing import List
class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        IMP = [-1, -1]

        S = sum(A)
        if S % 3: return IMP
        T = S / 3
        if T == 0:
            return [0, len(A) - 1]

        breaks = []
        su = 0
        for i, x in enumerate(A):
            if x:
                su += x
                if su in {1, T+1, 2*T+1}:
                    breaks.append(i)
                if su in {T, 2*T, 3*T}:
                    breaks.append(i)
        print(breaks)
        i1, j1, i2, j2, i3, j3 = breaks

        # The array is in the form W [i1, j1] X [i2, j2] Y [i3, j3] Z
        # where [i1, j1] is a block of 1s, etc.
        if not(A[i1:j1+1] == A[i2:j2+1] == A[i3:j3+1]):
            return [-1,-1]

        # x, y, z: the number of zeros after part 1, 2, 3
        x = i2 - j1 - 1
        y = i3 - j2 - 1
        z = len(A) - j3 - 1

        if x < z or y < z: return IMP
        j1 += z
        j2 += z
        return [j1, j2+1]