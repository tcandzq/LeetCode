#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/31 10:00
# @Author  : tc
# @File    : Permutations.py

"""
给定一个没有重复数字的序列，返回其所有可能的全排列。
Input1:[1,2,3]
Output1:[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

参考:https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/
“状态重置”是“回溯”的重要操作，“回溯搜索”是有方向的搜索，否则我们要写多重循环，代码量不可控。

这个系列的解答非常详细没事一定一套要多看看
这题的答案可以看成一个标准写法,可以作为写回溯算法的模板，类似的问题写出来的代码基本都是这个样子，要牢记于心啊

"""
def permute(nums):
    if len(nums) == 0:
        return []
    # index:当前处理的数
    # used:已经处理的数
    # pre：已经处理的数组成的数组
    # res:存储完整遍历一次结果的数组
    used = [False] * len(nums)
    res = []
    __dfs(nums, 0, [], used, res)
    return res


def __dfs(nums, index, pre, used, res):
    # 先写递归终止条件
    if index == len(nums):
        res.append(pre.copy())
        return
    # 这个循环的理解有两种方式1:对所有可能的数进行组合;2.当走到第n层的某个结点进行操作时,理论上会有len(nums)种岔路可以走,但其中已经有n-1条路
    # 已经走过了所以 不能再走了 故加一个逻辑判断 这个引出了第二种写法
    for i in range(len(nums)):
        if not used[i]:
            # 如果没有用过，就用它
            used[i] = True   # 标记这个数已经被用过了
            pre.append(nums[i])  # 将这个数添加到pre中

            # 在 dfs 前后，代码是对称的
            __dfs(nums, index + 1, pre, used, res)  # 进入下一个分支
            used[i] = False
            pre.pop()  # 状态重置 这条路已经完整的走完了需要一直回退到上一个分支点 准备进入下一个岔路。而这个岔路是可以进入上一次走过的路径

if __name__ == '__main__':
    nums = [1,2,3]
    print(permute(nums))