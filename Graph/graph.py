#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 15:38
# @Author  : tc
# @File    : graph.py
"""

"""

# BFS遍历图

#  邻接矩阵版
MAXV = 1000
INF = float('inf')
vis = [False for _ in range(MAXV)]

def dfs(u, depth, n, G): #  u为当前访问的定点标号,depth为深度,n为顶点数,G为图
    vis[u] = True  # 设置u已被访问
    # 如果需要对u进行一些操作,可以在这里设置
    for v in range(len(n)):  # 下面对所有从u出发能到达的分支顶点进行枚举
        if vis[v] is False and G[u][v] != INF:  # 如果v没有被访问,且u可达到v
            dfs(u, depth+1, n, G)  # 递归访问v,深度+1

def dfs_trave(n, G):  # 遍历图G
    for u in range(n):  # 对G的每个顶点u
        if vis[u] is False:  # 如果u未被访问
            dfs(u, 1, n, G)  # 访问u和u所在的连通块,1表示为初始的第一层

# 邻接表版

