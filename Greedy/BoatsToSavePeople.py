# -*- coding: utf-8 -*-
# @File    : BoatsToSavePeople.py
# @Date    : 2022-08-21
# @Author  : tc
"""
881. 救生艇
给定数组 people 。people[i]表示第 i 个人的体重 ，船的数量不限，每艘船可以承载的最大重量为 limit。
每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。
返回 承载所有人所需的最小船数 。

示例 1：
输入：people = [1,2], limit = 3
输出：1
解释：1 艘船载 (1, 2)

示例 2：
输入：people = [3,2,2,1], limit = 3
输出：3
解释：3 艘船分别载 (1, 2), (2) 和 (3)

示例 3：
输入：people = [3,5,3,4], limit = 5
输出：4
解释：4 艘船分别载 (3), (3), (4), (5)

观察这么一件事儿，越重的人，越容易自己独占一条船。如果想尽可能地利用空间，就尽可能往它们上面塞人。
“
如果最重的，重到连最轻的都加不上去，那它只能自己一个人一条船。剩下的问题就是一个递归的解了;
如果最重的可以带上最轻的，那它们俩一艘船是最优的。因为最轻的能和任一个人一起，但其他人不一定能和最重的人一起。
”
排序后，双指针。如果两人的和小于等于limit，那么左右凑一对儿，往中间递归；否则右边独自占一条船。

参考：https://leetcode.cn/problems/boats-to-save-people/solution/python-tan-xin-pai-xu-shuang-zhi-zhen-by-vsk9/

"""
from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        left, right = 0, n - 1
        ans = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            ans += 1
        return ans
