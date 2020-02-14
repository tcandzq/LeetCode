# -*- coding: utf-8 -*-
# @File    : FrogJump.py
# @Date    : 2020-02-11
# @Author  : tc
"""
题号 403 青蛙过河

一只青蛙想要过河。 假定河流被等分为 x 个单元格，并且在每一个单元格内都有可能放有一石子（也有可能没有）。 青蛙可以跳上石头，但是不可以跳入水中。

给定石子的位置列表（用单元格序号升序表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一个石子上）。 开始时， 青蛙默认已站在第一个石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格1跳至单元格2）。

如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。

请注意：

石子的数量 ≥ 2 且 < 1100；
每一个石子的位置序号都是一个非负整数，且其 < 231；
第一个石子的位置永远是0。
示例 1:

[0,1,3,5,6,8,12,17]

总共有8个石子。
第一个石子处于序号为0的单元格的位置, 第二个石子处于序号为1的单元格的位置,
第三个石子在序号为3的单元格的位置， 以此定义整个数组...
最后一个石子处于序号为17的单元格的位置。

返回 true。即青蛙可以成功过河，按照如下方案跳跃：
跳1个单位到第2块石子, 然后跳2个单位到第3块石子, 接着
跳2个单位到第4块石子, 然后跳3个单位到第6块石子,
跳4个单位到第7块石子, 最后，跳5个单位到第8个石子（即最后一块石子）。
示例 2:

[0,1,2,3,4,8,9,11]

返回 false。青蛙没有办法过河。
这是因为第5和第6个石子之间的间距太大，没有可选的方案供青蛙跳跃过去。


思路：
自底向上
dp[i][k]表示能否从第i个石头前面的任意一个石头j用k步跳到第i个石头，则状态转移方程：

dp[i][k]=dp[j][k-1]||dp[j][k]||dp[j][k+1] for j = 0,1,...,i.

乍一看可能很难想通，但我们可以反过来想：
如果从第j个石头到达第i个石头需要用k步，那这个k步是怎么来的呢？
根据题目的要求，如果青蛙上一步跳跃了k个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1个单位。因此当前的k步，可能由上一步的
k-1、k、k+1步而来，这三种都有可能，但只要其中任何一步跳跃成功那么青蛙就能从第j个石头跳到第i个石头。

参考：https://leetcode-cn.com/problems/frog-jump/solution/zi-ding-xiang-xia-he-zi-di-xiang-shang-by-powcai-3/
"""
from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        size = len(stones)
        dp = [[False] * (size+1) for _ in range(size)]  # dp的长度之所以定义为len+1是因为第0块石头为0步，就算每跳一次加一步，最多也只能跳len步。
        dp[0][0] = True  # 青蛙一开始已经站在了第一块石头上了
        for i in range(1,size):
            for j in range(i):
                diff = stones[i] - stones[j]
                if diff+1 <= size : # 要考虑dp[,][diff+1]的边界情况
                    dp[i][diff] = dp[j][diff-1] or dp[j][diff] or dp[j][diff+1]
                    if i == size - 1 and dp[i][diff]:  # 如果青蛙在最后一块石头上且可以从前面的任何一块石头上跳过来
                        return True
        return False

    # 记忆化搜索
    def canCross2(self, stones: List[int]) -> bool:
        from functools import lru_cache
        end = stones[-1]
        s = set(stones)
        @lru_cache(None)
        def dfs(start,jump):
            if start == end:
                return True
            for j in [jump-1,jump,jump+1]:
                if j <= 0:continue
                if start+j in s and dfs(start+j,j):
                    return True
            return False
        return dfs(0,0)


if __name__ == '__main__':
    stones = [0,1,3,6,10,13,14]
    solution = Solution()
    print(solution.canCross2(stones))
