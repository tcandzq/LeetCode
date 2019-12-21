#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/31 11:48
# @Author  : tc
# @File    : NQueens.py
"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
皇后可以攻击同一行、同一列、左上左下右上右下四个方向的任意单位。
给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
Input1:4
Output1:
 [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。

典型的"全排列"问题+"剪枝"
搜索问题的解决策略是画递归树。

答案参考:https://leetcode-cn.com/problems/n-queens/solution/gen-ju-di-46-ti-quan-pai-lie-de-hui-su-suan-fa-si-/
本题的关键是记住如何保存"状态",主对角线和副对角线上元素的特点。
"""
def solveNQueens(n):
    res = []
    if n == 0:
        return res

    nums = [i for i in range(n)]
    # 列状态集合
    col = set()
    # 主对角线状态集合
    master = set()
    # 副对角线状态集合
    slave = set()    # 注意以上状态都用HashSet存储
    stack = []

    __backtracking(nums, 0, n, col, master, slave, stack, res)
    return res


def __backtracking(nums, row, n, col, master, slave, stack, res):
    if row == n:
        board = __convert2board(stack, n)
        res.append(board)
        return
    # 有n个列可供选择
    for i in range(n):
        # 如果第row行第i列没有出现在行、主对角线、副对角线的状态集合中,即与前面所有摆放的皇后位置都没有冲突
        if i not in col and row + i not in master and row - i not in slave:
            stack.append(nums[i])
            col.add(i)
            master.add(row + i)
            slave.add(row - i)

            __backtracking(nums, row + 1, n, col, master, slave, stack, res)
            # 下面所有的代码都是进行状态回溯
            slave.remove(row - i)
            master.remove(row + i)
            col.remove(i)
            stack.pop()


def __convert2board(stack, n):
    return ["." * stack[i] + "Q" + "." * (n - stack[i] - 1) for i in range(n)]


if __name__ == '__main__':
    n = 4
    res = solveNQueens(n)
    print(res)

