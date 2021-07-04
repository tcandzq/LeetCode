# -*- coding: utf-8 -*-
# @File    : ScoreAfterFlippingMatrix.py
# @Date    : 2021-07-05
# @Author  : tc
"""
题号 861. 翻转矩阵后的得分
有一个二维矩阵 A 其中每个元素的值为 0 或 1 。
移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。
在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。
返回尽可能高的分数。

示例：

输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
输出：39
解释：
转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

提示：

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] 是 0 或 1

1.先横竖变换保证第一列全部是1
2.竖变换保证其他列1比0多

代码参考：

思路参考:https://leetcode-cn.com/problems/score-after-flipping-matrix/solution/fan-zhuan-ju-zhen-tan-xin-xin-lu-li-chen-21h7/

"""
from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            if grid[i][0] == 0: # 如果该行的第一列元素为0
                for j in range(m):
                    grid[i][j] = 1 ^ grid[i][j] # 进行按行反转,保证该行第一列的值为1
        res = 0
        for i in zip(*grid): # 按列展开
            m -= 1
            res += 2 ** m * max(i.count(1), i.count(0)) # 按列维度计算和并累加
        return res