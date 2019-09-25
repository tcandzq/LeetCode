#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/25 0:36
# @Author  : tc
# @File    : 0-1KnapsackProblem.py
"""
0-1背包问题:
有n件物品,每件物品的重量为w[i],价值为c[i]。现有一个容量为V的背包,问如何选取物品放入包中,使得包内的物品的总价值最大。其中每种物品都
只有1件。
示例:
5 8
3 5 1 2 2 w[i]
4 5 2 1 3 c[i]

令dp[i][v]表示前i件物品恰好装入容量为v的背包中所能获得最大价值,每次都有两种选择:
1.放第i件物品,那么问题就是前i-1件物品恰好装入容量为v-w[i]的背包中所能获得的最大价值,即dp[i-1][v-w[i]]+c[i];
2.不放第i件物品,那么问题就是前i-1件物品恰好装入容量为v的背包中所能获得的最大价值,也即dp[i-1][v]

"""

maxn  = 100 # 物品最大件数
maxv = 1000 # V的上限
def result(n,V,nums_w,nums_c):
    dp = [0]*V
    for i in range(1,n):
        for v in range(V,nums_w[i]+1,-1):
                print(dp)
                dp[v] = max(dp[v],dp[v-nums_w[i]] + nums_c[i])
    # print(dp)
    return max(dp)

if __name__ == '__main__':
    n = 5
    V = 8
    nums_w = [3,5, 1, 2, 2]
    nums_c = [4,5, 2, 1, 3]
    print(result(n,V,nums_w,nums_c))