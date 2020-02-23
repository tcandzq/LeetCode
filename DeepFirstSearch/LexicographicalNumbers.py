# -*- coding: utf-8 -*-
# @File    : LexicographicalNumbers.py
# @Date    : 2020-02-23
# @Author  : tc
"""
题号 386. 字典序排数
给定一个整数 n, 返回从 1 到 n 的字典顺序。

例如，

给定 n =13，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。

请尽可能的优化算法的时间复杂度和空间复杂度。 输入的数据 n 小于等于 5,000,000。

参考：https://leetcode.com/problems/lexicographical-numbers/discuss/86231/Simple-Java-DFS-Solution

"""
from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = [0] * n
        cur = 1
        for i in range(n):
            res[i] = cur
            if cur*10 <= n:
                cur *= 10
            else:
                if cur >= n:
                    cur //= 10
                cur += 1
                while cur % 10 == 0:
                    cur //= 10
        return res

    # dfs 解法
    def lexicalOrder2(self, n: int) -> List[int]:
        res = []

        def dfs(cur,n,res):
            if cur > n:
                return
            else:
                res.append(cur)
                for i in range(10):
                    if 10*cur + i > n:
                        return
                    dfs(10*cur+i,n,res)
        for i in range(1,10): # 注意从1开始
            dfs(i,n,res)
        return res


if __name__ == '__main__':
    n = 13
    solution = Solution()
    print(solution.lexicalOrder2(n))
