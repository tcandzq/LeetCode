#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 20:54
# @Author  : tc
# @File    : SearchA2DMatrix.py


def searchMatrix(matrix, target):
    rows = len(matrix)
    for row in range(rows):
        if binary_search(matrix[row], target) != -1:
            return 'true'
    return 'false'


def binary_search(nums, target):
    left = 0

    right = len(nums)

    while left < right:
        mid = left + ((right - left) >> 1)

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return -1 if left >= len(nums) else left


if __name__ == '__main__':
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]

    print(searchMatrix(matrix,13))