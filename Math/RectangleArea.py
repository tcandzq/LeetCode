# -*- coding: utf-8 -*-
# @File    : RectangleArea.py
# @Date    : 2020-02-23
# @Author  : tc
"""
题号 223. 矩形面积
在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。

每个矩形由其左下顶点和右上顶点坐标表示，如图所示。
示例:

输入: -3, 0, 3, 4, 0, -1, 9, 2
输出: 45
"""
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        wide1 = [A,C]
        high1 = [B,D]
        wide2 = [E,G]
        high2 = [F,H]
        area = (C - A)*(D - B) + (G - E)*(H - F)

        def helper(a,b):
            wide = 0
            if a[0] == a[1] or b[0] == b[1]:
                return wide
            if a[0] <= b[0] <= a[1] :
                wide = min(a[1],b[1]) - b[0]
            elif b[0] <= a[0] <= b[1] :
                wide = min(b[1],a[1]) - a[0]
            return wide

        wide = helper(wide1,wide2)
        height = helper(high1,high2)
        return area - wide * height

    # 解法2
    def computeArea2(self, A, B, C, D, E, F, G, H):
        a = (C - A) * (D - B)
        b = (G - E) * (H - F)
        x = max(0, min(C, G) - max(A, E))
        y = max(0, min(D, H) - max(B, F))
        area = a + b - x * y
        return area


if __name__ == '__main__':
    solution = Solution()
    A = -2
    B = -2
    C = 2
    D = 2
    E = -1
    F = -1
    G = 1
    H = 1

    print(solution.computeArea(A, B, C, D, E, F, G, H))