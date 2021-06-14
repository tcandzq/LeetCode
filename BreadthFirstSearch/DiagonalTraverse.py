# -*- coding: utf-8 -*-
# @File    : DiagonalTraverse.py
# @Date    : 2021-06-14
# @Author  : tc
"""
题号 498. 对角线遍历
给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。

示例:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

输出:  [1,2,4,7,5,3,6,8,9]

解释:
有以下两个事实:
1.同一层的横纵坐标和为固定值
2.通过将偶数层中的数组元素进行反转，可以达到蛇形遍历的效果

参考：https://leetcode.com/problems/diagonal-traverse/discuss/581868/Easy-Python-NO-DIRECTION-CHECKING

"""


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        d = {}
        # loop through matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                # if no entry in dictionary for sum of indices aka the diagonal, create one
                if i + j not in d:
                    d[i + j] = [matrix[i][j]]
                else:
                    # If you've already passed over this diagonal, keep adding elements to it!
                    d[i + j].append(matrix[i][j])
            # we're done with the pass, let's build our answer array
        ans = []
        # look at the diagonal and each diagonal's elements
        for entry in d.items():
            # each entry looks like (diagonal level (sum of indices), [elem1, elem2, elem3, ...])
            # snake time, look at the diagonal level
            if entry[0] % 2 == 0:
                # Here we append in reverse order because its an even numbered level/diagonal.
                [ans.append(x) for x in entry[1][::-1]]
            else:
                [ans.append(x) for x in entry[1]]
        return ans