#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 23:29
# @Author  : tc
# @File    : HammingDistance.py
"""
题号 461 汉明距离

两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。

"""
class Solution:
    # 正规解法
    def hammingDistance(self, x: int, y: int) -> int:
        res = x ^ y
        count = 0
        while res:
            res = res & (res - 1)
            count += 1
        return count

    # 非正规解法
    def hammingDistance2(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')

if __name__ == '__main__':
    x = 1
    y = 4
    solution = Solution()
    print(solution.hammingDistance(x,y))