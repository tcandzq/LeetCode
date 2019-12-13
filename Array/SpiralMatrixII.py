"""
题号 59 螺旋矩阵II
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

参考:https://leetcode-cn.com/problems/spiral-matrix-ii/solution/spiral-matrix-ii-mo-ni-fa-she-ding-bian-jie-qing-x/

"""
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        up = 0
        down = n - 1
        left = 0
        right = n - 1
        num = 1
        target = n * n
        matrix = [[0] * n for _ in range(n)]
        while num <= target:
            for i in range(left,right+1):
                matrix[up][i] = num
                num += 1
            up += 1

            for i in range(up,down+1):
                matrix[i][right] = num
                num += 1
            right -= 1

            for i in range(right,left -1,-1):
                matrix[down][i] = num
                num += 1
            down -= 1

            for i in range(down,up -1,-1):
                matrix[i][left] = num
                num += 1
            left += 1
        return matrix

if __name__ == '__main__':
    n = 3
    solution = Solution()
    print(solution.generateMatrix(n))