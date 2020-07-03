# -*- coding: utf-8 -*-
# @File    : BeautifulArrangement.py
# @Date    : 2020-07-01
# @Author  : tc

"""
题号 526. 优美的排列
假设有从 1 到 N 的 N 个整数，如果从这 N 个数字中成功构造出一个数组，使得数组的第 i 位 (1 <= i <= N) 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。条件：

第i位的数字能被 i 整除
i能被第i位上的数字整除
现在给定一个整数 N，请问可以构造多少个优美的排列？

示例1:

输入: 2
输出: 2
解释:

第 1 个优美的排列是 [1, 2]:
  第 1 个位置（i=1）上的数字是1，1能被 i（i=1）整除
  第 2 个位置（i=2）上的数字是2，2能被 i（i=2）整除

第 2 个优美的排列是 [2, 1]:
  第 1 个位置（i=1）上的数字是2，2能被 i（i=1）整除
  第 2 个位置（i=2）上的数字是1，i（i=2）能被 1 整除
说明:

N 是一个正整数，并且不会超过15。

"""


class Solution:
    def countArrangement(self, N: int) -> int:
        cur = set(range(1, N + 1))
        visited = set()
        res = 0

        def dfs(i):
            nonlocal res
            if i == N + 1:
                res += 1
                return
            for num in cur - visited:
                if i % num == 0 or num % i == 0:
                    visited.add(num)
                    dfs(i + 1)
                    visited.remove(num)

        dfs(1)
        return res


if __name__ == '__main__':
    N = 2
    solution = Solution()
    print(solution.countArrangement(N))
