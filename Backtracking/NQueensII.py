# -*- coding: utf-8 -*-
# @File    : NQueensII.py
# @Date    : 2019-12-21
# @Author  : tc
"""
题号 52 N皇后II
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
皇后可以攻击同一行、同一列、左上左下右上右下四个方向的任意单位。
给定一个整数 n，返回 n 皇后不同的解决方案的数量。
示例:

输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]

"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        def backtrack(i, col, z_diagonal, f_diagonal):
            if i == n: return True
            for j in range(n):
                if j not in col and i + j not in z_diagonal and i - j not in f_diagonal:
                    if backtrack(i + 1, col | {j}, z_diagonal | {i + j}, f_diagonal | {i - j}):
                        self.res += 1
            return False

        backtrack(0, set(), set(), set())
        return self.res


if __name__ == '__main__':
    n = 4
    solution = Solution()
    print(solution.totalNQueens(n))
