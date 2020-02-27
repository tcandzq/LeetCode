#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 23:39
# @Author  : tc
# @File    : FlowerPlantingWithNoAdjacent.py
"""
题号 1042 不邻接植花
有 N 个花园，按从 1 到 N 标记。在每个花园中，你打算种下四种花之一。

paths[i] = [x, y] 描述了花园 x 到花园 y 的双向路径。

另外，没有花园有 3 条以上的路径可以进入或者离开。

你需要为每个花园选择一种花，使得通过路径相连的任何两个花园中的花的种类互不相同。

以数组形式返回选择的方案作为答案 answer，其中 answer[i] 为在第 (i+1) 个花园中种植的花的种类。花的种类用  1, 2, 3, 4 表示。保证存在答案。

示例 1：

输入：N = 3, paths = [[1,2],[2,3],[3,1]]
输出：[1,2,3]
示例 2：

输入：N = 4, paths = [[1,2],[3,4]]
输出：[1,2,1,2]
示例 3：

输入：N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
输出：[1,2,3,4]
 

提示：

1 <= N <= 10000
0 <= paths.size <= 20000
不存在花园有 4 条或者更多路径可以进入或离开。
保证存在答案。

参考1:https://leetcode-cn.com/problems/flower-planting-with-no-adjacent/solution/pythonjie-fa-by-cloud_zhongyi/
参考2:https://leetcode-cn.com/problems/flower-planting-with-no-adjacent/solution/jian-dan-de-ran-se-wen-ti-bu-xu-yao-kao-lu-hui-su-/

"""
from typing import List

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        result = [0 for _ in range(N + 1)]  # result存放结果，下标是花园，值是花的种类。
        path_map = [[] for _ in range(N + 1)]

        # 用邻接表构建地图
        for num in paths:
            path_map[num[0]].append(num[1])
            path_map[num[1]].append(num[0])
        s = set()  # 存储该花园相邻的花园种植的花
        for i in range(1, N + 1):
            s.clear()
            for j in path_map[i]:
                if j < i:  # 只看下标比i小的花园 与它相邻的花园中编号i大的先不用管，该花园还没有种花
                    s.add(result[j])  # 存储花园j摆放的花
            for j in range(1, 5):
                if j not in s:
                    count = j
                    break
            result[i] = count  # 花园i摆放其周围花园没有摆放的花

        return result[1:]


if __name__ == '__main__':
    N = 3
    paths = [[1, 2], [2, 3], [3, 1]]
    solution = Solution()
    print(solution.gardenNoAdj(N,paths))