#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 11:13
# @Author  : tc
# @File    : SearchA2DMatrixII.py


def searchMatrix(matrix,target):
    rows = len(matrix)

    if not rows:
        return False

    columns = len(matrix[0])

    i = rows -1

    j = 0

    # while  (i >= 0 and i <= rows - 1) and (j >= 0 and j <= columns -1):
    while (0 <= i <= rows - 1) and (0 <= j <= columns - 1):  #这种写法更简单
        if matrix[i][j] == target:
            return True

        if matrix[i][j] > target:
            i -= 1

        if matrix[i][j] < target:
            j += 1
    return False

if __name__ == '__main__':
    matrix = [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]

    target = 20

    print(searchMatrix(matrix, target))