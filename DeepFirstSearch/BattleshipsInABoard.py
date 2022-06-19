# -*- coding: utf-8 -*-
# @File    : BattleshipsInABoard.py
# @Date    : 2022-06-19
# @Author  : tc
"""
419. 甲板上的战舰
给你一个大小为 m x n 的矩阵 board 表示甲板，其中，每个单元格可以是一艘战舰 'X' 或者是一个空位 '.' ，返回在甲板 board 上放置的 战舰 的数量。
战舰 只能水平或者垂直放置在 board 上。换句话说，战舰只能按 1 x k（1 行，k 列）或 k x 1（k 行，1 列）的形状建造，其中 k 可以是任意大小。
两艘战舰之间至少有一个水平或垂直的空位分隔 （即没有相邻的战舰）。


输入：board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
输出：2
示例 2：

输入：board = [["."]]
输出：0

"""
from typing import List
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                # 题目的意思是战舰群,是由多个‘X’组成,且这些‘X’只能出现在矩阵的第一行或者第一列,因此只要统计战舰头的数量即可
                # 如果战舰头在第一列，那么它的上方不能有战舰即board[i - 1][j] != 'X'
                # 如果战舰头在第一行，那么它的左边不能有战舰即board[i][j - 1] != 'X'
                if board[i][j] == 'X' and (i == 0 or board[i - 1][j] != 'X') and (j == 0 or board[i][j - 1] != 'X'):
                    ans += 1
        return ans