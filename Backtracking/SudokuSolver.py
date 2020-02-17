# -*- coding: utf-8 -*-
# @File    : SudokuSolver.py
# @Date    : 2020-02-17
# @Author  : tc
"""
题号 37 解数独
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。

答案被标成红色。

Note:

给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。

两个函数互相调用构成回溯

参考：https://leetcode-cn.com/problems/sudoku-solver/solution/jie-shu-du-by-leetcode/

"""
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import defaultdict
        N = 9
        rows = [defaultdict(int) for _ in range(N)]
        cols = [defaultdict(int) for _ in range(N)]
        boxes = [defaultdict(int) for _ in range(N)]

        # lambda function to compute box index
        box_index = lambda row,col:(row // 3)*3 + col // 3
        def could_place(d,row,col):
            return not (d in rows[row] or d in cols[col] or d in boxes[box_index(row,col)])

        def place_number(d,row,col):
            rows[row][d] += 1
            cols[col][d] += 1
            boxes[box_index(row,col)][d] += 1
            board[row][col] = str(d)

        def remove_number(d,row,col):
            del rows[row][d]
            del cols[col][d]
            del boxes[box_index(row,col)][d]
            board[row][col] = '.'

        def place_next_number(row,col):
            if row == N - 1 and col == N - 1:  # 如果这是最后一个格子row == 8, col == 8
                nonlocal sudoku_solved
                sudoku_solved = True  # 意味着已经找出了数独的解。

            # 否则 继续放下一个数
            else:
                if col == N - 1:  # 如果在一行末尾，那么下一个数就位于第二行的开头
                    backtrack(row+1,0)
                else:
                    backtrack(row, col+1) # 否则 下一个数位于当前行的 col+1列

        def backtrack(row=0,col=0):
            if board[row][col] == '.':
                # 尝试放置数字 d 进入 (row, col) 的格子
                for d in range(1,10):
                    if could_place(d, row, col):  # 如果数字 d 还没有出现在当前行，列和子方块中：
                        place_number(d,row,col)  # 将 d 放入 (row, col) 格子中，且记录下 d 已经出现在当前行，列和子方块中
                        place_next_number(row,col)
                        if not sudoku_solved:
                            remove_number(d,row,col)
            else:
                place_next_number(row,col)
        # 先将数独中已有的点放入字典中
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)
        sudoku_solved = False
        backtrack()


if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    solution = Solution()
    print(solution.solveSudoku(board))