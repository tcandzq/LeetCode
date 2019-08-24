#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 20:54
# @Author  : tc
# @File    : SearchA2DMatrix.py

# 解法1：
def searchMatrix(matrix, target):
    rows = len(matrix)

    if not rows:
        return 'false'

    for row in range(rows):
        if binary_search(matrix[row], target) != -1:
            return 'true'
    return 'false'


def binary_search(nums, target):
    left = 0

    right = len(nums) - 1

    while left <= right:
        mid = left + ((right - left) >> 1)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1


# 解法2
def searchMatrix2(matrix, target):
    rows = len(matrix)
    if not rows:
        return False
    columns = len(matrix[0]) #这行容易报错
    left = 0
    right = rows * columns - 1
    while left <= right:
        mid = left + (right - left) // 2

        if matrix[mid // columns][mid % columns] == target:
            return True

        elif matrix[mid // columns][mid % columns] < target:
            left = mid + 1

        elif matrix[mid // columns][mid % columns] > target:
            right = mid - 1

    return False
if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]

    print(searchMatrix2(matrix, 13))
