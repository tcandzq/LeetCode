#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/13 16:10
# @Author  : tc
# @File    : Candy.py
"""
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？
示例 1:
输入: [1,0,2]
输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。

示例 2:

输入: [1,2,2]
输出: 4
解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这已满足上述两个条件。

本题的答案可以参考:https://leetcode-cn.com/problems/candy/solution/fen-fa-tang-guo-by-leetcode/
中的题解三

本题的标签是贪心算法,我的理解是每一轮扫描都是按照最少的糖果分配来做
第一轮:首先每个人分配一个糖果,满足最低要求;
第二轮:由于要求相邻的孩子中评分高的孩子获得更多糖果,所以我们可以先满足如果右边孩子的评分比左边孩子评分高就获得更多的糖果;
第三轮:满足如果左边的孩子大于右边的孩子就获得更多的糖果。
这样每一轮都是按照最低要求来的,所以三轮下来的和一定是最少的。
"""

def candy(ratings):
    if not len(ratings):
        return 0
    total_list = [1] * (len(ratings))
    for i in range(0,len(ratings)-1):
        if ratings[i+1] > ratings[i]:
            total_list[i+1] = total_list[i] + 1
    for i in range(len(ratings) - 1,0,-1): # 注意这里的索引范围,可能会造成nums[-1]与nums[0]的比较
        if ratings[i-1] > ratings[i]:
            if total_list[i-1] <= total_list[i]:
                total_list[i - 1] = total_list[i] + 1
    return sum(total_list)

if __name__ == '__main__':
    ratings = [1,0,2]
    print(candy(ratings))